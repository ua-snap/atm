import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
from math import exp as exp

"""
The purpose of this module is blah blah blah.

"""

def set_pond_growth_array(self):
    #self.pond_growth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)

    # adding new arrays for Wetland Tundra, Young, Medium, and Old age
    # 18 October 2016

    self.Pond_growth_WT_Y = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.Pond_growth_WT_M = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.Pond_growth_WT_O = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
