import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
from math import exp as exp

def check_Wet_LCP(self, element, time):
    
    # Define WET_LCP curve constants:
    # ! For 'Above' Drainage threshold
    A1_above = -1.186e-1
    A2_above = 1.01
    x0_above = 4.856e-1
    dx_above = 1.398e-1
    # ! for 'Below' Drainage threshold
    A1_below = 3.454e-2
    A2_below = 1.01
    x0_below = 1.04
    dx_below = 1.617e-1
    # ! Position on the POI curve
    if self.Wet_LCP_PL[element] == 0:
        x = -1.0
    else:
        x        = (self.ALD[element] / self.Wet_LCP_PL[element]) - 1.0
    # Maximum rate of terrain transition
    max_rate_terrain_transition = 0.00056
    
    # Rate of terrain transition as f(ice)
    if self.ice[element] == 'poor'    : ice_slope = 0.05
    if self.ice[element] == 'pore'    : ice_slope = 0.5
    if self.ice[element] == 'wedge'   : ice_slope = 1.25
    if self.ice[element] == 'massive' : ice_slope = 3.33
    
    
    # check if Wetland Non-polygonal ground is present in the element
    if self.ATTM_Wet_LCP[element] > 0.0:

        # Active Layer > Protective Layer
        if self.ALD[element] >= self.Wet_LCP_PL[element]:
            # Determine the Probability of Initiation (POI) for time-step

            if self.drainage_efficiency[element] == 'above':
                A1 = A1_above
                A2 = A2_above
                x0 = x0_above
                dx = dx_above
            else:
                # Drainage efficiency = 'below'
                A1 = A1_below
                A2 = A2_below
                x0 = x0_below
                dx = dx_below
                
            # Probability of Initiation (POI) at current time
            POI = A2 + (A1 - A2)/(1.+exp((x - x0)/dx))
            # Cumulative POI
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
                                                                   self.Wet_LCP_PL[element])*0.5)

            # Determine rate of terrain transition from Wet_LCP -> Wet_FCP & Wet_CLC
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
