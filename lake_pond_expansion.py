import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
from decimal import *

getcontext().prec = 4       # Set a new precision


def lake_pond_expansion(self, element):
    """
    If a lake or pond exists in an element, expand it by the prescribed rate.

    There is a corresponding reduction in land area to all cohorts following
    expansion.
    """
    
    ##########################################################################################
    #               LAKES 
    ##########################################################################################
    ATTM_Lake_Total = self.ATTM_LargeLakes_WT_Y[element] + self.ATTM_LargeLakes_WT_M[element] + \
                      self.ATTM_LargeLakes_WT_M[element] + self.ATTM_MediumLakes_WT_Y[element] + \
                      self.ATTM_MediumLakes_WT_M[element] + self.ATTM_MediumLakes_WT_O[element] + \
                      self.ATTM_SmallLakes_WT_Y[element] + self.ATTM_SmallLakes_WT_M[element] + \
                      self.ATTM_SmallLakes_WT_O[element]
                      
    #if self.ATTM_Lakes[element] > 0.0 and self.ATTM_Lakes[element] < 1.0 :
    if ATTM_Lake_Total > 0.0 and ATTM_Lake_Total < 1.0 :
        # --------------------------------------------------
        # Determine the fractional amount of lake expansion
        # --------------------------------------------------
        if self.climate_expansion_lakes[element] == 1.0:
            #lake_fraction_increase = self.ATTM_Lakes[element] * self.LakePond['Lake_Expansion'] * 2.0
            largelake_wt_y_increase = self.ATTM_LargeLakes_WT_Y[element] * \
              self.LakePond['LargeLake_WT_Y_Expansion'] * 2.0
            largelake_wt_m_increase = self.ATTM_LargeLakes_WT_M[element] * \
              self.LakePond['LargeLake_WT_M_Expansion'] * 2.0
            largelake_wt_o_increase = self.ATTM_LargeLakes_WT_O[element] * \
              self.LakePond['LargeLake_WT_O_Expansion'] * 2.0
            mediumlake_wt_y_increase = self.ATTM_MediumLakes_WT_Y[element] * \
              self.LakePond['MediumLake_WT_Y_Expansion'] * 2.0
            mediumlake_wt_m_increase = self.ATTM_MediumLakes_WT_M[element] * \
              self.LakePond['MediumLake_WT_M_Expansion'] * 2.0
            mediumlake_wt_o_increase = self.ATTM_MediumLakes_WT_O[element] * \
              self.LakePond['MediumLake_WT_O_Expansion'] * 2.0
            smalllake_wt_y_increase = self.ATTM_SmallLakes_WT_Y[element] * \
              self.LakePond['SmallLake_WT_Y_Expansion'] * 2.0
            smalllake_wt_m_increase = self.ATTM_SmallLakes_WT_M[element] * \
              self.LakePond['SmallLake_WT_M_Expansion'] * 2.0
            smalllake_wt_o_increase = self.ATTM_SmallLakes_WT_O[element] * \
              self.LakePond['SmallLake_WT_O_Expansion'] * 2.0
            
            self.climate_expansion_lakes[element] = 0.0
        else:
            largelake_wt_y_increase = self.ATTM_LargeLakes_WT_Y[element] * \
              self.LakePond['LargeLake_WT_Y_Expansion'] 
            largelake_wt_m_increase = self.ATTM_LargeLakes_WT_M[element] * \
              self.LakePond['LargeLake_WT_M_Expansion'] 
            largelake_wt_o_increase = self.ATTM_LargeLakes_WT_O[element] * \
              self.LakePond['LargeLake_WT_O_Expansion'] 
            mediumlake_wt_y_increase = self.ATTM_MediumLakes_WT_Y[element] * \
              self.LakePond['MediumLake_WT_Y_Expansion']
            mediumlake_wt_m_increase = self.ATTM_MediumLakes_WT_M[element] * \
              self.LakePond['MediumLake_WT_M_Expansion']
            mediumlake_wt_o_increase = self.ATTM_MediumLakes_WT_O[element] * \
              self.LakePond['MediumLake_WT_O_Expansion']
            smalllake_wt_y_increase = self.ATTM_SmallLakes_WT_Y[element] * \
              self.LakePond['SmallLake_WT_Y_Expansion'] 
            smalllake_wt_m_increase = self.ATTM_SmallLakes_WT_M[element] * \
              self.LakePond['SmallLake_WT_M_Expansion'] 
            smalllake_wt_o_increase = self.ATTM_SmallLakes_WT_O[element] * \
              self.LakePond['SmallLake_WT_O_Expansion']

        lake_fraction_increase = largelake_wt_y_increase + largelake_wt_m_increase + \
                                 largelake_wt_o_increase + mediumlake_wt_y_increase + \
                                 mediumlake_wt_m_increase + mediumlake_wt_o_increase + \
                                 smalllake_wt_y_increase + smalllake_wt_m_increase + \
                                 smalllake_wt_o_increase
            
 #       land_available = self.ATTM_Wet_NPG[element] + self.ATTM_Wet_LCP[element] + \
 #                        self.ATTM_Wet_CLC[element] + self.ATTM_Wet_FCP[element] + \
 #                        self.ATTM_Wet_HCP[element] + self.ATTM_Gra_NPG[element] + \
 #                        self.ATTM_Gra_LCP[element] + self.ATTM_Gra_FCP[element] + \
 #                        self.ATTM_Gra_HCP[element] + self.ATTM_Shr_NPG[element] + \
 #                        self.ATTM_Shr_LCP[element] + self.ATTM_Shr_FCP[element] + \
 #                        self.ATTM_Shr_HCP[element]

        land_available = self.ATTM_CLC_WT_Y[element] + self.ATTM_CLC_WT_M[element] + \
                         self.ATTM_CLC_WT_O[element] + self.ATTM_CoastalWaters_WT_O[element] + \
                         self.ATTM_DrainedSlope_WT_Y[element] + self.ATTM_DrainedSlope_WT_M[element] + \
                         self.ATTM_DrainedSlope_WT_O[element] + self.ATTM_FCP_WT_Y[element] + \
                         self.ATTM_FCP_WT_M[element] + self.ATTM_FCP_WT_O[element] + \
                         self.ATTM_HCP_WT_Y[element] + self.ATTM_HCP_WT_M[element] + \
                         self.ATTM_HCP_WT_O[element] + self.ATTM_LCP_WT_Y[element] + \
                         self.ATTM_LCP_WT_M[element] + self.ATTM_LCP_WT_O[element] + \
                         self.ATTM_Meadow_WT_Y[element] + self.ATTM_Meadow_WT_M[element] + \
                         self.ATTM_Meadow_WT_O[element] + self.ATTM_NoData_WT_O[element] + \
                         self.ATTM_SandDunes_WT_Y[element] + self.ATTM_SandDunes_WT_M[element] + \
                         self.ATTM_SandDunes_WT_O[element] + self.ATTM_SaturatedBarrens_WT_Y[element] + \
                         self.ATTM_SaturatedBarrens_WT_M[element] + self.ATTM_SaturatedBarrens_WT_O[element] + \
                         self.ATTM_Shrubs_WT_O[element]

        
        # ==================================================================================
        # Case 0:
        #    The sum of the fractional lake area + lake_fraction_increase >= the available
        #    land available for pond expansion (not expanding into rivers, urban, lakes).
        #
        #    In this case, the fractional lake area is equal to the total amount of land
        #    cohorts and all the land cohorts are set to 0.0
        # ==================================================================================
        if lake_fraction_increase >= land_available:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            self.ATTM_LargeLakes_WT_Y[element] = self.ATTM_LargeLakes_WT_Y[element] + \
              ((self.ATTM_LargeLakes_WT_Y[element] / ATTM_Lake_Total) * land_available)
            self.ATTM_LargeLakes_WT_M[element] = self.ATTM_LargeLakes_WT_M[element] + \
              ((self.ATTM_LargeLakes_WT_M[element] / ATTM_Lake_Total) * land_available)
            self.ATTM_LargeLakes_WT_O[element] = self.ATTM_LargeLakes_WT_O[element] + \
              ((self.ATTM_LargeLakes_WT_O[element] / ATTM_Lake_Total) * land_available)
            self.ATTM_MediumLakes_WT_Y[element] = self.ATTM_MediumLakes_WT_Y[element] + \
              ((self.ATTM_MediumLakes_WT_Y[element] / ATTM_Lake_Total) * land_available)
            self.ATTM_MediumLakes_WT_M[element] = self.ATTM_MediumLakes_WT_M[element] + \
              ((self.ATTM_MediumLakes_WT_M[element] / ATTM_Lake_Total) * land_available)
            self.ATTM_MediumLakes_WT_O[element] = self.ATTM_MediumLakes_WT_O[element] + \
              ((self.ATTM_MediumLakes_WT_O[element] / ATTM_Lake_Total) * land_available)
            self.ATTM_SmallLakes_WT_Y[element] = self.ATTM_SmallLakes_WT_Y[element] + \
              ((self.ATTM_SmallLakes_WT_Y[element] / ATTM_Lake_Total) * land_available)
            self.ATTM_SmallLakes_WT_M[element] = self.ATTM_SmallLakes_WT_M[element] + \
              ((self.ATTM_SmallLakes_WT_M[element] / ATTM_Lake_Total) * land_available)
            self.ATTM_SmallLakes_WT_O[element] = self.ATTM_SmallLakes_WT_O[element] + \
              ((self.ATTM_SmallLakes_WT_O[element] / ATTM_Lake_Total) * land_available)
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            self.ATTM_CLC_WT_Y[element] = 0.0
#            if 'CLC_WT_Y' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('CLC_WT_Y')

            self.ATTM_CLC_WT_M[element] = 0.0
#            if 'CLC_WT_M' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('CLC_WT_M')
            
            self.ATTM_CLC_WT_O[element] = 0.0
#            if 'CLC_WT_O' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('CLC_WT_O')

            self.ATTM_DrainedSlope_WT_Y[element] = 0.0
#           if 'DrainedSlope_WT_Y' in self.land_cohorts[element]:
#               self.land_cohorts[element].remove('DrainedSlope_WT_Y')

            self.ATTM_DrainedSlope_WT_M[element] = 0.0
#            if 'DrainedSlope_WT_M' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('DrainedSlope_WT_M')

            self.ATTM_DrainedSlope_WT_O[element] = 0.0
#            if 'DrainedSlope_WT_O' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('DrainedSlope_WT_O')

            self.ATTM_FCP_WT_Y[element] = 0.0
#            if 'FCP_WT_Y' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('FCP_WT_Y')

            self.ATTM_FCP_WT_M[element] = 0.0
#            if 'FCP_WT_M' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('FCP_WT_O')

            self.ATTM_HCP_WT_Y[element] = 0.0
#            if 'HCP_WT_Y' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('HCP_WT_Y')

            self.ATTM_HCP_WT_M[element] = 0.0
#            if 'HCP_WT_M' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('HCP_WT_M')

            self.ATTM_HCP_WT_O[element] = 0.0
#            if 'HCP_WT_O' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('HCP_WT_O')

            self.ATTM_LCP_WT_Y[element] = 0.0
#            if 'LCP_WT_Y' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('LCP_WT_Y')

            self.ATTM_LCP_WT_M[element] = 0.0
#            if 'LCP_WT_M' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('LCP_WT_M')

            self.ATTM_LCP_WT_O[element] = 0.0
#            if 'LCP_WT_O' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('LCP_WT_O')

            self.ATTM_Meadow_WT_Y[element] = 0.0
#            if 'Meadow_WT_Y' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Meadow_WT_Y')

            self.ATTM_Meadow_WT_M[element] = 0.0
#            if 'Meadow_WT_M' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Meadow_WT_M')

            self.ATTM_Meadow_WT_O[element] = 0.0
#            if 'Meadow_WT_O' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Meadow_WT_O')

            self.ATTM_SandDunes_WT_Y[element]  = 0.0
#            if 'SandDunes_WT_Y' in self.land_cohort[element]:
#                self.land_cohorts[element].remove('SandDunes_WT_Y')

            self.ATTM_SandDunes_WT_M[element] = 0.0
#            if 'SandDunes_WT_M' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('SandDunes_WT_M')

            self.ATTM_SandDunes_WT_O[element] = 0.0
#            if 'SandDunes_WT_O' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('SandDunes_WT_O')

            self.ATTM_SaturatedBarrens_WT_Y[element] = 0.0
#            if 'SaturatedBarrens_WT_Y' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('SaturatedBarrens_WT_Y')

            self.ATTM_SaturatedBarrens_WT_M[element] = 0.0
#            if 'SaturatedBarrens_WT_M' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('SaturatedBarrens_WT_M')

            self.ATTM_SaturatedBarrens_WT_O[element] = 0.0
#            if 'SaturatedBarrens_WT_O' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('SaturatedBarrens_WT_O')

            self.ATTM_Shrubs_WT_O[element] = 0.0
#            if 'Shrubs_WT_O' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Shrubs_WT_O')

            self.ATTM_NoData_WT_O[element] = 0.0
#            if 'NoData_WT_O' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('NoData_WT_O')
            
#            self.ATTM_Wet_NPG[element] = 0.0
#            if 'Wet_NPG' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Wet_NPG')
#            self.ATTM_Wet_LCP[element] = 0.0
#           if 'Wet_LCP' in self.land_cohorts[element]:
#               self.land_cohorts[element].remove('Wet_LCP')
#           self.ATTM_Wet_CLC[element] = 0.0
#           if 'Wet_CLC' in self.land_cohorts[element]:
#               self.land_cohorts[element].remove('Wet_CLC')
#           self.ATTM_Wet_FCP[element] = 0.0
#           if 'Wet_FCP' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Wet_FCP')
#            self.ATTM_Wet_HCP[element] = 0.0
#            if 'Wet_HCP' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Wet_HCP')
#            self.ATTM_Gra_NPG[element] = 0.0
#            if 'Gra_NPG' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Gra_NPG')
#            self.ATTM_Gra_LCP[element] = 0.0
#            if 'Gra_LCP' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Gra_LCP')
#            self.ATTM_Gra_FCP[element] = 0.0
#            if 'Gra_FCP' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Gra_FCP')
#            self.ATTM_Gra_HCP[element] = 0.0
#            if 'Gra_HCP' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Gra_HCP')
#            self.ATTM_Shr_NPG[element] = 0.0
#            if 'Shr_NPG' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Shr_NPG')
#            self.ATTM_Shr_LCP[element] = 0.0
#            if 'Shr_LCP' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Shr_LCP')
#            self.ATTM_Shr_FCP[element] = 0.0
#            if 'Shr_FCP' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Shr_FCP')
#            self.ATTM_Shr_HCP[element] = 0.0
#            if 'Shr_HCP' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Shr_HCP')
            
        # ==================================================================================
        # Case 1:
        #   The sum of all the land cohorts exceeds the fractional amount of lake
        #   area increase. However, one or more of the land cohorts has a fractional area
        #   less than (or equal to) the lake_proportional_reduction value.  In this case,
        #   the land cohort(s) with the fractional areas less than the lake_proportional_area
        #   are reduced to zero and the excess expansion is carried by the remaining cohorts.
        #
        #   This case may result in a cascading reduction of cohorts.  For example, if on the
        #   first pass one land cohort is zeroed out, the remaining fractional reduction added
        #   to the remaining cohorts may result in a lake_proportional_area being greater than
        #   one of the remaining land cohorts.  In this case, the 2nd cohort will need to be
        #   zeroed out and the remaining lake area expansion is passed on to the remaining
        #   land cohorts.
        # -----------------------------------------------------------------------------------
#        elif len(self.land_cohorts[element]) == 0.0:   #### 11 Oct 2016. I can't remember what this does!
#                                                       ####              Or why this is included
#                 #self.ATTM_Lakes[element] = self.ATTM_Lakes[element]
#            self.ATTM_LargeLakes_WT_Y[element] = self.ATTM_LargeLakes_WT_Y[element]
#            self.ATTM_LargeLakes_WT_M[element] = self.ATTM_LargeLakes_WT_M[element]
#            self.ATTM_LargeLakes_WT_O[element] = self.ATTM_LargeLakes_WT_O[element]
#            self.ATTM_MediumLakes_WT_Y[element] = self.ATTM_MediumLakes_WT_Y[element]
#            self.ATTM_MediumLakes_WT_M[element] = self.ATTM_MediumLakes_WT_M[element]
#            self.ATTM_MediumLakes_WT_O[element] = self.ATTM_MediumLakes_WT_O[element]
#            self.ATTM_SmallLakes_WT_Y[element] = self.ATTM_SmallLakes_WT_Y[element]
#            self.ATTM_SmallLakes_WT_M[element] = self.ATTM_SmallLakes_WT_M[element]
#            self.ATTM_SmallLakes_WT_O[element] = self.ATTM_SmallLakes_WT_O[element]
            
        else:             # land_available > lake_fraction_increase:
            #self.ATTM_Lakes[element] = self.ATTM_Lakes[element] + lake_fraction_increase
            self.ATTM_LargeLakes_WT_Y[element] = self.ATTM_LargeLakes_WT_Y[element] + largelake_wt_y_increase
            self.ATTM_LargeLakes_WT_M[element] = self.ATTM_LargeLakes_WT_M[element] + largelake_wt_m_increase
            self.ATTM_LargeLakes_WT_O[element] = self.ATTM_LargeLakes_WT_O[element] + largelake_wt_o_increase
            self.ATTM_MediumLakes_WT_Y[element] = self.ATTM_MediumLakes_WT_Y[element] + mediumlake_wt_y_increase
            self.ATTM_MediumLakes_WT_M[element] = self.ATTM_MediumLakes_WT_M[element] + mediumlake_wt_m_increase
            self.ATTM_MediumLakes_WT_O[element] = self.ATTM_MediumLakes_WT_O[element] + mediumlake_wt_o_increase
            self.ATTM_SmallLakes_WT_Y[element] = self.ATTM_SmallLakes_WT_Y[element] + smalllake_wt_y_increase
            self.ATTM_SmallLakes_WT_M[element] = self.ATTM_SmallLakes_WT_M[element] + smalllake_wt_m_increase
            self.ATTM_SmallLakes_WT_O[element] = self.ATTM_SmallLakes_WT_O[element] + smalllake_wt_o_increase
            
#            cohort_reduction = lake_fraction_increase / len(self.land_cohorts[element])

            # -------------------------------------
            # Reduce all appropriate land cohorts
            # -------------------------------------
            not_enough_land = 0.0
            not_enough_land_count = 0.0
            land_count = 0.0
            lake_count = 0.0
            # Determine land cohorts available for reduction in element
            if self.ATTM_CLC_WT_Y[element] > 0.0: land_count = land_count + 1
            if self.ATTM_CLC_WT_M[element] > 0.0: land_count = land_count + 1
            if self.ATTM_CLC_WT_O[element] > 0.0: land_count = land_count + 1
            if self.ATTM_CoastalWaters_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_DrainedSlope_WT_Y[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_DrainedSlope_WT_M[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_DrainedSlope_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_FCP_WT_Y[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_FCP_WT_M[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_FCP_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_HCP_WT_Y[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_HCP_WT_M[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_HCP_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_LCP_WT_Y[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_LCP_WT_M[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_LCP_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_Meadow_WT_Y[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_Meadow_WT_M[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_Meadow_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_NoData_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_SandDunes_WT_Y[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_SandDunes_WT_M[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_SandDunes_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_SaturatedBarrens_WT_Y[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_SaturatedBarrens_WT_M[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_SaturatedBarrens_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_Shrubs_WT_O[element] > 0.0 : land_count = land_count + 1
            # Determine proportional reduction for land cohorts present
            cohort_reduction = lake_fraction_increase / land_count
            # Sequence through land cohorts and reduce as appropriate
            if self.ATTM_CLC_WT_Y[element] > 0.0:
                self.ATTM_CLC_WT_Y[element] = self.ATTM_CLC_WT_Y[element] - cohort_reduction
                if self.ATTM_CLC_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_CLC_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_CLC_WT_Y[element] = 0.0
            if self.ATTM_CLC_WT_M[element] > 0.0:
                self.ATTM_CLC_WT_M[element] = self.ATTM_CLC_WT_M[element] - cohort_reduction
                if self.ATTM_CLC_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_CLC_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_CLC_WT_M[element] = 0.0
            if self.ATTM_CLC_WT_O[element] > 0.0:
                self.ATTM_CLC_WT_O[element] = self.ATTM_CLC_WT_O[element] - cohort_reduction
                if self.ATTM_CLC_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_CLC_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_CLC_WT_O[element] = 0.0
            if self.ATTM_CoastalWaters_WT_O[element] > 0.0:
                self.ATTM_CoastalWaters_WT_O[element] = self.ATTM_CoastalWaters_WT_O[element] - cohort_reduction
                if self.ATTM_CoastalWaters_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_CoastalWaters_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_CoastalWaters_WT_O[element] = 0.0                    
            if self.ATTM_DrainedSlope_WT_Y[element] > 0.0:
                self.ATTM_DrainedSlope_WT_Y[element] = self.ATTM_DrainedSlope_WT_Y[element] - cohort_reduction
                if self.ATTM_DrainedSlope_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_DrainedSlope_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_DrainedSlope_WT_Y[element] = 0.0
            if self.ATTM_DrainedSlope_WT_M[element] > 0.0:
                self.ATTM_DrainedSlope_WT_M[element] = self.ATTM_DrainedSlope_WT_M[element] - cohort_reduction
                if self.ATTM_DrainedSlope_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_DrainedSlope_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_DrainedSlope_WT_M[element] = 0.0
            if self.ATTM_DrainedSlope_WT_O[element] > 0.0:
                self.ATTM_DrainedSlope_WT_O[element] = self.ATTM_DrainedSlope_WT_O[element] - cohort_reduction
                if self.ATTM_DrainedSlope_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_DrainedSlope_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_DrainedSlope_WT_O[element] = 0.0
            if self.ATTM_FCP_WT_Y[element] > 0.0:
                self.ATTM_FCP_WT_Y[element] = self.ATTM_FCP_WT_Y[element] - cohort_reduction
                if self.ATTM_FCP_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_FCP_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_FCP_WT_Y[element] = 0.0
            if self.ATTM_FCP_WT_M[element] > 0.0:
                self.ATTM_FCP_WT_M[element] = self.ATTM_FCP_WT_M[element] - cohort_reduction
                if self.ATTM_FCP_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_FCP_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_FCP_WT_M[element] = 0.0
            if self.ATTM_FCP_WT_O[element] > 0.0:
                self.ATTM_FCP_WT_O[element] = self.ATTM_FCP_WT_O[element] - cohort_reduction
                if self.ATTM_FCP_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_FCP_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_FCP_WT_O[element] = 0.0
            if self.ATTM_HCP_WT_Y[element] > 0.0:
                self.ATTM_HCP_WT_Y[element] = self.ATTM_HCP_WT_Y[element] - cohort_reduction
                if self.ATTM_HCP_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_HCP_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_HCP_WT_Y[element] = 0.0
            if self.ATTM_HCP_WT_M[element] > 0.0:
                self.ATTM_HCP_WT_M[element] = self.ATTM_HCP_WT_M[element] - cohort_reduction
                if self.ATTM_HCP_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_HCP_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_HCP_WT_M[element] = 0.0
            if self.ATTM_HCP_WT_O[element] > 0.0:
                self.ATTM_HCP_WT_O[element] = self.ATTM_HCP_WT_O[element] - cohort_reduction
                if self.ATTM_HCP_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_HCP_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_HCP_WT_O[element] = 0.0
            if self.ATTM_LCP_WT_Y[element] > 0.0:
                self.ATTM_LCP_WT_Y[element] = self.ATTM_LCP_WT_Y[element] - cohort_reduction
                if self.ATTM_LCP_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_LCP_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_LCP_WT_Y[element] = 0.0
            if self.ATTM_LCP_WT_M[element] > 0.0:
                self.ATTM_LCP_WT_M[element] = self.ATTM_LCP_WT_M[element] - cohort_reduction
                if self.ATTM_LCP_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_LCP_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_LCP_WT_M[element] = 0.0
            if self.ATTM_LCP_WT_O[element] > 0.0:
                self.ATTM_LCP_WT_O[element] = self.ATTM_LCP_WT_O[element] - cohort_reduction
                if self.ATTM_LCP_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_LCP_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_LCP_WT_O[element] = 0.0
            if self.ATTM_Meadow_WT_Y[element] > 0.0:
                self.ATTM_Meadow_WT_Y[element] = self.ATTM_Meadow_WT_Y[element] - cohort_reduction
                if self.ATTM_Meadow_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Meadow_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_Meadow_WT_Y[element] = 0.0
            if self.ATTM_Meadow_WT_M[element] > 0.0:
                self.ATTM_Meadow_WT_M[element] = self.ATTM_Meadow_WT_M[element] - cohort_reduction
                if self.ATTM_Meadow_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Meadow_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_Meadow_WT_M[element] = 0.0
            if self.ATTM_Meadow_WT_O[element] > 0.0:
                self.ATTM_Meadow_WT_O[element] = self.ATTM_Meadow_WT_O[element] - cohort_reduction
                if self.ATTM_Meadow_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Meadow_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_Meadow_WT_O[element] = 0.0
            if self.ATTM_SandDunes_WT_Y[element] > 0.0:
                self.ATTM_SandDunes_WT_Y[element] = self.ATTM_SandDunes_WT_Y[element] - cohort_reduction
                if self.ATTM_SandDunes_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_SandDunes_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_SandDunes_WT_Y[element] = 0.0
            if self.ATTM_SandDunes_WT_M[element] > 0.0:
                self.ATTM_SandDunes_WT_M[element] = self.ATTM_SandDunes_WT_M[element] - cohort_reduction
                if self.ATTM_SandDunes_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_SandDunes_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_SandDunes_WT_M[element] = 0.0
            if self.ATTM_SandDunes_WT_O[element] > 0.0:
                self.ATTM_SandDunes_WT_O[element] = self.ATTM_SandDunes_WT_O[element] - cohort_reduction
                if self.ATTM_SandDunes_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_SandDunes_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_SandDunes_WT_O[element] = 0.0
            if self.ATTM_NoData_WT_O[element] > 0.0:
                self.ATTM_NoData_WT_O[element] = self.ATTM_NoData_WT_O[element] - cohort_reduction
                if self.ATTM_NoData_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_NoData_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_NoData_WT_O[element] = 0.0
            if self.ATTM_SaturatedBarrens_WT_Y[element] > 0.0:
                self.ATTM_SaturatedBarrens_WT_Y[element] = self.ATTM_SaturatedBarrens_WT_Y[element] - cohort_reduction
                if self.ATTM_SaturatedBarrens_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_SaturatedBarrens_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_SaturatedBarrens_WT_Y[element] = 0.0
            if self.ATTM_SaturatedBarrens_WT_M[element] > 0.0:
                self.ATTM_SaturatedBarrens_WT_M[element] = self.ATTM_SaturatedBarrens_WT_M[element] - cohort_reduction
                if self.ATTM_SaturatedBarrens_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_SaturatedBarrens_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_SaturatedBarrens_WT_M[element] = 0.0
            if self.ATTM_SaturatedBarrens_WT_O[element] > 0.0:
                self.ATTM_SaturatedBarrens_WT_O[element] = self.ATTM_SaturatedBarrens_WT_O[element] - cohort_reduction
                if self.ATTM_SaturatedBarrens_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_SaturatedBarrens_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_SaturatedBarrens_WT_O[element] = 0.0                 
            if self.ATTM_Shrubs_WT_O[element] > 0.0:
                self.ATTM_Shrubs_WT_O[element] = self.ATTM_Shrubs_WT_O[element] - cohort_reduction
                if self.ATTM_Shrubs_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Shrubs_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_Shrubss_WT_O[element] = 0.0             
            # If not_enough_land_count is > 0, reduce size of lake
            if self.ATTM_LargeLakes_WT_Y[element] > 0. : lake_count = lake_count + 1.
            if self.ATTM_LargeLakes_WT_M[element] > 0. : lake_count = lake_count + 1.
            if self.ATTM_LargeLakes_WT_O[element] > 0. : lake_count = lake_count + 1.
            if self.ATTM_MediumLakes_WT_Y[element] > 0. : lake_count = lake_count + 1.
            if self.ATTM_MediumLakes_WT_M[element] > 0. : lake_count = lake_count + 1.
            if self.ATTM_MediumLakes_WT_O[element] > 0. : lake_count = lake_count + 1.
            if self.ATTM_SmallLakes_WT_Y[element] > 0. : lake_count = lake_count + 1.
            if self.ATTM_SmallLakes_WT_M[element] > 0. : lake_count = lake_count + 1.
            if self.ATTM_SmallLakes_WT_O[element] > 0. : lake_count = lake_count + 1.

            lake_reduction = not_enough_land / lake_count

            if self.ATTM_LargeLakes_WT_Y[element] > 0. :
                self.ATTM_LargeLakes_WT_Y[element] = self.ATTM_LargeLakes_WT_Y[element] - lake_reduction
            if self.ATTM_LargeLakes_WT_M[element] > 0. :
                self.ATTM_LargeLakes_WT_M[element] = self.ATTM_LargeLakes_WT_M[element] - lake_reduction
            if self.ATTM_LargeLakes_WT_O[element] > 0. :
                self.ATTM_LargeLakes_WT_O[element] = self.ATTM_LargeLakes_WT_O[element] - lake_reduction
            if self.ATTM_MediumLakes_WT_Y[element] > 0. :
                self.ATTM_MediumLakes_WT_Y[element] = self.ATTM_MediumLakes_WT_Y[element] - lake_reduction
            if self.ATTM_MediumLakes_WT_M[element] > 0. :
                self.ATTM_MediumLakes_WT_M[element] = self.ATTM_MediumLakes_WT_M[element] - lake_reduction
            if self.ATTM_MediumLakes_WT_O[element] > 0. :
                self.ATTM_MediumLakes_WT_O[element] = self.ATTM_MediumLakes_WT_O[element] - lake_reduction
            if self.ATTM_SmallLakes_WT_Y[element] > 0. :
                self.ATTM_SmallLakes_WT_Y[element] = self.ATTM_SmallLakes_WT_Y[element] - lake_reduction
            if self.ATTM_SmallLakes_WT_M [element] > 0. :
                self.ATTM_SmallLakes_WT_M[element] = self.ATTM_SmallLakes_WT_M[element] - lake_reduction
            if self.ATTM_SmallLakes_WT_O[element] > 0. :
                self.ATTM_SmallLakes_WT_O[element] = self.ATTM_SmallLakes_WT_O[element] - lake_reduction
        #-------------------------------------------------------------------------------
        # Check to ensure the fractional lake area does not exceed 1.0
        #
        # If Lake area is greater than or equal to 1., assume 1 large lake for the element that will
        # be divided up between the young, medium, and old age components (based upon
        # fractional relationship between young, medium and old age lakes).
        #
        # All other cohorts are also zeroed out (precaution/check).
        #--------------------------------------------------------------------------------
        ATTM_Lake_Area  = self.ATTM_LargeLakes_WT_Y[element] + self.ATTM_LargeLakes_WT_M[element] + \
                          self.ATTM_LargeLakes_WT_M[element] + self.ATTM_MediumLakes_WT_Y[element] + \
                          self.ATTM_MediumLakes_WT_M[element] + self.ATTM_MediumLakes_WT_O[element] + \
                          self.ATTM_SmallLakes_WT_Y[element] + self.ATTM_SmallLakes_WT_M[element] + \
                          self.ATTM_SmallLakes_WT_O[element]

        if ATTM_Lake_Area >= 1.0:
            large_lake_total = self.ATTM_LargeLakes_WT_Y[element] + self.ATTM_LargeLakes_WT_M[element] + \
              self.ATTM_LargeLakes_WT_O[element]

            self.ATTM_LargeLakes_WT_Y[element] = self.ATTM_LargeLakes_WT_Y[element] / large_lake_total
            self.ATTM_LargeLakes_WT_M[element] = self.ATTM_LargeLakes_WT_M[element] / large_lake_total
            self.ATTM_LargeLakes_WT_O[element] = self.ATTM_LargeLakes_WT_O[element] / large_lake_total
            self.ATTM_MediumLakes_WT_Y[element] = 0.0
            self.ATTM_MediumLakes_WT_M[element] = 0.0
            self.ATTM_MediumLakes_WT_O[element] = 0.0
            self.ATTM_SmallLakes_WT_Y[element] = 0.0
            self.ATTM_SmallLakes_WT_M[element] = 0.0
            self.ATTM_SmallLakes_WT_O[element] = 0.0
            
            self.ATTM_CLC_WT_Y[element] = 0.0
            self.ATTM_CLC_WT_M[element] = 0.0
            self.ATTM_CLC_WT_O[element] = 0.0
            self.ATTM_CoastalWaters_WT_O[element] = 0.0
            self.ATTM_DrainedSlope_WT_Y[element] = 0.0
            self.ATTM_DrainedSlope_WT_M[element] = 0.0
            self.ATTM_DrainedSlope_WT_O[element] = 0.0
            self.ATTM_FCP_WT_Y[element] = 0.0
            self.ATTM_FCP_WT_M[element] = 0.0
            self.ATTM_FCP_WT_O[element] = 0.0
            self.ATTM_HCP_WT_Y[element] = 0.0
            self.ATTM_HCP_WT_M[element] = 0.0
            self.ATTM_HCP_WT_O[element] = 0.0
            self.ATTM_LCP_WT_Y[element] = 0.0
            self.ATTM_LCP_WT_M[element] = 0.0
            self.ATTM_LCP_WT_O[element] = 0.0
            self.ATTM_Meadow_WT_Y[element] = 0.0
            self.ATTM_Meadow_WT_M[element] = 0.0
            self.ATTM_Meadow_WT_O[element] = 0.0
            self.ATTM_NoData_WT_O[element] = 0.0
            self.ATTM_SandDunes_WT_Y[element] = 0.0
            self.ATTM_SandDunes_WT_M[element] = 0.0
            self.ATTM_SandDunes_WT_O[element] = 0.0
            self.SaturatedBarrens_WT_Y[element] = 0.0
            self.SaturatedBarrens_WT_M[element] = 0.0
            self.SaturatedBarrens_WT_O[element] = 0.0
            self.Shrubs_WT_O[element] = 0.0
            self.Urban_WT[element] = 0.0
            self.Rivers_WT_O[element] = 0.0
            self.Rivers_WT_M[element] = 0.0
            self.Rivers_WT_Y[element] = 0.0
            self.Ponds_WT_Y[element] = 0.0
            self.Ponds_WT_M[element] = 0.0
            self.Ponds_WT_O[element] = 0.0
            
#            if 'Wet_NPG' in self.land_cohorts[element]:
#                self.ATTM_Wet_NPG[element] = self.ATTM_Wet_NPG[element] - cohort_reduction
#                if self.ATTM_Wet_NPG[element] < 0.0:
#                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_NPG[element])
#                    self.ATTM_Wet_NPG[element] = 0.0
#                    self.land_cohorts[element].remove('Wet_NPG')
#            if 'Wet_LCP' in self.land_cohorts[element]:
#                self.ATTM_Wet_LCP[element] = self.ATTM_Wet_LCP[element] - cohort_reduction
#                if self.ATTM_Wet_LCP[element] < 0.0:
#                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_LCP[element])
#                    self.ATTM_Wet_LCP[element] = 0.0
#                    self.land_cohorts[element].remove('Wet_LCP')
#            if 'Wet_CLC' in self.land_cohorts[element]:
#                self.ATTM_Wet_CLC[element] = self.ATTM_Wet_CLC[element] - cohort_reduction
#                if self.ATTM_Wet_CLC[element] < 0.0 :
#                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_CLC[element])
#                    self.ATTM_Wet_CLC[element] = 0.0
#                    self.land_cohorts[element].remove('Wet_CLC')
#            if 'Wet_FCP' in self.land_cohorts[element]:
#                self.ATTM_Wet_FCP[element] = self.ATTM_Wet_FCP[element] - cohort_reduction
#                if self.ATTM_Wet_FCP[element] < 0.0:
#                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_FCP[element])
#                    self.ATTM_Wet_FCP[element] = 0.0
#                    self.land_cohorts[element].remove('Wet_FCP')
#            if 'Wet_HCP' in self.land_cohorts[element]:
#                self.ATTM_Wet_HCP[element] = self.ATTM_Wet_HCP[element] - cohort_reduction
#                if self.ATTM_Wet_HCP[element] < 0.0:
#                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_HCP[element])
#                    self.ATTM_Wet_HCP[element] = 0.0
#                    self.land_cohorts[element].remove('Wet_HCP')
#            # --------------------------------------------------------
#            # Increase lake fractional area by 'not enough land area'
#            # --------------------------------------------------------
#            self.ATTM_Lakes[element] = self.ATTM_Lakes[element] - not_enough_land
            
    ##########################################################################################
    #               PONDS 
    ###########################################################################################
#    if self.ATTM_Ponds[element] > 0.0 and self.ATTM_Ponds[element] < 1.0 :
    ATTM_Pond_Total = self.ATTM_Ponds_WT_Y[element] + self.ATTM_Ponds_WT_M[element] + \
                      self.ATTM_Ponds_WT_O[element]
    if ATTM_Pond_Total > 0.0 and ATTM_Pond_Total < 1.0 :
        # --------------------------------------------------
        # Determine the fractional amount of pond expansion
        # --------------------------------------------------
        # If climate event happens, double the expansion constant
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if self.climate_expansion_ponds[element] == 1.0:
            #pond_fraction_increase = self.ATTM_Ponds[element] * self.LakePond['Pond_Expansion'] *2.0
            pond_wt_fraction_increase_y = self.ATTM_Ponds_WT_Y[element] * self.LakePond['Pond_WT_Y_Expansion'] * 2.0
            pond_wt_fraction_increase_m = self.ATTM_Ponds_WT_M[element] * self.LakePond['Pond_WT_M_Expansion'] * 2.0
            pond_wt_fraction_increase_o = self.ATTM_Ponds_WT_O[element] * self.LakePond['Pond_WT_O_Expansion'] * 2.0

            self.climate_expansion_ponds[element] = 0.0
        else:
            #pond_fraction_increase = self.ATTM_Ponds[element] * self.LakePond['Pond_Expansion']
            pond_wt_fraction_increase_y = self.ATTM_Ponds_WT_Y[element] * self.LakePond['Pond_WT_Y_Expansion']
            pond_wt_fraction_increase_m = self.ATTM_Ponds_WT_M[element] * self.LakePond['Pond_WT_M_Expansion']
            pond_wt_fraction_increase_o = self.ATTM_Ponds_WT_O[element] * self.LakePond['Pond_WT_O_Expansion']
        

        pond_fraction_increase = pond_wt_fraction_increase_y + pond_wt_fraction_increase_m + \
          pond_wt_fraction_increase_o
        
        land_available = self.ATTM_CLC_WT_Y[element] + self.ATTM_CLC_WT_M[element] + \
                         self.ATTM_CLC_WT_O[element] + self.ATTM_CoastalWaters_WT_O[element] + \
                         self.ATTM_DrainedSlope_WT_Y[element] + self.ATTM_DrainedSlope_WT_M[element] + \
                         self.ATTM_DrainedSlope_WT_O[element] + self.ATTM_FCP_WT_Y[element] + \
                         self.ATTM_FCP_WT_M[element] + self.ATTM_FCP_WT_O[element] + \
                         self.ATTM_HCP_WT_Y[element] + self.ATTM_HCP_WT_M[element] + \
                         self.ATTM_HCP_WT_O[element] + self.ATTM_LCP_WT_Y[element] + \
                         self.ATTM_LCP_WT_M[element] + self.ATTM_LCP_WT_O[element] + \
                         self.ATTM_Meadow_WT_Y[element] + self.ATTM_Meadow_WT_M[element] + \
                         self.ATTM_Meadow_WT_O[element] + self.ATTM_NoData_WT_O[element] + \
                         self.ATTM_SandDunes_WT_Y[element] + self.ATTM_SandDunes_WT_M[element] + \
                         self.ATTM_SandDunes_WT_O[element] + self.ATTM_SaturatedBarrens_WT_Y[element] + \
                         self.ATTM_SaturatedBarrens_WT_M[element] + self.ATTM_SaturatedBarrens_WT_O[element] + \
                         self.ATTM_Shrubs_WT_O[element]
        

        # ==================================================================================
        # Case 0:
        #    The sum of the fractional pond area + pond_fraction_increase > the available
        #    land available for pond expansion (not expanding into rivers, urban, lakes).
        #
        #    In this case, the fractional pond area is equal to the total amount of land
        #    cohorts and all the land cohorts are set to 0.0
        # ==================================================================================
        if pond_fraction_increase > land_available:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
            #self.ATTM_Ponds[element] = self.ATTM_Ponds[element] + land_available
            self.ATTM_Ponds_WT_Y[element] = self.ATTM_Ponds_WT_Y[element] + \
              ((self.ATTM_Ponds_WT_Y[element] / ATTM_Pond_Total) * land_available)
            self.ATTM_Ponds_WT_M[element] = self.ATTM_Ponds_WT_M[element] + \
              ((self.ATTM_Ponds_WT_M[element] / ATTM_Pond_Total) * land_available)
            self.ATTM_Ponds_WT_O[element] = self.ATTM_Ponds_WT_O[element] + \
              ((self.ATTM_Ponds_WT_O[element] / ATTM_Pond_Total) * land_available)
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#            self.ATTM_Wet_NPG[element] = 0.0
#            if 'Wet_NPG' in self.land_cohorts[element] :
#                self.land_cohorts[element].remove('Wet_NPG')
#            self.ATTM_Wet_LCP[element] = 0.0
#            if 'Wet_LCP' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Wet_LCP')
#            self.ATTM_Wet_CLC[element] = 0.0
#            if 'Wet_CLC' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Wet_CLC')
#            self.ATTM_Wet_FCP[element] = 0.0
#            if 'Wet_FCP' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Wet_FCP')
#            self.ATTM_Wet_HCP[element] = 0.0
#            if 'Wet_HCP' in self.land_cohorts[element]:
#                self.land_cohorts[element].remove('Wet_HCP')
#            self.ATTM_Gra_NPG[element] = 0.0
            
#            self.ATTM_Gra_LCP[element] = 0.0
#            self.ATTM_Gra_FCP[element] = 0.0
#            self.ATTM_Gra_HCP[element] = 0.0
#            self.ATTM_Shr_NPG[element] = 0.0
#            self.ATTM_Shr_LCP[element] = 0.0
#            self.ATTM_Shr_FCP[element] = 0.0
#            self.ATTM_Shr_HCP[element] = 0.0
            
       
 #       elif len(self.land_cohorts[element]) == 0:
 #          # all water and/or urban cohorts in the element
 #          self.ATTM_Ponds[element] = self.ATTM_Ponds[element]
           
        else:
            # ==================================================================================
            # Case 1:
            #   The sum of all the land cohorts equals or exceeds the fractional amount of lake
            #   area increase. However, one or more of the land cohorts has a fractional area
            #   less than (or equal to) the lake_proportional_reduction value.  In this case,
            #   the land cohort(s) with the fractional areas less than the lake_proportional_area
            #   are reduced to zero and the excess expansion is carried by the remaining cohorts.
            #
            #   This case may result in a cascading reduction of cohorts.  For example, if on the
            #   first pass one land cohort is zeroed out, the remaining fractional reduction added
            #   to the remaining cohorts may result in a lake_proportional_area being greater than
            #   one of the remaining land cohorts.  In this case, the 2nd cohort will need to be
            #   zeroed out and the remaining lake area expansion is passed on to the remaining
            #   land cohorts.
            # -----------------------------------------------------------------------------------
            #self.ATTM_Ponds[element] = self.ATTM_Ponds[element] + pond_fraction_increase
            self.ATTM_Ponds_WT_Y[element] = self.ATTM_Ponds_WT_Y[element] + pond_wt_fraction_increase_y
            self.ATTM_Ponds_WT_M[element] = self.ATTM_Ponds_WT_M[element] + pond_wt_fraction_increase_m
            self.ATTM_Ponds_WT_O[element] = self.ATTM_Ponds_WT_O[element] + pond_wt_fraction_increase_o
            
            #cohort_reduction = pond_fraction_increase / len(self.land_cohorts[element])
            not_enough_land = 0.0
            not_enough_land_count = 0.0
            land_count = 0.0
            pond_count = 0.0
            # Determine land cohorts available for reduction in the element
            if self.ATTM_CLC_WT_Y[element] > 0.0: land_count = land_count + 1
            if self.ATTM_CLC_WT_M[element] > 0.0: land_count = land_count + 1
            if self.ATTM_CLC_WT_O[element] > 0.0: land_count = land_count + 1
            if self.ATTM_CoastalWaters_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_DrainedSlope_WT_Y[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_DrainedSlope_WT_M[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_DrainedSlope_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_FCP_WT_Y[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_FCP_WT_M[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_FCP_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_HCP_WT_Y[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_HCP_WT_M[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_HCP_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_LCP_WT_Y[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_LCP_WT_M[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_LCP_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_Meadow_WT_Y[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_Meadow_WT_M[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_Meadow_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_NoData_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_SandDunes_WT_Y[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_SandDunes_WT_M[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_SandDunes_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_SaturatedBarrens_WT_Y[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_SaturatedBarrens_WT_M[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_SaturatedBarrens_WT_O[element] > 0.0 : land_count = land_count + 1
            if self.ATTM_Shrubs_WT_O[element] > 0.0 : land_count = land_count + 1
            # Determine proportional reduction for land cohorts present
            cohort_reduction = pond_fraction_increase / land_count
            # Sequence through land cohorts and reduce as appropriate
            if self.ATTM_CLC_WT_Y[element] > 0.0:
                self.ATTM_CLC_WT_Y[element] = self.ATTM_CLC_WT_Y[element] - cohort_reduction
                if self.ATTM_CLC_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_CLC_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_CLC_WT_Y[element] = 0.0
            if self.ATTM_CLC_WT_M[element] > 0.0:
                self.ATTM_CLC_WT_M[element] = self.ATTM_CLC_WT_M[element] - cohort_reduction
                if self.ATTM_CLC_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_CLC_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_CLC_WT_M[element] = 0.0
            if self.ATTM_CLC_WT_O[element] > 0.0:
                self.ATTM_CLC_WT_O[element] = self.ATTM_CLC_WT_O[element] - cohort_reduction
                if self.ATTM_CLC_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_CLC_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_CLC_WT_O[element] = 0.0
            if self.ATTM_CoastalWaters_WT_O[element] > 0.0:
                self.ATTM_CoastalWaters_WT_O[element] = self.ATTM_CoastalWaters_WT_O[element] - cohort_reduction
                if self.ATTM_CoastalWaters_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_CoastalWaters_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_CoastalWaters_WT_O[element] = 0.0                    
            if self.ATTM_DrainedSlope_WT_Y[element] > 0.0:
                self.ATTM_DrainedSlope_WT_Y[element] = self.ATTM_DrainedSlope_WT_Y[element] - cohort_reduction
                if self.ATTM_DrainedSlope_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_DrainedSlope_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_DrainedSlope_WT_Y[element] = 0.0
            if self.ATTM_DrainedSlope_WT_M[element] > 0.0:
                self.ATTM_DrainedSlope_WT_M[element] = self.ATTM_DrainedSlope_WT_M[element] - cohort_reduction
                if self.ATTM_DrainedSlope_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_DrainedSlope_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_DrainedSlope_WT_M[element] = 0.0
            if self.ATTM_DrainedSlope_WT_O[element] > 0.0:
                self.ATTM_DrainedSlope_WT_O[element] = self.ATTM_DrainedSlope_WT_O[element] - cohort_reduction
                if self.ATTM_DrainedSlope_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_DrainedSlope_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_DrainedSlope_WT_O[element] = 0.0
            if self.ATTM_FCP_WT_Y[element] > 0.0:
                self.ATTM_FCP_WT_Y[element] = self.ATTM_FCP_WT_Y[element] - cohort_reduction
                if self.ATTM_FCP_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_FCP_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_FCP_WT_Y[element] = 0.0
            if self.ATTM_FCP_WT_M[element] > 0.0:
                self.ATTM_FCP_WT_M[element] = self.ATTM_FCP_WT_M[element] - cohort_reduction
                if self.ATTM_FCP_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_FCP_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_FCP_WT_M[element] = 0.0
            if self.ATTM_FCP_WT_O[element] > 0.0:
                self.ATTM_FCP_WT_O[element] = self.ATTM_FCP_WT_O[element] - cohort_reduction
                if self.ATTM_FCP_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_FCP_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_FCP_WT_O[element] = 0.0
            if self.ATTM_HCP_WT_Y[element] > 0.0:
                self.ATTM_HCP_WT_Y[element] = self.ATTM_HCP_WT_Y[element] - cohort_reduction
                if self.ATTM_HCP_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_HCP_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_HCP_WT_Y[element] = 0.0
            if self.ATTM_HCP_WT_M[element] > 0.0:
                self.ATTM_HCP_WT_M[element] = self.ATTM_HCP_WT_M[element] - cohort_reduction
                if self.ATTM_HCP_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_HCP_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_HCP_WT_M[element] = 0.0
            if self.ATTM_HCP_WT_O[element] > 0.0:
                self.ATTM_HCP_WT_O[element] = self.ATTM_HCP_WT_O[element] - cohort_reduction
                if self.ATTM_HCP_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_HCP_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_HCP_WT_O[element] = 0.0
            if self.ATTM_LCP_WT_Y[element] > 0.0:
                self.ATTM_LCP_WT_Y[element] = self.ATTM_LCP_WT_Y[element] - cohort_reduction
                if self.ATTM_LCP_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_LCP_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_LCP_WT_Y[element] = 0.0
            if self.ATTM_LCP_WT_M[element] > 0.0:
                self.ATTM_LCP_WT_M[element] = self.ATTM_LCP_WT_M[element] - cohort_reduction
                if self.ATTM_LCP_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_LCP_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_LCP_WT_M[element] = 0.0
            if self.ATTM_LCP_WT_O[element] > 0.0:
                self.ATTM_LCP_WT_O[element] = self.ATTM_LCP_WT_O[element] - cohort_reduction
                if self.ATTM_LCP_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_LCP_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_LCP_WT_O[element] = 0.0
            if self.ATTM_Meadow_WT_Y[element] > 0.0:
                self.ATTM_Meadow_WT_Y[element] = self.ATTM_Meadow_WT_Y[element] - cohort_reduction
                if self.ATTM_Meadow_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Meadow_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_Meadow_WT_Y[element] = 0.0
            if self.ATTM_Meadow_WT_M[element] > 0.0:
                self.ATTM_Meadow_WT_M[element] = self.ATTM_Meadow_WT_M[element] - cohort_reduction
                if self.ATTM_Meadow_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Meadow_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_Meadow_WT_M[element] = 0.0
            if self.ATTM_Meadow_WT_O[element] > 0.0:
                self.ATTM_Meadow_WT_O[element] = self.ATTM_Meadow_WT_O[element] - cohort_reduction
                if self.ATTM_Meadow_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Meadow_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_Meadow_WT_O[element] = 0.0
            if self.ATTM_SandDunes_WT_Y[element] > 0.0:
                self.ATTM_SandDunes_WT_Y[element] = self.ATTM_SandDunes_WT_Y[element] - cohort_reduction
                if self.ATTM_SandDunes_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_SandDunes_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_SandDunes_WT_Y[element] = 0.0
            if self.ATTM_SandDunes_WT_M[element] > 0.0:
                self.ATTM_SandDunes_WT_M[element] = self.ATTM_SandDunes_WT_M[element] - cohort_reduction
                if self.ATTM_SandDunes_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_SandDunes_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_SandDunes_WT_M[element] = 0.0
            if self.ATTM_SandDunes_WT_O[element] > 0.0:
                self.ATTM_SandDunes_WT_O[element] = self.ATTM_SandDunes_WT_O[element] - cohort_reduction
                if self.ATTM_SandDunes_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_SandDunes_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_SandDunes_WT_O[element] = 0.0
            if self.ATTM_NoData_WT_O[element] > 0.0:
                self.ATTM_NoData_WT_O[element] = self.ATTM_NoData_WT_O[element] - cohort_reduction
                if self.ATTM_NoData_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_NoData_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_NoData_WT_O[element] = 0.0
            if self.ATTM_SaturatedBarrens_WT_Y[element] > 0.0:
                self.ATTM_SaturatedBarrens_WT_Y[element] = self.ATTM_SaturatedBarrens_WT_Y[element] - cohort_reduction
                if self.ATTM_SaturatedBarrens_WT_Y[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_SaturatedBarrens_WT_Y[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_SaturatedBarrens_WT_Y[element] = 0.0
            if self.ATTM_SaturatedBarrens_WT_M[element] > 0.0:
                self.ATTM_SaturatedBarrens_WT_M[element] = self.ATTM_SaturatedBarrens_WT_M[element] - cohort_reduction
                if self.ATTM_SaturatedBarrens_WT_M[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_SaturatedBarrens_WT_M[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_SaturatedBarrens_WT_M[element] = 0.0
            if self.ATTM_SaturatedBarrens_WT_O[element] > 0.0:
                self.ATTM_SaturatedBarrens_WT_O[element] = self.ATTM_SaturatedBarrens_WT_O[element] - cohort_reduction
                if self.ATTM_SaturatedBarrens_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_SaturatedBarrens_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_SaturatedBarrens_WT_O[element] = 0.0                 
            if self.ATTM_Shrubs_WT_O[element] > 0.0:
                self.ATTM_Shrubs_WT_O[element] = self.ATTM_Shrubs_WT_O[element] - cohort_reduction
                if self.ATTM_Shrubs_WT_O[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Shrubs_WT_O[element])
                    not_enough_land_count = not_enough_land_count + 1
                    self.ATTM_Shrubss_WT_O[element] = 0.0             
            # If not_enough_land_count is > 0, reduce size of ponds
            if self.ATTM_Ponds_WT_Y[element] > 0.0 : pond_count = pond_count + 1.
            if self.ATTM_Ponds_WT_M[element] > 0.0 : pond_count = pond_count + 1.
            if self.ATTM_Ponds_WT_O[element] > 0.0 : pond_count = pond_count + 1.

            pond_reduction = not_enough_land / pond_count

            if self.ATTM_Ponds_WT_Y[element] > 0. :
                self.ATTM_Ponds_WT_Y[element] = self.ATTM_Ponds_WT_Y[element] - pond_reduction
            if self.ATTM_Ponds_WT_M[element] > 0. :
                self.ATTM_Ponds_WT_M[element] = self.ATTM_Ponds_WT_M[element] - pond_reduction
            if self.ATTM_Ponds_WT_O[element] > 0. :
                self.ATTM_Ponds_WT_O[element] = self.ATTM_Ponds_WT_O[element] - pond_reduction
        #-------------------------------------------------------------------------------
        # Check to ensure the fractional pond area does not exceed 1.0
        #
        # If Pond area is greater than or equal to 1., assume 1 for all ponds for the element that will
        # be divided up between the young, medium, and old age components (based upon
        # fractional relationship between young, medium and old age lakes).
        #
        # All other cohorts are also zeroed out (precaution/check).
        #--------------------------------------------------------------------------------
        ATTM_Pond_Area  = self.ATTM_Ponds_WT_Y[element] + self.ATTM_Ponds_WT_M[element] + \
          self.ATTM_Ponds_WT_O[element]

        if ATTM_Pond_Area >= 1.0:
            self.ATTM_Ponds_WT_Y[element] = self.ATTM_Ponds_WT_Y[element] / ATTM_Pond_Area
            self.ATTM_Ponds_WT_M[element] = self.ATTM_Ponds_WT_M[element] / ATTM_Pond_Area
            self.ATTM_Ponds_WT_O[element] = self.ATTM_Ponds_WT_O[element] / ATTM_Pond_Area
            self.ATTM_LargeLakes_WT_Y[element] = 0.0
            self.ATTM_LargeLakes_WT_M[element] = 0.0
            self.ATTM_LargeLakes_WT_O[element] = 0.0
            self.ATTM_MediumLakes_WT_Y[element] = 0.0
            self.ATTM_MediumLakes_WT_M[element] = 0.0
            self.ATTM_MediumLakes_WT_O[element] = 0.0
            self.ATTM_SmallLakes_WT_Y[element] = 0.0
            self.ATTM_SmallLakes_WT_M[element] = 0.0
            self.ATTM_SmallLakes_WT_O[element] = 0.0

            self.ATTM_CLC_WT_Y[element] = 0.0
            self.ATTM_CLC_WT_M[element] = 0.0
            self.ATTM_CLC_WT_O[element] = 0.0
            self.ATTM_CoastalWaters_WT_O[element] = 0.0
            self.DrainedSlope_WT_Y[element] = 0.0
            self.DrainedSlope_WT_M[element] = 0.0
            self.DrainedSlope_WT_O[element] = 0.0
            self.FCP_WT_Y[element] = 0.0
            self.FCP_WT_M[element] = 0.0
            self.FCP_WT_O[element] = 0.0
            self.HCP_WT_Y[element] = 0.0
            self.HCP_WT_M[element] = 0.0
            self.HCP_WT_O[element] = 0.0
            self.LCP_WT_Y[element] = 0.0
            self.LCP_WT_M[element] = 0.0
            self.LCP_WT_O[element] = 0.0
            self.Meadow_WT_Y[element] = 0.0
            self.Meadow_WT_M[element] = 0.0
            self.Meadow_WT_O[element] = 0.0
            self.NoData_WT_O[element] = 0.0
            self.SandDunes_WT_Y[element] = 0.0
            self.SandDunes_WT_M[element] = 0.0
            self.SandDunes_WT_O[element] = 0.0
            self.SaturatedBarrens_WT_Y[element] = 0.0
            self.SaturatedBarrens_WT_M[element] = 0.0
            self.SaturatedBarrens_WT_O[element] = 0.0
            self.Shrubs_WT_O[element] = 0.0
            self.Urban_WT[element] = 0.0
            self.Rivers_WT_Y[element] = 0.0
            self.Rivers_WT_M[element] = 0.0
            self.Rivers_WT_O[element] = 0.0
#            # -------------------------------------
#           # Reduce all appropriate land cohorts
#           # -------------------------------------
#            if 'Wet_NPG' in self.land_cohorts[element]:
#                self.ATTM_Wet_NPG[element] = self.ATTM_Wet_NPG[element] - cohort_reduction
#                if self.ATTM_Wet_NPG[element] < 0.0:
#                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_NPG[element])
#                    self.ATTM_Wet_NPG[element] = 0.0
#                    self.land_cohorts[element].remove('Wet_NPG')
#            if 'Wet_LCP' in self.land_cohorts[element]:
#                self.ATTM_Wet_LCP[element] = self.ATTM_Wet_LCP[element] - cohort_reduction
#                if self.ATTM_Wet_LCP[element] < 0.0:
#                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_LCP[element])
#                    self.ATTM_Wet_LCP[element] = 0.0
#                    self.land_cohorts[element].remove('Wet_LCP')
#            if 'Wet_CLC' in self.land_cohorts[element]:
#                self.ATTM_Wet_CLC[element] = self.ATTM_Wet_CLC[element] - cohort_reduction
#                if self.ATTM_Wet_CLC[element] < 0.0 :
#                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_CLC[element])
#                    self.ATTM_Wet_CLC[element] = 0.0
#                    self.land_cohorts[element].remove('Wet_CLC')
#            if 'Wet_FCP' in self.land_cohorts[element]:
#                self.ATTM_Wet_FCP[element] = self.ATTM_Wet_FCP[element] - cohort_reduction
#                if self.ATTM_Wet_FCP[element] < 0.0:
#                    not_enough_land = not_enough_land +  abs(self.ATTM_Wet_FCP[element])
#                    self.ATTM_Wet_FCP[element] = 0.0
#                    self.land_cohorts[element].remove('Wet_FCP')
#            if 'Wet_HCP' in self.land_cohorts[element]:
#                self.ATTM_Wet_HCP[element] = self.ATTM_Wet_HCP[element] - cohort_reduction
#                if self.ATTM_Wet_HCP[element] < 0.0:
#                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_HCP[element])
#                    self.ATTM_Wet_HCP[element] = 0.0
#                    self.land_cohorts[element].remove('Wet_HCP')

#            # ------------------------------
#            # Increase pond fractional area
#            # ------------------------------
#            self.ATTM_Ponds[element] = self.ATTM_Ponds[element] - not_enough_land
            

#===============================================================================================
def pond_infill(self, element, time):
    """
    The purpose of this module is to infill ponds at a prescribed rate with vegetation,
    which will presumably be non-polygonal ground.

    # - - -- - - - - - - -- - - - - - - - -- - - - - - - - -- - - - -- - - -
    !!! I should double check to see if non-polygonal ground is the correct
    !!! transition ...
    # - - - - - - - - - - - - - - - - - --- - - - - - - - - - - - - - - - - -

    This module is developed due to paper that states with warming temperatures,
    ponds are shrinking due in part to infilling of vegetation.  Paper is in press
    and was set out by Anna L. in March 2015.

    # - - - - - -------------------------------------------------------------------
    I think initially, I will set pond infilling to occur every time step. I might
    try to infill when temperature in year N is greater than temperature in year N-1.

    #-------------------------------------------------------------------------------
    """
#    if self.ATTM_Ponds[element] > 0.0 and self.ATTM_Ponds[element] < 1.0:
    pond_area = self.ATTM_Ponds_WT_Y[element] + self.ATTM_Ponds_WT_M[element] + self.ATTM_Ponds_WT_O[element]
    if pond_area > 0.0 and pond_area < 1.0 :
        # Is this the first time step? If yes, no infilling occurs
        if time == 0:
            pass
        else:
            # If Degree Days are greater than previous time step, infill
            if self.TDD[time, element] > self.TDD[time-1, element]:
                #infill = self.ATTM_Ponds[element] * self.LakePond['Pond_Infill_Constant']
                infill_y = self.ATTM_Ponds_WT_Y[element] * self.LakePond['Pond_WT_Y_Infill_Constant']
                infill_m = self.ATTM_Ponds_WT_M[element] * self.LakePond['Pond_WT_M_Infill_Constant']
                infill_o = self.ATTM_Ponds_WT_O[element] * self.LakePond['Pond_WT_O_Infill_Constant']
                # Reduce Pond size and increase WetNPG size
                #self.ATTM_Ponds[element] = self.ATTM_Ponds[element] - infill
                #self.ATTM_Wet_NPG[element] = self.ATTM_Wet_NPG[element] + infill
                self.ATTM_Ponds_WT_Y[element] = self.ATTM_Ponds_WT_Y[element] - infill_y
                self.ATTM_Ponds_WT_M[element] = self.ATTM_Ponds_WT_M[element] - infill_m
                self.ATTM_Ponds_WT_O[element] = self.ATTM_Ponds_WT_O[element] - infill_o
                self.ATTM_Meadow_WT_Y[element] = self.ATTM_Meadow_WT_Y[element] + infill_y
                self.ATTM_Meadow_WT_M[element] = self.ATTM_Meadow_WT_M[element] + infill_m
                self.ATTM_Meadow_WT_O[element] = self.ATTM_Meadow_WT_O[element] + infill_o

