import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def set_lake_expansion_constant(self):
    """
    The purpose of this module is to set the prescribed lake expansion
    rate.  I am not sure if it should be a random value or a constant.

    At this point, it is just set to a constant.
    Initially: set to 0.1% (0.001)
    """
    print '    Set Lake Expansion Constant'
    self.Lake_Expansion_Constant = self.LakePond['Lake_Expansion']
    self.Pond_Expansion_Constant = self.LakePond['Pond_Expansion']

    # This 0.5% expansion is close to what Ben Jones estimates in his paper.
    # Very approximately... Need to think harder about this.
    
    
    print '      the lake expansion constant is: ', self.LakePond['Lake_Pond_Expansion']
    print '    done. \n  '
