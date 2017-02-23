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
        #cohorts = ['Wet_NPG', 'Wet_LCP', 'Wet_CLC', 'Wet_FCP', 'Wet_HCP', 'Lakes', 'Ponds']
        #land_cohorts = ['Wet_NPG', 'Wet_LCP', 'Wet_CLC', 'Wet_FCP', 'Wet_HCP']

        cohorts = ['Meadow_WT_Y', 'Meadow_WT_M', 'Meadow_WT_O', \
                   'LCP_WT_Y', 'LCP_WT_M', 'LCP_WT_O', \
                   'CLC_WT_Y', 'CLC_WT_M', 'CLC_WT_O', \
                   'FCP_WT_Y', 'FCP_WT_M', 'FCP_WT_O', \
                   'HCP_WT_Y', 'HCP_WT_M', 'HCP_WT_O', \
                   'Rivers_WT_Y', 'Rivers_WT_M', 'Rivers_WT_O', \
                   'LargeLakes_WT_Y', 'LargeLakes_WT_M', 'LargeLakes_WT_O', \
                   'MediumLakes_WT_Y', 'MediumLakes_WT_M', 'MediumLakes_WT_O', \
                   'SmallLakes_WT_Y', 'SmallLakes_WT_M', 'SmallLakes_WT_O', \
                   'Ponds_WT_Y', 'Ponds_WT_M', 'Ponds_WT_O', \
                   'Urban_WT', 'NoData_WT_O', \
                   'CoastalWaters_WT_O', \
                   'DrainedSlope_WT_Y', 'DrainedSlope_WT_M', 'DrainedSlope_WT_O', \
                   'SandDunes_WT_Y', 'SandDunes_WT_M', 'SandDunes_WT_O', \
                   'SaturatedBarrens_WT_Y', 'SaturatedBarrens_WT_M', 'SaturatedBarrens_WT_O', \
                   'Shrubs_WT_O' \
                   ]

        land_cohorts = ['Meadow_WT_Y', 'Meadow_WT_M', 'Meadow_WT_O', \
                        'LCP_WT_Y', 'LCP_WT_M', 'LCP_WT_O', \
                        'CLC_WT_Y', 'CLC_WT_M', 'CLC_WT_O', \
                        'FCP_WT_Y', 'FCP_WT_M', 'FCP_WT_O', \
                        'HCP_WT_Y', 'HCP_WT_M', 'HCP_WT_O', \
                        'DrainedSlope_WT_Y', 'DrainedSlope_WT_M', 'DrainedSlope_WT_O', \
                        'SandDunes_WT_Y', 'SandDunes_WT_M', 'SandDunes_WT_O', \
                        'SaturatedBarrens_WT_Y', 'SaturatedBarrens_WT_M', 'SaturatedBarrens_WT_O', \
                        'Shrubs_WT_O' , 'Urban_WT', 'NoData_WT_O' \
                        ]
        
        if self.ATTM_Meadow_WT_Y[i] == 0.0 :
            cohorts.remove('Meadow_WT_Y')
            land_cohorts.remove('Meadow_WT_Y')
        if self.ATTM_Meadow_WT_M[i] == 0.0 :
            cohorts.remove('Meadow_WT_M')
            land_cohorts.remove('Meadow_WT_M')
        if self.ATTM_Meadow_WT_Y[i] == 0.0 :
            cohorts.remove('Meadow_WT_O')
            land_cohorts.remove('Meadow_WT_O')
        if self.ATTM_LCP_WT_Y[i] == 0 :
            cohorts.remove('LCP_WT_Y')
            land_cohorts.remove('LCP_WT_Y')
        if self.ATTM_LCP_WT_M[i] == 0.0 :
            cohorts.remove('LCP_WT_M')
            land_cohorts.remove('LCP_WT_M')
        if self.ATTM_LCP_WT_O[i] == 0.0 :
            cohorts.remove('LCP_WT_O')
            land_cohorts.remove('LCP_WT_O')
        if self.ATTM_CLC_WT_Y[i] == 0.0 :
            cohorts.remove('CLC_WT_Y')
            land_cohorts.remove('CLC_WT_Y')
        if self.ATTM_CLC_WT_M[i] == 0.0 :
            cohorts.remove('CLC_WT_M')
            land_cohorts.remove('CLC_WT_M')
        if self.ATTM_CLC_WT_O[i] == 0.0:
            cohorts.remove('CLC_WT_O')
            land_cohorts.remove('CLC_WT_O')
        if self.ATTM_HCP_WT_Y[i] == 0.0:
            cohorts.remove('HCP_WT_Y')
            land_cohorts.remove('HCP_WT_Y')
        if self.ATTM_HCP_WT_M[i] == 0.0 :
            cohorts.remove('HCP_WT_M')
            land_cohorts.remove('HCP_WT_M')
        if self.ATTM_HCP_WT_O[i] == 0.0 :
            cohorts.remove('HCP_WT_O')
            land_cohorts.remove('HCP_WT_O')
        if self.ATTM_DrainedSlope_WT_Y[i] == 0:
            cohorts.remove('DrainedSlope_WT_Y')
            land_cohorts.remove('DrainedSlope_WT_Y')
        if self.ATTM_DrainedSlope_WT_M[i] == 0:
            cohorts.remove('DrainedSlope_WT_M')
            land_cohorts.remove('DrainedSlope_WT_M')
        if self.ATTM_DrainedSlope_WT_O[i] == 0.0:
            cohorts.remove('DrainedSlope_WT_O')
            land_cohorts.remove('DrainedSlope_WT_O')
        if self.ATTM_SandDunes_WT_Y[i] == 0.0:
            cohorts.remove('SandDunes_WT_Y')
            land_cohorts.remove('SandDunes_WT_Y')
        if self.ATTM_SandDunes_WT_M[i] == 0.0 :
            cohorts.remove('SandDunes_WT_M')
            land_cohorts.remove('SandDunes_WT_M')
        if self.ATTM_SandDunes_WT_O[i] == 0.0 :
            cohorts.remove('SandDunes_WT_O')
            land_cohorts.remove('SandDunes_WT_O')
        if self.ATTM_SaturatedBarrens_WT_Y[i] == 0.0 :
            cohorts.remove('SaturatedBarrens_WT_Y')
            land_cohorts.remove('SaturatedBarrens_WT_Y')
        if self.ATTM_SaturatedBarrens_WT_M[i] == 0.0 :
            cohorts.remove('SaturatedBarrens_WT_M')
            land_cohorts.remove('SaturatedBarrens_WT_M')
        if self.ATTM_SaturatedBarrens_WT_O[i] == 0.0 :
            cohorts.remove('SaturatedBarrens_WT_O')
            land_cohorts.remove('SaturatedBarrens_WT_O')
        if self.ATTM_Shrubs_WT_O[i] == 0.0 :
            cohorts.remove('Shrubs_WT_O')
            land_cohorts.remove('Shrubs_WT_O')
        if self.ATTM_Urban_WT[i] == 0.0 :
            cohorts.remove('Urban_WT')
            land_cohorts.remove('Urban_WT')
        if self.ATTM_LargeLakes_WT_Y[i] == 0.0 : cohorts.remove('LargeLakes_WT_Y')
        if self.ATTM_LargeLakes_WT_M[i] == 0.0 : cohorts.remove('LargeLakes_WT_M')
        if self.ATTM_LargeLakes_WT_O[i] == 0.0 : cohorts.remove('LargeLakes_WT_O')
        if self.ATTM_MediumLakes_WT_Y[i] == 0.0 : cohorts.remove('MediumLakes_WT_Y')
        if self.ATTM_MediumLakes_WT_M[i] == 0.0 : cohorts.remove('MediumLakes_WT_M')
        if self.ATTM_MediumLakes_WT_O[i] == 0.0 : cohorts.remove('MediumLakes_WT_O')
        if self.ATTM_SmallLakes_WT_Y[i] == 0.0 : cohorts.remove('SmallLakes_WT_Y')
        if self.ATTM_SmallLakes_WT_M[i] == 0.0 : cohorts.remove('SmallLakes_WT_M')
        if self.ATTM_SmallLakes_WT_O[i] == 0.0 : cohorts.remove('SmallLakes_WT_O')
        if self.ATTM_Ponds_WT_Y[i] == 0.0 : cohorts.remove('Ponds_WT_Y')
        if self.ATTM_Ponds_WT_M[i] == 0.0 : cohorts.remove('Ponds_WT_M')
        if self.ATTM_Ponds_WT_O[i] == 0.0 : cohorts.remove('Ponds_WT_O')
        if self.ATTM_Rivers_WT_Y[i] == 0.0 : cohorts.remove('Rivers_WT_Y')
        if self.ATTM_Rivers_WT_M[i] == 0.0 : cohorts.remove('Rivers_WT_M')
        if self.ATTM_Rivers_WT_O[i] == 0.0 : cohorts.remove('Rivers_WT_O')
        if self.ATTM_CoastalWaters_WT_O[i] == 0.0 : cohorts.remove('CoastalWaters_WT_O')
                                            
        #if self.ATTM_Wet_NPG[i] == 0.0 :
        #    cohorts.remove('Wet_NPG')
        #    land_cohorts.remove('Wet_NPG')
        #if self.ATTM_Wet_LCP[i] == 0.0 :
        #    cohorts.remove('Wet_LCP')
        #    land_cohorts.remove('Wet_LCP')
        #if self.ATTM_Wet_CLC[i] == 0.0 :
        #    cohorts.remove('Wet_CLC')
        #    land_cohorts.remove('Wet_CLC')
        #if self.ATTM_Wet_FCP[i] == 0.0 :
        #    cohorts.remove('Wet_FCP')
        #    land_cohorts.remove('Wet_FCP')
        #if self.ATTM_Wet_HCP[i] == 0.0 :
        #    cohorts.remove('Wet_HCP')
        #    land_cohorts.remove('Wet_HCP')
        #if self.ATTM_Lakes[i]   == 0.0 : cohorts.remove('Lakes')
        #if self.ATTM_Ponds[i]   == 0.0 : cohorts.remove('Ponds')

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
    
#================================================================================================
def yukon_cohort_present(self):

    # Created 6 July 2016. Bolton

    """ 
    The purpose of this module is to create a dictionary with a list of 
    each cohort in each model element. This list will be used for lake
    expansion/terrestrial cohort losses, and to short the processing time 
    (process only those cohorts present in a model element.)
    
    """
    print '    Creating a list of thermokarst susceptible cohorts.'

    self.cohort_list = {}
    self.land_cohorts = {}

    #list = Barren_Yukon, Bog_Yukon, DeciduousForest_Yukon, DwarfShrub_Yukon, EvergreenForest_Yukon,
    #       Fen_Yukon, Lake_Yukon, Pond_Yukon, River_Yukon, ShrubScrub_Yukon, Unclassified_Yukon

    for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
        
        cohorts = ['Barren_Yukon', 'Bog_Yukon', 'DeciduousForest_Yukon', 'DwarfShrub_Yukon', \
                   'EvergreenForest_Yukon', 'Fen_Yukon', 'Lake_Yukon', 'Pond_Yukon', 'River_Yukon', \
                   'ShrubScrub_Yukon', 'Unclassified_Yukon']

        land_cohorts = ['Barren_Yukon', 'Bog_Yukon', 'DeciduousForest_Yukon', 'DwarfShrub_Yukon', \
                        'EvergreenForest_Yukon', 'Fen_Yukon', 'ShrubScrub_Yukon', 'Unclassified_Yukon']

        if self.ATTM_Barren_Yukon[i] == 0.0:
            cohorts.remove('Barren_Yukon')
            land_cohorts.remove('Barren_Yukon')
        if self.ATTM_Bog_Yukon[i] == 0.0:
            cohorts.remove('Bog_Yukon')
            land_cohorts.remove('Bog_Yukon')
        if self.ATTM_DeciduousForest_Yukon[i] == 0.0:
            cohorts.remove('DeciduousForest_Yukon')
            land_cohorts.remove('DeciduousForest_Yukon')
        if self.ATTM_DwarfShrub_Yukon[i] == 0.0:
            cohorts.remove('DwarfShrub_Yukon')
            land_cohorts.remove('DwarfShrub_Yukon')
        if self.ATTM_EvergreenForest_Yukon[i]== 0.0:
            cohorts.remove('EvergreenForest_Yukon')
            land_cohorts.remove('EvergreenForest_Yukon')
        if self.ATTM_Fen_Yukon[i] == 0.0:
            cohorts.remove('Fen_Yukon')
            land_cohorts.remove('Fen_Yukon')
        if self.ATTM_Lake_Yukon[i] == 0.0:
            cohorts.remove('Lake_Yukon')
        if self.ATTM_Pond_Yukon[i] == 0.0:
            cohorts.remove('Pond_Yukon')
        if self.ATTM_River_Yukon[i] == 0.0:
            cohorts.remove('River_Yukon')
        if self.ATTM_ShrubScrub_Yukon[i] == 0.0:
            cohorts.remove('ShrubScrub_Yukon')
            land_cohorts.remove('ShrubScrub_Yukon')
        if self.ATTM_Unclassified_Yukon[i] == 0.0:
            cohorts.remove('Unclassified_Yukon')
            land_cohorts.remove('Unclassified_Yukon')

        self.cohort_list[i] = cohorts
        self.land_cohorts[i] = land_cohorts
    
    print '    done. \n  '
