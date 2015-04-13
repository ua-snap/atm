import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def active_layer_depth(self, time, element):
     ### -------------------------------------------------------------------------------------------
     # Formulation of the active layer depth following discussion with Vlad Romanosky in July 2014.
     ### -------------------------------------------------------------------------------------------

    if self.Met['met_distribution'].lower() == 'point':
        self.ALD[element] = self.initial_ALD_depth[element] * np.sqrt(self.degree_days[time,1]/self.degree_days[0,1])
    else:
        self.ALD[element] = self.initial_ALD_depth[element] * np.sqrt(self.TDD[time,element]/self.TDD[0,element])
             

             

     ############################
     # Create a plot here
     ############################
     
