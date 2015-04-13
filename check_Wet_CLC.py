import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
from math import exp as exp

def check_Wet_CLC(self, element, time):
    
    # ! Position on the POI curve
    if self.Wet_CLC_PL[element] == 0.0:
        x = -1.0
    else:
        x        = (self.ALD[element] / self.Wet_CLC_PL[element]) - 1.0
        
    # Maximum rate of terrain transition
    max_rate_terrain_transition = self.WetCLC['max_terrain_transition']
    
    # Rate of terrain transition as f(ice)
    if self.ice[element] == 'poor'    : ice_slope = self.WetCLC['ice_slope_poor']
    if self.ice[element] == 'pore'    : ice_slope = self.WetCLC['ice_slope_pore']
    if self.ice[element] == 'wedge'   : ice_slope = self.WetCLC['ice_slope_wedge']
    if self.ice[element] == 'massive' : ice_slope = self.WetCLC['ice_slope_massive']
    
    # check if Wetland Coalescent Low Center Polygons are  present in the element
    if self.ATTM_Wet_CLC[element] > 0.0:
        # Active Layer > Protective Layer
        if self.ALD[element] >= self.Wet_CLC_PL[element]:
            # Determine the Probability of Initiation (POI) for time-step
            if self.WetCLC['POI_Function'].lower() == 'sigmoid':
                if self.drainage_efficiency[element] == 'above':
                    A1 = self.WetCLC['A1_above']
                    A2 = self.WetCLC['A2_above']
                    x0 = self.WetCLC['x0_above']
                    dx = self.WetCLC['dx_above']
                else:
                    # Drainage efficiency = 'below'
                    A1 = self.WetCLC['A1_below']
                    A2 = self.WetCLC['A2_below']
                    x0 = self.WetCLC['x0_below']
                    dx = self.WetCLC['dx_below']
                
                # Probability of Initiation (POI) at current time
                POI = A2 + (A1 - A2)/(1.+exp((x - x0)/dx))
            elif self.WetCLC['POI_Function'].lower() == 'linear':
                if self.drainage_efficiency[element] == 'above':
                    a = self.WetCLC['a_above']
                    b = self.WetCLC['b_above']
                else:
                    a = self.WetCLC['a_below']
                    b = self.WetCLC['b_below']
                # Probability of Initiation (POI) at current time
                POI = a + (b * x)
            elif self.WetCLC['POI_Function'].lower() == 'sigmoid2':
                if self.drainage_efficiency[element] == 'above':
                    K = self.WetCLC['K_above']
                    C = self.WetCLC['C_above']
                    A = self.WetCLC['A_above']
                    B = self.WetCLC['B_above']
                else:
                    K = self.WetCLC['K_below']
                    C = self.WetCLC['C_below']
                    A = self.WetCLC['A_below']
                    B = self.WetCLC['B_below']
                # Probability of Initation (POI) at current time
                POI = K / (C + (A * x**B))
            elif self.WetCLC['POI_Function'].lower() == 'hill':
                if self.drainage_efficiency[element] == 'above':
                    B = self.WetCLC['HillB_above']
                    N = self.WetCLC['HillN_above']
                else:
                    B = self.WetCLC['HillB_below']
                    N = self.WetCLC['HillN_below']
                # Probability of Intiation (POI) at current time
                POI = (B * (x**N))/(1. + (x**N))
            #-------------------------------------------------------------------
            # Cumulative POI
            if time == 0:
                self.Wet_CLC_POI[element, time] = POI
            else:
                self.Wet_CLC_POI[element, time] = self.Wet_CLC_POI[element, time -1] + POI
            
            # Check that 0.0 < POI < 1.0
            if self.Wet_CLC_POI[element, time] < 0.0: self.Wet_CLC_POI[element, time] = 0.0
            if self.Wet_CLC_POI[element, time] > 1.0: self.Wet_CLC_POI[element, time] = 1.0

            # Adjust the Protective layer depth
            self.Wet_CLC_PL[element] = self.Wet_CLC_PL[element] + ((self.ALD[element] - \
                                                                   self.Wet_CLC_PL[element])* \
                                                                   self.WetCLC['porosity'])

            # Determine rate of terrain transition from Wet_CLC -> Ponds
            rate_of_transition = (self.Wet_CLC_POI[element, time] * ice_slope) * max_rate_terrain_transition
            # error check
            if rate_of_transition > max_rate_terrain_transition: rate_of_transition = max_rate_terrain_transition

            # Determine the fractional change from Wet_CLC -> Ponds
            cohort_change = self.ATTM_Wet_CLC[element] * rate_of_transition

            # cohort_change > Wet_CLC available
            if cohort_change > self.ATTM_Wet_CLC[element]:
                self.ATTM_Ponds[element] = self.ATTM_Ponds[element] + self.ATTM_Wet_CLC[element]
                self.ATTM_Wet_CLC[element] = 0.0
            else:
                # cohort_change < Wet_CLC available
                self.ATTM_Ponds[element]   = self.ATTM_Ponds[element] + cohort_change
                self.ATTM_Wet_CLC[element] = self.ATTM_Wet_CLC[element] - cohort_change
        else:
            # Active layer depth < Protective layer -> reset the cumulative POI to 0.0
            self.Wet_CLC_POI[element,time] = 0.0
