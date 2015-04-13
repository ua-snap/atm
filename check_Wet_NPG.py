import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
from math import exp as exp

def check_Wet_NPG(self, element, time):

    # ! Determine the position on the POI curve
    if self.Wet_NPG_PL[element] == 0.0:   # Outside of area of interest (ocean, etc)
        x = -1.0
    else:
        x        = (self.ALD[element] / self.Wet_NPG_PL[element]) - 1.0
    
    # Maximum rate of terrain transition
    max_rate_terrain_transition = self.WetNPG['max_terrain_transition']
    
    # Rate of terrain transition as f(ice)
    if self.ice[element] == 'poor'    : ice_slope = self.WetNPG['ice_slope_poor']
    if self.ice[element] == 'pore'    : ice_slope = self.WetNPG['ice_slope_pore']
    if self.ice[element] == 'wedge'   : ice_slope = self.WetNPG['ice_slope_wedge']
    if self.ice[element] == 'massive' : ice_slope = self.WetNPG['ice_slope_massive']
    
    # check if Wetland Non-polygonal ground is present in the element
    if self.ATTM_Wet_NPG[element] > 0.0:

        # Active Layer > Protective Layer
        if self.ALD[element] >= self.Wet_NPG_PL[element]:
            # Determine the Probability of Initiation (POI) for time-step
            if self.WetNPG['POI_Function'].lower() == 'sigmoid':
                if self.drainage_efficiency[element] == 'above':
                    A1 = self.WetNPG['A1_above']
                    A2 = self.WetNPG['A2_above']
                    x0 = self.WetNPG['x0_above']
                    dx = self.WetNPG['dx_above']
                else:
                    # Drainage efficiency = 'below'
                    A1 = self.WetNPG['A1_below']
                    A2 = self.WetNPG['A2_below']
                    x0 = self.WetNPG['x0_below']
                    dx = self.WetNPG['dx_below']
                
                # Probability of Initiation (POI) at current time
                POI = A2 + (A1 - A2)/(1.+exp((x - x0)/dx))
            elif self.WetNPG['POI_Function'].lower() == 'linear':
                if self.drainage_efficiency[element] == 'above':
                    a = self.WetNPG['a_above']
                    b = self.WetNPG['b_above']
                else:
                    a = self.WetNPG['a_below']
                    b = self.WetNPG['b_below']
                # Probability of Initiation (POI) at current time
                POI = a + (b * x)
            elif self.WetNPG['POI_Function'].lower() == 'sigmoid2':
                if self.drainage_efficiency[element] == 'above':
                    K = self.WetNPG['K_above']
                    C = self.WetNPG['C_above']
                    A = self.WetNPG['A_above']
                    B = self.WetNPG['B_above']
                else:
                    K = self.WetNPG['K_below']
                    C = self.WetNPG['C_below']
                    A = self.WetNPG['A_below']
                    B = self.WetNPG['B_below']
                # Probability of Initation (POI) at current time
                POI = K / (C + (A * x**B))
            elif self.WetNPG['POI_Function'].lower() == 'hill':
                if self.drainage_efficiency[element] == 'above':
                    B = self.WetNPG['HillB_above']
                    N = self.WetNPG['HillN_above']
                else:
                    B = self.WetNPG['HillB_below']
                    N = self.WetNPG['HillN_below']
                # Probability of Intiation (POI) at current time
                POI = (B * (x**N))/(1. + (x**N))
            # Cumulative POI
            if time == 0:
                self.Wet_NPG_POI[element, time] = POI
            else:
                self.Wet_NPG_POI[element, time] = self.Wet_NPG_POI[element, time -1] + POI
            
            # Check that 0.0 < POI < 1.0
            if self.Wet_NPG_POI[element, time] < 0.0: self.Wet_NPG_POI[element, time] = 0.0
            if self.Wet_NPG_POI[element, time] > 1.0: self.Wet_NPG_POI[element, time] = 1.0

            # Adjust the Protective layer depth
            self.Wet_NPG_PL[element] = self.Wet_NPG_PL[element] + ((self.ALD[element] - \
                                                                   self.Wet_NPG_PL[element])* \
                                                                   self.WetNPG['porosity'])

            # Determine rate of terrain transition from Wet_NPG -> Wet_LCP
            rate_of_transition = (self.Wet_NPG_POI[element, time] * ice_slope) * max_rate_terrain_transition
            # error check
            if rate_of_transition > max_rate_terrain_transition: rate_of_transition = max_rate_terrain_transition

            # Determine the fractional change from Wet_NPG ->: Wet_LCP
            cohort_change = self.ATTM_Wet_NPG[element] * rate_of_transition

            # cohort_change > Wet_NPG available
            if cohort_change > self.ATTM_Wet_NPG[element]:
                self.ATTM_Wet_LCP[element] = self.ATTM_Wet_LCP[element] + self.ATTM_Wet_NPG[element]
                self.ATTM_Wet_NPG[element] = 0.0
            else:
                # cohort_change < Wet_NPG available
                self.ATTM_Wet_LCP[element] = self.ATTM_Wet_LCP[element] + cohort_change
                self.ATTM_Wet_NPG[element] = self.ATTM_Wet_NPG[element] - cohort_change
        else:
            # Active layer depth < Protective layer -> reset the cumulative POI to 0.0
            self.Wet_NPG_POI[element,time] = 0.0
                                     
            

            
            
                     
        
        
