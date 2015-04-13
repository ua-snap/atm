import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
from math import exp as exp

def check_Lakes(self, element, time):
    
    if self.ATTM_Lakes[element] > 0.0:
        
        # Determine the new lake depth
        depth_change = np.sqrt(time)/self.LakePond['lake_depth_control'] 
        self.Lake_Depth[element] = self.Lake_Depth[element] + depth_change

        # Determine the fractional change from Lakes -> Ponds
        # (if ice thickness is greater than lake depth)
        if self.Lake_Depth[element] <= self.ice_thickness[element]:
            self.ATTM_Ponds[element] = self.ATTM_Ponds[element] + self.ATTM_Lakes[element]
            self.ATTM_Lakes[element] = 0.0


            
