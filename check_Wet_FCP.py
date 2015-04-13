import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
from math import exp as exp

def check_Wet_FCP(self, element, time):
    
    # ! Position on the POI curve
    if self.Wet_FCP_PL[element] == 0.0:
        x = -1.0
    else:
        x        = (self.ALD[element] / self.Wet_FCP_PL[element]) - 1.0

    # Maximum rate of terrain transition
    max_rate_terrain_transition = self.WetFCP['max_terrain_transition']
    
    # Rate of terrain transition as f(ice)
    if self.ice[element] == 'poor'    : ice_slope = self.WetFCP['ice_slope_poor']
    if self.ice[element] == 'pore'    : ice_slope = self.WetFCP['ice_slope_pore']
    if self.ice[element] == 'wedge'   : ice_slope = self.WetFCP['ice_slope_wedge']
    if self.ice[element] == 'massive' : ice_slope = self.WetFCP['ice_slope_massive']
    
    # check if Wetland Non-polygonal ground is present in the element
    if self.ATTM_Wet_FCP[element] > 0.0:
        # Active Layer > Protective Layer
        if self.ALD[element] >= self.Wet_FCP_PL[element]:
            # Determine the Probability of Initiation (POI) for time-step
            if self.WetFCP['POI_Function'].lower == 'sigmoid':
                if self.drainage_efficiency[element] == 'above':
                    A1 = self.WetFCP['A1_above']
                    A2 = self.WetFCP['A2_above']
                    x0 = self.WetFCP['x0_above']
                    dx = self.WetFCP['dx_above']
                else:
                    # Drainage efficiency = 'below'
                    A1 = self.WetFCP['A1_below']
                    A2 = self.WetFCP['A2_below']
                    x0 = self.WetFCP['x0_below']
                    dx = self.WetFCP['dx_below']
                # Probability of Initiation (POI) at current time
                POI = A2 + (A1 - A2)/(1.+exp((x - x0)/dx))
            elif self.WetFCP['POI_Function'].lower() == 'linear' :
                if self.drainage_efficiency[element] == 'above' :
                    a = self.WetFCP['a_above']
                    b = self.WetFCP['b_above']
                else:
                    a = self.WetFCP['a_below']
                    b = self.WetFCP['b_below']
                # Probability of Initation (POI) at current time step
                POI = a + (b * x)
            elif self.WetFCP['POI_Function'].lower() == 'sigmoid2':
                if self.drainage_efficiency[element] == 'above':
                    K = self.WetFCP['K_above']
                    C = self.WetFCP['C_above']
                    A = self.WetFCP['A_above']
                    B = self.WetFCP['B_above']
                else:
                    K = self.WetFCP['K_below']
                    C = self.WetFCP['C_below']
                    A = self.WetFCP['A_below']
                    B = self.WetFCP['B_below']
                # Probability of Intiation (POI) at current time
                POI = K / (C + (A * x**B))
            elif self.WetFCP['POI_Function'].lower() == 'hill':
                if self.drainage_efficiency[element] == 'above':
                    B = self.WetFCP['HillB_above']
                    N = self.WetFCP['HillN_above']
                else:
                    B = self.WetFCP['HillB_below']
                    N = self.WetFCP['HillN_below']
                # Probability of Intiation (POI) at current time
                POI = (B * (x**N))/(1. + (x**N))
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -- - - -
            # Cumulative POI
            if time == 0:
                self.Wet_FCP_POI[element, time] = POI
            else:
                self.Wet_FCP_POI[element, time] = self.Wet_FCP_POI[element, time -1] + POI
            
            # Check that 0.0 < POI < 1.0
            if self.Wet_FCP_POI[element, time] < 0.0: self.Wet_FCP_POI[element, time] = 0.0
            if self.Wet_FCP_POI[element, time] > 1.0: self.Wet_FCP_POI[element, time] = 1.0

            # Adjust the Protective layer depth
            # ! Note: Assuming porosity of soil = 0.5. 
            self.Wet_FCP_PL[element] = self.Wet_FCP_PL[element] + ((self.ALD[element] - \
                                                                   self.Wet_FCP_PL[element])* \
                                                                   self.WetFCP['porosity'])

            # Determine rate of terrain transition from Wet_FCP -> Wet_HCP
            rate_of_transition = (self.Wet_FCP_POI[element, time] * ice_slope) * max_rate_terrain_transition
            # error check
            if rate_of_transition > max_rate_terrain_transition: rate_of_transition = max_rate_terrain_transition

            # Determine the fractional change from Wet_FCP ->: Wet_HCP
            cohort_change = self.ATTM_Wet_FCP[element] * rate_of_transition

            # cohort_change > Wet_FCP available
            if cohort_change > self.ATTM_Wet_FCP[element]:
                self.ATTM_Wet_HCP[element] = self.ATTM_Wet_HCP[element] + self.ATTM_Wet_FCP[element]
                self.ATTM_Wet_FCP[element] = 0.0
            else:
                # cohort_change < Wet_FCP available
                self.ATTM_Wet_HCP[element] = self.ATTM_Wet_HCP[element] + cohort_change
                self.ATTM_Wet_FCP[element] = self.ATTM_Wet_FCP[element] - cohort_change
        else:
            # Active layer depth < Protective layer -> reset the cumulative POI to 0.0
            self.Wet_FCP_POI[element,time] = 0.0
