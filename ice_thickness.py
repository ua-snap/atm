import numpy as np
import gdal, os, sys, glob, random
import pylab as pl



"""
This module sets the ice thickness in each element using a modified Stefan Equation as
described in set_lake_ice_constant.py file.

h     : ice thickness (m)
alpha : Stefan coefficient (set in set_lake_ice_constant.py)
FDD   : Freezing Degree days
100   : Conversion from cm to m

h = (alpha * sqrt(FDD))/100.0  
"""
def ice_thickness(self, time, element):
    if self.Met['met_distribution'].lower() == 'point':
        self.ice_thickness[element] = (self.Lake_Ice_Depth_alpha[element] * \
                                    np.sqrt(-1.*self.degree_days[time,2]))/100.
    else:
        self.ice_thickness[element] = (self.Lake_Ice_Depth_alpha[element] * \
                                       np.sqrt(-1. * self.FDD[time,element]))/100.
            
# ----------------
#    self test
# ----------------
#    if element == 1600:
#        print 'Ice thickness is :', self.ice_thickness[element]
