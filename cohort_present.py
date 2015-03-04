import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def cohort_present(self):

    """
    The purpose of this module is to create a dictionary with a list of
    each cohort in each model element.  This list will be used for lake expansion/
    terrestrial losses, and to shorten the processing time (only process
    cohorts present)
    """

    print '   Creating a list of thermokarst susceptible cohorts '


    self.cohort_list = {}
    self.land_cohorts = {}
    
    #list = ('Wet_NPG', 'Wet_LCP', 'Wet_CLC', 'Wet_FCP', 'Wet_HCP', 'Lakes', 'Ponds')
    
    for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
        cohorts = ['Wet_NPG', 'Wet_LCP', 'Wet_CLC', 'Wet_FCP', 'Wet_HCP', 'Lakes', 'Ponds']
        land_cohorts = ['Wet_NPG', 'Wet_LCP', 'Wet_CLC', 'Wet_FCP', 'Wet_HCP']
        
        if self.ATTM_Wet_NPG[i] == 0.0 :
            cohorts.remove('Wet_NPG')
            land_cohorts.remove('Wet_NPG')
        if self.ATTM_Wet_LCP[i] == 0.0 :
            cohorts.remove('Wet_LCP')
            land_cohorts.remove('Wet_LCP')
        if self.ATTM_Wet_CLC[i] == 0.0 :
            cohorts.remove('Wet_CLC')
            land_cohorts.remove('Wet_CLC')
        if self.ATTM_Wet_FCP[i] == 0.0 :
            cohorts.remove('Wet_FCP')
            land_cohorts.remove('Wet_FCP')
        if self.ATTM_Wet_HCP[i] == 0.0 :
            cohorts.remove('Wet_HCP')
            land_cohorts.remove('Wet_HCP')
        if self.ATTM_Lakes[i]   == 0.0 : cohorts.remove('Lakes')
        if self.ATTM_Ponds[i]   == 0.0 : cohorts.remove('Ponds')

        self.cohort_list[i] = cohorts
        self.land_cohorts[i] = land_cohorts
        
        
        
    print '    done. \n  '
    
        
