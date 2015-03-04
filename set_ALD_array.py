import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def set_ALD_array(self):
    self.ALD = np.zeros(self.ATTM_ncols * self.ATTM_nrows)
