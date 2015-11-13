import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def barrow_cohort_present(self):

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

#===================================================================================================    
def tanana_cohort_present(self):

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
        cohorts = ['TF_OB', 'TF_YB', 'TF_OF', 'TF_YF', 'TF_Con_PP', 'TF_Dec_PP', 'TF_TL']
        land_cohorts = ['TF_OB', 'TF_YB', 'TF_OF', 'TF_YF', 'TF_Con_PP', 'TF_Dec_PP',  'TF_TL']
        
        if self.ATTM_TF_OB[i] == 0.0 :
            cohorts.remove('TF_OB')
            land_cohorts.remove('TF_OB')
        if self.ATTM_TF_YB[i] == 0.0 :
            cohorts.remove('TF_YB')
            land_cohorts.remove('TF_YB')
        if self.ATTM_TF_OF[i] == 0.0 :
            cohorts.remove('TF_OF')
            land_cohorts.remove('TF_OF')
        if self.ATTM_TF_YF[i] == 0.0 :
            cohorts.remove('TF_YF')
            land_cohorts.remove('TF_YF')
        if self.ATTM_TF_Con_PP[i] == 0.0 :
            cohorts.remove('TF_Con_PP')
            land_cohorts.remove('TF_Con_PP')
        if self.ATTM_TF_Dec_PP[i] == 0.0 :
            cohorts.remove('TF_Dec_PP')
            land_cohorts.remove('TF_Dec_PP')
        if self.ATTM_TF_TL[i] == 0.0:
            cohorts.remove('TF_TL')
            land_cohorts.remove('TF_TL')

        self.cohort_list[i] = cohorts
        self.land_cohorts[i] = land_cohorts
        
        
        
    print '    done. \n  '
