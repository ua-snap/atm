import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def set_lake_ice_depth_constant(self):
    """
    Lake ice thickness is calculated using a modified Stefan Equation.
    alpha-coefficients range from 1.7-2.4 for average lake with snow and 2.7
    for windy lake with no snow.

    The Stefan equation that will be used is:
    h = alpha * sqrt(FDD)
    
    where: h is ice thickness (cm)
           alpha is Stefan Equation Coefficent
           FDD are the freezing degree days

    Assuming that the ice thickness in Barrow is ~2.2 m and
    the number of freezing degree days in 2006 is 4160, the
    alpha value required to get to 2.2 m ice is 3.4 - quite
    a bit higher than the published values.


    Arp et al 2011 calculated alpha to be 2.43. Going to use
    a 5% range around this value.
    
    """

    print '   Set Lake Ice Depth Constant'
    
    # Set the Lake_ice_depth_factor
    self.Lake_Ice_Depth_alpha = np.zeros(self.ATTM_nrows * self.ATTM_ncols)

    for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
        if (self.ATTM_Lakes[i] + self.ATTM_Ponds[i] + self.ATTM_Wet_NPG[i] +
            self.ATTM_Wet_LCP[i] + self.ATTM_Wet_CLC[i] + self.ATTM_Wet_FCP[i] +
            self.ATTM_Wet_HCP[i] + self.ATTM_Rivers[i] + self.ATTM_Urban[i]) > 0.0:

            if self.LakePond['ice_thickness_distribution'].lower == 'uniform':
                self.Lake_Ice_Depth_alpha[i] = self.LakePond['ice_thickness_uniform_alpha']
            elif self.LakePond['ice_thickness_distribution'].lower() == 'random':
                self.Lake_Ice_Depth_alpha[i] = random.uniform(self.LakePond['Lower_ice_thickness_alpha'],\
                                                              self.LakePond['Upper_ice_thickness_alpha'])
    
    print '   done. \n  '
