import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def set_ice_thickness_array(self):
    self.ice_thickness = np.zeros(self.ATTM_ncols * self.ATTM_nrows)
