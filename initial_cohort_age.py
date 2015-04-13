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

    self.Wet_NPG_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Wet_LCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Wet_CLC_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Wet_FCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Wet_HCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])  

    self.Gra_NPG_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Gra_LCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Gra_FCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Gra_HCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])   

    self.Shr_NPG_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Shr_LCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Shr_FCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Shr_HCP_age = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])  

    self.Lakes_age   = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Ponds_age   = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])  

    for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
        if self.ATTM_Wet_NPG[i] > 0.0 : self.Wet_NPG_age[i,0] = 1.
        if self.ATTM_Wet_LCP[i] > 0.0 : self.Wet_LCP_age[i,0] = 1.
        if self.ATTM_Wet_CLC[i] > 0.0 : self.Wet_CLC_age[i,0] = 1.
        if self.ATTM_Wet_FCP[i] > 0.0 : self.Wet_FCP_age[i,0] = 1.
        if self.ATTM_Wet_HCP[i] > 0.0 : self.Wet_HCP_age[i,0] = 1.
        if self.ATTM_Gra_NPG[i] > 0.0 : self.Gra_NPG_age[i,0] = 1.
        if self.ATTM_Gra_LCP[i] > 0.0 : self.Gra_LCP_age[i,0] = 1.
        if self.ATTM_Gra_FCP[i] > 0.0 : self.Gra_FCP_age[i,0] = 1.
        if self.ATTM_Gra_HCP[i] > 0.0 : self.Gra_HCP_age[i,0] = 1.
        if self.ATTM_Shr_NPG[i] > 0.0 : self.Shr_NPG_age[i,0] = 1.
        if self.ATTM_Shr_LCP[i] > 0.0 : self.Shr_LCP_age[i,0] = 1.
        if self.ATTM_Shr_FCP[i] > 0.0 : self.Shr_FCP_age[i,0] = 1.
        if self.ATTM_Shr_HCP[i] > 0.0 : self.Shr_HCP_age[i,0] = 1.
        if self.ATTM_Lakes[i]   > 0.0 : self.Lakes_age[i,0]   = 1.
        if self.ATTM_Ponds[i]   > 0.0 : self.Ponds_age[i,0]   = 1.
    
    if self.initialize['Initial_Cohort_Age_Figure'].lower() == 'yes':

        # ----------------------------------------------------------------------------------
        Wet_NPG_age = np.reshape(self.Wet_NPG_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Wet_LCP_age = np.reshape(self.Wet_LCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Wet_CLC_age = np.reshape(self.Wet_CLC_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Wet_FCP_age = np.reshape(self.Wet_FCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Wet_HCP_age = np.reshape(self.Wet_HCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        # ----------------------------------------------------------------------------------
        Gra_NPG_age = np.reshape(self.Gra_NPG_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Gra_LCP_age = np.reshape(self.Gra_LCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Gra_FCP_age = np.reshape(self.Gra_FCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Gra_HCP_age = np.reshape(self.Gra_HCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        # ----------------------------------------------------------------------------------
        Shr_NPG_age = np.reshape(self.Shr_NPG_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Shr_LCP_age = np.reshape(self.Shr_LCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Shr_FCP_age = np.reshape(self.Shr_FCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        Shr_HCP_age = np.reshape(self.Shr_HCP_age[:,0], [self.ATTM_nrows, self.ATTM_ncols])
        # ----------------------------------------------------------------------------------
        Lakes_age   = np.reshape(self.Lakes_age[:,0],   [self.ATTM_nrows, self.ATTM_ncols])
        Ponds_age   = np.reshape(self.Ponds_age[:,0],   [self.ATTM_nrows, self.ATTM_ncols])
        # ----------------------------------------------------------------------------------
        # Move to Output Directory
        #----------------------------------------------------------------------------------
        os.chdir(self.control['Run_dir']+self.Output_directory)
        # ----------------------------------------------------------------------------------
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
