import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def initial_cohort_age(self):
    """
    The purpose of this module is to initialize the ages of
    each cohort present in the model domain. If the cohort is
    present, the age is set to 1.

    Initially, ages will be tracked in arrays. At each time step,
    if the cohort is still present, the age will increase by 1. If
    the cohort disappears, the age will be set to 0.  Using arrays
    will make it easy to track when the cohort emerge and disappear
    from each element.
    """

    print '    Initializing the age of all cohorts.'
    self.ATTM_CLC_WT_Y_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_CLC_WT_M_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_CLC_WT_O_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_CoastalWaters_WT_O_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_DrainedSlope_WT_Y_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_DrainedSlope_WT_M_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_DrainedSlope_WT_O_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_FCP_WT_Y_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_FCP_WT_M_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_FCP_WT_O_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_HCP_WT_Y_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_HCP_WT_M_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_HCP_WT_O_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_LCP_WT_Y_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_LCP_WT_M_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_LCP_WT_O_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_Meadow_WT_Y_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_Meadow_WT_M_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_Meadow_WT_O_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_NoData_WT_O_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_SandDunes_WT_Y_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_SandDunes_WT_M_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_SandDunes_WT_O_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.ATTM_SaturatedBarrens_WT_Y_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_SaturatedBarrens_WT_M_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_SaturatedBarrens_WT_O_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_Shrubs_WT_O_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_Urban_WT_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_LargeLakes_WT_Y_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_LargeLakes_WT_M_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_LargeLakes_WT_O_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_MediumLakes_WT_Y_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_MediumLakes_WT_M_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_MediumLakes_WT_O_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_SmallLakes_WT_Y_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_SmallLakes_WT_M_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_SmallLakes_WT_O_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_Ponds_WT_Y_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_Ponds_WT_M_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_Ponds_WT_O_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_Rivers_WT_Y_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_Rivers_WT_M_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    self.ATTM_Rivers_WT_O_age = np.zeros([self.ATTM_ncols * self.ATTM_nrows, self.ATTM_time_steps])
    
#    self.Wet_NPG_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
#    self.Wet_LCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
#    self.Wet_CLC_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
#    self.Wet_FCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
#    self.Wet_HCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])  

#    self.Gra_NPG_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
#    self.Gra_LCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
#    self.Gra_FCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
#    self.Gra_HCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])   

#    self.Shr_NPG_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
#    self.Shr_LCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
#    self.Shr_FCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
#    self.Shr_HCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])  

#    self.Lakes_age   = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
#    self.Ponds_age   = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])  

    for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
        if self.ATTM_CLC_WT_Y[i] > 0.0 : self.ATTM_CLC_WT_Y_age[i,0] = 1.
        if self.ATTM_CLC_WT_M[i] > 0.0 : self.ATTM_CLC_WT_M_age[i,0] = 1.
        if self.ATTM_CLC_WT_O[i] > 0.0 : self.ATTM_CLC_WT_O_age[i,0] = 1.
        if self.ATTM_CoastalWaters_WT_O[i] > 0.0 : self.ATTM_CoastalWaters_WT_O_age[i,0] = 1.
        if self.ATTM_DrainedSlope_WT_Y[i] > 0.0 : self.ATTM_DrainedSlope_WT_Y_age[i,0] = 1.
        if self.ATTM_DrainedSlope_WT_M[i] > 0.0 : self.ATTM_DrainedSlope_WT_M_age[i,0] = 1.
        if self.ATTM_DrainedSlope_WT_O[i] > 0.0 : self.ATTM_DrainedSlope_WT_O_age[i,0] = 1.
        if self.ATTM_FCP_WT_Y[i] > 0.0 : self.ATTM_FCP_WT_Y_age[i,0] = 1.
        if self.ATTM_FCP_WT_M[i] > 0.0 : self.ATTM_FCP_WT_M_age[i,0] = 1.
        if self.ATTM_FCP_WT_O[i] > 0.0 : self.ATTM_FCP_WT_O_age[i,0] = 1.
        if self.ATTM_HCP_WT_Y[i] > 0.0 : self.ATTM_HCP_WT_Y_age[i,0] = 1.
        if self.ATTM_HCP_WT_M[i] > 0.0 : self.ATTM_HCP_WT_M_age[i,0] = 1.
        if self.ATTM_HCP_WT_O[i] > 0.0 : self.ATTM_HCP_WT_O_age[i,0] = 1.
        if self.ATTM_LCP_WT_Y[i] > 0.0 : self.ATTM_LCP_WT_Y_age[i,0] = 1.
        if self.ATTM_LCP_WT_M[i] > 0.0 : self.ATTM_LCP_WT_M_age[i,0] = 1.
        if self.ATTM_LCP_WT_O[i] > 0.0 : self.ATTM_LCP_WT_O_age[i,0] = 1.
        if self.ATTM_Meadow_WT_Y[i] > 0.0 : self.ATTM_Meadow_WT_Y_age[i,0] = 1.
        if self.ATTM_Meadow_WT_M[i] > 0.0 : self.ATTM_Meadow_WT_M_age[i,0] = 1.
        if self.ATTM_Meadow_WT_O[i] > 0.0 : self.ATTM_Meadow_WT_O_age[i,0] = 1.
        if self.ATTM_NoData_WT_O[i] > 0.0 : self.ATTM_NoData_WT_O_age[i,0] = 1.
        if self.ATTM_SandDunes_WT_Y[i] > 0.0 : self.ATTM_SandDunes_WT_Y_age[i,0] = 1.
        if self.ATTM_SandDunes_WT_M[i] > 0.0 : self.ATTM_SandDunes_WT_M_age[i,0] = 1.
        if self.ATTM_SandDunes_WT_O[i] > 0.0 : self.ATTM_SandDunes_WT_O_age[i,0] = 1.
        if self.ATTM_SaturatedBarrens_WT_Y[i] > 0.0 : self.ATTM_SaturatedBarrens_WT_Y_age[i,0] = 1.
        if self.ATTM_SaturatedBarrens_WT_M[i] > 0.0 : self.ATTM_SaturatedBarrens_WT_M_age[i,0] = 1.
        if self.ATTM_SaturatedBarrens_WT_O[i] > 0.0 : self.ATTM_SaturatedBarrens_WT_O_age[i,0] = 1.
        if self.ATTM_Shrubs_WT_O[i] > 0.0 : self.ATTM_Shrubs_WT_O_age[i,0] = 1.
        if self.ATTM_Urban_WT[i] > 0.0 : self.ATTM_Urban_WT_age[i,0] = 1.
        if self.ATTM_LargeLakes_WT_Y[i] > 0.0 : self.ATTM_LargeLakes_WT_Y_age[i,0] = 1.
        if self.ATTM_LargeLakes_WT_M[i] > 0.0 : self.ATTM_LargeLakes_WT_M_age[i,0] = 1.
        if self.ATTM_LargeLakes_WT_O[i] > 0.0 : self.ATTM_LargeLakes_WT_O_age[i,0] = 1.
        if self.ATTM_MediumLakes_WT_Y[i] > 0.0 : self.ATTM_MediumLakes_WT_Y_age[i,0] = 1.
        if self.ATTM_MediumLakes_WT_M[i] > 0.0 : self.ATTM_MediumLakes_WT_M_age[i,0] = 1.
        if self.ATTM_MediumLakes_WT_O[i] > 0.0 : self.ATTM_MediumLakes_WT_O_age[i,0] = 1.
        if self.ATTM_SmallLakes_WT_Y[i] > 0.0 : self.ATTM_SmallLakes_WT_Y_age[i,0] = 1.
        if self.ATTM_SmallLakes_WT_M[i] > 0.0 : self.ATTM_SmallLakes_WT_M_age[i,0] = 1.
        if self.ATTM_SmallLakes_WT_O[i] > 0.0 : self.ATTM_SmallLakes_WT_O_age[i,0] = 1.
        if self.ATTM_Ponds_WT_Y[i] > 0.0 : self.ATTM_Ponds_WT_Y_age[i,0] = 1.
        if self.ATTM_Ponds_WT_M[i] > 0.0 : self.ATTM_Ponds_WT_M_age[i,0] = 1.
        if self.ATTM_Ponds_WT_O[i] > 0.0 : self.ATTM_Ponds_WT_O_age[i,0] = 1.
        if self.ATTM_Rivers_WT_Y[i] > 0.0 : self.ATTM_Rivers_WT_Y_age[i,0] = 1.
        if self.ATTM_Rivers_WT_M[i] > 0.0 : self.ATTM_Rivers_WT_M_age[i,0] = 1.
        if self.ATTM_Rivers_WT_O[i] > 0.0 : self.ATTM_Rivers_WT_O_age[i,0] = 1.
#        if self.ATTM_Wet_NPG[i] > 0.0 : self.Wet_NPG_age[i,0] = 1.
#        if self.ATTM_Wet_LCP[i] > 0.0 : self.Wet_LCP_age[i,0] = 1.
#        if self.ATTM_Wet_CLC[i] > 0.0 : self.Wet_CLC_age[i,0] = 1.
#        if self.ATTM_Wet_FCP[i] > 0.0 : self.Wet_FCP_age[i,0] = 1.
#        if self.ATTM_Wet_HCP[i] > 0.0 : self.Wet_HCP_age[i,0] = 1.
#        if self.ATTM_Gra_NPG[i] > 0.0 : self.Gra_NPG_age[i,0] = 1.
#        if self.ATTM_Gra_LCP[i] > 0.0 : self.Gra_LCP_age[i,0] = 1.
#        if self.ATTM_Gra_FCP[i] > 0.0 : self.Gra_FCP_age[i,0] = 1.
#        if self.ATTM_Gra_HCP[i] > 0.0 : self.Gra_HCP_age[i,0] = 1.
#        if self.ATTM_Shr_NPG[i] > 0.0 : self.Shr_NPG_age[i,0] = 1.
#        if self.ATTM_Shr_LCP[i] > 0.0 : self.Shr_LCP_age[i,0] = 1.
#        if self.ATTM_Shr_FCP[i] > 0.0 : self.Shr_FCP_age[i,0] = 1.
#        if self.ATTM_Shr_HCP[i] > 0.0 : self.Shr_HCP_age[i,0] = 1.
#        if self.ATTM_Lakes[i]   > 0.0 : self.Lakes_age[i,0]   = 1.
#        if self.ATTM_Ponds[i]   > 0.0 : self.Ponds_age[i,0]   = 1.
    
    if self.initialize['Initial_Cohort_Age_Figure'].lower() == 'yes':
        CLC_WT_Y_age = np.reshape(self.ATTM_CLC_WT_Y_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        CLC_WT_M_age = np.reshape(self.ATTM_CLC_WT_M_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        CLC_WT_O_age = np.reshape(self.ATTM_CLC_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        CoastalWaters_WT_O_age = np.reshape(self.ATTM_CoastalWaters_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        DrainedSlope_WT_Y_age = np.reshape(self.ATTM_DrainedSlope_WT_Y_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        DrainedSlope_WT_M_age = np.reshape(self.ATTM_DrainedSlope_WT_M_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        DrainedSlope_WT_O_age = np.reshape(self.ATTM_DrainedSlope_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        FCP_WT_Y_age = np.reshape(self.ATTM_FCP_WT_Y_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        FCP_WT_M_age = np.reshape(self.ATTM_FCP_WT_M_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        FCP_WT_O_age = np.reshape(self.ATTM_FCP_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        HCP_WT_Y_age = np.reshape(self.ATTM_HCP_WT_Y_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        HCP_WT_M_age = np.reshape(self.ATTM_HCP_WT_M_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        HCP_WT_O_age = np.reshape(self.ATTM_HCP_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        LCP_WT_Y_age = np.reshape(self.ATTM_LCP_WT_Y_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        LCP_WT_M_age = np.reshape(self.ATTM_LCP_WT_M_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        LCP_WT_O_age = np.reshape(self.ATTM_LCP_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Meadow_WT_Y_age = np.reshape(self.ATTM_Meadow_WT_Y_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Meadow_WT_M_age = np.reshape(self.ATTM_Meadow_WT_M_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Meadow_WT_O_age = np.reshape(self.ATTM_Meadow_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        NoData_WT_O_age = np.reshape(self.ATTM_NoData_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        SandDunes_WT_Y_age = np.reshape(self.ATTM_SandDunes_WT_Y_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        SandDunes_WT_M_age = np.reshape(self.ATTM_SandDunes_WT_M_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        SandDunes_WT_O_age = np.reshape(self.ATTM_SandDunes_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        SaturatedBarrens_WT_Y_age = np.reshape(self.ATTM_SaturatedBarrens_WT_Y_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        SaturatedBarrens_WT_M_age = np.reshape(self.ATTM_SaturatedBarrens_WT_M_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        SaturatedBarrens_WT_O_age = np.reshape(self.ATTM_SaturatedBarrens_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Shrubs_WT_O_age = np.reshape(self.ATTM_Shrubs_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Urban_WT_age = np.reshape(self.ATTM_Urban_WT_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        LargeLakes_WT_Y_age = np.reshape(self.ATTM_LargeLakes_WT_Y_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        LargeLakes_WT_M_age = np.reshape(self.ATTM_LargeLakes_WT_M_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        LargeLakes_WT_O_age = np.reshape(self.ATTM_LargeLakes_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        MediumLakes_WT_Y_age = np.reshape(self.ATTM_MediumLakes_WT_Y_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        MediumLakes_WT_M_age = np.reshape(self.ATTM_MediumLakes_WT_M_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        MediumLakes_WT_O_age = np.reshape(self.ATTM_MediumLakes_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        SmallLakes_WT_Y_age = np.reshape(self.ATTM_SmallLakes_WT_Y_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        SmallLakes_WT_M_age = np.reshape(self.ATTM_SmallLakes_WT_M_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        SmallLakes_WT_O_age = np.reshape(self.ATTM_SmallLakes_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Ponds_WT_Y_age = np.reshape(self.ATTM_Ponds_WT_Y_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Ponds_WT_M_age = np.reshape(self.ATTM_Ponds_WT_M_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Ponds_WT_O_age = np.reshape(self.ATTM_Ponds_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Rivers_WT_Y_age = np.reshape(self.ATTM_Rivers_WT_Y_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Rivers_WT_M_age = np.reshape(self.ATTM_Rivers_WT_M_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Rivers_WT_O_age = np.reshape(self.ATTM_Rivers_WT_O_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        # ----------------------------------------------------------------------------------
#        Wet_NPG_age = np.reshape(self.Wet_NPG_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
#        Wet_LCP_age = np.reshape(self.Wet_LCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
#        Wet_CLC_age = np.reshape(self.Wet_CLC_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
#        Wet_FCP_age = np.reshape(self.Wet_FCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
#        Wet_HCP_age = np.reshape(self.Wet_HCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        # ----------------------------------------------------------------------------------
#        Gra_NPG_age = np.reshape(self.Gra_NPG_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
#        Gra_LCP_age = np.reshape(self.Gra_LCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
#        Gra_FCP_age = np.reshape(self.Gra_FCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
#        Gra_HCP_age = np.reshape(self.Gra_HCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        # ----------------------------------------------------------------------------------
#        Shr_NPG_age = np.reshape(self.Shr_NPG_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
#        Shr_LCP_age = np.reshape(self.Shr_LCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
#        Shr_FCP_age = np.reshape(self.Shr_FCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
#        Shr_HCP_age = np.reshape(self.Shr_HCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        # ----------------------------------------------------------------------------------
#        Lakes_age   = np.reshape(self.Lakes_age[:,0],   [self.ATTM_nrows, self.ATTM_ncols])
#        Ponds_age   = np.reshape(self.Ponds_age[:,0],   [self.ATTM_nrows, self.ATTM_ncols])
        # ----------------------------------------------------------------------------------
        # Move to Output Directory
        #----------------------------------------------------------------------------------
        if self.initialize['Initial_Cohort_Age_Figure'].lower() == 'yes' : \
          os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/')
        # ----------------------------------------------------------------------------------
        if self.initialize['CLC_WT_Y_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(CLC_WT_Y_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Coalescent Low Center Polygon Initial Age - Young Age')
            pl.savefig('./CLC_WT_Y/CLC_WT_Y_age.png', format = 'png')
            CLC_WT_Y_age.tofile('./CLC_WT_Y/CLC_WT_Y_age.bin')
            pl.close()
        if self.initialize['CLC_WT_M_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(CLC_WT_M_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Coalescent Low Center Polygon Initial Age - Medium Age')
            pl.savefig('./CLC_WT_M/CLC_WT_M_age.png', format = 'png')
            CLC_WT_M_age.tofile('./CLC_WT_M/CLC_WT_M_age.bin')
            pl.close()
        if self.initialize['CLC_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(CLC_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Coalescent Low Center Polygon Initial Age - Old Age')
            pl.savefig('./CLC_WT_O/CLC_WT_O_age.png', format = 'png')
            CLC_WT_O_age.tofile('./CLC_WT_O/CLC_WT_O_age.bin')
            pl.close()
        if self.initialize['CoastalWaters_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(CoastalWaters_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Coastal Waters Initial Age - Old Age')
            pl.savefig('./CoastalWaters_WT_O/CoastalWaters_WT_O_age.png', format = 'png')
            CLC_WT_O_age.tofile('./CoastalWaters_WT_O/CoastalWaters_WT_O_age.bin')
            pl.close()           
        if self.initialize['DrainedSlope_WT_Y_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(DrainedSlope_WT_Y_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Drained Slopes Initial Age - Young Age')
            pl.savefig('./DrainedSlope_WT_Y/DrainedSlope_WT_Y_age.png', format = 'png')
            DrainedSlope_WT_Y_age.tofile('./DrainedSlope_WT_Y/DrainedSlope_WT_Y_age.bin')
            pl.close()           
        if self.initialize['DrainedSlope_WT_M_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(DrainedSlope_WT_M_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Drained Slopes Initial Age - Medium Age')
            pl.savefig('./DrainedSlope_WT_M/DrainedSlope_WT_M_age.png', format = 'png')
            DrainedSlope_WT_M_age.tofile('./DrainedSlope_WT_M/DrainedSlope_WT_M_age.bin')
            pl.close() 
        if self.initialize['DrainedSlope_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(DrainedSlope_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Drained Slopes Initial Age - Old Age')
            pl.savefig('./DrainedSlope_WT_O/DrainedSlope_WT_O_age.png', format = 'png')
            DrainedSlope_WT_O_age.tofile('./DrainedSlope_WT_O/DrainedSlope_WT_O_age.bin')
            pl.close() 
        if self.initialize['FCP_WT_Y_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(FCP_WT_Y_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Flat Center Polygon Initial Age - Young Age')
            pl.savefig('./FCP_WT_Y/FCP_WT_Y_age.png', format = 'png')
            FCP_WT_Y_age.tofile('./FCP_WT_Y/FCP_WT_Y_age.bin')
            pl.close()           
        if self.initialize['FCP_WT_M_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(FCP_WT_M_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Flat Center Polygon Initial Age - Medium Age')
            pl.savefig('./FCP_WT_M/FCP_WT_M_age.png', format = 'png')
            FCP_WT_M_age.tofile('./FCP_WT_M/FCP_WT_M_age.bin')
            pl.close() 
        if self.initialize['FCP_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(FCP_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Flat Center Polygon Initial Age - Old Age')
            pl.savefig('./FCP_WT_O/FCP_WT_O_age.png', format = 'png')
            FCP_WT_O_age.tofile('./FCP_WT_O/FCP_WT_O_age.bin')
            pl.close() 
        if self.initialize['HCP_WT_Y_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(HCP_WT_Y_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra High Center Polygon Initial Age - Young Age')
            pl.savefig('./HCP_WT_Y/HCP_WT_Y_age.png', format = 'png')
            HCP_WT_Y_age.tofile('./HCP_WT_Y/HCP_WT_Y_age.bin')
            pl.close()           
        if self.initialize['HCP_WT_M_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(HCP_WT_M_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra High Center Polygon Initial Age - Medium Age')
            pl.savefig('./HCP_WT_M/HCP_WT_M_age.png', format = 'png')
            HCP_WT_M_age.tofile('./HCP_WT_M/HCP_WT_M_age.bin')
            pl.close() 
        if self.initialize['HCP_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(HCP_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra High Center Polygon Initial Age - Old Age')
            pl.savefig('./HCP_WT_O/HCP_WT_O_age.png', format = 'png')
            HCP_WT_O_age.tofile('./HCP_WT_O/HCP_WT_O_age.bin')
            pl.close() 
        if self.initialize['LCP_WT_Y_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(LCP_WT_Y_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Low Center Polygon Initial Age - Young Age')
            pl.savefig('./LCP_WT_Y/LCP_WT_Y_age.png', format = 'png')
            LCP_WT_Y_age.tofile('./LCP_WT_Y/LCP_WT_Y_age.bin')
            pl.close()           
        if self.initialize['LCP_WT_M_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(LCP_WT_M_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Low Center Polygon Initial Age - Medium Age')
            pl.savefig('./LCP_WT_M/LCP_WT_M_age.png', format = 'png')
            LCP_WT_M_age.tofile('./LCP_WT_M/LCP_WT_M_age.bin')
            pl.close() 
        if self.initialize['LCP_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(LCP_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Low Center Polygon Initial Age - Old Age')
            pl.savefig('./LCP_WT_O/LCP_WT_O_age.png', format = 'png')
            LCP_WT_O_age.tofile('./LCP_WT_O/LCP_WT_O_age.bin')
            pl.close() 
        if self.initialize['Meadow_WT_Y_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Meadow_WT_Y_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Meadow Initial Age - Young Age')
            pl.savefig('./Meadow_WT_Y/Meadow_WT_Y_age.png', format = 'png')
            Meadow_WT_Y_age.tofile('./Meadow_WT_Y/Meadow_WT_Y_age.bin')
            pl.close()           
        if self.initialize['Meadow_WT_M_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Meadow_WT_M_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Meadow Initial Age - Medium Age')
            pl.savefig('./Meadow_WT_M/Meadow_WT_M_age.png', format = 'png')
            Meadow_WT_M_age.tofile('./Meadow_WT_M/Meadow_WT_M_age.bin')
            pl.close() 
        if self.initialize['Meadow_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Meadow_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Meadow Initial Age - Old Age')
            pl.savefig('./Meadow_WT_O/Meadow_WT_O_age.png', format = 'png')
            Meadow_WT_O_age.tofile('./Meadow_WT_O/Meadow_WT_O_age.bin')
            pl.close() 
        if self.initialize['SandDunes_WT_Y_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(SandDunes_WT_Y_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Sand Dunes Initial Age - Young Age')
            pl.savefig('./SandDunes_WT_Y/SandDunes_WT_Y_age.png', format = 'png')
            SandDunes_WT_Y_age.tofile('./SandDunes_WT_Y/SandDunes_WT_Y_age.bin')
            pl.close()           
        if self.initialize['SandDunes_WT_M_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(SandDunes_WT_M_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Sand Dunes Initial Age - Medium Age')
            pl.savefig('./SandDunes_WT_M/SandDunes_WT_M_age.png', format = 'png')
            SandDunes_WT_M_age.tofile('./SandDunes_WT_M/SandDunes_WT_M_age.bin')
            pl.close() 
        if self.initialize['SandDunes_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(SandDunes_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Sand Dunes Initial Age - Old Age')
            pl.savefig('./SandDunes_WT_O/SandDunes_WT_O_age.png', format = 'png')
            SandDunes_WT_O_age.tofile('./SandDunes_WT_O/SandDunes_WT_O_age.bin')
            pl.close() 
        if self.initialize['SaturatedBarrens_WT_Y_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(SaturatedBarrens_WT_Y_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Saturated Barrens Initial Age - Young Age')
            pl.savefig('./SaturatedBarrens_WT_Y/SaturatedBarrens_WT_Y_age.png', format = 'png')
            SaturatedBarrens_WT_Y_age.tofile('./SaturatedBarrens_WT_Y/SaturatedBarrens_WT_Y_age.bin')
            pl.close()           
        if self.initialize['SaturatedBarrens_WT_M_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(SaturatedBarrens_WT_M_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Saturated Barrens Initial Age - Medium Age')
            pl.savefig('./SaturatedBarrens_WT_M/SaturatedBarrens_WT_M_age.png', format = 'png')
            SaturatedBarrens_WT_M_age.tofile('./SaturatedBarrens_WT_M/SaturatedBarrens_WT_M_age.bin')
            pl.close() 
        if self.initialize['SaturatedBarrens_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(SaturatedBarrens_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Saturated Barrens Initial Age - Old Age')
            pl.savefig('./SaturatedBarrens_WT_O/SaturatedBarrens_WT_O_age.png', format = 'png')
            SaturatedBarrens_WT_O_age.tofile('./SaturatedBarrens_WT_O/SaturatedBarrens_WT_O_age.bin')
            pl.close() 
        if self.initialize['Shrubs_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Shrubs_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Shrubs Initial Age - Old Age')
            pl.savefig('./Shrubs_WT_O/Shrubs_WT_O_age.png', format = 'png')
            Shrubs_WT_O_age.tofile('./Shrubs_WT_O/Shrubss_WT_O_age.bin')
            pl.close() 
        if self.initialize['Urban_WT_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Urban_WT_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Urban Initial Age')
            pl.savefig('./Urban_WT/Urban_WT_age.png', format = 'png')
            Urban_WT_age.tofile('./Urban_WT/Urban_WT_age.bin')
            pl.close()           
        if self.initialize['LargeLakes_WT_Y_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(LargeLakes_WT_Y_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Large Lakes Initial Age - Young Age')
            pl.savefig('./LargeLakes_WT_Y/LargeLakes_WT_Y_age.png', format = 'png')
            LargeLakes_WT_Y_age.tofile('./LargeLakes_WT_Y/LargeLakes_WT_Y_age.bin')
            pl.close()           
        if self.initialize['LargeLakes_WT_M_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(LargeLakes_WT_M_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Large Lakes Initial Age - Medium Age')
            pl.savefig('./LargeLakes_WT_M/LargeLakes_WT_M_age.png', format = 'png')
            LargeLakes_WT_M_age.tofile('./LargeLakes_WT_M/LargeLakes_WT_M_age.bin')
            pl.close() 
        if self.initialize['LargeLakes_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(LargeLakes_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Large Lakes Initial Age - Old Age')
            pl.savefig('./LargeLakes_WT_O/LargeLakes_WT_O_age.png', format = 'png')
            LargeLakes_WT_O_age.tofile('./LargeLakes_WT_O/LargeLakes_WT_O_age.bin')
            pl.close() 
        if self.initialize['MediumLakes_WT_Y_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(MediumLakes_WT_Y_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Medium Lakes Initial Age - Young Age')
            pl.savefig('./MediumLakes_WT_Y/MediumLakes_WT_Y_age.png', format = 'png')
            MediumLakes_WT_Y_age.tofile('./MediumLakes_WT_Y/MediumLakes_WT_Y_age.bin')
            pl.close()           
        if self.initialize['MediumLakes_WT_M_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(MediumLakes_WT_M_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Medium Lakes Initial Age - Medium Age')
            pl.savefig('./MediumLakes_WT_M/MediumLakes_WT_M_age.png', format = 'png')
            MediumLakes_WT_M_age.tofile('./MediumLakes_WT_M/MediumLakes_WT_M_age.bin')
            pl.close() 
        if self.initialize['MediumLakes_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(MediumLakes_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Medium Lakes Initial Age - Old Age')
            pl.savefig('./MediumLakes_WT_O/MediumLakes_WT_O_age.png', format = 'png')
            MediumLakes_WT_O_age.tofile('./MediumLakes_WT_O/MediumLakes_WT_O_age.bin')
            pl.close() 
        if self.initialize['SmallLakes_WT_Y_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(SmallLakes_WT_Y_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Small Lakes Initial Age - Young Age')
            pl.savefig('./SmallLakes_WT_Y/SmallLakes_WT_Y_age.png', format = 'png')
            SmallLakes_WT_Y_age.tofile('./SmallLakes_WT_Y/SmallLakes_WT_Y_age.bin')
            pl.close()           
        if self.initialize['SmallLakes_WT_M_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(SmallLakes_WT_M_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Small Lakes Initial Age - Medium Age')
            pl.savefig('./SmallLakes_WT_M/SmallLakes_WT_M_age.png', format = 'png')
            SmallLakes_WT_M_age.tofile('./SmallLakes_WT_M/SmallLakes_WT_M_age.bin')
            pl.close() 
        if self.initialize['SmallLakes_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(SmallLakes_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Small Lakes Initial Age - Old Age')
            pl.savefig('./SmallLakes_WT_O/SmallLakes_WT_O_age.png', format = 'png')
            SmallLakes_WT_O_age.tofile('./SmallLakes_WT_O/SmallLakes_WT_O_age.bin')
            pl.close() 
        if self.initialize['Ponds_WT_Y_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Ponds_WT_Y_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Ponds Initial Age - Young Age')
            pl.savefig('./Ponds_WT_Y/Ponds_WT_Y_age.png', format = 'png')
            Ponds_WT_Y_age.tofile('./Ponds_WT_Y/Ponds_WT_Y_age.bin')
            pl.close()           
        if self.initialize['Ponds_WT_M_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Ponds_WT_M_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Ponds Initial Age - Medium Age')
            pl.savefig('./Ponds_WT_M/Ponds_WT_M_age.png', format = 'png')
            Ponds_WT_M_age.tofile('./Ponds_WT_M/Ponds_WT_M_age.bin')
            pl.close() 
        if self.initialize['Ponds_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Ponds_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Ponds Initial Age - Old Age')
            pl.savefig('./Ponds_WT_O/Ponds_WT_O_age.png', format = 'png')
            Ponds_WT_O_age.tofile('./Ponds_WT_O/Ponds_WT_O_age.bin')
            pl.close() 
        if self.initialize['Rivers_WT_Y_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Rivers_WT_Y_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Rivers Initial Age - Young Age')
            pl.savefig('./Rivers_WT_Y/Riers_WT_Y_age.png', format = 'png')
            Rivers_WT_Y_age.tofile('./Rivers_WT_Y/Rivers_WT_Y_age.bin')
            pl.close()           
        if self.initialize['Rivers_WT_M_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Rivers_WT_M_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Rivers Initial Age - Medium Age')
            pl.savefig('./Rivers_WT_M/Rivers_WT_M_age.png', format = 'png')
            Rivers_WT_M_age.tofile('./Rivers_WT_M/Rivers_WT_M_age.bin')
            pl.close() 
        if self.initialize['Rivers_WT_O_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Rivers_WT_O_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Rivers Initial Age - Old Age')
            pl.savefig('./Rivers_WT_O/Rivers_WT_O_age.png', format = 'png')
            Rivers_WT_O_age.tofile('./Rivers_WT_O/Rivers_WT_O_age.bin')
            pl.close() 
              
         
        if self.initialize['WetNPG_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Wet_NPG_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Non-polygonal Ground Age')
            pl.savefig('./Wet_NPG/Wet_NPG_age.png', format = 'png')
            self.Wet_NPG_age.tofile('./Wet_NPG/Wet_NPG_Age.bin')
            pl.close()
        # ----------------------------------------------------------------------------------
        if self.initialize['WetLCP_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Wet_LCP_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Low Center Polygon Age')
            pl.savefig('./Wet_LCP/Wet_LCP_age.png', format = 'png')
            self.Wet_LCP_age.tofile('./Wet_LCP/Wet_LCP_age.bin')
            pl.close()
        # ----------------------------------------------------------------------------------
        if self.initialize['WetCLC_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Wet_CLC_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Coalescent Low Center Polygon Age')
            pl.savefig('./Wet_CLC/Wet_CLC_age.png', format = 'png')
            self.Wet_CLC_age.tofile('./Wet_CLC/Wet_CLC_age.bin')
            pl.close()
        # ----------------------------------------------------------------------------------
        if self.initialize['WetFCP_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Wet_FCP_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland Flat Center Polygon Age')
            pl.savefig('./Wet_FCP/Wet_FCP_age.png', format = 'png')
            self.Wet_FCP_age.tofile('./Wet_FCP/Wet_FCP_age.bin')
            pl.close()
        # ----------------------------------------------------------------------------------
        if self.initialize['WetHCP_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Wet_HCP_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Wetland High Center Polygon Age')
            pl.savefig('./Wet_HCP/Wet_HCP_age.png', format = 'png')
            self.Wet_HCP_age.tofile('./Wet_HCP/Wet_HCP_age.bin')
            pl.close()
        ## # ----------------------------------------------------------------------------------
        ## fig = pl.figure()
        ## pl.imshow(Gra_NPG_age, interpolation='nearest', cmap='bone')
        ## pl.colorbar( extend = 'max', shrink = 0.92)
        ## pl.title('Graminoid Non-polygonal Ground Age')
        ## if FIGURE == 'TRUE':
        ##     pl.savefig('Gra_NPG_age.png', format = 'png')
        ## if PLOT == 'TRUE':
        ##     pl.show()
        ## # ----------------------------------------------------------------------------------
        ## fig = pl.figure()
        ## pl.imshow(Gra_LCP_age, interpolation='nearest', cmap='bone')
        ## pl.colorbar( extend = 'max', shrink = 0.92)
        ## pl.title('Graminoid Low Center Polygon Age')
        ## if FIGURE == 'TRUE':
        ##     pl.savefig('Gra_LCP_age.png', format = 'png')
        ## if PLOT == 'TRUE':
        ##     pl.show()
        ## # ----------------------------------------------------------------------------------
        ## fig = pl.figure()
        ## pl.imshow(Gra_FCP_age, interpolation='nearest', cmap='bone')
        ## pl.colorbar( extend = 'max', shrink = 0.92)
        ## pl.title('Graminoid Flat Center Polygon Age')
        ## if FIGURE == 'TRUE':
        ##     pl.savefig('Gra_FCP_age.png', format = 'png')
        ## if PLOT == 'TRUE':
        ##     pl.show()
        ## # ----------------------------------------------------------------------------------
        ## fig = pl.figure()
        ## pl.imshow(Gra_HCP_age, interpolation='nearest', cmap='bone')
        ## pl.colorbar( extend = 'max', shrink = 0.92)
        ## pl.title('Graminoid High Center Polygon Age')
        ## if FIGURE == 'TRUE':
        ##     pl.savefig('Gra_HCP_age.png', format = 'png')
        ## if PLOT == 'TRUE':
        ##     pl.show()
        ## # ----------------------------------------------------------------------------------
        ## fig = pl.figure()
        ## pl.imshow(Shr_NPG_age, interpolation='nearest', cmap='bone')
        ## pl.colorbar( extend = 'max', shrink = 0.92)
        ## pl.title('Shrub Non-polygonal Ground Age')
        ## if FIGURE == 'TRUE':
        ##     pl.savefig('Shr_NPG_age.png', format = 'png')
        ## if PLOT == 'TRUE':
        ##     pl.show()
        ## # ----------------------------------------------------------------------------------
        ## fig = pl.figure()
        ## pl.imshow(Shr_LCP_age, interpolation='nearest', cmap='bone')
        ## pl.colorbar( extend = 'max', shrink = 0.92)
        ## pl.title('Shrub Low Center Polygon Age')
        ## if FIGURE == 'TRUE':
        ##     pl.savefig('Shr_LCP_age.png', format = 'png')
        ## if PLOT == 'TRUE':
        ##     pl.show()
        ## # ----------------------------------------------------------------------------------
        ## fig = pl.figure()
        ## pl.imshow(Shr_FCP_age, interpolation='nearest', cmap='bone')
        ## pl.colorbar( extend = 'max', shrink = 0.92)
        ## pl.title('Shrub Flat Center Polygon Age')
        ## if FIGURE == 'TRUE':
        ##     pl.savefig('Shr_FCP_age.png', format = 'png')
        ## if PLOT == 'TRUE':
        ##     pl.show()
        ## # ----------------------------------------------------------------------------------
        ## fig = pl.figure()
        ## pl.imshow(Shr_HCP_age, interpolation='nearest', cmap='bone')
        ## pl.colorbar( extend = 'max', shrink = 0.92)
        ## pl.title('Shrub High Center Polygon Age')
        ## if FIGURE == 'TRUE':
        ##     pl.savefig('Shr_HCP_age.png', format = 'png')
        ## if PLOT == 'TRUE':
        ##     pl.show()
        # ----------------------------------------------------------------------------------
        if self.initialize['Lakes_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Lakes_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Lakes Age')
            pl.savefig('./Lakes/Lakes_age.png', format = 'png')
            self.Lakes_age.tofile('./Lakes/Lakes_age.bin')
            pl.close()
        # ----------------------------------------------------------------------------------
        if self.initialize['Ponds_Age'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(Ponds_age, interpolation='nearest', cmap='bone')
            pl.colorbar( extend = 'max', shrink = 0.92)
            pl.title('Ponds Age')
            pl.savefig('./Ponds/Ponds_age.png', format = 'png')
            self.Ponds_age.tofile('./Ponds/Ponds_age.bin')

        
        os.chdir(self.control['Run_dir'])
        # ----------------------------------------------------------------------------------

    print '    done. \n  '
