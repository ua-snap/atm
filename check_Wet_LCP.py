import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
from math import exp as exp

def check_Wet_LCP(self, element, time):
    
    # ! Position on the POI curve
    if self.Wet_LCP_PL[element] == 0:
        x = -1.0
    else:
        x        = (self.ALD[element] / self.Wet_LCP_PL[element]) - 1.0
            
    # Maximum rate of terrain transition
    max_rate_terrain_transition = self.WetLCP['max_terrain_transition']
    
    # Rate of terrain transition as f(ice)
    if self.ice[element] == 'poor'    : ice_slope = self.WetLCP['ice_slope_poor']
    if self.ice[element] == 'pore'    : ice_slope = self.WetLCP['ice_slope_pore']
    if self.ice[element] == 'wedge'   : ice_slope = self.WetLCP['ice_slope_wedge']
    if self.ice[element] == 'massive' : ice_slope = self.WetLCP['ice_slope_massive']
    
    
    # check if Wetland Non-polygonal ground is present in the element
    if self.ATTM_Wet_LCP[element] > 0.0:
        # Active Layer > Protective Layer
        if self.ALD[element] >= self.Wet_LCP_PL[element]:
            #=============================================================
            # Determine the Probability of Initiation (POI) for time-step
            #=============================================================
            if self.WetLCP['POI_Function'].lower() == 'sigmoid':
                if self.drainage_efficiency[element] == 'above':
                    A1 = self.WetLCP['A1_above']
                    A2 = self.WetLCP['A2_above']
                    x0 = self.WetLCP['x0_above']
                    dx = self.WetLCP['dx_above']
                else:
                    # Drainage efficiency = 'below'
                    A1 = self.WetLCP['A1_below']
                    A2 = self.WetLCP['A2_below']
                    x0 = self.WetLCP['x0_below']
                    dx = self.WetLCP['dx_below']
                
                # Probability of Initiation (POI) at current time
                POI = A2 + (A1 - A2)/(1.+exp((x - x0)/dx))
            elif self.WetLCP['POI_Function'].lower() == 'linear':
                if self.drainage_efficiency[element] == 'above':
                    a = self.WetLCP['a_above']
                    b = self.WetLCP['b_above']
                else:
                    a = self.WetLCP['a_below']
                    b = self.WetLCP['b_below']
                # Probability of Initation (POI) at current time
                POI = a + (b * x)
            elif self.WetLCP['POI_Function'].lower() == 'sigmoid2':
                if self.drainage_efficiency[element] == 'above':
                    K = self.WetLCP['K_above']
                    C = self.WetLCP['C_above']
                    A = self.WetLCP['A_above']
                    B = self.WetLCP['B_above']
                else:
                    K = self.WetLCP['K_below']
                    C = self.WetLCP['C_below']
                    A = self.WetLCP['A_below']
                    B = self.WetLCP['B_below']
                # Probability of Initiation (POI) at current time
                POI = K / (C + (A * x**B))
            elif self.WetLCP['POI_Function'].lower() == 'hill':
                if self.drainage_efficiency[element] == 'above':
                    B = self.WetLCP['HillB_above']
                    N = self.WetLCP['HillN_above']
                else:
                    B = self.WetLCP['HillB_below']
                    N = self.WetLCP['HillN_below']
                # Probability of Intiation (POI) at current time
                POI = (B * (x**N))/(1. + (x**N))
            #==============================    
            # Calculate the Cumulative POI
            #==============================
            if time == 0:
                self.Wet_LCP_POI[element, time] = POI
            else:
                self.Wet_LCP_POI[element, time] = self.Wet_LCP_POI[element, time -1] + POI
            
            # Check that 0.0 < POI < 1.0
            if self.Wet_LCP_POI[element, time] < 0.0: self.Wet_LCP_POI[element, time] = 0.0
            if self.Wet_LCP_POI[element, time] > 1.0: self.Wet_LCP_POI[element, time] = 1.0

            # Adjust the Protective layer depth
            # ! Note: Assuming porosity of soil = 0.5. 
            self.Wet_LCP_PL[element] = self.Wet_LCP_PL[element] + ((self.ALD[element] - \
                                                                   self.Wet_LCP_PL[element])* \
                                                                   self.WetLCP['porosity'])
            #========================================================================
            # Determine rate of terrain transition from Wet_LCP -> Wet_FCP & Wet_CLC
            #========================================================================
            rate_of_transition = (self.Wet_LCP_POI[element, time] * ice_slope) * max_rate_terrain_transition
            # error check
            if rate_of_transition > max_rate_terrain_transition: rate_of_transition = max_rate_terrain_transition
            
            # Determine the fractional change from Wet_LCP ->: Wet_FCP & Wet_CLC
            
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
            # ! Note: Our current pathways show that the LCP cohorts can transition to both
            #         FCP and CLC polygons. At this point, I am not sure how to distribute the
            #         cohort_change between the coalescent and flat center polygons.
            #
            #         Initial code (for infrastructure purposes) will set the distribution
            #         based upon the ratio of CLC:FCP at the time step. If the ratio is 2:1,
            #         then 2/3 of the cohort_change will go toward CLC and 1/2 will go toward
            #         FCP.
            #
            #         This will need to be refined over time.
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            cohort_change = self.ATTM_Wet_LCP[element] * rate_of_transition
            
            if self.ATTM_Wet_CLC[element] > 0.0 and self.ATTM_Wet_FCP[element] > 0.0:
                clc_fraction = self.ATTM_Wet_CLC[element] / self.ATTM_Wet_FCP[element]
                fcp_fraction = 1.0 - clc_fraction
            else:
                if self.ATTM_Wet_CLC[element] == 0.0 :
                    clc_fraction = 0.0
                    fcp_fraction = 1.0
                if self.ATTM_Wet_FCP[element] == 0.0:
                    clc_fraction = 1.0
                    fcp_fraction = 0.0
            
            # cohort_change > Wet_LCP available
            if cohort_change > self.ATTM_Wet_LCP[element]:
                self.ATTM_Wet_FCP[element] = self.ATTM_Wet_FCP[element] + \
                                             (self.ATTM_Wet_LCP[element] * fcp_fraction) + \
                                             (self.ATTM_Wet_CLC[element] * clc_fraction)
                self.ATTM_Wet_LCP[element] = 0.0
            else:
                # cohort_change < Wet_LCP available
                self.ATTM_Wet_FCP[element] = self.ATTM_Wet_FCP[element] + (cohort_change * fcp_fraction)
                self.ATTM_Wet_CLC[element] = self.ATTM_Wet_CLC[element] + (cohort_change * clc_fraction)
                self.ATTM_Wet_LCP[element] = self.ATTM_Wet_LCP[element] - cohort_change
        else:
            # Active layer depth < Protective layer -> reset the cumulative POI to 0.0
            self.Wet_LCP_POI[element,time] = 0.0
