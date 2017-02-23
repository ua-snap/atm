import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def barrow_initial_cohort_check(self):
    """
    The purpose of this module is to ensure that all fractional land-surface cohorts, in each element,
    sums to one.  There are errors introducted in the the interpolation process
    (from Mark Lara files to 25x25m resolution).

    The initial step is to compare the total number of fine-resolution cohorts to the total number
    of cohorts.  In nearly all the ATTM elements, the total fractional area is not 1.0 (either above
    or below).  At this point, the land-surface cohorts are normalized to the ATTM element (in order to
    ensure 1.0.

    On the edges of the model domain (i.e. in areas in contact with the ocean), the total fractional area
    of land-surface cohorts is most likely significantly less than 1.0.  In these cases, the fractional
    area will not be normalized.

    The minimum total fractional area required for normalization is 0.50.

    """
    # Statement for debugging
    print '    Checking initial cohorts, normalizing to 1.0'
    
    # ----------------------------------------------------------------------
    # Determine the initial/original total fractional area of each element.
    # ----------------------------------------------------------------------
    cohort_check = self.ATTM_Total / ((float(self.X_resolution)/(self.x_res)) * float(self.Y_resolution)/ \
                   (self.y_res))

    #=====================================================================================
    # If the total fractional area of element is greater than 0.5, normalize each cohort
    # in order get to 1.0
    #=====================================================================================
    # Note: In the Barrow example, the cohorts_required = 1600. Just leaving as flexible as
    #       possible.
    #-------------------------------------------------------------------------------------
    cohorts_required = ((float(self.X_resolution)/(self.x_res)) * float(self.Y_resolution)/ \
                        (self.y_res))

    for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
        if cohort_check[i] > 0.5:
            #-----------------------------------------------
            # The normalization process
            # adjustment = (cohorts_required / ATTM_Total)
            # cohort_new = cohort * adjustment
            # - - - - - - - - - - - - - - - - - - - - - - - 
            # The new ATTM_Total should = cohorts_required
            #-----------------------------------------------
            adjustment = cohorts_required / self.ATTM_Total[i]

            # Adjust all the land surface cohorts
            #if self.ATTM_Wet_NPG[i] > 0. : self.ATTM_Wet_NPG[i] = self.ATTM_Wet_NPG[i]*adjustment
            #if self.ATTM_Wet_LCP[i] > 0. : self.ATTM_Wet_LCP[i] = self.ATTM_Wet_LCP[i]*adjustment
            #if self.ATTM_Wet_CLC[i] > 0. : self.ATTM_Wet_CLC[i] = self.ATTM_Wet_CLC[i]*adjustment
            #if self.ATTM_Wet_FCP[i] > 0. : self.ATTM_Wet_FCP[i] = self.ATTM_Wet_FCP[i]*adjustment
            #if self.ATTM_Wet_HCP[i] > 0. : self.ATTM_Wet_HCP[i] = self.ATTM_Wet_HCP[i]*adjustment
            #if self.ATTM_Gra_NPG[i] > 0. : self.ATTM_Gra_NPG[i] = self.ATTM_Gra_NPG[i]*adjustment
            #if self.ATTM_Gra_LCP[i] > 0. : self.ATTM_Gra_LCP[i] = self.ATTM_Gra_LCP[i]*adjustment
            #if self.ATTM_Gra_FCP[i] > 0. : self.ATTM_Gra_FCP[i] = self.ATTM_Gra_FCP[i]*adjustment
            #if self.ATTM_Gra_HCP[i] > 0. : self.ATTM_Gra_HCP[i] = self.ATTM_Gra_HCP[i]*adjustment
            #if self.ATTM_Shr_NPG[i] > 0. : self.ATTM_Shr_NPG[i] = self.ATTM_Shr_NPG[i]*adjustment
            #if self.ATTM_Shr_LCP[i] > 0. : self.ATTM_Shr_LCP[i] = self.ATTM_Shr_LCP[i]*adjustment
            #if self.ATTM_Shr_FCP[i] > 0. : self.ATTM_Shr_FCP[i] = self.ATTM_Shr_FCP[i]*adjustment
            #if self.ATTM_Shr_HCP[i] > 0. : self.ATTM_Shr_HCP[i] = self.ATTM_Shr_HCP[i]*adjustment
            #if self.ATTM_Urban[i]   > 0. : self.ATTM_Urban[i]   = self.ATTM_Urban[i]*adjustment
            #if self.ATTM_Rivers[i]  > 0. : self.ATTM_Rivers[i]  = self.ATTM_Rivers[i]*adjustment
            #if self.ATTM_Lakes[i]   > 0. : self.ATTM_Lakes[i]   = self.ATTM_Lakes[i]*adjustment
            #if self.ATTM_Ponds[i]   > 0. : self.ATTM_Ponds[i]   = self.ATTM_Ponds[i]*adjustment
            if self.ATTM_CLC_WT_Y[i] > 0. : self.ATTM_CLC_WT_Y[i] = self.ATTM_CLC_WT_Y[i]*adjustment
            if self.ATTM_CLC_WT_M[i] > 0. : self.ATTM_CLC_WT_M[i] = self.ATTM_CLC_WT_M[i]*adjustment
            if self.ATTM_CLC_WT_O[i] > 0. : self.ATTM_CLC_WT_O[i] = self.ATTM_CLC_WT_O[i]*adjustment
            if self.ATTM_CoastalWaters_WT_O[i] > 0. : self.ATTM_CoastalWaters_WT_O[i] = \
               self.ATTM_CoastalWaters_WT_O[i]*adjustment
            if self.ATTM_DrainedSlope_WT_Y[i] > 0. : self.ATTM_DrainedSlope_WT_Y[i] = \
               self.ATTM_DrainedSlope_WT_Y[i]*adjustment
            if self.ATTM_DrainedSlope_WT_M[i] > 0. : self.ATTM_DrainedSlope_WT_M[i] = \
               self.ATTM_DrainedSlope_WT_M[i]*adjustment
            if self.ATTM_DrainedSlope_WT_O[i] > 0. : self.ATTM_DrainedSlope_WT_O[i] = \
               self.ATTM_DrainedSlope_WT_O[i]*adjustment
            if self.ATTM_FCP_WT_Y[i] > 0. : self.ATTM_FCP_WT_Y[i] = self.ATTM_FCP_WT_Y[i]*adjustment
            if self.ATTM_FCP_WT_M[i] > 0. : self.ATTM_FCP_WT_M[i] = self.ATTM_FCP_WT_M[i]*adjustment
            if self.ATTM_FCP_WT_O[i] > 0. : self.ATTM_FCP_WT_O[i] = self.ATTM_FCP_WT_O[i]*adjustment
            if self.ATTM_HCP_WT_Y[i] > 0. : self.ATTM_HCP_WT_Y[i] = self.ATTM_HCP_WT_Y[i]*adjustment
            if self.ATTM_HCP_WT_M[i] > 0. : self.ATTM_HCP_WT_M[i] = self.ATTM_HCP_WT_M[i]*adjustment
            if self.ATTM_HCP_WT_O[i] > 0. : self.ATTM_HCP_WT_O[i] = self.ATTM_HCP_WT_O[i]*adjustment
            if self.ATTM_LCP_WT_Y[i] > 0. : self.ATTM_LCP_WT_Y[i] = self.ATTM_LCP_WT_Y[i]*adjustment
            if self.ATTM_LCP_WT_M[i] > 0. : self.ATTM_LCP_WT_M[i] = self.ATTM_LCP_WT_M[i]*adjustment
            if self.ATTM_LCP_WT_O[i] > 0. : self.ATTM_LCP_WT_O[i] = self.ATTM_LCP_WT_O[i]*adjustment
            if self.ATTM_Meadow_WT_Y[i] > 0. : self.ATTM_Meadow_WT_Y[i] = \
               self.ATTM_Meadow_WT_Y[i]*adjustment
            if self.ATTM_Meadow_WT_M[i] > 0. : self.ATTM_Meadow_WT_M[i] = \
               self.ATTM_Meadow_WT_M[i]*adjustment
            if self.ATTM_Meadow_WT_O[i] > 0. : self.ATTM_Meadow_WT_O[i] = \
               self.ATTM_Meadow_WT_O[i]*adjustment
            if self.ATTM_NoData_WT_O[i] > 0. : self.ATTM_NoData_WT_O[i] = self.ATTM_NoData_WT_O[i]*adjustment
            if self.ATTM_SandDunes_WT_Y[i] > 0. : self.ATTM_SandDunes_WT_Y[i] = \
               self.ATTM_SandDunes_WT_Y[i]*adjustment
            if self.ATTM_SandDunes_WT_M[i] > 0. : self.ATTM_SandDunes_WT_M[i] = \
               self.ATTM_SandDunes_WT_M[i]*adjustment
            if self.ATTM_SandDunes_WT_O[i] > 0. : self.ATTM_SandDunes_WT_O[i] =  \
               self.ATTM_SandDunes_WT_O[i]*adjustment
            if self.ATTM_SaturatedBarrens_WT_Y[i] > 0. : self.ATTM_SaturatedBarrens_WT_Y[i] = \
               self.ATTM_SaturatedBarrens_WT_Y[i]*adjustment
            if self.ATTM_SaturatedBarrens_WT_M[i] > 0. : self.ATTM_SaturatedBarrens_WT_M[i] = \
               self.ATTM_SaturatedBarrens_WT_M[i]*adjustment
            if self.ATTM_SaturatedBarrens_WT_O[i] > 0. : self.ATTM_SaturatedBarrens_WT_O[i] = \
               self.ATTM_SaturatedBarrens_WT_O[i]*adjustment
            if self.ATTM_Shrubs_WT_O[i] > 0. : self.ATTM_Shrubs_WT_O[i] = self.ATTM_Shrubs_WT_O[i]*adjustment
            if self.ATTM_Urban_WT[i] > 0. : self.ATTM_Urban_WT[i] = self.ATTM_Urban_WT[i]*adjustment
            if self.ATTM_LargeLakes_WT_Y[i] > 0. : self.ATTM_LargeLakes_WT_Y[i] = self.ATTM_LargeLakes_WT_Y[i]*adjustment
            if self.ATTM_LargeLakes_WT_M[i] > 0. : self.ATTM_LargeLakes_WT_M[i] = self.ATTM_LargeLakes_WT_M[i]*adjustment
            if self.ATTM_LargeLakes_WT_O[i] > 0. : self.ATTM_LargeLakes_WT_O[i] = self.ATTM_LargeLakes_WT_O[i]*adjustment
            if self.ATTM_MediumLakes_WT_Y[i] > 0. : self.ATTM_MediumLakes_WT_Y[i] = self.ATTM_MediumLakes_WT_Y[i]*adjustment
            if self.ATTM_MediumLakes_WT_M[i] > 0. : self.ATTM_MediumLakes_WT_M[i] = self.ATTM_MediumLakes_WT_M[i]*adjustment
            if self.ATTM_MediumLakes_WT_O[i] > 0. : self.ATTM_MediumLakes_WT_O[i] = self.ATTM_MediumLakes_WT_M[i]*adjustment
            if self.ATTM_SmallLakes_WT_Y[i] > 0. : self.ATTM_SmallLakes_WT_Y[i] = self.ATTM_SmallLakes_WT_Y[i]*adjustment
            if self.ATTM_SmallLakes_WT_M[i] > 0. : self.ATTM_SmallLakes_WT_M[i] = self.ATTM_SmallLakes_WT_M[i]*adjustment
            if self.ATTM_SmallLakes_WT_O[i] > 0. : self.ATTM_SmallLakes_WT_O[i] = self.ATTM_SmallLakes_WT_O[i]*adjustment
            if self.ATTM_Ponds_WT_Y[i] > 0. : self.ATTM_Ponds_WT_Y[i] = self.ATTM_Ponds_WT_Y[i]*adjustment
            if self.ATTM_Ponds_WT_M[i] > 0. : self.ATTM_Ponds_WT_M[i] = self.ATTM_Ponds_WT_M[i]*adjustment
            if self.ATTM_Ponds_WT_O[i] > 0. : self.ATTM_Ponds_WT_O[i] = self.ATTM_Ponds_WT_O[i]*adjustment
            if self.ATTM_Rivers_WT_Y[i] > 0. : self.ATTM_Rivers_WT_Y[i] = self.ATTM_Rivers_WT_Y[i]*adjustment
            if self.ATTM_Rivers_WT_M[i] > 0. : self.ATTM_Rivers_WT_M[i] = self.ATTM_Rivers_WT_M[i]*adjustment
            if self.ATTM_Rivers_WT_O[i] > 0. : self.ATTM_Rivers_WT_O[i] = self.ATTM_Rivers_WT_O[i]*adjustment
            
    # Convert all land surface cohorts into fractional area of element
    #self.ATTM_Wet_NPG = np.round((self.ATTM_Wet_NPG) / cohorts_required, decimals = 6)
    #self.ATTM_Wet_LCP = np.round((self.ATTM_Wet_LCP) / cohorts_required, decimals = 6)
    #self.ATTM_Wet_CLC = np.round((self.ATTM_Wet_CLC) / cohorts_required, decimals = 6)
    #self.ATTM_Wet_FCP = np.round((self.ATTM_Wet_FCP) / cohorts_required, decimals = 6)
    #self.ATTM_Wet_HCP = np.round((self.ATTM_Wet_HCP) / cohorts_required, decimals = 6)
    #self.ATTM_Gra_NPG = np.round((self.ATTM_Gra_NPG) / cohorts_required, decimals = 6)
    #self.ATTM_Gra_LCP = np.round((self.ATTM_Gra_LCP) / cohorts_required, decimals = 6)
    #self.ATTM_Gra_FCP = np.round((self.ATTM_Gra_FCP) / cohorts_required, decimals = 6)
    #self.ATTM_Gra_HCP = np.round((self.ATTM_Gra_HCP) / cohorts_required, decimals = 6)
    #self.ATTM_Shr_NPG = np.round((self.ATTM_Shr_NPG) / cohorts_required, decimals = 6)
    #self.ATTM_Shr_LCP = np.round((self.ATTM_Shr_LCP) / cohorts_required, decimals = 6)
    #self.ATTM_Shr_FCP = np.round((self.ATTM_Shr_FCP) / cohorts_required, decimals = 6)
    #self.ATTM_Shr_HCP = np.round((self.ATTM_Shr_HCP) / cohorts_required, decimals = 6)
    #self.ATTM_Urban   = np.round((self.ATTM_Urban)   / cohorts_required, decimals = 6)
    #self.ATTM_Rivers  = np.round((self.ATTM_Rivers)  / cohorts_required, decimals = 6)
    #self.ATTM_Lakes   = np.round((self.ATTM_Lakes)   / cohorts_required, decimals = 6)
    #self.ATTM_Ponds   = np.round((self.ATTM_Ponds)   / cohorts_required, decimals = 6)

    self.ATTM_CLC_WT_Y = np.round((self.ATTM_CLC_WT_Y) / cohorts_required, decimals = 6)
    self.ATTM_CLC_WT_M = np.round((self.ATTM_CLC_WT_M) / cohorts_required, decimals = 6)
    self.ATTM_CLC_WT_O = np.round((self.ATTM_CLC_WT_O) / cohorts_required, decimals = 6)
    self.ATTM_CoastalWaters_WT_O = np.round((self.ATTM_CoastalWaters_WT_O) / cohorts_required, decimals = 6)
    self.ATTM_DrainedSlope_WT_Y = np.round((self.ATTM_DrainedSlope_WT_Y) / cohorts_required, decimals = 6)
    self.ATTM_DrainedSlope_WT_M = np.round((self.ATTM_DrainedSlope_WT_M) / cohorts_required, decimals = 6)
    self.ATTM_DrainedSlope_WT_O = np.round((self.ATTM_DrainedSlope_WT_O) / cohorts_required, decimals = 6)
    self.ATTM_FCP_WT_Y = np.round((self.ATTM_FCP_WT_Y) / cohorts_required, decimals = 6)
    self.ATTM_FCP_WT_M = np.round((self.ATTM_FCP_WT_M) / cohorts_required, decimals = 6)
    self.ATTM_FCP_WT_O = np.round((self.ATTM_FCP_WT_O) / cohorts_required, decimals = 6)
    self.ATTM_HCP_WT_Y = np.round((self.ATTM_HCP_WT_Y) / cohorts_required, decimals = 6)
    self.ATTM_HCP_WT_M = np.round((self.ATTM_HCP_WT_M) / cohorts_required, decimals = 6)
    self.ATTM_HCP_WT_O = np.round((self.ATTM_HCP_WT_O) / cohorts_required, decimals = 6)
    self.ATTM_LCP_WT_Y = np.round((self.ATTM_LCP_WT_Y) / cohorts_required, decimals = 6)
    self.ATTM_LCP_WT_M = np.round((self.ATTM_LCP_WT_M) / cohorts_required, decimals = 6)
    self.ATTM_LCP_WT_O = np.round((self.ATTM_LCP_WT_O) / cohorts_required, decimals = 6)
    self.ATTM_Meadow_WT_Y = np.round((self.ATTM_Meadow_WT_Y) / cohorts_required, decimals = 6)
    self.ATTM_Meadow_WT_M = np.round((self.ATTM_Meadow_WT_M) / cohorts_required, decimals = 6)
    self.ATTM_Meadow_WT_O = np.round((self.ATTM_Meadow_WT_O) / cohorts_required, decimals = 6)
    self.ATTM_SandDunes_WT_Y = np.round((self.ATTM_SandDunes_WT_Y) / cohorts_required, decimals = 6)
    self.ATTM_SandDunes_WT_M = np.round((self.ATTM_SandDunes_WT_M) / cohorts_required, decimals = 6)
    self.ATTM_SandDunes_WT_O = np.round((self.ATTM_SandDunes_WT_O) / cohorts_required, decimals = 6)
    self.ATTM_SaturatedBarrens_WT_Y = np.round((self.ATTM_SaturatedBarrens_WT_Y) / cohorts_required, decimals = 6)
    self.ATTM_SaturatedBarrens_WT_M = np.round((self.ATTM_SaturatedBarrens_WT_M) / cohorts_required, decimals = 6)
    self.ATTM_SaturatedBarrens_WT_O = np.round((self.ATTM_SaturatedBarrens_WT_O) / cohorts_required, decimals = 6)
    self.ATTM_Shrubs_WT_O = np.round((self.ATTM_Shrubs_WT_O) / cohorts_required, decimals = 6)
    self.ATTM_Urban_WT = np.round((self.ATTM_Urban_WT) / cohorts_required, decimals = 6)
    self.ATTM_LargeLakes_WT_Y = np.round((self.ATTM_LargeLakes_WT_Y) / cohorts_required, decimals = 6)
    self.ATTM_LargeLakes_WT_M = np.round((self.ATTM_LargeLakes_WT_M) / cohorts_required, decimals = 6)
    self.ATTM_LargeLakes_WT_O = np.round((self.ATTM_LargeLakes_WT_O) / cohorts_required, decimals = 6)
    self.ATTM_MediumLakes_WT_Y = np.round((self.ATTM_MediumLakes_WT_Y) / cohorts_required, decimals = 6)
    self.ATTM_MediumLakes_WT_M = np.round((self.ATTM_MediumLakes_WT_M) / cohorts_required, decimals = 6)
    self.ATTM_MediumLakes_WT_O = np.round((self.ATTM_MediumLakes_WT_O) / cohorts_required, decimals = 6)
    self.ATTM_SmallLakes_WT_Y = np.round((self.ATTM_SmallLakes_WT_Y) / cohorts_required, decimals = 6)
    self.ATTM_SmallLakes_WT_M = np.round((self.ATTM_SmallLakes_WT_M) / cohorts_required, decimals = 6)
    self.ATTM_SmallLakes_WT_O = np.round((self.ATTM_SmallLakes_WT_O) / cohorts_required, decimals = 6)
    self.ATTM_Ponds_WT_Y = np.round((self.ATTM_Ponds_WT_Y) / cohorts_required, decimals = 6)
    self.ATTM_Ponds_WT_M = np.round((self.ATTM_Ponds_WT_M) / cohorts_required, decimals = 6)
    self.ATTM_Ponds_WT_O = np.round((self.ATTM_Ponds_WT_O) / cohorts_required, decimals = 6)
    self.ATTM_Rivers_WT_Y = np.round((self.ATTM_Rivers_WT_Y) / cohorts_required, decimals = 6)
    self.ATTM_Rivers_WT_M = np.round((self.ATTM_Rivers_WT_M) / cohorts_required, decimals = 6)
    self.ATTM_Rivers_WT_O = np.round((self.ATTM_Rivers_WT_O) / cohorts_required, decimals = 6)
    
    self.ATTM_Total_Fractional_Area = np.round( \
                        self.ATTM_CLC_WT_Y + self.ATTM_CLC_WT_M + self.ATTM_CLC_WT_O + \
                        self.ATTM_CoastalWaters_WT_O + \
                        self.ATTM_DrainedSlope_WT_Y + self.ATTM_DrainedSlope_WT_M + self.ATTM_DrainedSlope_WT_O + \
                        self.ATTM_FCP_WT_Y + self.ATTM_FCP_WT_M + self.ATTM_FCP_WT_O + \
                        self.ATTM_HCP_WT_Y + self.ATTM_HCP_WT_M + self.ATTM_HCP_WT_O + \
                        self.ATTM_LargeLakes_WT_Y + self.ATTM_LargeLakes_WT_M + self.ATTM_LargeLakes_WT_O + \
                        self.ATTM_LCP_WT_Y + self.ATTM_LCP_WT_M + self.ATTM_LCP_WT_O + \
                        self.ATTM_Meadow_WT_Y + self.ATTM_Meadow_WT_M + self.ATTM_Meadow_WT_O + \
                        self.ATTM_MediumLakes_WT_Y + self.ATTM_MediumLakes_WT_M + self.ATTM_MediumLakes_WT_O + \
                        self.ATTM_NoData_WT_O + \
                        self.ATTM_Ponds_WT_Y + self.ATTM_Ponds_WT_M + self.ATTM_Ponds_WT_O + \
                        self.ATTM_Rivers_WT_Y + self.ATTM_Rivers_WT_M + self.ATTM_Rivers_WT_O + \
                        self.ATTM_SandDunes_WT_Y + self.ATTM_SandDunes_WT_M + self.ATTM_SandDunes_WT_O + \
                        self.ATTM_SaturatedBarrens_WT_Y + self.ATTM_SaturatedBarrens_WT_M + self.ATTM_SaturatedBarrens_WT_O +\
                        self.ATTM_Shrubs_WT_O + \
                        self.ATTM_SmallLakes_WT_Y + self.ATTM_SmallLakes_WT_M + self.ATTM_SmallLakes_WT_O + \
                        self.ATTM_Urban_WT, \
                        decimals = 6 )
                                                
    #self.ATTM_Total_Fractional_Area = np.round( \
    #                       self.ATTM_Wet_NPG + self.ATTM_Wet_LCP + \
    #                       self.ATTM_Wet_CLC + self.ATTM_Wet_FCP + \
    #                       self.ATTM_Wet_HCP + self.ATTM_Gra_NPG + \
    #                       self.ATTM_Gra_LCP + self.ATTM_Gra_FCP + \
    #                       self.ATTM_Gra_HCP + self.ATTM_Shr_NPG + \
    #                       self.ATTM_Shr_LCP + self.ATTM_Shr_FCP + \
    #                       self.ATTM_Shr_HCP + self.ATTM_Urban   + \
    #                       self.ATTM_Rivers  + self.ATTM_Lakes   + \
    #                       self.ATTM_Ponds, decimals = 6)

    for i in range(self.ATTM_nrows * self.ATTM_ncols):
        if np.round(self.ATTM_Total_Fractional_Area[i], decimals = 4) > 1.0:
            print 'There is a mass balance problem in element: ', i
            print 'The total fractional area of all cohorts is greater than 1.0'
            print '[in initial_cohort_check]'
            print ' '
            print 'Coalescent Low Center Polygon, Wetland Tundra, Young age: ', self.ATTM_CLC_WT_Y[i]
            print 'Coalescent Low Center Polygon, Wetland Tundra, Medium age: ', self.ATTM_CLC_WT_M[i]
            print 'Coalescent Low Center Polygon, Wetland Tundra, Old age: ', self.ATTM_CLC_WT_O[i]
            print 'Coastal Waters, Wetland Tundra, Old age: ', self.ATTM_CoastalWaters_WT_O[i]
            print 'Drained Slope, Wetland Tundra, Young age: ', self.ATTM_DrainedSlope_WT_Y[i]
            print 'Drained Slope, Wetland Tundra, Medium age: ', self.ATTM_DrainedSlope_WT_M[i]
            print 'Drained Slope, Wetland Tundra, Old age: ', self.ATTM_DrainedSlope_WT_O[i]
            print 'Flat Center Polygon, Wetland Tundra, Young age: ', self.ATTM_FCP_WT_Y[i]
            print 'Flat Center Polygon, Wetland Tundra, Medium age: ', self.ATTM_FCP_WT_M[i]
            print 'Flat Center Polygon, Wetland Tundra, Old age: ', self.ATTM_FCP_WT_O[i]
            print 'High Center Polygon, Wetland Tundra, Young age: ', self.ATTM_HCP_WT_Y[i]
            print 'High Center Polygon, Wetland Tundra, Medium age: ', self.ATTM_HCP_WT_M[i]
            print 'High Center Polygon, Wetland Tundra, Old age: ', self.ATTM_HCP_WT_O[i]
            print 'Large Lakes, Wetland Tundra, Young age: ', self.ATTM_LargeLakes_WT_Y[i]
            print 'Large Lakes, Wetland Tundra, Medium age: ', self.ATTM_LargeLakes_WT_M[i]
            print 'Large Lakes, Wetland Tundra, Old age: ', self.ATTM_LargeLakes_WT_O[i]
            print 'Low Center Polygon, Wetland Tundra, Young age: ', self.ATTM_LCP_WT_Y[i]
            print 'Low Center Polygon, Wetland Tundra, Medium age: ', self.ATTM_LCP_WT_M[i]
            print 'Low Center Polygon, Wetland Tundra, Old age: ', self.ATTM_LCP_WT_O[i]
            print 'Meadow, Wetland Tundra, Young age: ', self.ATTM_Meadow_WT_Y[i]
            print 'Meadow, Wetland Tundra, Medium age: ', self.ATTM_Meadow_WT_M[i]
            print 'Meadow, Wetland Tundra, Old age: ', self.ATTM_Meadow_WT_O[i]
            print 'Medium Lakes, Wetland Tundra, Young age: ', self.ATTM_MediumLakes_WT_Y[i]
            print 'Medium Lakes, Wetland Tundra, Medium age: ', self.ATTM_MediumLakes_WT_M[i]
            print 'Medium Lakes, Wetland Tundra, Old age: ', self. ATTM_MediumLakes_WT_O[i]
            print 'No Data, Wetland Tundra, Old age: ', self.ATTM_NoData_WT_O[i]
            print 'Ponds, Wetland Tundra, Young age: ', self.ATTM_Ponds_WT_Y[i]
            print 'Ponds, Wetland Tundra, Medium age: ', self.ATTM_Ponds_WT_M[i]
            print 'Ponds, Wetland Tundra, Old age: ', self.ATTM_Ponds_WT_O[i]
            print 'Rivers, Wetland Tundra, Young age: ', self.ATTM_Rivers_WT_Y[i]
            print 'Rivers, Wetland Tundra, Medium age: ', self.ATTM_Rivers_WT_M[i]
            print 'Rivers, Wetland Tundra, Old age: ', self.ATTM_Rivers_WT_O[i]
            print 'Sand Dunes, Wetland Tundra, Young age: ', self.SandDunes_WT_Y[i]
            print 'Sand Dunes, Wetland Tundra, Medium age: ', self.SandDunes_WT_M[i]
            print 'Sand Dunes, Wetland Tundra, Old age: ', self.SandDunes_WT_O[i]
            print 'Saturated Barrens, Wetland Tundra, Young age: ', self.SaturatedBarrens_WT_Y[i]
            print 'Saturated Barrens, Wetland Tundra, Medium age: ', self.SatureatedBarrens_WT_M[i]
            print 'Saturated Barrens, Wetland Tundra, Old age: ', self.SaturatedBarrens_WT_O[i]
            print 'Shrubs, Wetland Tundra, Old age: ', self.Shrubs_WT_O[i]
            print 'Small Lakes, Wetland Tundra, Young age: ', self.ATTM_SmallLakes_WT_Y[i]
            print 'Small Lakes, Wetland Tundra, Medium age: ', self.ATTM_SmallLakes_WT_M[i]
            print 'Small Lakes, Wetland Tundra, Old age: ', self.ATTM_SmallLakes_WT_O[i]
            print 'Urban area, Wetland Tundra: ', self.ATTM_Urban_WT[i]
            #print 'Wetland Non Polygonal Ground: ',          self.ATTM_Wet_NPG[i]
            #print 'Wetland Low Center Polygon: ',            self.ATTM_Wet_LCP[i]
            #print 'Wetland Coalescent Low Center Polygon: ', self.ATTM_Wet_CLC[i]
            #print 'Wetland Flat Center Polygon: ',           self.ATTM_Wet_FCP[i]
            #print 'Wetland High Center Polygon: ',           self.ATTM_Wet_HCP[i]
            #print 'Rivers: ' ,                               self.ATTM_Rivers[i]
            #print 'Lakes: ',                                 self.ATTM_Lakes[i]
            #print 'Ponds: ',                                 self.ATTM_Ponds[i]
            #print 'Urban: ',                                 self.ATTM_Urban[i]
            print 'Total Fractions: ',                       self.ATTM_Total_Fractional_Area[i]
            exit()
        if np.round(self.ATTM_Total_Fractional_Area[i], decimals = 4) < 0.0:
            print 'There is a mass balance problem in element: ', i
            print 'The total fractional area of all cohorts is less than 0.0.'
            print '[in initial_cohort_check]'
            print ' '
            #print 'Wetland Non Polygonal Ground: ',          self.ATTM_Wet_NPG[i]
            #print 'Wetland Low Center Polygon: ',            self.ATTM_Wet_LCP[i]
            #print 'Wetland Coalescent Low Center Polygon: ', self.ATTM_Wet_CLC[i]
            #print 'Wetland Flat Center Polygon: ',           self.ATTM_Wet_FCP[i]
            #print 'Wetland High Center Polygon: ',           self.ATTM_Wet_HCP[i]
            #print 'Rivers: ' ,                               self.ATTM_Rivers[i]
            #print 'Lakes: ',                                 self.ATTM_Lakes[i]
            #print 'Ponds: ',                                 self.ATTM_Ponds[i]
            #print 'Urban: ',                                 self.ATTM_Urban[i]
            print 'Coalescent Low Center Polygon, Wetland Tundra, Young age: ', self.ATTM_CLC_WT_Y[i]
            print 'Coalescent Low Center Polygon, Wetland Tundra, Medium age: ', self.ATTM_CLC_WT_M[i]
            print 'Coalescent Low Center Polygon, Wetland Tundra, Old age: ', self.ATTM_CLC_WT_O[i]
            print 'Coastal Waters, Wetland Tundra, Old age: ', self.ATTM_CoastalWaters_WT_O[i]
            print 'Drained Slope, Wetland Tundra, Young age: ', self.ATTM_DrainedSlope_WT_Y[i]
            print 'Drained Slope, Wetland Tundra, Medium age: ', self.ATTM_DrainedSlope_WT_M[i]
            print 'Drained Slope, Wetland Tundra, Old age: ', self.ATTM_DrainedSlope_WT_O[i]
            print 'Flat Center Polygon, Wetland Tundra, Young age: ', self.ATTM_FCP_WT_Y[i]
            print 'Flat Center Polygon, Wetland Tundra, Medium age: ', self.ATTM_FCP_WT_M[i]
            print 'Flat Center Polygon, Wetland Tundra, Old age: ', self.ATTM_FCP_WT_O[i]
            print 'High Center Polygon, Wetland Tundra, Young age: ', self.ATTM_HCP_WT_Y[i]
            print 'High Center Polygon, Wetland Tundra, Medium age: ', self.ATTM_HCP_WT_M[i]
            print 'High Center Polygon, Wetland Tundra, Old age: ', self.ATTM_HCP_WT_O[i]
            print 'Large Lakes, Wetland Tundra, Young age: ', self.ATTM_LargeLakes_WT_Y[i]
            print 'Large Lakes, Wetland Tundra, Medium age: ', self.ATTM_LargeLakes_WT_M[i]
            print 'Large Lakes, Wetland Tundra, Old age: ', self.ATTM_LargeLakes_WT_O[i]
            print 'Low Center Polygon, Wetland Tundra, Young age: ', self.ATTM_LCP_WT_Y[i]
            print 'Low Center Polygon, Wetland Tundra, Medium age: ', self.ATTM_LCP_WT_M[i]
            print 'Low Center Polygon, Wetland Tundra, Old age: ', self.ATTM_LCP_WT_O[i]
            print 'Meadow, Wetland Tundra, Young age: ', self.ATTM_Meadow_WT_Y[i]
            print 'Meadow, Wetland Tundra, Medium age: ', self.ATTM_Meadow_WT_M[i]
            print 'Meadow, Wetland Tundra, Old age: ', self.ATTM_Meadow_WT_O[i]
            print 'Medium Lakes, Wetland Tundra, Young age: ', self.ATTM_MediumLakes_WT_Y[i]
            print 'Medium Lakes, Wetland Tundra, Medium age: ', self.ATTM_MediumLakes_WT_M[i]
            print 'Medium Lakes, Wetland Tundra, Old age: ', self. ATTM_MediumLakes_WT_O[i]
            print 'No Data, Wetland Tundra, Old age: ', self.ATTM_NoData_WT_O[i]
            print 'Ponds, Wetland Tundra, Young age: ', self.ATTM_Ponds_WT_Y[i]
            print 'Ponds, Wetland Tundra, Medium age: ', self.ATTM_Ponds_WT_M[i]
            print 'Ponds, Wetland Tundra, Old age: ', self.ATTM_Ponds_WT_O[i]
            print 'Rivers, Wetland Tundra, Young age: ', self.ATTM_Rivers_WT_Y[i]
            print 'Rivers, Wetland Tundra, Medium age: ', self.ATTM_Rivers_WT_M[i]
            print 'Rivers, Wetland Tundra, Old age: ', self.ATTM_Rivers_WT_O[i]
            print 'Sand Dunes, Wetland Tundra, Young age: ', self.SandDunes_WT_Y[i]
            print 'Sand Dunes, Wetland Tundra, Medium age: ', self.SandDunes_WT_M[i]
            print 'Sand Dunes, Wetland Tundra, Old age: ', self.SandDunes_WT_O[i]
            print 'Saturated Barrens, Wetland Tundra, Young age: ', self.SaturatedBarrens_WT_Y[i]
            print 'Saturated Barrens, Wetland Tundra, Medium age: ', self.SatureatedBarrens_WT_M[i]
            print 'Saturated Barrens, Wetland Tundra, Old age: ', self.SaturatedBarrens_WT_O[i]
            print 'Shrubs, Wetland Tundra, Old age: ', self.Shrubs_WT_O[i]
            print 'Small Lakes, Wetland Tundra, Young age: ', self.ATTM_SmallLakes_WT_Y[i]
            print 'Small Lakes, Wetland Tundra, Medium age: ', self.ATTM_SmallLakes_WT_M[i]
            print 'Small Lakes, Wetland Tundra, Old age: ', self.ATTM_SmallLakes_WT_O[i]
            print 'Urban area, Wetland Tundra: ', self.ATTM_Urban_WT[i]
            print 'Total Fractions: ',                       self.ATTM_Total_Fractional_Area[i]
            exit()
    # Statement of what has been done for debugging
    print '      done.'
    print ' '

    if self.initialize['Normalized_Cohort_Distribution_Figure'].lower() == 'yes':    
        cohort_check = np.reshape(self.ATTM_Total_Fractional_Area,  [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # Files for plotting & reference #
        #ATTM_Wet_NPG_plot =  np.reshape(self.ATTM_Wet_NPG,      [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Wet_LCP_plot =  np.reshape(self.ATTM_Wet_LCP,      [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Wet_CLC_plot =  np.reshape(self.ATTM_Wet_CLC,      [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Wet_FCP_plot =  np.reshape(self.ATTM_Wet_FCP,      [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Wet_HCP_plot =  np.reshape(self.ATTM_Wet_FCP,      [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Rivers_plot  =  np.reshape(self.ATTM_Rivers,       [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Lakes_plot   =  np.reshape(self.ATTM_Lakes,        [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Ponds_plot   =  np.reshape(self.ATTM_Ponds,        [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Urban_plot   =  np.reshape(self.ATTM_Urban,        [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Total_plot   =  np.reshape(self.ATTM_Total_Fractional_Area,\
                                        [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        ATTM_CLC_WT_Y_plot = np.reshape(self.ATTM_CLC_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_CLC_WT_M_plot = np.reshape(self.ATTM_CLC_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_CLC_WT_O_plot = np.reshape(self.ATTM_CLC_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_CoastalWaters_WT_O_plot = np.reshape(self.ATTM_CoastalWaters_WT_O, \
                                                   [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_DrainedSlope_WT_Y_plot = np.reshape(self.ATTM_DrainedSlope_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_DrainedSlope_WT_M_plot = np.reshape(self.ATTM_DrainedSlope_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_DrainedSlope_WT_O_plot = np.reshape(self.ATTM_DrainedSlope_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_FCP_WT_Y_plot = np.reshape(self.ATTM_FCP_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_FCP_WT_M_plot = np.reshape(self.ATTM_FCP_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_FCP_WT_O_plot = np.reshape(self.ATTM_FCP_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_HCP_WT_Y_plot = np.reshape(self.ATTM_HCP_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_HCP_WT_M_plot = np.reshape(self.ATTM_HCP_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_HCP_WT_O_plot = np.reshape(self.ATTM_HCP_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_LCP_WT_Y_plot = np.reshape(self.ATTM_LCP_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_LCP_WT_M_plot = np.reshape(self.ATTM_LCP_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_LCP_WT_O_plot = np.reshape(self.ATTM_LCP_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Meadow_WT_Y_plot = np.reshape(self.ATTM_Meadow_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Meadow_WT_M_plot = np.reshape(self.ATTM_Meadow_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Meadow_WT_O_plot = np.reshape(self.ATTM_Meadow_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SandDunes_WT_Y_plot = np.reshape(self.ATTM_SandDunes_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SandDunes_WT_M_plot = np.reshape(self.ATTM_SandDunes_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SandDunes_WT_O_plot = np.reshape(self.ATTM_SandDunes_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SaturatedBarrens_WT_Y_plot = np.reshape(self.ATTM_SandDunes_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SaturatedBarrens_WT_M_plot = np.reshape(self.ATTM_SandDunes_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SaturatedBarrens_WT_O_plot = np.reshape(self.ATTM_SandDunes_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Shrubs_WT_O_plot = np.reshape(self.ATTM_Shrubs_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Urban_WT_plot = np.reshape(self.ATTM_Urban_WT, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_LargeLakes_WT_Y_plot = np.reshape(self.ATTM_LargeLakes_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_LargeLakes_WT_M_plot = np.reshape(self.ATTM_LargeLakes_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_LargeLakes_WT_O_plot = np.reshape(self.ATTM_LargeLakes_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_MediumLakes_WT_Y_plot = np.reshape(self.ATTM_MediumLakes_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_MediumLakes_WT_M_plot = np.reshape(self.ATTM_MediumLakes_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_MediumLakes_WT_O_plot = np.reshape(self.ATTM_MediumLakes_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SmallLakes_WT_Y_plot = np.reshape(self.ATTM_SmallLakes_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SmallLakes_WT_M_plot = np.reshape(self.ATTM_SmallLakes_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SmallLakes_WT_O_plot = np.reshape(self.ATTM_SmallLakes_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Ponds_WT_Y_plot = np.reshape(self.ATTM_Ponds_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Ponds_WT_M_plot = np.reshape(self.ATTM_Ponds_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Ponds_WT_O_plot = np.reshape(self.ATTM_Ponds_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Rivers_WT_Y_plot = np.reshape(self.ATTM_Rivers_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Rivers_WT_M_plot = np.reshape(self.ATTM_Rivers_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Rivers_WT_O_plot = np.reshape(self.ATTM_Rivers_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

                                        
        #----------------------------
        # Move to Output Directory
        #----------------------------
        os.chdir(self.control['Run_dir']+self.Output_directory)

        # -----------------------------------------------------------------------------
        # Output files and figures
        # -----------------------------------------------------------------------------
        if self.initialize['WetNPG_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_NPG_plot, interpolation='nearest', cmap='bone')
            pl.title('Wetland Non-polygonal Ground (meadow) Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./Wet_NPG/Wet_NPG_Initial_Fraction.png', format = 'png')
            self.ATTM_Wet_NPG.tofile('./Wet_NPG/Wet_NPG_fractional_cohorts.bin')
            pl.close()
        # -----------------------------------------------------------------------------
        if self.initialize['WetLCP_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_LCP_plot, interpolation='nearest', cmap='bone')
            pl.title('Wetland Low Center Polygon Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./Wet_LCP/Wet_LCP_Initial_Fraction.png', format = 'png')
            self.ATTM_Wet_LCP.tofile('./Wet_LCP/Wet_LCP_fractional_cohorts.bin')
            pl.close()
        # -----------------------------------------------------------------------------
        if self.initialize['WetCLC_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_CLC_plot, interpolation='nearest', cmap='bone')
            pl.title('Wetland Coalescent Low Center Polygon Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./Wet_CLC/Wet_CLC_Initial_Fraction.png', format = 'png')
            self.ATTM_Wet_CLC.tofile('./Wet_CLC/Wet_CLC_fractional_cohorts.bin')
            pl.close()
        # -----------------------------------------------------------------------------
        if self.initialize['WetFCP_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_FCP_plot, interpolation='nearest', cmap='bone')
            pl.title('Wetland Flat Center Polygon Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./Wet_FCP/Wet_FCP_Initial_Fraction.png', format = 'png')
            self.ATTM_Wet_FCP.tofile('./Wet_FCP/Wet_FCP_fractional_cohorts.bin')
            pl.close()
         # -----------------------------------------------------------------------------
        if self.initialize['WetHCP_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_HCP_plot, interpolation='nearest', cmap='bone')
            pl.title('Wetland High Center Polygon Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./Wet_HCP/Wet_HCP_Initial_Fraction.png', format = 'png')
            self.ATTM_Wet_HCP.tofile('./Wet_HCP/Wet_HCP_fractional_cohorts.bin')
            pl.close()
        # -----------------------------------------------------------------------------
        if self.initialize['Rivers_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Rivers_plot, interpolation='nearest', cmap='bone')
            pl.title('Rivers Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./Other_Cohorts/Rivers_Initial_Fraction.png', format = 'png')
            self.ATTM_Rivers.tofile('./Other_Cohorts/Rivers_fractional_cohorts.bin')
            pl.close()
        # -----------------------------------------------------------------------------
        if self.initialize['Ponds_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Ponds_plot, interpolation='nearest', cmap='bone')
            pl.title('Ponds (shallow lake) Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./Ponds/Ponds_Initial_Fraction.png', format = 'png')
            self.ATTM_Ponds.tofile('./Ponds/Ponds_fractional_cohorts.bin')
            pl.close()
        # -----------------------------------------------------------------------------
        if self.initialize['Lakes_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Lakes_plot, interpolation='nearest', cmap='bone')
            pl.title('Lakes Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./Lakes/Lakes_Initial_Fraction.png', format = 'png')
            self.ATTM_Lakes.tofile('./Lakes/Lakes_fractional_cohorts.bin')
            pl.close()
        # -----------------------------------------------------------------------------
        if self.initialize['Urban_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Urban_plot, interpolation='nearest', cmap='bone')
            pl.title('Urban Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./Other_Cohorts/Urban_Initial_Fraction.png', format = 'png')
            ATTM_Urban_plot.tofile('./Other_Cohorts/Urban_fractional_cohorts.bin')
            pl.close()
        # -----------------------------------------------------------------------------
        if self.initialize['Total_Cohorts_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Total_plot, interpolation='nearest', cmap='bone')
            pl.title('Total of All Initial Fractional Areas')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./All_Cohorts/Total_Cohort_Initial_Fraction.png', format = 'png')
            self.ATTM_Total_Fractional_Area.tofile('./All_Cohorts/Initial_Cohort_Fractional_Area.bin')
            pl.close()

        # ----------------------------------------------------------------------
        if self.initialize['CLC_WT_Y_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_CLC_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Coalescent Low Center Polygon\n Wetland Tundra - Young Age\n Initial Cohort Fraction')
            pl.savefig('./CLC_WT_Y/Initial_Fraction_CLC_WT_Y.png', format = 'png')
            self.ATTM_CLC_WT_Y.tofile('./CLC_WT_Y/CLC_WT_Y_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['CLC_WT_M_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_CLC_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Coalescent Low Center Polygon\n Wetland Tundra - Medium Age\n Initial Cohort Fraction')
            pl.savefig('./CLC_WT_M/Initial_Fraction_CLC_WT_M.png', format = 'png')
            self.ATTM_CLC_WT_M.tofile('./CLC_WT_M/CLC_WT_M_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['CLC_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_CLC_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Coalescent Low Center Polygon\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./CLC_WT_O/Initial_Fraction_CLC_WT_O.png', format = 'png')
            self.ATTM_CLC_WT_O.tofile('./CLC_WT_O/CLC_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['CoastalWaters_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_CoastalWaters_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Coastal Waters\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./CoastalWaters_WT_O/Initial_fractions_CoastalWaters_WT_O.png', format = 'png')
            self.ATTM_CoastalWaters_WT_O.tofile('./CoastalWaters_WT_O/CoastalWaters_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['DrainedSlope_WT_Y_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_DrainedSlope_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Drained Slope\n Wetland Tundra - Young Age\n Initial Cohort Fraction')
            pl.savefig('./DrainedSlope_WT_Y/Initial_Fraction_DrainedSlope_WT_Y.png', format = 'png')
            self.ATTM_DrainedSlope_WT_Y.tofile('./DrainedSlope_WT_Y/DrainedSlope_WT_Y_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['DrainedSlope_WT_M_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_DrainedSlope_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Drained Slope\n Wetland Tundra - Medium Age\n Initial Cohort Fraction')
            pl.savefig('./DrainedSlope_WT_M/Initial_Fraction_DrainedSlope_WT_M.png', format = 'png')
            self.ATTM_DrainedSlope_WT_M.tofile('./DrainedSlope_WT_M/DrainedSlope_WT_M_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['DrainedSlope_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_DrainedSlope_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Drained Slope\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./DrainedSlope_WT_O/Initial_Fraction_DrainedSlope_WT_O.png', format = 'png')
            self.ATTM_DrainedSlope_WT_O.tofile('./DrainedSlope_WT_O/DrainedSlope_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['FCP_WT_Y_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_FCP_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Flat Center Polygon\n Wetland Tundra - Young Age\n Initial Cohort Fraction')
            pl.savefig('./FCP_WT_Y/Initial_Fraction_FCP_WT_Y.png', format = 'png')
            self.ATTM_FCP_WT_Y.tofile('./FCP_WT_Y/FCP_WT_Y_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['FCP_WT_M_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_FCP_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Flat Center Polygon\n Wetland Tundra - Medium Age\n Initial Cohort Fraction')
            pl.savefig('./FCP_WT_M/Initial_Fraction_FCP_WT_M.png', format = 'png')
            self.ATTM_FCP_WT_M.tofile('./FCP_WT_M/FCP_WT_M_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['FCP_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_FCP_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Flat Center Polygon\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./FCP_WT_O/Initial_Fraction_FCP_WT_O.png', format = 'png')
            self.ATTM_FCP_WT_O.tofile('./FCP_WT_O/FCP_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['HCP_WT_Y_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_HCP_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('High Center Polygon\n Wetland Tundra - Young Age\n Initial Cohort Fraction')
            pl.savefig('./HCP_WT_Y/Initial_Fraction_HCP_WT_Y.png', format = 'png')
            self.ATTM_HCP_WT_Y.tofile('./HCP_WT_Y/HCP_WT_Y_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['HCP_WT_M_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_HCP_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('High Center Polygon\n Wetland Tundra - Medium Age\n Initial Cohort Fraction')
            pl.savefig('./HCP_WT_M/Initial_Fraction_HCP_WT_M.png', format = 'png')
            self.ATTM_HCP_WT_M.tofile('./HCP_WT_M/HCP_WT_M_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['HCP_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_HCP_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('High Center Polygon\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./HCP_WT_O/Initial_Fraction_HCP_WT_O.png', format = 'png')
            self.ATTM_HCP_WT_O.tofile('./HCP_WT_O/HCP_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['LCP_WT_Y_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_LCP_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Low Center Polygon\n Wetland Tundra - Young Age\n Initial Cohort Fraction')
            pl.savefig('./LCP_WT_Y/Initial_Fraction_LCP_WT_Y.png', format = 'png')
            self.ATTM_LCP_WT_Y.tofile('./LCP_WT_Y/LCP_WT_Y_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['LCP_WT_M_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_LCP_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Low Center Polygon\n Wetland Tundra - Medium Age\n Initial Cohort Fraction')
            pl.savefig('./LCP_WT_M/Initial_Fraction_LCP_WT_M.png', format = 'png')
            self.ATTM_LCP_WT_M.tofile('./LCP_WT_M/LCP_WT_M_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['LCP_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_LCP_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Low Center Polygon\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./LCP_WT_O/Initial_Fraction_LCP_WT_O.png', format = 'png')
            self.ATTM_LCP_WT_O.tofile('./LCP_WT_O/LCP_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Meadow_WT_Y_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Meadow_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Meadow\n Wetland Tundra - Young Age\n Initial Cohort Fraction')
            pl.savefig('./Meadow_WT_Y/Initial_Fraction_Meadow_WT_Y.png', format = 'png')
            self.ATTM_Meadow_WT_Y.tofile('./Meadow_WT_Y/Meadow_WT_Y_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Meadow_WT_M_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Meadow_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Meadow\n Wetland Tundra - Medium Age\n Initial Cohort Fraction')
            pl.savefig('./Meadow_WT_M/Initial_Fraction_Meadow_WT_M.png', format = 'png')
            self.ATTM_Meadow_WT_M.tofile('./Meadow_WT_M/Meadow_WT_M_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Meadow_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Meadow_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Meadow\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./Meadow_WT_O/Initial_Fraction_Meadow_WT_O.png', format = 'png')
            self.ATTM_Meadow_WT_O.tofile('./Meadow_WT_O/Meadow_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SaturatedBarrens_WT_Y_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SaturatedBarrens_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Saturated Barrens\n Wetland Tundra - Young Age\n Initial Cohort Fraction')
            pl.savefig('./SaturatedBarrens_WT_Y/Initial_Fraction_SaturatedBarrens_WT_Y.png', format = 'png')
            self.ATTM_SaturatedBarrens_WT_Y.tofile('./SaturatedBarrens_WT_Y/SaturatedBarrens_WT_Y_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SaturatedBarrens_WT_M_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SaturatedBarrens_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Saturated Barrens\n Wetland Tundra - Medium Age\n Initial Cohort Fraction')
            pl.savefig('./SaturatedBarrens_WT_M/Initial_Fraction_SaturatedBarrens_WT_M.png', format = 'png')
            self.ATTM_SaturatedBarrens_WT_M.tofile('./SaturatedBarrens_WT_M/SaturatedBarrens_WT_M_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SaturatedBarrens_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SaturatedBarrens_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Saturated Barrens\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./SaturatedBarrens_WT_O/Initial_Fraction_SaturatedBarrens_WT_O.png', format = 'png')
            self.ATTM_SaturatedBarrens_WT_O.tofile('./SaturatedBarrens_WT_O/SaturatedBarrens_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SandDunes_WT_Y_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SandDunes_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Sand Dunes\n Wetland Tundra - Young Age\n Initial Cohort Fraction')
            pl.savefig('./SandDunes_WT_Y/Initial_Fraction_SandDunes_WT_Y.png', format = 'png')
            self.ATTM_SandDunes_WT_Y.tofile('./SandDunes_WT_Y/SandDunes_WT_Y_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SandDunes_WT_M_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SandDunes_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Sand Dunes\n Wetland Tundra - Medium Age\n Initial Cohort Fraction')
            pl.savefig('./SandDunes_WT_M/Initial_Fraction_SandDunes_WT_M.png', format = 'png')
            self.ATTM_SandDunes_WT_M.tofile('./SandDunes_WT_M/SandDunes_WT_M_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SandDunes_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SandDunes_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Sand Dunes\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./SandDunes_WT_O/Initial_Fraction_SandDunes_WT_O.png', format = 'png')
            self.ATTM_SandDunes_WT_O.tofile('./SandDunes_WT_O/SandDunes_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Shrubs_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Shrubs_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Shrubs\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./Shrubs_WT_O/Initial_Fraction_Shrubs_WT_O.png', format = 'png')
            self.ATTM_Shrubs_WT_O.tofile('./Shrubs_WT_O/Shrubs_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Urban_WT_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Urban_WT_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Urban Area \n Wetland Tundra \n Initial Cohort Fraction')
            pl.savefig('./Urban_WT/Initial_Fraction_Urban_WT.png', format = 'png')
            self.ATTM_Urban_WT.tofile('./Urban_WT/Urban_WT_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['LargeLakes_WT_Y_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_LargeLakes_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Large Lakes\n Wetland Tundra - Young Age\n Initial Cohort Fraction')
            pl.savefig('./LargeLakes_WT_Y/Initial_Fraction_LargeLakes_WT_Y.png', format = 'png')
            self.ATTM_LargeLakes_WT_Y.tofile('./LargeLakes_WT_Y/LargeLakes_WT_Y_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['LargeLakes_WT_M_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_LargeLakes_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Large Lakes\n Wetland Tundra - Medium Age\n Initial Cohort Fraction')
            pl.savefig('./LargeLakes_WT_M/Initial_Fraction_LargeLakes_WT_M.png', format = 'png')
            self.ATTM_LargeLakes_WT_M.tofile('./LargeLakes_WT_M/LargeLakes_WT_M_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['LargeLakes_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_LargeLakes_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('LargeLakes\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./LargeLakes_WT_O/Initial_Fraction_LargeLakes_WT_O.png', format = 'png')
            self.ATTM_LargeLakes_WT_O.tofile('./LargeLakes_WT_O/LargeLakes_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['MediumLakes_WT_Y_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_MediumLakes_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Medium Lakes\n Wetland Tundra - Young Age\n Initial Cohort Fraction')
            pl.savefig('./MediumLakes_WT_Y/Initial_Fraction_MediumLakes_WT_Y.png', format = 'png')
            self.ATTM_MediumLakes_WT_Y.tofile('./MediumLakes_WT_Y/MediumLakes_WT_Y_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['MediumLakes_WT_M_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_MediumLakes_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Medium Lakes\n Wetland Tundra - Medium Age\n Initial Cohort Fraction')
            pl.savefig('./MediumLakes_WT_M/Initial_Fraction_MediumLakes_WT_M.png', format = 'png')
            self.ATTM_MediumLakes_WT_M.tofile('./MediumLakes_WT_M/MediumLakes_WT_M_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['MediumLakes_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_MediumLakes_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('MediumLakes\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./MediumLakes_WT_O/Initial_Fraction_MediumLakes_WT_O.png', format = 'png')
            self.ATTM_MediumLakes_WT_O.tofile('./MediumLakes_WT_O/MediumLakes_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SmallLakes_WT_Y_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SmallLakes_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Small Lakes\n Wetland Tundra - Young Age\n Initial Cohort Fraction')
            pl.savefig('./SmallLakes_WT_Y/Initial_Fraction_SmallLakes_WT_Y.png', format = 'png')
            self.ATTM_SmallLakes_WT_Y.tofile('./SmallLakes_WT_Y/SmallLakes_WT_Y_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SmallLakes_WT_M_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SmallLakes_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Small Lakes\n Wetland Tundra - Medium Age\n Initial Cohort Fraction')
            pl.savefig('./SmallLakes_WT_M/Initial_Fraction_SmallLakes_WT_M.png', format = 'png')
            self.ATTM_SmallLakes_WT_M.tofile('./SmallLakes_WT_M/SmallLakes_WT_M_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SmallLakes_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SmallLakes_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('SmallLakes\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./SmallLakes_WT_O/Initial_Fraction_SmallLakes_WT_O.png', format = 'png')
            self.ATTM_SmallLakes_WT_O.tofile('./SmallLakes_WT_O/SmallLakes_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Ponds_WT_Y_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Ponds_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Ponds\n Wetland Tundra - Young Age\n Initial Cohort Fraction')
            pl.savefig('./Ponds_WT_Y/Initial_Fraction_Ponds_WT_Y.png', format = 'png')
            self.ATTM_Ponds_WT_Y.tofile('./Ponds_WT_Y/Ponds_WT_Y_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Ponds_WT_M_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Ponds_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Ponds\n Wetland Tundra - Medium Age\n Initial Cohort Fraction')
            pl.savefig('./Ponds_WT_M/Initial_Fraction_Ponds_WT_M.png', format = 'png')
            self.ATTM_Ponds_WT_M.tofile('./Ponds_WT_M/Ponds_WT_M_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Ponds_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Ponds_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Ponds\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./Ponds_WT_O/Initial_Fraction_Ponds_WT_O.png', format = 'png')
            self.ATTM_Ponds_WT_O.tofile('./Ponds_WT_O/Ponds_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Rivers_WT_Y_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Rivers_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Rivers\n Wetland Tundra - Young Age\n Initial Cohort Fraction')
            pl.savefig('./Rivers_WT_Y/Initial_Fraction_Rivers_WT_Y.png', format = 'png')
            self.ATTM_Rivers_WT_Y.tofile('./Rivers_WT_Y/Rivers_WT_Y_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Rivers_WT_M_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Rivers_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Rivers\n Wetland Tundra - Medium Age\n Initial Cohort Fraction')
            pl.savefig('./Rivers_WT_M/Initial_Fraction_Rivers_WT_M.png', format = 'png')
            self.ATTM_Rivers_WT_M.tofile('./Rivers_WT_M/Rivers_WT_M_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Rivers_WT_O_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Rivers_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Rivers\n Wetland Tundra - Old Age\n Initial Cohort Fraction')
            pl.savefig('./Rivers_WT_O/Initial_Fraction_Rivers_WT_O.png', format = 'png')
            self.ATTM_Rivers_WT_O.tofile('./Rivers_WT_O/Rivers_WT_O_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        # -----------------------------------------------------------------------------
        # Return to Run Directory
        #----------------------------------
        os.chdir(self.control['Run_dir'])


def tanana_initial_cohort_check(self):
    """
    The purpose of this module is to ensure that all fractional land-surface cohorts, in each element,
    sums to one.  There are errors introducted in the the interpolation process
    (from Mark Lara files to 25x25m resolution).

    The initial step is to compare the total number of fine-resolution cohorts to the total number
    of cohorts.  In nearly all the ATTM elements, the total fractional area is not 1.0 (either above
    or below).  At this point, the land-surface cohorts are normalized to the ATTM element (in order to
    ensure 1.0.

    On the edges of the model domain (i.e. in areas in contact with the ocean), the total fractional area
    of land-surface cohorts is most likely significantly less than 1.0.  In these cases, the fractional
    area will not be normalized.

    The minimum total fractional area required for normalization is 0.50.

    """
    # Statement for debugging
    print '    Checking initial cohorts, normalizing to 1.0'
    
    # ----------------------------------------------------------------------
    # Determine the initial/original total fractional area of each element.
    # ----------------------------------------------------------------------
    cohort_check = self.ATTM_Total / ((float(self.X_resolution)/(self.x_res)) * float(self.Y_resolution)/ \
                   (self.y_res))

    #=====================================================================================
    # If the total fractional area of element is greater than 0.5, normalize each cohort
    # in order get to 1.0
    #=====================================================================================
    # Note: In the Barrow example, the cohorts_required = 1600. Just leaving as flexible as
    #       possible.
    #-------------------------------------------------------------------------------------
    cohorts_required = ((float(self.X_resolution)/(self.x_res)) * float(self.Y_resolution)/ \
                        (self.y_res))

    for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
        if cohort_check[i] > 0.5:
            #-----------------------------------------------
            # The normalization process
            # adjustment = (cohorts_required / ATTM_Total)
            # cohort_new = cohort * adjustment
            # - - - - - - - - - - - - - - - - - - - - - - - 
            # The new ATTM_Total should = cohorts_required
            #-----------------------------------------------
            adjustment = cohorts_required / self.ATTM_Total[i]

            # Adjust all the land surface cohorts
            if self.ATTM_TF_OB[i] > 0. : self.ATTM_TF_OB[i] = self.ATTM_TF_OB[i]*adjustment
            if self.ATTM_TF_YB[i] > 0. : self.ATTM_TF_YB[i] = self.ATTM_TF_YB[i]*adjustment
            if self.ATTM_TF_OF[i] > 0. : self.ATTM_TF_OF[i] = self.ATTM_TF_OF[i]*adjustment
            if self.ATTM_TF_YF[i] > 0. : self.ATTM_TF_YF[i] = self.ATTM_TF_YF[i]*adjustment
            if self.ATTM_TF_Dec_PP[i] > 0. : self.ATTM_TF_Dec_PP[i] = self.ATTM_TF_Dec_PP[i]*adjustment
            if self.ATTM_TF_Con_PP[i] > 0. : self.ATTM_TF_Con_PP[i] = self.ATTM_TF_Con_PP[i]*adjustment
            if self.ATTM_TF_TL[i] > 0. : self.ATTM_TF_TL[i] = self.ATTM_TF_TL[i]*adjustment

    # Convert all land surface cohorts into fractional area of element
    self.ATTM_TF_OB = np.round((self.ATTM_TF_OB) / cohorts_required, decimals = 6)
    self.ATTM_TF_YB = np.round((self.ATTM_TF_YB) / cohorts_required, decimals = 6)
    self.ATTM_TF_OF = np.round((self.ATTM_TF_OF) / cohorts_required, decimals = 6)
    self.ATTM_TF_YF = np.round((self.ATTM_TF_YF) / cohorts_required, decimals = 6)
    self.ATTM_TF_Con_PP = np.round((self.ATTM_TF_Con_PP) / cohorts_required, decimals = 6)
    self.ATTM_TF_Dec_PP = np.round((self.ATTM_TF_Dec_PP) / cohorts_required, decimals = 6)
    self.ATTM_TF_TL = np.round((self.ATTM_TF_TL) / cohorts_required, decimals = 6)

    self.ATTM_Total_Fractional_Area = np.round( \
                           self.ATTM_TF_OB + self.ATTM_TF_YB + \
                           self.ATTM_TF_OF + self.ATTM_TF_YF + \
                           self.ATTM_TF_Dec_PP + self.ATTM_TF_Con_PP + \
                           self.ATTM_TF_TL,  decimals = 6)

    for i in range(self.ATTM_nrows * self.ATTM_ncols):
        if np.round(self.ATTM_Total_Fractional_Area[i], decimals = 4) > 1.0:
            print 'There is a mass balance problem in element: ', i
            print 'The total fractional area of all cohorts is greater than 1.0'
            print '[in initial_cohort_check]'
            print ' '
            print 'Tanana Flats Old Bog: ',                  self.ATTM_TF_OB[i]
            print 'Tanana Flats Young Bog: ',                self.ATTM_TF_YB[i]
            print 'Tanana Flats Old Fen: ',                  self.ATTM_TF_OF[i]
            print 'Tanana Flats Young Fen: ',                self.ATTM_TF_YF[i]
            print 'Tanana Flats Deciduous Permafrost Plateau: ',  self.ATTM_TF_Dec_PP[i]
            print 'Tanana Flats Coniferous Permafrost Plateau: ', self.ATTM_TF_Con_PP[i]
            print 'Tanana Flats Thermokarst Lakes: ' ,       self.ATTM_TF_TL[i]
            print 'Total Fractions: ',                       self.ATTM_Total_Fractional_Area[i]
            exit()
        if np.round(self.ATTM_Total_Fractional_Area[i], decimals = 4) < 0.0:
            print 'There is a mass balance problem in element: ', i
            print 'The total fractional area of all cohorts is less than 0.0.'
            print '[in initial_cohort_check]'
            print ' '
            print 'Tanana Flats Old Bog: ',                  self.ATTM_TF_OB[i]
            print 'Tanana Flats Young Bog: ',                self.ATTM_TF_YB[i]
            print 'Tanana Flats Old Fen: ',                  self.ATTM_TF_OF[i]
            print 'Tanana Flats Young Fen: ',                self.ATTM_TF_YF[i]
            print 'Tanana Flats Coniferous Permafrost Plateau: ', self.ATTM_TF_Con_PP[i]
            print 'Tanana Flats Deciduous Permafrost Plateau: ', self.ATTM_TF_Dec_PP[i]
            print 'Tanana Flats Thermokarst Lakes: ' ,       self.ATTM_TF_TL[i]
            print 'Total Fractions: ',                       self.ATTM_Total_Fractional_Area[i]
            exit()
    # Statement of what has been done for debugging
    print '      done.'
    print ' '

    if self.initialize['Normalized_Cohort_Distribution_Figure'].lower() == 'yes':    
        cohort_check = np.reshape(self.ATTM_Total_Fractional_Area,  [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # Files for plotting & reference #
        ATTM_TF_OB_plot =  np.reshape(self.ATTM_TF_OB,        [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_YB_plot =  np.reshape(self.ATTM_TF_YB,        [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_OF_plot =  np.reshape(self.ATTM_TF_OF,        [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_YF_plot =  np.reshape(self.ATTM_TF_YF,        [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_Con_PP_plot = np.reshape(self.ATTM_TF_Con_PP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_Dec_PP_plot = np.reshape(self.ATTM_TF_Dec_PP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_TL_plot     =  np.reshape(self.ATTM_TF_TL,    [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Total_plot     =  np.reshape(self.ATTM_Total_Fractional_Area,\
                                        [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        #----------------------------
        # Move to Output Directory
        #----------------------------
        os.chdir(self.control['Run_dir']+self.Output_directory)

        # -----------------------------------------------------------------------------
        # Output files and figures
        # -----------------------------------------------------------------------------
        if self.initialize['TF_OB_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_OB_plot, interpolation='nearest', cmap='bone')
            pl.title('Tanana Flat Old Bog Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./TF_OB/TF_OB_Initial_Fraction.png', format = 'png')
            self.ATTM_TF_OB.tofile('./TF_OB/TF_OB_fractional_cohorts.bin')
            pl.close()
        # -----------------------------------------------------------------------------
        if self.initialize['TF_YB_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_YB_plot, interpolation='nearest', cmap='bone')
            pl.title('Tanana Flats Young Bog Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./TF_YB/TF_YB_Initial_Fraction.png', format = 'png')
            self.ATTM_TF_YB.tofile('./TF_YB/TF_YB_fractional_cohorts.bin')
            pl.close()
        # -----------------------------------------------------------------------------
        if self.initialize['TF_OF_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_OF_plot, interpolation='nearest', cmap='bone')
            pl.title('Tanana Flats Old Fen Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./TF_OF/TF_OF_Initial_Fraction.png', format = 'png')
            self.ATTM_TF_OF.tofile('./TF_OF/TF_OF_fractional_cohorts.bin')
            pl.close()
        # -----------------------------------------------------------------------------
        if self.initialize['TF_YF_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_YF_plot, interpolation='nearest', cmap='bone')
            pl.title('Tanana Flats Young Fen Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./TF_YF/TF_YF_Initial_Fraction.png', format = 'png')
            self.ATTM_TF_YF.tofile('./TF_YF/TF_YF_fractional_cohorts.bin')
            pl.close()
         # -----------------------------------------------------------------------------
        if self.initialize['TF_Con_PP_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_Con_PP_plot, interpolation='nearest', cmap='bone')
            pl.title('Tanana Flats Coniferous Permafrost Plateau Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./TF_Con_PP/TF_Con_PP_Initial_Fraction.png', format = 'png')
            self.ATTM_TF_Con_PP.tofile('./TF_Con_PP/TF_Con_PP_fractional_cohorts.bin')
            pl.close()
        # -----------------------------------------------------------------------------
        if self.initialize['TF_Dec_PP_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_Dec_PP_plot, interpolation='nearest', cmap='bone')
            pl.title('Tanana Flats Deciduous Permafrost Plateau Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./TF_Dec_PP/TF_Dec_PP_Initial_Fraction.png', format = 'png')
            self.ATTM_TF_Dec_PP.tofile('./TF_Dec_PP/TF_Dec_PP_fractional_cohorts.bin')
            pl.close()
        # -----------------------------------------------------------------------------        
        if self.initialize['TF_TL_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_TL_plot, interpolation='nearest', cmap='bone')
            pl.title('Tanana Flats Thermokarst Lake Initial Fractional Area')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./TF_TL/TF_TL_Initial_Fraction.png', format = 'png')
            self.ATTM_TF_TL.tofile('./TF_TL/TL_TL_fractional_cohorts.bin')
            pl.close()
        # -----------------------------------------------------------------------------
        if self.initialize['TF_Total_Cohorts_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Total_plot, interpolation='nearest', cmap='bone')
            pl.title('Total of All Initial Fractional Areas')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.savefig('./TF_All_Cohorts/Total_Cohort_Initial_Fraction.png', format = 'png')
            self.ATTM_Total_Fractional_Area.tofile('./TF_All_Cohorts/Initial_Cohort_Fractional_Area.bin')
            pl.close()
        # -----------------------------------------------------------------------------
        # Return to Run Directory
        #----------------------------------
        os.chdir(self.control['Run_dir'])


def yukon_initial_cohort_check(self):
    """
    The purpose of this module is to ensure that all fractional land-surface cohorts, in each element,
    sums to one.  There are errors introducted in the the interpolation process
    (from Mark Lara files to 25x25m resolution).

    The initial step is to compare the total number of fine-resolution cohorts to the total number
    of cohorts.  In nearly all the ATTM elements, the total fractional area is not 1.0 (either above
    or below).  At this point, the land-surface cohorts are normalized to the ATTM element (in order to
    ensure 1.0.

    On the edges of the model domain (i.e. in areas in contact with the ocean), the total fractional area
    of land-surface cohorts is most likely significantly less than 1.0.  In these cases, the fractional
    area will not be normalized.

    The minimum total fractional area required for normalization is 0.50.

    """
    # Statement for debugging
    print '    Checking initial cohorts, normalizing to 1.0'
    
    # ----------------------------------------------------------------------
    # Determine the initial/original total fractional area of each element.
    # ----------------------------------------------------------------------
    cohort_check = self.ATTM_Total / ((float(self.X_resolution)/(self.x_res)) * float(self.Y_resolution)/ \
                   (self.y_res))

    #=====================================================================================
    # If the total fractional area of element is greater than 0.5, normalize each cohort
    # in order get to 1.0
    #=====================================================================================
    # Note: In the Barrow example, the cohorts_required = 1600. Just leaving as flexible as
    #       possible.
    #-------------------------------------------------------------------------------------
    cohorts_required = ((float(self.X_resolution)/(self.x_res)) * float(self.Y_resolution)/ \
                        (self.y_res))

    for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
        if cohort_check[i] > 0.5:
            #-----------------------------------------------
            # The normalization process
            # adjustment = (cohorts_required / ATTM_Total)
            # cohort_new = cohort * adjustment
            # - - - - - - - - - - - - - - - - - - - - - - - 
            # The new ATTM_Total should = cohorts_required
            #-----------------------------------------------
            adjustment = cohorts_required / self.ATTM_Total[i]

            # Adjust all the land surface cohorts
            if self.ATTM_Barren_Yukon[i] > 0. : self.ATTM_Barren_Yukon[i] = self.ATTM_Barren_Yukon[i]*adjustment
            if self.ATTM_Bog_Yukon[i] > 0. : self.ATTM_Bog_Yukon[i] = self.ATTM_Bog_Yukon[i]*adjustment
            if self.ATTM_DeciduousForest_Yukon[i] > 0. : self.ATTM_DeciduousForest_Yukon[i]= self.ATTM_DeciduousForest_Yukon[i]*adjustment
            if self.ATTM_DwarfShrub_Yukon[i] > 0. : self.ATTM_DwarfShrub_Yukon[i] = self.ATTM_DwarfShrub_Yukon[i]*adjustment
            if self.ATTM_Fen_Yukon[i] > 0. : self.ATTM_Fen_Yukon[i] = self.ATTM_Fen_Yukon[i]*adjustment
            if self.ATTM_EvergreenForest_Yukon[i] > 0. : self.ATTM_EvergreenForest_Yukon[i] = self.ATTM_EvergreenForest_Yukon[i]*adjustment
            if self.ATTM_Lake_Yukon[i] > 0. : self.ATTM_Lake_Yukon[i] = self.ATTM_Lake_Yukon[i]*adjustment
            if self.ATTM_Pond_Yukon[i] > 0. : self.ATTM_Pond_Yukon[i] = self.ATTM_Pond_Yukon[i]*adjustment
            if self.ATTM_River_Yukon[i] > 0. : self.ATTM_River_Yukon[i] = self.ATTM_River_Yukon[i]*adjustment
            if self.ATTM_ShrubScrub_Yukon[i] > 0. : self.ATTM_ShrubScrub_Yukon[i] = self.ATTM_ShrubScrub_Yukon[i]*adjustment
            if self.ATTM_Unclassified_Yukon[i] > 0. : self.ATTM_Unclassified_Yukon[i] = self.ATTM_Unclassified_Yukon[i]*adjustment
            if self.ATTM_Bog_Yukon_00[i] > 0. : self.ATTM_Bog_Yukon_00[i] = self.ATTM_Bog_Yukon_00[i] * adjustment
            if self.ATTM_Bog_Yukon_01[i] > 0. : self.ATTM_Bog_Yukon_01[i] = self.ATTM_Bog_Yukon_01[i] * adjustment
            if self.ATTM_Bog_Yukon_02[i] > 0. : self.ATTM_Bog_Yukon_02[i] = self.ATTM_Bog_Yukon_02[i] * adjustment
            if self.ATTM_Bog_Yukon_03[i] > 0. : self.ATTM_Bog_Yukon_03[i] = self.ATTM_Bog_Yukon_03[i] * adjustment
            if self.ATTM_Bog_Yukon_04[i] > 0. : self.ATTM_Bog_Yukon_04[i] = self.ATTM_Bog_Yukon_04[i] * adjustment
            if self.ATTM_Bog_Yukon_05[i] > 0. : self.ATTM_Bog_Yukon_05[i] = self.ATTM_Bog_Yukon_05[i] * adjustment
            if self.ATTM_Bog_Yukon_06[i] > 0. : self.ATTM_Bog_Yukon_06[i] = self.ATTM_Bog_Yukon_06[i] * adjustment
            if self.ATTM_Bog_Yukon_07[i] > 0. : self.ATTM_Bog_Yukon_07[i] = self.ATTM_Bog_Yukon_07[i] * adjustment
            if self.ATTM_Bog_Yukon_08[i] > 0. : self.ATTM_Bog_Yukon_08[i] = self.ATTM_Bog_Yukon_08[i] * adjustment
            if self.ATTM_Bog_Yukon_09[i] > 0. : self.ATTM_Bog_Yukon_09[i] = self.ATTM_Bog_Yukon_09[i] * adjustment
            if self.ATTM_Bog_Yukon_10[i] > 0. : self.ATTM_Bog_Yukon_10[i] = self.ATTM_Bog_Yukon_10[i] * adjustment
            if self.ATTM_Bog_Yukon_11[i] > 0. : self.ATTM_Bog_Yukon_11[i] = self.ATTM_Bog_Yukon_11[i] * adjustment
            if self.ATTM_Bog_Yukon_12[i] > 0. : self.ATTM_Bog_Yukon_12[i] = self.ATTM_Bog_Yukon_12[i] * adjustment
            if self.ATTM_Bog_Yukon_13[i] > 0. : self.ATTM_Bog_Yukon_13[i] = self.ATTM_Bog_Yukon_13[i] * adjustment
            if self.ATTM_Bog_Yukon_14[i] > 0. : self.ATTM_Bog_Yukon_14[i] = self.ATTM_Bog_Yukon_14[i] * adjustment
            if self.ATTM_Bog_Yukon_15[i] > 0. : self.ATTM_Bog_Yukon_15[i] = self.ATTM_Bog_Yukon_15[i] * adjustment
            if self.ATTM_Bog_Yukon_16[i] > 0. : self.ATTM_Bog_Yukon_16[i] = self.ATTM_Bog_Yukon_16[i] * adjustment
            if self.ATTM_Bog_Yukon_17[i] > 0. : self.ATTM_Bog_Yukon_17[i] = self.ATTM_Bog_Yukon_17[i] * adjustment
            if self.ATTM_Bog_Yukon_18[i] > 0. : self.ATTM_Bog_Yukon_18[i] = self.ATTM_Bog_Yukon_18[i] * adjustment
            if self.ATTM_Bog_Yukon_19[i] > 0. : self.ATTM_Bog_Yukon_19[i] = self.ATTM_Bog_Yukon_19[i] * adjustment
            if self.ATTM_Bog_Yukon_20[i] > 0. : self.ATTM_Bog_Yukon_20[i] = self.ATTM_Bog_Yukon_20[i] * adjustment
            if self.ATTM_Bog_Yukon_21[i] > 0. : self.ATTM_Bog_Yukon_21[i] = self.ATTM_Bog_Yukon_21[i] * adjustment
            if self.ATTM_Bog_Yukon_22[i] > 0. : self.ATTM_Bog_Yukon_22[i] = self.ATTM_Bog_Yukon_22[i] * adjustment
            if self.ATTM_Bog_Yukon_23[i] > 0. : self.ATTM_Bog_Yukon_23[i] = self.ATTM_Bog_Yukon_23[i] * adjustment
            if self.ATTM_Bog_Yukon_24[i] > 0. : self.ATTM_Bog_Yukon_24[i] = self.ATTM_Bog_Yukon_24[i] * adjustment
            if self.ATTM_Bog_Yukon_25[i] > 0. : self.ATTM_Bog_Yukon_25[i] = self.ATTM_Bog_Yukon_25[i] * adjustment
            if self.ATTM_Bog_Yukon_26[i] > 0. : self.ATTM_Bog_Yukon_26[i] = self.ATTM_Bog_Yukon_26[i] * adjustment
            if self.ATTM_Bog_Yukon_27[i] > 0. : self.ATTM_Bog_Yukon_27[i] = self.ATTM_Bog_Yukon_27[i] * adjustment
            if self.ATTM_Bog_Yukon_28[i] > 0. : self.ATTM_Bog_Yukon_28[i] = self.ATTM_Bog_Yukon_28[i] * adjustment
            if self.ATTM_Bog_Yukon_29[i] > 0. : self.ATTM_Bog_Yukon_29[i] = self.ATTM_Bog_Yukon_29[i] * adjustment
            if self.ATTM_Bog_Yukon_30[i] > 0. : self.ATTM_Bog_Yukon_30[i] = self.ATTM_Bog_Yukon_30[i] * adjustment
            if self.ATTM_Bog_Yukon_31[i] > 0. : self.ATTM_Bog_Yukon_31[i] = self.ATTM_Bog_Yukon_31[i] * adjustment
            if self.ATTM_Bog_Yukon_32[i] > 0. : self.ATTM_Bog_Yukon_32[i] = self.ATTM_Bog_Yukon_32[i] * adjustment
            if self.ATTM_Bog_Yukon_33[i] > 0. : self.ATTM_Bog_Yukon_33[i] = self.ATTM_Bog_Yukon_33[i] * adjustment
            if self.ATTM_Bog_Yukon_34[i] > 0. : self.ATTM_Bog_Yukon_34[i] = self.ATTM_Bog_Yukon_34[i] * adjustment
            if self.ATTM_Bog_Yukon_35[i] > 0. : self.ATTM_Bog_Yukon_35[i] = self.ATTM_Bog_Yukon_35[i] * adjustment
            if self.ATTM_Bog_Yukon_36[i] > 0. : self.ATTM_Bog_Yukon_36[i] = self.ATTM_Bog_Yukon_36[i] * adjustment
            if self.ATTM_Bog_Yukon_37[i] > 0. : self.ATTM_Bog_Yukon_37[i] = self.ATTM_Bog_Yukon_37[i] * adjustment
            if self.ATTM_Bog_Yukon_38[i] > 0. : self.ATTM_Bog_Yukon_38[i] = self.ATTM_Bog_Yukon_38[i] * adjustment
            if self.ATTM_Bog_Yukon_39[i] > 0. : self.ATTM_Bog_Yukon_39[i] = self.ATTM_Bog_Yukon_39[i] * adjustment
            if self.ATTM_Bog_Yukon_40[i] > 0. : self.ATTM_Bog_Yukon_40[i] = self.ATTM_Bog_Yukon_40[i] * adjustment
            if self.ATTM_Bog_Yukon_41[i] > 0. : self.ATTM_Bog_Yukon_41[i] = self.ATTM_Bog_Yukon_41[i] * adjustment
            if self.ATTM_Bog_Yukon_42[i] > 0. : self.ATTM_Bog_Yukon_42[i] = self.ATTM_Bog_Yukon_42[i] * adjustment
            if self.ATTM_Bog_Yukon_43[i] > 0. : self.ATTM_Bog_Yukon_43[i] = self.ATTM_Bog_Yukon_43[i] * adjustment
            if self.ATTM_Bog_Yukon_44[i] > 0. : self.ATTM_Bog_Yukon_44[i] = self.ATTM_Bog_Yukon_44[i] * adjustment
            if self.ATTM_Bog_Yukon_45[i] > 0. : self.ATTM_Bog_Yukon_45[i] = self.ATTM_Bog_Yukon_45[i] * adjustment
            if self.ATTM_Bog_Yukon_46[i] > 0. : self.ATTM_Bog_Yukon_46[i] = self.ATTM_Bog_Yukon_46[i] * adjustment
            if self.ATTM_Bog_Yukon_47[i] > 0. : self.ATTM_Bog_Yukon_47[i] = self.ATTM_Bog_Yukon_47[i] * adjustment
            if self.ATTM_Bog_Yukon_48[i] > 0. : self.ATTM_Bog_Yukon_48[i] = self.ATTM_Bog_Yukon_48[i] * adjustment
            if self.ATTM_Bog_Yukon_49[i] > 0. : self.ATTM_Bog_Yukon_49[i] = self.ATTM_Bog_Yukon_49[i] * adjustment
            if self.ATTM_Bog_Yukon_50[i] > 0. : self.ATTM_Bog_Yukon_50[i] = self.ATTM_Bog_Yukon_50[i] * adjustment
            if self.ATTM_Bog_Yukon_51[i] > 0. : self.ATTM_Bog_Yukon_51[i] = self.ATTM_Bog_Yukon_51[i] * adjustment
            if self.ATTM_Bog_Yukon_52[i] > 0. : self.ATTM_Bog_Yukon_52[i] = self.ATTM_Bog_Yukon_52[i] * adjustment
            if self.ATTM_Bog_Yukon_53[i] > 0. : self.ATTM_Bog_Yukon_53[i] = self.ATTM_Bog_Yukon_53[i] * adjustment
            if self.ATTM_Bog_Yukon_54[i] > 0. : self.ATTM_Bog_Yukon_54[i] = self.ATTM_Bog_Yukon_54[i] * adjustment
            if self.ATTM_Bog_Yukon_55[i] > 0. : self.ATTM_Bog_Yukon_55[i] = self.ATTM_Bog_Yukon_55[i] * adjustment
            if self.ATTM_Bog_Yukon_56[i] > 0. : self.ATTM_Bog_Yukon_56[i] = self.ATTM_Bog_Yukon_56[i] * adjustment
            if self.ATTM_Bog_Yukon_57[i] > 0. : self.ATTM_Bog_Yukon_57[i] = self.ATTM_Bog_Yukon_57[i] * adjustment
            if self.ATTM_Bog_Yukon_58[i] > 0. : self.ATTM_Bog_Yukon_58[i] = self.ATTM_Bog_Yukon_58[i] * adjustment
            if self.ATTM_Bog_Yukon_59[i] > 0. : self.ATTM_Bog_Yukon_59[i] = self.ATTM_Bog_Yukon_59[i] * adjustment
            if self.ATTM_Bog_Yukon_60[i] > 0. : self.ATTM_Bog_Yukon_60[i] = self.ATTM_Bog_Yukon_60[i] * adjustment
            if self.ATTM_Bog_Yukon_61[i] > 0. : self.ATTM_Bog_Yukon_61[i] = self.ATTM_Bog_Yukon_61[i] * adjustment
            if self.ATTM_Bog_Yukon_62[i] > 0. : self.ATTM_Bog_Yukon_62[i] = self.ATTM_Bog_Yukon_62[i] * adjustment
            if self.ATTM_Bog_Yukon_63[i] > 0. : self.ATTM_Bog_Yukon_63[i] = self.ATTM_Bog_Yukon_63[i] * adjustment
            if self.ATTM_Bog_Yukon_64[i] > 0. : self.ATTM_Bog_Yukon_64[i] = self.ATTM_Bog_Yukon_64[i] * adjustment
            if self.ATTM_Bog_Yukon_65[i] > 0. : self.ATTM_Bog_Yukon_65[i] = self.ATTM_Bog_Yukon_65[i] * adjustment
            if self.ATTM_Bog_Yukon_66[i] > 0. : self.ATTM_Bog_Yukon_66[i] = self.ATTM_Bog_Yukon_66[i] * adjustment
            if self.ATTM_Bog_Yukon_67[i] > 0. : self.ATTM_Bog_Yukon_67[i] = self.ATTM_Bog_Yukon_67[i] * adjustment
            if self.ATTM_Bog_Yukon_68[i] > 0. : self.ATTM_Bog_Yukon_68[i] = self.ATTM_Bog_Yukon_68[i] * adjustment
            if self.ATTM_Bog_Yukon_69[i] > 0. : self.ATTM_Bog_Yukon_69[i] = self.ATTM_Bog_Yukon_69[i] * adjustment
            if self.ATTM_Bog_Yukon_70[i] > 0. : self.ATTM_Bog_Yukon_70[i] = self.ATTM_Bog_Yukon_70[i] * adjustment
            if self.ATTM_Bog_Yukon_71[i] > 0. : self.ATTM_Bog_Yukon_71[i] = self.ATTM_Bog_Yukon_71[i] * adjustment
            if self.ATTM_Bog_Yukon_72[i] > 0. : self.ATTM_Bog_Yukon_72[i] = self.ATTM_Bog_Yukon_72[i] * adjustment
            if self.ATTM_Bog_Yukon_73[i] > 0. : self.ATTM_Bog_Yukon_73[i] = self.ATTM_Bog_Yukon_73[i] * adjustment
            if self.ATTM_Bog_Yukon_74[i] > 0. : self.ATTM_Bog_Yukon_74[i] = self.ATTM_Bog_Yukon_74[i] * adjustment
            if self.ATTM_Bog_Yukon_75[i] > 0. : self.ATTM_Bog_Yukon_75[i] = self.ATTM_Bog_Yukon_75[i] * adjustment
            if self.ATTM_Bog_Yukon_76[i] > 0. : self.ATTM_Bog_Yukon_76[i] = self.ATTM_Bog_Yukon_76[i] * adjustment
            if self.ATTM_Bog_Yukon_77[i] > 0. : self.ATTM_Bog_Yukon_77[i] = self.ATTM_Bog_Yukon_77[i] * adjustment
            if self.ATTM_Bog_Yukon_78[i] > 0. : self.ATTM_Bog_Yukon_78[i] = self.ATTM_Bog_Yukon_78[i] * adjustment
            if self.ATTM_Bog_Yukon_79[i] > 0. : self.ATTM_Bog_Yukon_79[i] = self.ATTM_Bog_Yukon_79[i] * adjustment
            if self.ATTM_Bog_Yukon_80[i] > 0. : self.ATTM_Bog_Yukon_80[i] = self.ATTM_Bog_Yukon_80[i] * adjustment
            if self.ATTM_Bog_Yukon_81[i] > 0. : self.ATTM_Bog_Yukon_81[i] = self.ATTM_Bog_Yukon_81[i] * adjustment
            if self.ATTM_Bog_Yukon_82[i] > 0. : self.ATTM_Bog_Yukon_82[i] = self.ATTM_Bog_Yukon_82[i] * adjustment
            if self.ATTM_Bog_Yukon_83[i] > 0. : self.ATTM_Bog_Yukon_83[i] = self.ATTM_Bog_Yukon_83[i] * adjustment
            if self.ATTM_Bog_Yukon_84[i] > 0. : self.ATTM_Bog_Yukon_84[i] = self.ATTM_Bog_Yukon_84[i] * adjustment
            if self.ATTM_Bog_Yukon_85[i] > 0. : self.ATTM_Bog_Yukon_85[i] = self.ATTM_Bog_Yukon_85[i] * adjustment
            if self.ATTM_Bog_Yukon_86[i] > 0. : self.ATTM_Bog_Yukon_86[i] = self.ATTM_Bog_Yukon_86[i] * adjustment
            if self.ATTM_Bog_Yukon_87[i] > 0. : self.ATTM_Bog_Yukon_87[i] = self.ATTM_Bog_Yukon_87[i] * adjustment
            if self.ATTM_Bog_Yukon_88[i] > 0. : self.ATTM_Bog_Yukon_88[i] = self.ATTM_Bog_Yukon_88[i] * adjustment
            if self.ATTM_Bog_Yukon_89[i] > 0. : self.ATTM_Bog_Yukon_89[i] = self.ATTM_Bog_Yukon_89[i] * adjustment
            if self.ATTM_Bog_Yukon_90[i] > 0. : self.ATTM_Bog_Yukon_90[i] = self.ATTM_Bog_Yukon_90[i] * adjustment
            if self.ATTM_Bog_Yukon_91[i] > 0. : self.ATTM_Bog_Yukon_91[i] = self.ATTM_Bog_Yukon_91[i] * adjustment
            if self.ATTM_Bog_Yukon_92[i] > 0. : self.ATTM_Bog_Yukon_92[i] = self.ATTM_Bog_Yukon_92[i] * adjustment
            if self.ATTM_Bog_Yukon_93[i] > 0. : self.ATTM_Bog_Yukon_93[i] = self.ATTM_Bog_Yukon_93[i] * adjustment
            if self.ATTM_Bog_Yukon_94[i] > 0. : self.ATTM_Bog_Yukon_94[i] = self.ATTM_Bog_Yukon_94[i] * adjustment
            if self.ATTM_Bog_Yukon_95[i] > 0. : self.ATTM_Bog_Yukon_95[i] = self.ATTM_Bog_Yukon_95[i] * adjustment
            if self.ATTM_Bog_Yukon_96[i] > 0. : self.ATTM_Bog_Yukon_96[i] = self.ATTM_Bog_Yukon_96[i] * adjustment
            if self.ATTM_Bog_Yukon_97[i] > 0. : self.ATTM_Bog_Yukon_97[i] = self.ATTM_Bog_Yukon_97[i] * adjustment
            if self.ATTM_Bog_Yukon_98[i] > 0. : self.ATTM_Bog_Yukon_98[i] = self.ATTM_Bog_Yukon_98[i] * adjustment
            if self.ATTM_Bog_Yukon_99[i] > 0. : self.ATTM_Bog_Yukon_99[i] = self.ATTM_Bog_Yukon_99[i] * adjustment
            if self.ATTM_Fen_Yukon_00[i] > 0. : self.ATTM_Fen_Yukon_00[i] = self.ATTM_Fen_Yukon_00[i] * adjustment
            if self.ATTM_Fen_Yukon_01[i] > 0. : self.ATTM_Fen_Yukon_01[i] = self.ATTM_Fen_Yukon_01[i] * adjustment
            if self.ATTM_Fen_Yukon_02[i] > 0. : self.ATTM_Fen_Yukon_02[i] = self.ATTM_Fen_Yukon_02[i] * adjustment
            if self.ATTM_Fen_Yukon_03[i] > 0. : self.ATTM_Fen_Yukon_03[i] = self.ATTM_Fen_Yukon_03[i] * adjustment
            if self.ATTM_Fen_Yukon_04[i] > 0. : self.ATTM_Fen_Yukon_04[i] = self.ATTM_Fen_Yukon_04[i] * adjustment
            if self.ATTM_Fen_Yukon_05[i] > 0. : self.ATTM_Fen_Yukon_05[i] = self.ATTM_Fen_Yukon_05[i] * adjustment
            if self.ATTM_Fen_Yukon_06[i] > 0. : self.ATTM_Fen_Yukon_06[i] = self.ATTM_Fen_Yukon_06[i] * adjustment
            if self.ATTM_Fen_Yukon_07[i] > 0. : self.ATTM_Fen_Yukon_07[i] = self.ATTM_Fen_Yukon_07[i] * adjustment
            if self.ATTM_Fen_Yukon_08[i] > 0. : self.ATTM_Fen_Yukon_08[i] = self.ATTM_Fen_Yukon_08[i] * adjustment
            if self.ATTM_Fen_Yukon_09[i] > 0. : self.ATTM_Fen_Yukon_09[i] = self.ATTM_Fen_Yukon_09[i] * adjustment
            if self.ATTM_Fen_Yukon_10[i] > 0. : self.ATTM_Fen_Yukon_10[i] = self.ATTM_Fen_Yukon_10[i] * adjustment
            if self.ATTM_Fen_Yukon_11[i] > 0. : self.ATTM_Fen_Yukon_11[i] = self.ATTM_Fen_Yukon_11[i] * adjustment
            if self.ATTM_Fen_Yukon_12[i] > 0. : self.ATTM_Fen_Yukon_12[i] = self.ATTM_Fen_Yukon_12[i] * adjustment
            if self.ATTM_Fen_Yukon_13[i] > 0. : self.ATTM_Fen_Yukon_13[i] = self.ATTM_Fen_Yukon_13[i] * adjustment
            if self.ATTM_Fen_Yukon_14[i] > 0. : self.ATTM_Fen_Yukon_14[i] = self.ATTM_Fen_Yukon_14[i] * adjustment
            if self.ATTM_Fen_Yukon_15[i] > 0. : self.ATTM_Fen_Yukon_15[i] = self.ATTM_Fen_Yukon_15[i] * adjustment
            if self.ATTM_Fen_Yukon_16[i] > 0. : self.ATTM_Fen_Yukon_16[i] = self.ATTM_Fen_Yukon_16[i] * adjustment
            if self.ATTM_Fen_Yukon_17[i] > 0. : self.ATTM_Fen_Yukon_17[i] = self.ATTM_Fen_Yukon_17[i] * adjustment
            if self.ATTM_Fen_Yukon_18[i] > 0. : self.ATTM_Fen_Yukon_18[i] = self.ATTM_Fen_Yukon_18[i] * adjustment
            if self.ATTM_Fen_Yukon_19[i] > 0. : self.ATTM_Fen_Yukon_19[i] = self.ATTM_Fen_Yukon_19[i] * adjustment
            if self.ATTM_Fen_Yukon_20[i] > 0. : self.ATTM_Fen_Yukon_20[i] = self.ATTM_Fen_Yukon_20[i] * adjustment
            if self.ATTM_Fen_Yukon_21[i] > 0. : self.ATTM_Fen_Yukon_21[i] = self.ATTM_Fen_Yukon_21[i] * adjustment
            if self.ATTM_Fen_Yukon_22[i] > 0. : self.ATTM_Fen_Yukon_22[i] = self.ATTM_Fen_Yukon_22[i] * adjustment
            if self.ATTM_Fen_Yukon_23[i] > 0. : self.ATTM_Fen_Yukon_23[i] = self.ATTM_Fen_Yukon_23[i] * adjustment
            if self.ATTM_Fen_Yukon_24[i] > 0. : self.ATTM_Fen_Yukon_24[i] = self.ATTM_Fen_Yukon_24[i] * adjustment
            if self.ATTM_Fen_Yukon_25[i] > 0. : self.ATTM_Fen_Yukon_25[i] = self.ATTM_Fen_Yukon_25[i] * adjustment
            if self.ATTM_Fen_Yukon_26[i] > 0. : self.ATTM_Fen_Yukon_26[i] = self.ATTM_Fen_Yukon_26[i] * adjustment
            if self.ATTM_Fen_Yukon_27[i] > 0. : self.ATTM_Fen_Yukon_27[i] = self.ATTM_Fen_Yukon_27[i] * adjustment
            if self.ATTM_Fen_Yukon_28[i] > 0. : self.ATTM_Fen_Yukon_28[i] = self.ATTM_Fen_Yukon_28[i] * adjustment
            if self.ATTM_Fen_Yukon_29[i] > 0. : self.ATTM_Fen_Yukon_29[i] = self.ATTM_Fen_Yukon_29[i] * adjustment
            if self.ATTM_Fen_Yukon_30[i] > 0. : self.ATTM_Fen_Yukon_30[i] = self.ATTM_Fen_Yukon_30[i] * adjustment
            if self.ATTM_Fen_Yukon_31[i] > 0. : self.ATTM_Fen_Yukon_31[i] = self.ATTM_Fen_Yukon_31[i] * adjustment
            if self.ATTM_Fen_Yukon_32[i] > 0. : self.ATTM_Fen_Yukon_32[i] = self.ATTM_Fen_Yukon_32[i] * adjustment
            if self.ATTM_Fen_Yukon_33[i] > 0. : self.ATTM_Fen_Yukon_33[i] = self.ATTM_Fen_Yukon_33[i] * adjustment
            if self.ATTM_Fen_Yukon_34[i] > 0. : self.ATTM_Fen_Yukon_34[i] = self.ATTM_Fen_Yukon_34[i] * adjustment
            if self.ATTM_Fen_Yukon_35[i] > 0. : self.ATTM_Fen_Yukon_35[i] = self.ATTM_Fen_Yukon_35[i] * adjustment
            if self.ATTM_Fen_Yukon_36[i] > 0. : self.ATTM_Fen_Yukon_36[i] = self.ATTM_Fen_Yukon_36[i] * adjustment
            if self.ATTM_Fen_Yukon_37[i] > 0. : self.ATTM_Fen_Yukon_37[i] = self.ATTM_Fen_Yukon_37[i] * adjustment
            if self.ATTM_Fen_Yukon_38[i] > 0. : self.ATTM_Fen_Yukon_38[i] = self.ATTM_Fen_Yukon_38[i] * adjustment
            if self.ATTM_Fen_Yukon_39[i] > 0. : self.ATTM_Fen_Yukon_39[i] = self.ATTM_Fen_Yukon_39[i] * adjustment
            if self.ATTM_Fen_Yukon_40[i] > 0. : self.ATTM_Fen_Yukon_40[i] = self.ATTM_Fen_Yukon_40[i] * adjustment
            if self.ATTM_Fen_Yukon_41[i] > 0. : self.ATTM_Fen_Yukon_41[i] = self.ATTM_Fen_Yukon_41[i] * adjustment
            if self.ATTM_Fen_Yukon_42[i] > 0. : self.ATTM_Fen_Yukon_42[i] = self.ATTM_Fen_Yukon_42[i] * adjustment
            if self.ATTM_Fen_Yukon_43[i] > 0. : self.ATTM_Fen_Yukon_43[i] = self.ATTM_Fen_Yukon_43[i] * adjustment
            if self.ATTM_Fen_Yukon_44[i] > 0. : self.ATTM_Fen_Yukon_44[i] = self.ATTM_Fen_Yukon_44[i] * adjustment
            if self.ATTM_Fen_Yukon_45[i] > 0. : self.ATTM_Fen_Yukon_45[i] = self.ATTM_Fen_Yukon_45[i] * adjustment
            if self.ATTM_Fen_Yukon_46[i] > 0. : self.ATTM_Fen_Yukon_46[i] = self.ATTM_Fen_Yukon_46[i] * adjustment
            if self.ATTM_Fen_Yukon_47[i] > 0. : self.ATTM_Fen_Yukon_47[i] = self.ATTM_Fen_Yukon_47[i] * adjustment
            if self.ATTM_Fen_Yukon_48[i] > 0. : self.ATTM_Fen_Yukon_48[i] = self.ATTM_Fen_Yukon_48[i] * adjustment
            if self.ATTM_Fen_Yukon_49[i] > 0. : self.ATTM_Fen_Yukon_49[i] = self.ATTM_Fen_Yukon_49[i] * adjustment
            if self.ATTM_Fen_Yukon_50[i] > 0. : self.ATTM_Fen_Yukon_50[i] = self.ATTM_Fen_Yukon_50[i] * adjustment
            if self.ATTM_Fen_Yukon_51[i] > 0. : self.ATTM_Fen_Yukon_51[i] = self.ATTM_Fen_Yukon_51[i] * adjustment
            if self.ATTM_Fen_Yukon_52[i] > 0. : self.ATTM_Fen_Yukon_52[i] = self.ATTM_Fen_Yukon_52[i] * adjustment
            if self.ATTM_Fen_Yukon_53[i] > 0. : self.ATTM_Fen_Yukon_53[i] = self.ATTM_Fen_Yukon_53[i] * adjustment
            if self.ATTM_Fen_Yukon_54[i] > 0. : self.ATTM_Fen_Yukon_54[i] = self.ATTM_Fen_Yukon_54[i] * adjustment
            if self.ATTM_Fen_Yukon_55[i] > 0. : self.ATTM_Fen_Yukon_55[i] = self.ATTM_Fen_Yukon_55[i] * adjustment
            if self.ATTM_Fen_Yukon_56[i] > 0. : self.ATTM_Fen_Yukon_56[i] = self.ATTM_Fen_Yukon_56[i] * adjustment
            if self.ATTM_Fen_Yukon_57[i] > 0. : self.ATTM_Fen_Yukon_57[i] = self.ATTM_Fen_Yukon_57[i] * adjustment
            if self.ATTM_Fen_Yukon_58[i] > 0. : self.ATTM_Fen_Yukon_58[i] = self.ATTM_Fen_Yukon_58[i] * adjustment
            if self.ATTM_Fen_Yukon_59[i] > 0. : self.ATTM_Fen_Yukon_59[i] = self.ATTM_Fen_Yukon_59[i] * adjustment
            if self.ATTM_Fen_Yukon_60[i] > 0. : self.ATTM_Fen_Yukon_60[i] = self.ATTM_Fen_Yukon_60[i] * adjustment
            if self.ATTM_Fen_Yukon_61[i] > 0. : self.ATTM_Fen_Yukon_61[i] = self.ATTM_Fen_Yukon_61[i] * adjustment
            if self.ATTM_Fen_Yukon_62[i] > 0. : self.ATTM_Fen_Yukon_62[i] = self.ATTM_Fen_Yukon_62[i] * adjustment
            if self.ATTM_Fen_Yukon_63[i] > 0. : self.ATTM_Fen_Yukon_63[i] = self.ATTM_Fen_Yukon_63[i] * adjustment
            if self.ATTM_Fen_Yukon_64[i] > 0. : self.ATTM_Fen_Yukon_64[i] = self.ATTM_Fen_Yukon_64[i] * adjustment
            if self.ATTM_Fen_Yukon_65[i] > 0. : self.ATTM_Fen_Yukon_65[i] = self.ATTM_Fen_Yukon_65[i] * adjustment
            if self.ATTM_Fen_Yukon_66[i] > 0. : self.ATTM_Fen_Yukon_66[i] = self.ATTM_Fen_Yukon_66[i] * adjustment
            if self.ATTM_Fen_Yukon_67[i] > 0. : self.ATTM_Fen_Yukon_67[i] = self.ATTM_Fen_Yukon_67[i] * adjustment
            if self.ATTM_Fen_Yukon_68[i] > 0. : self.ATTM_Fen_Yukon_68[i] = self.ATTM_Fen_Yukon_68[i] * adjustment
            if self.ATTM_Fen_Yukon_69[i] > 0. : self.ATTM_Fen_Yukon_69[i] = self.ATTM_Fen_Yukon_69[i] * adjustment
            if self.ATTM_Fen_Yukon_70[i] > 0. : self.ATTM_Fen_Yukon_70[i] = self.ATTM_Fen_Yukon_70[i] * adjustment
            if self.ATTM_Fen_Yukon_71[i] > 0. : self.ATTM_Fen_Yukon_71[i] = self.ATTM_Fen_Yukon_71[i] * adjustment
            if self.ATTM_Fen_Yukon_72[i] > 0. : self.ATTM_Fen_Yukon_72[i] = self.ATTM_Fen_Yukon_72[i] * adjustment
            if self.ATTM_Fen_Yukon_73[i] > 0. : self.ATTM_Fen_Yukon_73[i] = self.ATTM_Fen_Yukon_73[i] * adjustment
            if self.ATTM_Fen_Yukon_74[i] > 0. : self.ATTM_Fen_Yukon_74[i] = self.ATTM_Fen_Yukon_74[i] * adjustment
            if self.ATTM_Fen_Yukon_75[i] > 0. : self.ATTM_Fen_Yukon_75[i] = self.ATTM_Fen_Yukon_75[i] * adjustment
            if self.ATTM_Fen_Yukon_76[i] > 0. : self.ATTM_Fen_Yukon_76[i] = self.ATTM_Fen_Yukon_76[i] * adjustment
            if self.ATTM_Fen_Yukon_77[i] > 0. : self.ATTM_Fen_Yukon_77[i] = self.ATTM_Fen_Yukon_77[i] * adjustment
            if self.ATTM_Fen_Yukon_78[i] > 0. : self.ATTM_Fen_Yukon_78[i] = self.ATTM_Fen_Yukon_78[i] * adjustment
            if self.ATTM_Fen_Yukon_79[i] > 0. : self.ATTM_Fen_Yukon_79[i] = self.ATTM_Fen_Yukon_79[i] * adjustment
            if self.ATTM_Fen_Yukon_80[i] > 0. : self.ATTM_Fen_Yukon_80[i] = self.ATTM_Fen_Yukon_80[i] * adjustment
            if self.ATTM_Fen_Yukon_81[i] > 0. : self.ATTM_Fen_Yukon_81[i] = self.ATTM_Fen_Yukon_81[i] * adjustment
            if self.ATTM_Fen_Yukon_82[i] > 0. : self.ATTM_Fen_Yukon_82[i] = self.ATTM_Fen_Yukon_82[i] * adjustment
            if self.ATTM_Fen_Yukon_83[i] > 0. : self.ATTM_Fen_Yukon_83[i] = self.ATTM_Fen_Yukon_83[i] * adjustment
            if self.ATTM_Fen_Yukon_84[i] > 0. : self.ATTM_Fen_Yukon_84[i] = self.ATTM_Fen_Yukon_84[i] * adjustment
            if self.ATTM_Fen_Yukon_85[i] > 0. : self.ATTM_Fen_Yukon_85[i] = self.ATTM_Fen_Yukon_85[i] * adjustment
            if self.ATTM_Fen_Yukon_86[i] > 0. : self.ATTM_Fen_Yukon_86[i] = self.ATTM_Fen_Yukon_86[i] * adjustment
            if self.ATTM_Fen_Yukon_87[i] > 0. : self.ATTM_Fen_Yukon_87[i] = self.ATTM_Fen_Yukon_87[i] * adjustment
            if self.ATTM_Fen_Yukon_88[i] > 0. : self.ATTM_Fen_Yukon_88[i] = self.ATTM_Fen_Yukon_88[i] * adjustment
            if self.ATTM_Fen_Yukon_89[i] > 0. : self.ATTM_Fen_Yukon_89[i] = self.ATTM_Fen_Yukon_89[i] * adjustment
            if self.ATTM_Fen_Yukon_90[i] > 0. : self.ATTM_Fen_Yukon_90[i] = self.ATTM_Fen_Yukon_90[i] * adjustment
            if self.ATTM_Fen_Yukon_91[i] > 0. : self.ATTM_Fen_Yukon_91[i] = self.ATTM_Fen_Yukon_91[i] * adjustment
            if self.ATTM_Fen_Yukon_92[i] > 0. : self.ATTM_Fen_Yukon_92[i] = self.ATTM_Fen_Yukon_92[i] * adjustment
            if self.ATTM_Fen_Yukon_93[i] > 0. : self.ATTM_Fen_Yukon_93[i] = self.ATTM_Fen_Yukon_93[i] * adjustment
            if self.ATTM_Fen_Yukon_94[i] > 0. : self.ATTM_Fen_Yukon_94[i] = self.ATTM_Fen_Yukon_94[i] * adjustment
            if self.ATTM_Fen_Yukon_95[i] > 0. : self.ATTM_Fen_Yukon_95[i] = self.ATTM_Fen_Yukon_95[i] * adjustment
            if self.ATTM_Fen_Yukon_96[i] > 0. : self.ATTM_Fen_Yukon_96[i] = self.ATTM_Fen_Yukon_96[i] * adjustment
            if self.ATTM_Fen_Yukon_97[i] > 0. : self.ATTM_Fen_Yukon_97[i] = self.ATTM_Fen_Yukon_97[i] * adjustment
            if self.ATTM_Fen_Yukon_98[i] > 0. : self.ATTM_Fen_Yukon_98[i] = self.ATTM_Fen_Yukon_98[i] * adjustment
            if self.ATTM_Fen_Yukon_99[i] > 0. : self.ATTM_Fen_Yukon_99[i] = self.ATTM_Fen_Yukon_99[i] * adjustment
            

    # Convert all land surface cohorts into fractional area of element
    self.ATTM_Barren_Yukon = np.round((self.ATTM_Barren_Yukon) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon    = np.round((self.ATTM_Bog_Yukon) / cohorts_required, decimals = 6)
    self.ATTM_DeciduousForest_Yukon = np.round((self.ATTM_DeciduousForest_Yukon)/cohorts_required, decimals = 6)
    self.ATTM_DwarfShrub_Yukon = np.round((self.ATTM_DwarfShrub_Yukon)/cohorts_required, decimals = 6)
    self.ATTM_EvergreenForest_Yukon = np.round((self.ATTM_EvergreenForest_Yukon)/cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon = np.round((self.ATTM_Fen_Yukon) / cohorts_required, decimals = 6)
    self.ATTM_Lake_Yukon = np.round((self.ATTM_Lake_Yukon) / cohorts_required, decimals = 6)
    self.ATTM_Pond_Yukon = np.round((self.ATTM_Pond_Yukon) / cohorts_required, decimals = 6)
    self.ATTM_River_Yukon = np.round((self.ATTM_River_Yukon) / cohorts_required, decimals = 6)
    self.ATTM_ShrubScrub_Yukon = np.round((self.ATTM_ShrubScrub_Yukon) / cohorts_required, decimals = 6)
    self.ATTM_Unclassified_Yukon = np.round((self.ATTM_Unclassified_Yukon) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_00 = np.round((self.ATTM_Bog_Yukon_00) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_01 = np.round((self.ATTM_Bog_Yukon_01) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_02 = np.round((self.ATTM_Bog_Yukon_02) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_03 = np.round((self.ATTM_Bog_Yukon_03) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_04 = np.round((self.ATTM_Bog_Yukon_04) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_05 = np.round((self.ATTM_Bog_Yukon_05) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_06 = np.round((self.ATTM_Bog_Yukon_06) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_07 = np.round((self.ATTM_Bog_Yukon_07) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_08 = np.round((self.ATTM_Bog_Yukon_08) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_09 = np.round((self.ATTM_Bog_Yukon_09) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_10 = np.round((self.ATTM_Bog_Yukon_10) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_11 = np.round((self.ATTM_Bog_Yukon_11) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_12 = np.round((self.ATTM_Bog_Yukon_12) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_13 = np.round((self.ATTM_Bog_Yukon_13) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_14 = np.round((self.ATTM_Bog_Yukon_14) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_15 = np.round((self.ATTM_Bog_Yukon_15) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_16 = np.round((self.ATTM_Bog_Yukon_16) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_17 = np.round((self.ATTM_Bog_Yukon_17) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_18 = np.round((self.ATTM_Bog_Yukon_18) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_19 = np.round((self.ATTM_Bog_Yukon_19) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_20 = np.round((self.ATTM_Bog_Yukon_20) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_21 = np.round((self.ATTM_Bog_Yukon_21) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_22 = np.round((self.ATTM_Bog_Yukon_22) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_23 = np.round((self.ATTM_Bog_Yukon_23) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_24 = np.round((self.ATTM_Bog_Yukon_24) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_25 = np.round((self.ATTM_Bog_Yukon_25) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_26 = np.round((self.ATTM_Bog_Yukon_26) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_27 = np.round((self.ATTM_Bog_Yukon_27) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_28 = np.round((self.ATTM_Bog_Yukon_28) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_29 = np.round((self.ATTM_Bog_Yukon_29) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_30 = np.round((self.ATTM_Bog_Yukon_30) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_31 = np.round((self.ATTM_Bog_Yukon_31) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_32 = np.round((self.ATTM_Bog_Yukon_32) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_33 = np.round((self.ATTM_Bog_Yukon_33) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_34 = np.round((self.ATTM_Bog_Yukon_34) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_35 = np.round((self.ATTM_Bog_Yukon_35) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_36 = np.round((self.ATTM_Bog_Yukon_36) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_37 = np.round((self.ATTM_Bog_Yukon_37) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_38 = np.round((self.ATTM_Bog_Yukon_38) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_39 = np.round((self.ATTM_Bog_Yukon_39) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_40 = np.round((self.ATTM_Bog_Yukon_40) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_41 = np.round((self.ATTM_Bog_Yukon_41) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_42 = np.round((self.ATTM_Bog_Yukon_42) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_43 = np.round((self.ATTM_Bog_Yukon_43) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_44 = np.round((self.ATTM_Bog_Yukon_44) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_45 = np.round((self.ATTM_Bog_Yukon_45) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_46 = np.round((self.ATTM_Bog_Yukon_46) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_47 = np.round((self.ATTM_Bog_Yukon_47) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_48 = np.round((self.ATTM_Bog_Yukon_48) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_49 = np.round((self.ATTM_Bog_Yukon_49) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_50 = np.round((self.ATTM_Bog_Yukon_50) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_51 = np.round((self.ATTM_Bog_Yukon_51) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_52 = np.round((self.ATTM_Bog_Yukon_52) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_53 = np.round((self.ATTM_Bog_Yukon_53) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_54 = np.round((self.ATTM_Bog_Yukon_54) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_55 = np.round((self.ATTM_Bog_Yukon_55) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_56 = np.round((self.ATTM_Bog_Yukon_56) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_57 = np.round((self.ATTM_Bog_Yukon_57) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_58 = np.round((self.ATTM_Bog_Yukon_58) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_59 = np.round((self.ATTM_Bog_Yukon_59) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_60 = np.round((self.ATTM_Bog_Yukon_60) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_61 = np.round((self.ATTM_Bog_Yukon_61) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_62 = np.round((self.ATTM_Bog_Yukon_62) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_63 = np.round((self.ATTM_Bog_Yukon_63) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_64 = np.round((self.ATTM_Bog_Yukon_64) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_65 = np.round((self.ATTM_Bog_Yukon_65) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_66 = np.round((self.ATTM_Bog_Yukon_66) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_67 = np.round((self.ATTM_Bog_Yukon_67) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_68 = np.round((self.ATTM_Bog_Yukon_68) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_69 = np.round((self.ATTM_Bog_Yukon_69) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_70 = np.round((self.ATTM_Bog_Yukon_70) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_71 = np.round((self.ATTM_Bog_Yukon_71) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_72 = np.round((self.ATTM_Bog_Yukon_72) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_73 = np.round((self.ATTM_Bog_Yukon_73) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_74 = np.round((self.ATTM_Bog_Yukon_74) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_75 = np.round((self.ATTM_Bog_Yukon_75) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_76 = np.round((self.ATTM_Bog_Yukon_76) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_77 = np.round((self.ATTM_Bog_Yukon_77) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_78 = np.round((self.ATTM_Bog_Yukon_78) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_79 = np.round((self.ATTM_Bog_Yukon_79) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_80 = np.round((self.ATTM_Bog_Yukon_80) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_81 = np.round((self.ATTM_Bog_Yukon_81) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_82 = np.round((self.ATTM_Bog_Yukon_82) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_83 = np.round((self.ATTM_Bog_Yukon_83) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_84 = np.round((self.ATTM_Bog_Yukon_84) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_85 = np.round((self.ATTM_Bog_Yukon_85) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_86 = np.round((self.ATTM_Bog_Yukon_86) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_87 = np.round((self.ATTM_Bog_Yukon_87) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_88 = np.round((self.ATTM_Bog_Yukon_88) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_89 = np.round((self.ATTM_Bog_Yukon_89) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_90 = np.round((self.ATTM_Bog_Yukon_90) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_91 = np.round((self.ATTM_Bog_Yukon_91) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_92 = np.round((self.ATTM_Bog_Yukon_92) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_93 = np.round((self.ATTM_Bog_Yukon_93) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_94 = np.round((self.ATTM_Bog_Yukon_94) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_95 = np.round((self.ATTM_Bog_Yukon_95) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_96 = np.round((self.ATTM_Bog_Yukon_96) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_97 = np.round((self.ATTM_Bog_Yukon_97) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_98 = np.round((self.ATTM_Bog_Yukon_98) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_99 = np.round((self.ATTM_Bog_Yukon_99) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_00 = np.round((self.ATTM_Fen_Yukon_00) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_01 = np.round((self.ATTM_Fen_Yukon_01) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_02 = np.round((self.ATTM_Fen_Yukon_02) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_03 = np.round((self.ATTM_Fen_Yukon_03) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_04 = np.round((self.ATTM_Fen_Yukon_04) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_05 = np.round((self.ATTM_Fen_Yukon_05) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_06 = np.round((self.ATTM_Fen_Yukon_06) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_07 = np.round((self.ATTM_Fen_Yukon_07) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_08 = np.round((self.ATTM_Fen_Yukon_08) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_09 = np.round((self.ATTM_Fen_Yukon_09) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_10 = np.round((self.ATTM_Fen_Yukon_10) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_11 = np.round((self.ATTM_Fen_Yukon_11) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_12 = np.round((self.ATTM_Fen_Yukon_12) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_13 = np.round((self.ATTM_Fen_Yukon_13) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_14 = np.round((self.ATTM_Fen_Yukon_14) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_15 = np.round((self.ATTM_Fen_Yukon_15) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_16 = np.round((self.ATTM_Fen_Yukon_16) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_17 = np.round((self.ATTM_Fen_Yukon_17) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_18 = np.round((self.ATTM_Fen_Yukon_18) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_19 = np.round((self.ATTM_Fen_Yukon_19) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_20 = np.round((self.ATTM_Fen_Yukon_20) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_21 = np.round((self.ATTM_Fen_Yukon_21) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_22 = np.round((self.ATTM_Fen_Yukon_22) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_23 = np.round((self.ATTM_Fen_Yukon_23) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_24 = np.round((self.ATTM_Fen_Yukon_24) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_25 = np.round((self.ATTM_Fen_Yukon_25) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_26 = np.round((self.ATTM_Fen_Yukon_26) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_27 = np.round((self.ATTM_Fen_Yukon_27) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_28 = np.round((self.ATTM_Fen_Yukon_28) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_29 = np.round((self.ATTM_Fen_Yukon_29) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_30 = np.round((self.ATTM_Fen_Yukon_30) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_31 = np.round((self.ATTM_Fen_Yukon_31) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_32 = np.round((self.ATTM_Fen_Yukon_32) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_33 = np.round((self.ATTM_Fen_Yukon_33) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_34 = np.round((self.ATTM_Fen_Yukon_34) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_35 = np.round((self.ATTM_Fen_Yukon_35) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_36 = np.round((self.ATTM_Fen_Yukon_36) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_37 = np.round((self.ATTM_Fen_Yukon_37) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_38 = np.round((self.ATTM_Fen_Yukon_38) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_39 = np.round((self.ATTM_Fen_Yukon_39) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_40 = np.round((self.ATTM_Fen_Yukon_40) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_41 = np.round((self.ATTM_Fen_Yukon_41) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_42 = np.round((self.ATTM_Fen_Yukon_42) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_43 = np.round((self.ATTM_Fen_Yukon_43) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_44 = np.round((self.ATTM_Fen_Yukon_44) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_45 = np.round((self.ATTM_Fen_Yukon_45) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_46 = np.round((self.ATTM_Fen_Yukon_46) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_47 = np.round((self.ATTM_Fen_Yukon_47) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_48 = np.round((self.ATTM_Fen_Yukon_48) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_49 = np.round((self.ATTM_Fen_Yukon_49) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_50 = np.round((self.ATTM_Fen_Yukon_50) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_51 = np.round((self.ATTM_Fen_Yukon_51) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_52 = np.round((self.ATTM_Fen_Yukon_52) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_53 = np.round((self.ATTM_Fen_Yukon_53) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_54 = np.round((self.ATTM_Fen_Yukon_54) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_55 = np.round((self.ATTM_Fen_Yukon_55) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_56 = np.round((self.ATTM_Fen_Yukon_56) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_57 = np.round((self.ATTM_Fen_Yukon_57) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_58 = np.round((self.ATTM_Fen_Yukon_58) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_59 = np.round((self.ATTM_Fen_Yukon_59) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_60 = np.round((self.ATTM_Fen_Yukon_60) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_61 = np.round((self.ATTM_Fen_Yukon_61) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_62 = np.round((self.ATTM_Fen_Yukon_62) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_63 = np.round((self.ATTM_Fen_Yukon_63) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_64 = np.round((self.ATTM_Fen_Yukon_64) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_65 = np.round((self.ATTM_Fen_Yukon_65) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_66 = np.round((self.ATTM_Fen_Yukon_66) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_67 = np.round((self.ATTM_Fen_Yukon_67) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_68 = np.round((self.ATTM_Fen_Yukon_68) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_69 = np.round((self.ATTM_Fen_Yukon_69) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_70 = np.round((self.ATTM_Fen_Yukon_70) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_71 = np.round((self.ATTM_Fen_Yukon_71) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_72 = np.round((self.ATTM_Fen_Yukon_72) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_73 = np.round((self.ATTM_Fen_Yukon_73) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_74 = np.round((self.ATTM_Fen_Yukon_74) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_75 = np.round((self.ATTM_Fen_Yukon_75) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_76 = np.round((self.ATTM_Fen_Yukon_76) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_77 = np.round((self.ATTM_Fen_Yukon_77) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_78 = np.round((self.ATTM_Fen_Yukon_78) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_79 = np.round((self.ATTM_Fen_Yukon_79) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_80 = np.round((self.ATTM_Fen_Yukon_80) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_81 = np.round((self.ATTM_Fen_Yukon_81) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_82 = np.round((self.ATTM_Fen_Yukon_82) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_83 = np.round((self.ATTM_Fen_Yukon_83) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_84 = np.round((self.ATTM_Fen_Yukon_84) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_85 = np.round((self.ATTM_Fen_Yukon_85) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_86 = np.round((self.ATTM_Fen_Yukon_86) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_87 = np.round((self.ATTM_Fen_Yukon_87) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_88 = np.round((self.ATTM_Fen_Yukon_88) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_89 = np.round((self.ATTM_Fen_Yukon_89) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_90 = np.round((self.ATTM_Fen_Yukon_90) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_91 = np.round((self.ATTM_Fen_Yukon_91) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_92 = np.round((self.ATTM_Fen_Yukon_92) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_93 = np.round((self.ATTM_Fen_Yukon_93) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_94 = np.round((self.ATTM_Fen_Yukon_94) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_95 = np.round((self.ATTM_Fen_Yukon_95) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_96 = np.round((self.ATTM_Fen_Yukon_96) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_97 = np.round((self.ATTM_Fen_Yukon_97) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_98 = np.round((self.ATTM_Fen_Yukon_98) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_99 = np.round((self.ATTM_Fen_Yukon_99) / cohorts_required, decimals = 6)
    # --------------------------------------------------------------------------------------------------
    self.ATTM_Bog_Yukon_00_09 = np.round((self.ATTM_Bog_Yukon_00_09) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_10_19 = np.round((self.ATTM_Bog_Yukon_10_19) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_20_29 = np.round((self.ATTM_Bog_Yukon_20_29) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_30_39 = np.round((self.ATTM_Bog_Yukon_30_39) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_40_49 = np.round((self.ATTM_Bog_Yukon_40_49) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_50_59 = np.round((self.ATTM_Bog_Yukon_50_59) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_60_69 = np.round((self.ATTM_Bog_Yukon_60_69) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_70_79 = np.round((self.ATTM_Bog_Yukon_70_79) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_80_89 = np.round((self.ATTM_Bog_Yukon_80_89) / cohorts_required, decimals = 6)
    self.ATTM_Bog_Yukon_90_99 = np.round((self.ATTM_Bog_Yukon_90_99) / cohorts_required, decimals = 6)
    # --------------------------------------------------------------------------------------------------
    self.ATTM_Fen_Yukon_00_09 = np.round((self.ATTM_Fen_Yukon_00_09) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_10_19 = np.round((self.ATTM_Fen_Yukon_10_19) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_20_29 = np.round((self.ATTM_Fen_Yukon_20_29) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_30_39 = np.round((self.ATTM_Fen_Yukon_30_39) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_40_49 = np.round((self.ATTM_Fen_Yukon_40_49) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_50_59 = np.round((self.ATTM_Fen_Yukon_50_59) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_60_69 = np.round((self.ATTM_Fen_Yukon_60_69) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_70_79 = np.round((self.ATTM_Fen_Yukon_70_79) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_80_89 = np.round((self.ATTM_Fen_Yukon_80_89) / cohorts_required, decimals = 6)
    self.ATTM_Fen_Yukon_90_99 = np.round((self.ATTM_Fen_Yukon_90_99) / cohorts_required, decimals = 6)
    #---------------------------------------------------------------------------------------------------
    self.ATTM_Total_Fractional_Area = np.round(self.ATTM_Barren_Yukon + self.ATTM_Bog_Yukon + \
                                                self.ATTM_DeciduousForest_Yukon + self.ATTM_DwarfShrub_Yukon + \
                                                self.ATTM_EvergreenForest_Yukon + self.ATTM_Fen_Yukon + \
                                                self.ATTM_Lake_Yukon + self.ATTM_Pond_Yukon + \
                                                self.ATTM_River_Yukon + self.ATTM_ShrubScrub_Yukon + \
                                                self.ATTM_Unclassified_Yukon +\
                                                self.ATTM_Bog_Yukon_00 + self.ATTM_Bog_Yukon_01 + \
                                                self.ATTM_Bog_Yukon_02 + self.ATTM_Bog_Yukon_03 + \
                                                self.ATTM_Bog_Yukon_04 + self.ATTM_Bog_Yukon_05 + \
                                                self.ATTM_Bog_Yukon_06 + self.ATTM_Bog_Yukon_07 + \
                                                self.ATTM_Bog_Yukon_08 + self.ATTM_Bog_Yukon_09 + \
                                                self.ATTM_Bog_Yukon_10 + self.ATTM_Bog_Yukon_11 + \
                                                self.ATTM_Bog_Yukon_12 + self.ATTM_Bog_Yukon_13 + \
                                                self.ATTM_Bog_Yukon_14 + self.ATTM_Bog_Yukon_15 + \
                                                self.ATTM_Bog_Yukon_16 + self.ATTM_Bog_Yukon_17 + \
                                                self.ATTM_Bog_Yukon_18 + self.ATTM_Bog_Yukon_19 + \
                                                self.ATTM_Bog_Yukon_20 + self.ATTM_Bog_Yukon_21 + \
                                                self.ATTM_Bog_Yukon_22 + self.ATTM_Bog_Yukon_23 + \
                                                self.ATTM_Bog_Yukon_24 + self.ATTM_Bog_Yukon_25 + \
                                                self.ATTM_Bog_Yukon_26 + self.ATTM_Bog_Yukon_27 + \
                                                self.ATTM_Bog_Yukon_28 + self.ATTM_Bog_Yukon_29 + \
                                                self.ATTM_Bog_Yukon_30 + self.ATTM_Bog_Yukon_31 + \
                                                self.ATTM_Bog_Yukon_32 + self.ATTM_Bog_Yukon_33 + \
                                                self.ATTM_Bog_Yukon_34 + self.ATTM_Bog_Yukon_35 + \
                                                self.ATTM_Bog_Yukon_36 + self.ATTM_Bog_Yukon_37 + \
                                                self.ATTM_Bog_Yukon_38 + self.ATTM_Bog_Yukon_39 + \
                                                self.ATTM_Bog_Yukon_40 + self.ATTM_Bog_Yukon_41 + \
                                                self.ATTM_Bog_Yukon_42 + self.ATTM_Bog_Yukon_43 + \
                                                self.ATTM_Bog_Yukon_44 + self.ATTM_Bog_Yukon_45 + \
                                                self.ATTM_Bog_Yukon_46 + self.ATTM_Bog_Yukon_47 + \
                                                self.ATTM_Bog_Yukon_48 + self.ATTM_Bog_Yukon_49 + \
                                                self.ATTM_Bog_Yukon_50 + self.ATTM_Bog_Yukon_51 + \
                                                self.ATTM_Bog_Yukon_52 + self.ATTM_Bog_Yukon_53 + \
                                                self.ATTM_Bog_Yukon_54 + self.ATTM_Bog_Yukon_55 + \
                                                self.ATTM_Bog_Yukon_56 + self.ATTM_Bog_Yukon_57 + \
                                                self.ATTM_Bog_Yukon_58 + self.ATTM_Bog_Yukon_59 + \
                                                self.ATTM_Bog_Yukon_60 + self.ATTM_Bog_Yukon_61 + \
                                                self.ATTM_Bog_Yukon_62 + self.ATTM_Bog_Yukon_63 + \
                                                self.ATTM_Bog_Yukon_64 + self.ATTM_Bog_Yukon_65 + \
                                                self.ATTM_Bog_Yukon_66 + self.ATTM_Bog_Yukon_67 + \
                                                self.ATTM_Bog_Yukon_68 + self.ATTM_Bog_Yukon_69 + \
                                                self.ATTM_Bog_Yukon_70 + self.ATTM_Bog_Yukon_71 + \
                                                self.ATTM_Bog_Yukon_72 + self.ATTM_Bog_Yukon_73 + \
                                                self.ATTM_Bog_Yukon_74 + self.ATTM_Bog_Yukon_75 + \
                                                self.ATTM_Bog_Yukon_76 + self.ATTM_Bog_Yukon_77 + \
                                                self.ATTM_Bog_Yukon_78 + self.ATTM_Bog_Yukon_79 + \
                                                self.ATTM_Bog_Yukon_80 + self.ATTM_Bog_Yukon_81 + \
                                                self.ATTM_Bog_Yukon_82 + self.ATTM_Bog_Yukon_83 + \
                                                self.ATTM_Bog_Yukon_84 + self.ATTM_Bog_Yukon_85 + \
                                                self.ATTM_Bog_Yukon_86 + self.ATTM_Bog_Yukon_87 + \
                                                self.ATTM_Bog_Yukon_88 + self.ATTM_Bog_Yukon_89 + \
                                                self.ATTM_Bog_Yukon_90 + self.ATTM_Bog_Yukon_91 + \
                                                self.ATTM_Bog_Yukon_92 + self.ATTM_Bog_Yukon_93 + \
                                                self.ATTM_Bog_Yukon_94 + self.ATTM_Bog_Yukon_95 + \
                                                self.ATTM_Bog_Yukon_96 + self.ATTM_Bog_Yukon_97 + \
                                                self.ATTM_Bog_Yukon_98 + self.ATTM_Bog_Yukon_99 + \
                                                self.ATTM_Fen_Yukon_00 + self.ATTM_Fen_Yukon_01 + \
                                                self.ATTM_Fen_Yukon_02 + self.ATTM_Fen_Yukon_03 + \
                                                self.ATTM_Fen_Yukon_04 + self.ATTM_Fen_Yukon_05 + \
                                                self.ATTM_Fen_Yukon_06 + self.ATTM_Fen_Yukon_07 + \
                                                self.ATTM_Fen_Yukon_08 + self.ATTM_Fen_Yukon_09 + \
                                                self.ATTM_Fen_Yukon_10 + self.ATTM_Fen_Yukon_11 + \
                                                self.ATTM_Fen_Yukon_12 + self.ATTM_Fen_Yukon_13 + \
                                                self.ATTM_Fen_Yukon_14 + self.ATTM_Fen_Yukon_15 + \
                                                self.ATTM_Fen_Yukon_16 + self.ATTM_Fen_Yukon_17 + \
                                                self.ATTM_Fen_Yukon_18 + self.ATTM_Fen_Yukon_19 + \
                                                self.ATTM_Fen_Yukon_20 + self.ATTM_Fen_Yukon_21 + \
                                                self.ATTM_Fen_Yukon_22 + self.ATTM_Fen_Yukon_23 + \
                                                self.ATTM_Fen_Yukon_24 + self.ATTM_Fen_Yukon_25 + \
                                                self.ATTM_Fen_Yukon_26 + self.ATTM_Fen_Yukon_27 + \
                                                self.ATTM_Fen_Yukon_28 + self.ATTM_Fen_Yukon_29 + \
                                                self.ATTM_Fen_Yukon_30 + self.ATTM_Fen_Yukon_31 + \
                                                self.ATTM_Fen_Yukon_32 + self.ATTM_Fen_Yukon_33 + \
                                                self.ATTM_Fen_Yukon_34 + self.ATTM_Fen_Yukon_35 + \
                                                self.ATTM_Fen_Yukon_36 + self.ATTM_Fen_Yukon_37 + \
                                                self.ATTM_Fen_Yukon_38 + self.ATTM_Fen_Yukon_39 + \
                                                self.ATTM_Fen_Yukon_40 + self.ATTM_Fen_Yukon_41 + \
                                                self.ATTM_Fen_Yukon_42 + self.ATTM_Fen_Yukon_43 + \
                                                self.ATTM_Fen_Yukon_44 + self.ATTM_Fen_Yukon_45 + \
                                                self.ATTM_Fen_Yukon_46 + self.ATTM_Fen_Yukon_47 + \
                                                self.ATTM_Fen_Yukon_48 + self.ATTM_Fen_Yukon_49 + \
                                                self.ATTM_Fen_Yukon_50 + self.ATTM_Fen_Yukon_51 + \
                                                self.ATTM_Fen_Yukon_52 + self.ATTM_Fen_Yukon_53 + \
                                                self.ATTM_Fen_Yukon_54 + self.ATTM_Fen_Yukon_55 + \
                                                self.ATTM_Fen_Yukon_56 + self.ATTM_Fen_Yukon_57 + \
                                                self.ATTM_Fen_Yukon_58 + self.ATTM_Fen_Yukon_59 + \
                                                self.ATTM_Fen_Yukon_60 + self.ATTM_Fen_Yukon_61 + \
                                                self.ATTM_Fen_Yukon_62 + self.ATTM_Fen_Yukon_63 + \
                                                self.ATTM_Fen_Yukon_64 + self.ATTM_Fen_Yukon_65 + \
                                                self.ATTM_Fen_Yukon_66 + self.ATTM_Fen_Yukon_67 + \
                                                self.ATTM_Fen_Yukon_68 + self.ATTM_Fen_Yukon_69 + \
                                                self.ATTM_Fen_Yukon_70 + self.ATTM_Fen_Yukon_71 + \
                                                self.ATTM_Fen_Yukon_72 + self.ATTM_Fen_Yukon_73 + \
                                                self.ATTM_Fen_Yukon_74 + self.ATTM_Fen_Yukon_75 + \
                                                self.ATTM_Fen_Yukon_76 + self.ATTM_Fen_Yukon_77 + \
                                                self.ATTM_Fen_Yukon_78 + self.ATTM_Fen_Yukon_79 + \
                                                self.ATTM_Fen_Yukon_80 + self.ATTM_Fen_Yukon_81 + \
                                                self.ATTM_Fen_Yukon_82 + self.ATTM_Fen_Yukon_83 + \
                                                self.ATTM_Fen_Yukon_84 + self.ATTM_Fen_Yukon_85 + \
                                                self.ATTM_Fen_Yukon_86 + self.ATTM_Fen_Yukon_87 + \
                                                self.ATTM_Fen_Yukon_88 + self.ATTM_Fen_Yukon_89 + \
                                                self.ATTM_Fen_Yukon_90 + self.ATTM_Fen_Yukon_91 + \
                                                self.ATTM_Fen_Yukon_92 + self.ATTM_Fen_Yukon_93 + \
                                                self.ATTM_Fen_Yukon_94 + self.ATTM_Fen_Yukon_95 + \
                                                self.ATTM_Fen_Yukon_96 + self.ATTM_Fen_Yukon_97 + \
                                                self.ATTM_Fen_Yukon_98 + self.ATTM_Fen_Yukon_99,  \
                                                decimals = 6)

    for i in range(self.ATTM_nrows * self.ATTM_ncols):
        if np.round(self.ATTM_Total_Fractional_Area[i], decimals = 3) > 1.0:
            print ' ' 
            print 'There is a mass balance problem in element: ', i
            print 'The total fractional area of all cohorts is greater than 1.0'
            print '[in initial_cohort_check]'
            print ' '
            print 'The total fractional area of all cohorts is: ', self.ATTM_Total_Fractional_Area[i]
            print ' '
            print 'Barren, Yukon: ', self.ATTM_Barren_Yukon[i]
            print 'Bog, Yukon: ', self.ATTM_Bog_Yukon[i]
            print 'Deciduous Forest, Yukon: ', self.ATTM_DeciduousForest_Yukon[i]
            print 'Dwarf Shrub, Yukon: ', self.ATTM_DwarfShrub_Yukon[i]
            print 'Evergreen Forest, Yukon: ', self.ATTM_EvergreenForest_Yukon[i]
            print 'Fen, Yukon: ', self.ATTM_Fen_Yukon[i]
            print 'Lake, Yukon: ', self.ATTM_Lake_Yukon[i]
            print 'Pond, Yukon: ', self.ATTM_Pond_Yukon[i]
            print 'River, Yukon: ', self.ATTM_River_Yukon[i]
            print 'Shrub-Scrub, Yukon: ', self.ATTM_ShrubScrub_Yukon[i]
            print 'Unclassified, Yukon: ', self.ATTM_Unclassified_Yukon[i]
    
        if np.round(self.ATTM_Total_Fractional_Area[i], decimals = 3) < 0.0:
            print 'There is a mass balance problem in element: ', i
            print 'The total fractional area of all cohorts is less than 0.0.'
            print '[in initial_cohort_check]'
            print ' '
            print 'Barren, Yukon: ', self.ATTM_Barren_Yukon[i]
            print 'Bog, Yukon: ', self.ATTM_Bog_Yukon[i]
            print 'Deciduous Forest, Yukon: ', self.ATTM_DeciduousForest_Yukon[i]
            print 'Dwarf Shrub, Yukon: ', self.ATTM_DwarfShrub_Yukon[i]
            print 'Evergreen Forest, Yukon: ', self.ATTM_EvergreenForest_Yukon[i]
            print 'Fen, Yukon: ', self.ATTM_Fen_Yukon[i]
            print 'Lake, Yukon: ', self.ATTM_Lake_Yukon[i]
            print 'Pond, Yukon: ', self.ATTM_Pond_Yukon[i]
            print 'River, Yukon: ', self.ATTM_River_Yukon[i]
            print 'Shrub-Scrub, Yukon: ', self.ATTM_ShrubScrub_Yukon[i]
            print 'Unclassified, Yukon: ', self.ATTM_Unclassified_Yukon[i]

    # Statement of what has been done for debugging
    print '      done.'
    print ' '

    if self.initialize['Normalized_Cohort_Distribution_Figure'].lower() == 'yes':    
        cohort_check = np.reshape(self.ATTM_Total_Fractional_Area,  [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        
        ATTM_Total_plot   =  np.reshape(self.ATTM_Total_Fractional_Area,\
                                        [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Barren_Yukon_plot = np.reshape(self.ATTM_Barren_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_plot    = np.reshape(self.ATTM_Bog_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_DeciduousForest_Yukon_plot = np.reshape(self.ATTM_DeciduousForest_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_DwarfShrub_Yukon_plot = np.reshape(self.ATTM_DwarfShrub_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_EvergreenForest_Yukon_plot = np.reshape(self.ATTM_EvergreenForest_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_plot = np.reshape(self.ATTM_Fen_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Lake_Yukon_plot = np.reshape(self.ATTM_Lake_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Pond_Yukon_plot = np.reshape(self.ATTM_Pond_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_River_Yukon_plot = np.reshape(self.ATTM_River_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_ShrubScrub_Yukon_plot = np.reshape(self.ATTM_ShrubScrub_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Unclassified_Yukon_plot = np.reshape(self.ATTM_Unclassified_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_00_09_plot = np.reshape(self.ATTM_Bog_Yukon_00_09, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_10_19_plot = np.reshape(self.ATTM_Bog_Yukon_10_19, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_20_29_plot = np.reshape(self.ATTM_Bog_Yukon_20_29, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_30_39_plot = np.reshape(self.ATTM_Bog_Yukon_30_39, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_40_49_plot = np.reshape(self.ATTM_Bog_Yukon_40_49, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_50_59_plot = np.reshape(self.ATTM_Bog_Yukon_50_59, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_60_69_plot = np.reshape(self.ATTM_Bog_Yukon_60_69, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_70_79_plot = np.reshape(self.ATTM_Bog_Yukon_70_79, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_80_89_plot = np.reshape(self.ATTM_Bog_Yukon_80_89, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_90_99_plot = np.reshape(self.ATTM_Bog_Yukon_90_99, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_00_09_plot = np.reshape(self.ATTM_Fen_Yukon_00_09, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_10_19_plot = np.reshape(self.ATTM_Fen_Yukon_10_19, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_20_29_plot = np.reshape(self.ATTM_Fen_Yukon_20_29, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_30_39_plot = np.reshape(self.ATTM_Fen_Yukon_30_39, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_40_49_plot = np.reshape(self.ATTM_Fen_Yukon_40_49, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_50_59_plot = np.reshape(self.ATTM_Fen_Yukon_50_59, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_60_69_plot = np.reshape(self.ATTM_Fen_Yukon_60_69, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_70_79_plot = np.reshape(self.ATTM_Fen_Yukon_70_79, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_80_89_plot = np.reshape(self.ATTM_Fen_Yukon_80_89, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_90_99_plot = np.reshape(self.ATTM_Fen_Yukon_90_99, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        
        # Move to output directory

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Yukon/')

        #---------------------------------------------------------
        # Create Figures, Plots and Binary files for each cohort
        #---------------------------------------------------------
        if self.initialize['Barren_Yukon_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Barren_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Barren\n Initial Cohort Fraction')
            pl.savefig('./Barren_Yukon/Initial_Fraction_Cohorts_Barren_Yukon.png', format = 'png')
            self.ATTM_Barren_Yukon.tofile('./Barren_Yukon/Barren_Yukon_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Bog_Yukon_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs\n Initial Cohort Fraction')
            pl.savefig('./Bog_Yukon/Initial_Fraction_Cohorts_Bog_Yukon.png', format = 'png')
            self.ATTM_Bog_Yukon.tofile('./Bog_Yukon/Bog_Yukon_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['DeciduousForest_Yukon_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_DeciduousForest_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Deciduous Forest\n Initial Cohort Fraction')
            pl.savefig('./DeciduousForest_Yukon/Initial_Fraction_Cohorts_DeciduousForest_Yukon.png', format = 'png')
            self.ATTM_DeciduousForest_Yukon.tofile('./DeciduousForest_Yukon/DeciduousForest_Yukon_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------                                       
        if self.initialize['DwarfShrub_Yukon_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_DwarfShrub_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Dwarf Shrub\n Initial Cohort Fraction')
            pl.savefig('./DwarfShrub_Yukon/Initial_Fraction_Cohorts_DwarfShrub_Yukon.png', format = 'png')
            self.ATTM_DwarfShrub_Yukon.tofile('./DwarfShrub_Yukon/DwarfShrub_Yukon_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Fen_Yukon_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens\n Initial Cohort Fraction')
            pl.savefig('./Fen_Yukon/Initial_Fraction_Cohorts_Fen_Yukon.png', format = 'png')
            self.ATTM_Fen_Yukon.tofile('./Fen_Yukon/Fen_Yukon_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['EvergreenForest_Yukon_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_EvergreenForest_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - EvergreenForest\n Initial Cohort Fraction')
            pl.savefig('./EvergreenForest_Yukon/Initial_Fraction_Cohorts_EvergreenForest_Yukon.png', format = 'png')
            self.ATTM_EvergreenForest_Yukon.tofile('./EvergreenForest_Yukon/EvergreenForest_Yukon_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Lake_Yukon_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Lake_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Lakes\n Initial Cohort Fraction')
            pl.savefig('./Lake_Yukon/Initial_Fraction_Cohorts_Lake_Yukon.png', format = 'png')
            self.ATTM_Lake_Yukon.tofile('./Lake_Yukon/Lake_Yukon_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Pond_Yukon_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Pond_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Ponds\n Initial Cohort Fraction')
            pl.savefig('./Pond_Yukon/Initial_Fraction_Cohorts_Pond_Yukon.png', format = 'png')
            self.ATTM_Pond_Yukon.tofile('./Pond_Yukon/Pond_Yukon_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['River_Yukon_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_River_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Rivers\n Initial Cohort Fraction')
            pl.savefig('./River_Yukon/Initial_Fraction_Cohorts_River_Yukon.png', format = 'png')
            self.ATTM_River_Yukon.tofile('./River_Yukon/River_Yukon_initial_fractional_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['ShrubScrub_Yukon_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_ShrubScrub_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Shrub-Scrub\n Initial Cohort Fraction')
            pl.savefig('./ShrubScrub_Yukon/Initial_Fraction_Cohorts_ShrubScrub_Yukon.png', format = 'png')
            self.ATTM_ShrubScrub_Yukon.tofile('./ShrubScrub_Yukon/ShrubScrub_Yukon_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Unclassified_Yukon_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Unclassified_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Unclassified\n Initial Cohort Fraction')
            pl.savefig('./Unclassified_Yukon/Initial_Fractional_Cohorts_Unclassifeid_Yukon.png', format = 'png')
            self.ATTM_Unclassified_Yukon.tofile('./Unclassified_Yukon/Unclassified_Yukon_initial_fractional_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['All_Cohorts_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Total_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('All Cohorts Combined Fractional Area')
            pl.savefig('./Yukon_All_Cohorts/Initial_Fractional_Total_Cohorts.png', format = 'png')
            self.ATTM_Total.tofile('./Yukon_All_Cohorts/Total_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_00_09_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_00_09_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs (age: 00-09)\n Initial Cohort Fraction')
            pl.savefig('./Bog_Yukon_00_09/Initial_Fractional_Cohorts_Bog_Yukon_00_09.png', format = 'png')
            self.ATTM_Bog_Yukon_00_09.tofile('./Bog_Yukon_00_09/Bog_Yukon_00_09_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_10_19_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_10_19_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs (age: 10-19)\n Initial Cohort Fraction')
            pl.savefig('./Bog_Yukon_10_19/Initial_Fractional_Cohorts_Bog_Yukon_10_19.png', format = 'png')
            self.ATTM_Bog_Yukon_10_19.tofile('./Bog_Yukon_10_19/Bog_Yukon_10_19_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_20_29_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_20_29_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs (age: 20-29)\n Initial Cohort Fraction')
            pl.savefig('./Bog_Yukon_20_29/Initial_Fractional_Cohorts_Bog_Yukon_20_29.png', format = 'png')
            self.ATTM_Bog_Yukon_20_29.tofile('./Bog_Yukon_20_29/Bog_Yukon_20_29_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_30_39_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_30_39_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs (age: 30-39)\n Initial Cohort Fraction')
            pl.savefig('./Bog_Yukon_30_39/Initial_Fractional_Cohorts_Bog_Yukon_30_39.png', format = 'png')
            self.ATTM_Bog_Yukon_30_39.tofile('./Bog_Yukon_30_39/Bog_Yukon_30_39_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_40_49_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_40_49_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs (age: 40-49)\n Initial Cohort Fraction')
            pl.savefig('./Bog_Yukon_40_49/Initial_Fractional_Cohorts_Bog_Yukon_40_49.png', format = 'png')
            self.ATTM_Bog_Yukon_40_49.tofile('./Bog_Yukon_40_49/Bog_Yukon_40_49_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_50_59_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_50_59_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs (age: 50-59)\n Initial Cohort Fraction')
            pl.savefig('./Bog_Yukon_50_59/Initial_Fractional_Cohorts_Bog_Yukon_50_59.png', format = 'png')
            self.ATTM_Bog_Yukon_50_59.tofile('./Bog_Yukon_50_59/Bog_Yukon_50_59_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_60_69_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_60_69_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs (age: 60-69)\n Initial Cohort Fraction')
            pl.savefig('./Bog_Yukon_60_69/Initial_Fractional_Cohorts_Bog_Yukon_60_69.png', format = 'png')
            self.ATTM_Bog_Yukon_60_69.tofile('./Bog_Yukon_60_69/Bog_Yukon_60_69_initial_fractional_cohorts.bin')
            pl.close()             
        #-------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_70_79_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_70_79_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs (age: 70-79)\n Initial Cohort Fraction')
            pl.savefig('./Bog_Yukon_70_79/Initial_Fractional_Cohorts_Bog_Yukon_70_79.png', format = 'png')
            self.ATTM_Bog_Yukon_70_79.tofile('./Bog_Yukon_70_79/Bog_Yukon_70_79_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_80_89_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_80_89_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs (age: 80-89)\n Initial Cohort Fraction')
            pl.savefig('./Bog_Yukon_80_89/Initial_Fractional_Cohorts_Bog_Yukon_80_89.png', format = 'png')
            self.ATTM_Bog_Yukon_80_89.tofile('./Bog_Yukon_80_89/Bog_Yukon_80_89_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_90_99_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_90_99_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs (age: 90-99)\n Initial Cohort Fraction')
            pl.savefig('./Bog_Yukon_90_99/Initial_Fractional_Cohorts_Bog_Yukon_90_99.png', format = 'png')
            self.ATTM_Bog_Yukon_90_99.tofile('./Bog_Yukon_90_99/Bog_Yukon_90_99_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_00_09_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_00_09_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens (age: 00-09)\n Initial Cohort Fraction')
            pl.savefig('./Fen_Yukon_00_09/Initial_Fractional_Cohorts_Fen_Yukon_00_09.png', format = 'png')
            self.ATTM_Fen_Yukon_00_09.tofile('./Fen_Yukon_00_09/Fen_Yukon_00_09_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_10_19_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_10_19_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens (age: 10-19)\n Initial Cohort Fraction')
            pl.savefig('./Fen_Yukon_10_19/Initial_Fractional_Cohorts_Fen_Yukon_10_19.png', format = 'png')
            self.ATTM_Fen_Yukon_10_19.tofile('./Fen_Yukon_10_19/Fen_Yukon_10_19_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_20_29_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_20_29_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens (age: 20-29)\n Initial Cohort Fraction')
            pl.savefig('./Fen_Yukon_20_29/Initial_Fractional_Cohorts_Fen_Yukon_20_29.png', format = 'png')
            self.ATTM_Fen_Yukon_20_29.tofile('./Fen_Yukon_20_29/Fen_Yukon_20_29_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_30_39_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_30_39_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens (age: 30-39)\n Initial Cohort Fraction')
            pl.savefig('./Fen_Yukon_30_39/Initial_Fractional_Cohorts_Fen_Yukon_30_39.png', format = 'png')
            self.ATTM_Fen_Yukon_30_39.tofile('./Fen_Yukon_30_39/Fen_Yukon_30_39_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_40_49_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_40_49_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens (age: 40-49)\n Initial Cohort Fraction')
            pl.savefig('./Fen_Yukon_40_49/Initial_Fractional_Cohorts_Fen_Yukon_40_49.png', format = 'png')
            self.ATTM_Fen_Yukon_40_49.tofile('./Fen_Yukon_40_49/Fen_Yukon_40_49_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_50_59_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_50_59_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens (age: 50-59)\n Initial Cohort Fraction')
            pl.savefig('./Fen_Yukon_50_59/Initial_Fractional_Cohorts_Fen_Yukon_50_59.png', format = 'png')
            self.ATTM_Fen_Yukon_50_59.tofile('./Fen_Yukon_50_59/Fen_Yukon_50_59_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_60_69_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_60_69_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens (age: 60-69)\n Initial Cohort Fraction')
            pl.savefig('./Fen_Yukon_60_69/Initial_Fractional_Cohorts_Fen_Yukon_60_69.png', format = 'png')
            self.ATTM_Fen_Yukon_60_69.tofile('./Fen_Yukon_60_69/Fen_Yukon_60_69_initial_fractional_cohorts.bin')
            pl.close()             
        #-------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_70_79_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_70_79_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens (age: 70-79)\n Initial Cohort Fraction')
            pl.savefig('./Fen_Yukon_70_79/Initial_Fractional_Cohorts_Fen_Yukon_70_79.png', format = 'png')
            self.ATTM_Fen_Yukon_70_79.tofile('./Fen_Yukon_70_79/Fen_Yukon_70_79_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_80_89_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_80_89_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens (age: 80-89)\n Initial Cohort Fraction')
            pl.savefig('./Fen_Yukon_80_89/Initial_Fractional_Cohorts_Fen_Yukon_80_89.png', format = 'png')
            self.ATTM_Fen_Yukon_80_89.tofile('./Fen_Yukon_80_89/Fen_Yukon_80_89_initial_fractional_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_90_99_Normal'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_90_99_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens (age: 90-99)\n Initial Cohort Fraction')
            pl.savefig('./Fen_Yukon_90_99/Initial_Fractional_Cohorts_Fen_Yukon_90_99.png', format = 'png')
            self.ATTM_Fen_Yukon_90_99.tofile('./Fen_Yukon_90_99/Fen_Yukon_90_99_initial_fractional_cohorts.bin')
            pl.close()
        #=====================================================================================================
    if self.initialize['Initial_Dominant_Cohort_Figure'].lower() == 'yes':

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Yukon/Yukon_All_Cohorts/')

        # Determine Dominant Cohort for each grid cell
        self.dominant_cohort = np.zeros([self.ATTM_nrows * self.ATTM_ncols])

        # Barren [0], Bog [1], Deciduous Forest [2], Dwarf Shrub [3], Fen [4],
        # Evergreen Forest [5], Lake [6], Pond [7], River[8], Shrub-Scrub [9],
        # Unclassified [10]
        
        cohort_compare = np.zeros(11)

        for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
            if np.sum(self.ATTM_Barren_Yukon[i] + self.ATTM_Bog_Yukon[i] + \
                      self.ATTM_DeciduousForest_Yukon[i] + self.ATTM_DwarfShrub_Yukon[i] + \
                      self.ATTM_Fen_Yukon[i] + self.ATTM_EvergreenForest_Yukon[i] + \
                      self.ATTM_Lake_Yukon[i] + self.ATTM_Pond_Yukon[i] + \
                      self.ATTM_River_Yukon[i] + self.ATTM_ShrubScrub_Yukon[i] + \
                      self.ATTM_Unclassified_Yukon[i]) > 0.0 :

                cohort_compare[0] = self.ATTM_Barren_Yukon[i]
                cohort_compare[1] = self.ATTM_Bog_Yukon[i] + self.ATTM_Bog_Yukon_00_09[i] + \
                                    self.ATTM_Bog_Yukon_10_19[i] + self.ATTM_Bog_Yukon_20_29[i] + \
                                    self.ATTM_Bog_Yukon_30_39[i] + self.ATTM_Bog_Yukon_40_49[i] + \
                                    self.ATTM_Bog_Yukon_50_59[i] + self.ATTM_Bog_Yukon_60_69[i] + \
                                    self.ATTM_Bog_Yukon_70_79[i] + self.ATTM_Bog_Yukon_80_89[i] + \
                                    self.ATTM_Bog_Yukon_90_99[i]
                cohort_compare[2] = self.ATTM_DeciduousForest_Yukon[i]
                cohort_compare[3] = self.ATTM_DwarfShrub_Yukon[i]
                cohort_compare[4] = self.ATTM_Fen_Yukon[i] + self.ATTM_Fen_Yukon_00_09[i] + \
                                    self.ATTM_Fen_Yukon_10_19[i] + self.ATTM_Fen_Yukon_20_29[i] + \
                                    self.ATTM_Fen_Yukon_30_39[i] + self.ATTM_Fen_Yukon_40_49[i] + \
                                    self.ATTM_Fen_Yukon_50_59[i] + self.ATTM_Fen_Yukon_60_69[i] + \
                                    self.ATTM_Fen_Yukon_70_79[i] + self.ATTM_Fen_Yukon_80_89[i] + \
                                    self.ATTM_Fen_Yukon_90_99[i]
                cohort_compare[5] = self.ATTM_EvergreenForest_Yukon[i]
                cohort_compare[6] = self.ATTM_Lake_Yukon[i]
                cohort_compare[7] = self.ATTM_Pond_Yukon[i]
                cohort_compare[8] = self.ATTM_River_Yukon[i]
                cohort_compare[9] = self.ATTM_ShrubScrub_Yukon[i]
                cohort_compare[10] = self.ATTM_Unclassified_Yukon[i]

                cohort_max = np.where(cohort_compare == cohort_compare.max())

                if cohort_max[0][0] == 0: self.dominant_cohort[i] = 1
                if cohort_max[0][0] == 1: self.dominant_cohort[i] = 2
                if cohort_max[0][0] == 2: self.dominant_cohort[i] = 3
                if cohort_max[0][0] == 3: self.dominant_cohort[i] = 4
                if cohort_max[0][0] == 4: self.dominant_cohort[i] = 5
                if cohort_max[0][0] == 5: self.dominant_cohort[i] = 6
                if cohort_max[0][0] == 6: self.dominant_cohort[i] = 7
                if cohort_max[0][0] == 7: self.dominant_cohort[i] = 8
                if cohort_max[0][0] == 8: self.dominant_cohort[i] = 9
                if cohort_max[0][0] == 9: self.dominant_cohort[i] = 10
                if cohort_max[0][0] == 10: self.dominant_cohort[i] = 11
            else:
                self.dominant_cohort[i] = 0
                
        dominant_cohort_plot = np.reshape(self.dominant_cohort, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()

        cax = pl.imshow(dominant_cohort_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0, vmax = 11)
        pl.title(' Initial Dominant Cohort ')
        
        cbar = pl.colorbar(ticks = [0,1,2,3,4,5,6,7,8,9,10,11], orientation = 'vertical')

        cbar.set_ticklabels(['', 'Barren', 'Bog', 'Dec. Forest', 'Dwarf Shrub', 'Fen', \
                             'Con. Forest', 'Lake', 'Pond', 'River', 'Shrub-Scrub', \
                             'Unclassified'])

        pl.savefig('Initial_Dominant_Cohort.jpg', format = 'jpg')
        dominant_cohort_plot.tofile('Initial_Dominant_Cohort.bin')
        pl.close()
        # Return to Run Directory
        os.chdir(self.control['Run_dir'])
        

        
        
    # Return to Run Directory
    os.chdir(self.control['Run_dir'])
