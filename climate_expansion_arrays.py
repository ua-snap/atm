import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
import lake_pond_expansion

def set_climate_expansion_arrays(self):
    self.climate_expansion_lakes = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
    self.climate_expansion_ponds = np.zeros([self.ATTM_nrows * self.ATTM_ncols])



    """ I am not exactly sure what I had in mind here with these arrays. Need to
        track this done. Bolton March 6, 2015 """
