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
    ###########################################################################################
    if self.ATTM_Lakes[element] > 0.0 and self.ATTM_Lakes[element] < 1.0 :
        
        # --------------------------------------------------
        # Determine the fractional amount of lake expansion
        # --------------------------------------------------
        if self.climate_expansion_lakes[element] == 1.0:
            #lake_fraction_increase = self.ATTM_Lakes[element] * self.Lake_Expansion_Constant * 2.0
            lake_fraction_increase = self.ATTM_Lakes[element] * self.LakePond['Lake_Expansion'] * 2.0
	    self.climate_expansion_lakes[element] = 0.0
        else:
            #lake_fraction_increase = self.ATTM_Lakes[element] * self.Lake_Expansion_Constant
            lake_fraction_increase = self.ATTM_Lakes[element] * self.LakePond['Lake_Expansion']

        land_available = self.ATTM_Wet_NPG[element] + self.ATTM_Wet_LCP[element] + \
                         self.ATTM_Wet_CLC[element] + self.ATTM_Wet_FCP[element] + \
                         self.ATTM_Wet_HCP[element] + self.ATTM_Gra_NPG[element] + \
                         self.ATTM_Gra_LCP[element] + self.ATTM_Gra_FCP[element] + \
                         self.ATTM_Gra_HCP[element] + self.ATTM_Shr_NPG[element] + \
                         self.ATTM_Shr_LCP[element] + self.ATTM_Shr_FCP[element] + \
                         self.ATTM_Shr_HCP[element]
        
        # ==================================================================================
        # Case 0:
        #    The sum of the fractional lake area + lake_fraction_increase > the available
        #    land available for pond expansion (not expanding into rivers, urban, lakes).
        #
        #    In this case, the fractional lake area is equal to the total amount of land
        #    cohorts and all the land cohorts are set to 0.0
        # ==================================================================================
        if lake_fraction_increase > land_available:
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            self.ATTM_Lakes[element] = self.ATTM_Lakes[element] + land_available
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            self.ATTM_Wet_NPG[element] = 0.0
            if 'Wet_NPG' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Wet_NPG')
            self.ATTM_Wet_LCP[element] = 0.0
            if 'Wet_LCP' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Wet_LCP')
            self.ATTM_Wet_CLC[element] = 0.0
            if 'Wet_CLC' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Wet_CLC')
            self.ATTM_Wet_FCP[element] = 0.0
            if 'Wet_FCP' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Wet_FCP')
            self.ATTM_Wet_HCP[element] = 0.0
            if 'Wet_HCP' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Wet_HCP')
            self.ATTM_Gra_NPG[element] = 0.0
            if 'Gra_NPG' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Gra_NPG')
            self.ATTM_Gra_LCP[element] = 0.0
            if 'Gra_LCP' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Gra_LCP')
            self.ATTM_Gra_FCP[element] = 0.0
            if 'Gra_FCP' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Gra_FCP')
            self.ATTM_Gra_HCP[element] = 0.0
            if 'Gra_HCP' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Gra_HCP')
            self.ATTM_Shr_NPG[element] = 0.0
            if 'Shr_NPG' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Shr_NPG')
            self.ATTM_Shr_LCP[element] = 0.0
            if 'Shr_LCP' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Shr_LCP')
            self.ATTM_Shr_FCP[element] = 0.0
            if 'Shr_FCP' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Shr_FCP')
            self.ATTM_Shr_HCP[element] = 0.0
            if 'Shr_HCP' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Shr_HCP')
            
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
        elif len(self.land_cohorts[element]) == 0.0:
                 self.ATTM_Lakes[element] = self.ATTM_Lakes[element]
        
        else:             # land_available > lake_fraction_increase:
            self.ATTM_Lakes[element] = self.ATTM_Lakes[element] + lake_fraction_increase
            
            cohort_reduction = lake_fraction_increase / len(self.land_cohorts[element])

            # -------------------------------------
            # Reduce all appropriate land cohorts
            # -------------------------------------
            not_enough_land = 0.0
            if 'Wet_NPG' in self.land_cohorts[element]:
                self.ATTM_Wet_NPG[element] = self.ATTM_Wet_NPG[element] - cohort_reduction
                if self.ATTM_Wet_NPG[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_NPG[element])
                    self.ATTM_Wet_NPG[element] = 0.0
                    self.land_cohorts[element].remove('Wet_NPG')
            if 'Wet_LCP' in self.land_cohorts[element]:
                self.ATTM_Wet_LCP[element] = self.ATTM_Wet_LCP[element] - cohort_reduction
                if self.ATTM_Wet_LCP[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_LCP[element])
                    self.ATTM_Wet_LCP[element] = 0.0
                    self.land_cohorts[element].remove('Wet_LCP')
            if 'Wet_CLC' in self.land_cohorts[element]:
                self.ATTM_Wet_CLC[element] = self.ATTM_Wet_CLC[element] - cohort_reduction
                if self.ATTM_Wet_CLC[element] < 0.0 :
                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_CLC[element])
                    self.ATTM_Wet_CLC[element] = 0.0
                    self.land_cohorts[element].remove('Wet_CLC')
            if 'Wet_FCP' in self.land_cohorts[element]:
                self.ATTM_Wet_FCP[element] = self.ATTM_Wet_FCP[element] - cohort_reduction
                if self.ATTM_Wet_FCP[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_FCP[element])
                    self.ATTM_Wet_FCP[element] = 0.0
                    self.land_cohorts[element].remove('Wet_FCP')
            if 'Wet_HCP' in self.land_cohorts[element]:
                self.ATTM_Wet_HCP[element] = self.ATTM_Wet_HCP[element] - cohort_reduction
                if self.ATTM_Wet_HCP[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_HCP[element])
                    self.ATTM_Wet_HCP[element] = 0.0
                    self.land_cohorts[element].remove('Wet_HCP')
            # ------------------------------
            # Increase lake fractional area
            # ------------------------------
            self.ATTM_Lakes[element] = self.ATTM_Lakes[element] - not_enough_land
            
    ##########################################################################################
    #               PONDS 
    ###########################################################################################
    if self.ATTM_Ponds[element] > 0.0 and self.ATTM_Ponds[element] < 1.0 :

        # --------------------------------------------------
        # Determine the fractional amount of pond expansion
        # --------------------------------------------------
        # If climate event happens, double the expansion constant
        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        if self.climate_expansion_ponds[element] == 1.0:
            #pond_fraction_increase = self.ATTM_Ponds[element] * self.Lake_Expansion_Constant * 2.0
            pond_fraction_increase = self.ATTM_Ponds[element] * self.LakePond['Pond_Expansion'] *2.0
        else:
            #pond_fraction_increase = self.ATTM_Ponds[element] * self.Lake_Expansion_Constant
            pond_fraction_increase = self.ATTM_Ponds[element] * self.LakePond['Pond_Expansion']
            
        

        land_available = self.ATTM_Wet_NPG[element] + self.ATTM_Wet_LCP[element] + \
                         self.ATTM_Wet_CLC[element] + self.ATTM_Wet_FCP[element] + \
                         self.ATTM_Wet_HCP[element] + self.ATTM_Gra_NPG[element] + \
                         self.ATTM_Gra_LCP[element] + self.ATTM_Gra_FCP[element] + \
                         self.ATTM_Gra_HCP[element] + self.ATTM_Shr_NPG[element] + \
                         self.ATTM_Shr_LCP[element] + self.ATTM_Shr_FCP[element] + \
                         self.ATTM_Shr_HCP[element]

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
            self.ATTM_Ponds[element] = self.ATTM_Ponds[element] + land_available
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            self.ATTM_Wet_NPG[element] = 0.0
            if 'Wet_NPG' in self.land_cohorts[element] :
                self.land_cohorts[element].remove('Wet_NPG')
            self.ATTM_Wet_LCP[element] = 0.0
            if 'Wet_LCP' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Wet_LCP')
            self.ATTM_Wet_CLC[element] = 0.0
            if 'Wet_CLC' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Wet_CLC')
            self.ATTM_Wet_FCP[element] = 0.0
            if 'Wet_FCP' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Wet_FCP')
            self.ATTM_Wet_HCP[element] = 0.0
            if 'Wet_HCP' in self.land_cohorts[element]:
                self.land_cohorts[element].remove('Wet_HCP')
            self.ATTM_Gra_NPG[element] = 0.0
            
            self.ATTM_Gra_LCP[element] = 0.0
            self.ATTM_Gra_FCP[element] = 0.0
            self.ATTM_Gra_HCP[element] = 0.0
            self.ATTM_Shr_NPG[element] = 0.0
            self.ATTM_Shr_LCP[element] = 0.0
            self.ATTM_Shr_FCP[element] = 0.0
            self.ATTM_Shr_HCP[element] = 0.0
            
       
        elif len(self.land_cohorts[element]) == 0:
           # all water and/or urban cohorts in the element
           self.ATTM_Ponds[element] = self.ATTM_Ponds[element]
           
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
            self.ATTM_Ponds[element] = self.ATTM_Ponds[element] + pond_fraction_increase

            cohort_reduction = pond_fraction_increase / len(self.land_cohorts[element])
            not_enough_land = 0.0
            # -------------------------------------
            # Reduce all appropriate land cohorts
            # -------------------------------------
            if 'Wet_NPG' in self.land_cohorts[element]:
                self.ATTM_Wet_NPG[element] = self.ATTM_Wet_NPG[element] - cohort_reduction
                if self.ATTM_Wet_NPG[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_NPG[element])
                    self.ATTM_Wet_NPG[element] = 0.0
                    self.land_cohorts[element].remove('Wet_NPG')
            if 'Wet_LCP' in self.land_cohorts[element]:
                self.ATTM_Wet_LCP[element] = self.ATTM_Wet_LCP[element] - cohort_reduction
                if self.ATTM_Wet_LCP[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_LCP[element])
                    self.ATTM_Wet_LCP[element] = 0.0
                    self.land_cohorts[element].remove('Wet_LCP')
            if 'Wet_CLC' in self.land_cohorts[element]:
                self.ATTM_Wet_CLC[element] = self.ATTM_Wet_CLC[element] - cohort_reduction
                if self.ATTM_Wet_CLC[element] < 0.0 :
                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_CLC[element])
                    self.ATTM_Wet_CLC[element] = 0.0
                    self.land_cohorts[element].remove('Wet_CLC')
            if 'Wet_FCP' in self.land_cohorts[element]:
                self.ATTM_Wet_FCP[element] = self.ATTM_Wet_FCP[element] - cohort_reduction
                if self.ATTM_Wet_FCP[element] < 0.0:
                    not_enough_land = not_enough_land +  abs(self.ATTM_Wet_FCP[element])
                    self.ATTM_Wet_FCP[element] = 0.0
                    self.land_cohorts[element].remove('Wet_FCP')
            if 'Wet_HCP' in self.land_cohorts[element]:
                self.ATTM_Wet_HCP[element] = self.ATTM_Wet_HCP[element] - cohort_reduction
                if self.ATTM_Wet_HCP[element] < 0.0:
                    not_enough_land = not_enough_land + abs(self.ATTM_Wet_HCP[element])
                    self.ATTM_Wet_HCP[element] = 0.0
                    self.land_cohorts[element].remove('Wet_HCP')

            # ------------------------------
            # Increase pond fractional area
            # ------------------------------
            self.ATTM_Ponds[element] = self.ATTM_Ponds[element] - not_enough_land
            

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
    if self.ATTM_Ponds[element] > 0.0 and self.ATTM_Ponds[element] < 1.0:
        # Is this the first time step? If yes, no infilling occurs
        if time == 0:
            pass
        else:
            # If Degree Days are greater than previous time step, infill
            if self.TDD[time, element] > self.TDD[time-1, element]:
                infill = self.ATTM_Ponds[element] * self.LakePond['Pond_Infill_Constant']
                # Reduce Pond size and increase WetNPG size
                self.ATTM_Ponds[element] = self.ATTM_Ponds[element] - infill
                self.ATTM_Wet_NPG[element] = self.ATTM_Wet_NPG[element] + infill
            

