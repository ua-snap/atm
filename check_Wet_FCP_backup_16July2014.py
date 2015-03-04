import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def check_Wet_FCP(self, element, time):
    # check if Wetland Non-polygonal ground is present in the element
    if self.ATTM_Wet_FCP[element] > 0:
        max_rate_of_terrain_transition = 0.075

        # check if active layer is greater than protective layer
        # IF YES
        if self.ALD[element] >= self.Wet_FCP_PL[element]:
            if time == 0:
                ALD_old = self.ALD[element]
            else:
                ALD_old = self.ALD[element - 1]
            
            # Set probability of initiation
            if self.drainage_efficiency[element] == 'above':
                if time == 0:
                    self.Wet_FCP_POI[element, time] = ((self.ALD[element] / self.Wet_FCP_PL[element]) - 1.) * 1.0
                    self.Wet_FCP_PL[element] = self.Wet_FCP_PL[element] + ((self.ALD[element])*0.5)
                else:
                    self.Wet_FCP_POI[element, time] = self.Wet_FCP_POI[element-1, time] + \
                                                ((self.ALD[element] / self.Wet_FCP_PL[element]) - 1.) * 1.0
                    self.Wet_FCP_PL[element] = self.Wet_FCP_PL[element] + ((self.ALD[element] - ALD_old)*0.5)

                     
            else :    # drainage efficiency == 'below'
                if time == 0:
                    self.Wet_FCP_POI[element, time] = ((self.ALD[element] / self.Wet_FCP_PL[element]) - 1.) * 0.66
                    # Adjust the Protective layer as it increases with active layer depth
                    self.Wet_FCP_PL[element] = self.Wet_FCP_PL[element] + ((self.ALD[element])*0.5)
                else:
                    self.Wet_FCP_POI[element, time] = self.Wet_FCP_POI[element-1, time] + \
                                                ((self.ALD[element] / self.Wet_FCP_PL[element]) - 1.) * 0.66
                    self.Wet_FCP_PL[element] = self.Wet_FCP_PL[element] + ((self.ALD[element] - ALD_old)*0.5)

            #### Rate of Transition
            if self.ice[element] == 'poor':
                rate_of_transition = (self.Wet_FCP_POI[element, time] * 0.001) * max_rate_of_terrain_transition
            elif self.ice[element] == 'pore':
                rate_of_transition = (self.Wet_FCP_POI[element, time] * 0.005) * max_rate_of_terrain_transition
            elif self.ice[element] == 'wedge':
                rate_of_transition = (self.Wet_FCP_POI[element, time] * 0.01) * max_rate_of_terrain_transition
            else:             # ice == 'massive'
                rate_of_transition = (self.Wet_FCP_POI[element, time] * 0.05) * max_rate_of_terrain_transition

            #### Transition cohorts
            transition = self.ATTM_Wet_FCP[element] * rate_of_transition

            if transition > self.ATTM_Wet_FCP[element]:
                transition = self.ATTM_Wet_FCP[element]
                self.ATTM_Wet_FCP[element] = 0.0
                self.land_cohorts[element].remove('Wet_FCP')
                self.ATTM_Wet_HCP[element] = self.ATTM_Wet_HCP[element] + transition
                if 'Wet_HCP' not in self.land_cohorts[element]:
                    self.land_cohorts[element].append('Wet_HCP')
            else:
                self.ATTM_Wet_FCP[element] = self.ATTM_Wet_FCP[element] - transition
                self.ATTM_Wet_HCP[element] = self.ATTM_Wet_HCP[element] + transition
                if 'Wet_HCP' not in self.land_cohorts[element]:
                    self.land_cohorts[element].append('Wet_HCP')

            

            
        else:
            self.Wet_FCP_POI[element, time] = 0.0

        
    if self.ATTM_Wet_FCP[element] <= 0.0 : self.ATTM_Wet_FCP[element] = 0.0
    if self.ATTM_Wet_FCP[element] >= 1.0 : self.ATTM_Wet_FCP[element] = 1.0
