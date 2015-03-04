import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
from math import exp as exp

"""
The purpose of this module is blah blah blah.

"""

def set_pond_growth_array(self):
    self.pond_growth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
