import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
from math import exp as exp

def check_Wet_HCP(self, element, time):
    
    # ! Position on the POI curve
    if self.Wet_HCP_PL[element] == 0.0:
        x = -1.0
    else:
        x        = (self.ALD[element] / self.Wet_HCP_PL[element]) - 1.0
        
    # Maximum rate of terrain transition
    max_rate_terrain_transition = self.WetHCP['max_terrain_transition']
    
    # Rate of terrain transition as f(ice)
    if self.ice[element] == 'poor'    : ice_slope = self.WetHCP['ice_slope_poor']
    if self.ice[element] == 'pore'    : ice_slope = self.WetHCP['ice_slope_pore']
    if self.ice[element] == 'wedge'   : ice_slope = self.WetHCP['ice_slope_wedge']
    if self.ice[element] == 'massive' : ice_slope = self.WetHCP['ice_slope_massive']    
    
    # check if Wetland Non-polygonal ground is present in the element
    if self.ATTM_Wet_HCP[element] > 0.0:

        # Active Layer > Protective Layer
        if self.ALD[element] >= self.Wet_HCP_PL[element]:
            # Determine the Probability of Initiation (POI) for time-step
            if self.WetHCP['POI_Function'].lower() == 'sigmoid':
                if self.drainage_efficiency[element] == 'above':
                    A1 = self.WetHCP['A1_above']
                    A2 = self.WetHCP['A2_above']
                    x0 = self.WetHCP['x0_above']
                    dx = self.WetHCP['dx_above']
                else:
                    # Drainage efficiency = 'below'
                    A1 = self.WetHCP['A1_below']
                    A2 = self.WetHCP['A2_below']
                    x0 = self.WetHCP['x0_below']
                    dx = self.WetHCP['dx_below']
                
                # Probability of Initiation (POI) at current time
                POI = A2 + (A1 - A2)/(1.+exp((x - x0)/dx))
            elif self.WetHCP['POI_Function'].lower() == 'linear':
                if self.drainage_efficiency[element] == 'above':
                    a = self.WetHCP['a_above']
                    b = self.WetHCP['b_above']
                else:
                    a = self.WetHCP['a_below']
                    b = self.WetHCP['b_below']

                # Probability of Initiation (POI) at current time
                POI = a + (b * x)
            elif self.WetHCP['POI_Function'].lower() == 'sigmoid2':
                if self.drainage_efficiency[element] == 'above':
                    K = self.WetHCP['K_above']
                    C = self.WetHCP['C_above']
                    A = self.WetHCP['A_above']
                    B = self.WetHCP['B_above']
                else:
                    K = self.WetHCP['K_below']
                    C = self.WetHCP['C_below']
                    A = self.WetHCP['A_below']
                    B = self.WetHCP['B_below']
                # Probability of Initiation (POI) at current time
                POI = K / (C + (A * x**B))
            elif self.WetHCP['POI_Function'].lower() == 'hill':
                if self.drainage_efficiency[element] == 'above':
                    B = self.WetHCP['HillB_above']
                    N = self.WetHCP['HillN_above']
                else:
                    B = self.WetHCP['HillB_below']
                    N = self.WetHCP['HillN_below']
                # Probability of Intiation (POI) at current time
                POI = (B * (x**N))/(1. + (x**N))
    
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -    
            # Cumulative POI
            if time == 0:
                self.Wet_HCP_POI[element, time] = POI
            else:
                self.Wet_HCP_POI[element, time] = self.Wet_HCP_POI[element, time -1] + POI
            
            # Check that 0.0 < POI < 1.0
            if self.Wet_HCP_POI[element, time] < 0.0: self.Wet_HCP_POI[element, time] = 0.0
            if self.Wet_HCP_POI[element, time] > 1.0: self.Wet_HCP_POI[element, time] = 1.0

            # Adjust the Protective layer depth
            # ! Note: Assuming porosity of soil = 0.5. 
            self.Wet_HCP_PL[element] = self.Wet_HCP_PL[element] + ((self.ALD[element] - \
                                                                   self.Wet_HCP_PL[element])* \
                                                                   self.WetHCP['porosity'])

            # Determine rate of terrain transition from Wet_HCP -> Ponds
            rate_of_transition = (self.Wet_HCP_POI[element, time] * ice_slope) * max_rate_terrain_transition
            # error check
            if rate_of_transition > max_rate_terrain_transition: rate_of_transition = max_rate_terrain_transition

            # Determine the fractional change from Wet_HCP -> Ponds
            cohort_change = self.ATTM_Wet_HCP[element] * rate_of_transition

            # cohort_change > Wet_HCP available
            if cohort_change > self.ATTM_Wet_HCP[element]:
                self.ATTM_Ponds[element] = self.ATTM_Ponds[element] + self.ATTM_Wet_HCP[element]
                self.ATTM_Wet_HCP[element] = 0.0
            else:
                # cohort_change < Wet_HCP available
                self.ATTM_Ponds[element]   = self.ATTM_Ponds[element] + cohort_change
                self.ATTM_Wet_HCP[element] = self.ATTM_Wet_HCP[element] - cohort_change
        else:
            # Active layer depth < Protective layer -> reset the cumulative POI to 0.0
            self.Wet_HCP_POI[element,time] = 0.0
