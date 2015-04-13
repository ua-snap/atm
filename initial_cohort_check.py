import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def initial_cohort_check(self):
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
            if self.ATTM_Wet_NPG[i] > 0. : self.ATTM_Wet_NPG[i] = self.ATTM_Wet_NPG[i]*adjustment
            if self.ATTM_Wet_LCP[i] > 0. : self.ATTM_Wet_LCP[i] = self.ATTM_Wet_LCP[i]*adjustment
            if self.ATTM_Wet_CLC[i] > 0. : self.ATTM_Wet_CLC[i] = self.ATTM_Wet_CLC[i]*adjustment
            if self.ATTM_Wet_FCP[i] > 0. : self.ATTM_Wet_FCP[i] = self.ATTM_Wet_FCP[i]*adjustment
            if self.ATTM_Wet_HCP[i] > 0. : self.ATTM_Wet_HCP[i] = self.ATTM_Wet_HCP[i]*adjustment
            if self.ATTM_Gra_NPG[i] > 0. : self.ATTM_Gra_NPG[i] = self.ATTM_Gra_NPG[i]*adjustment
            if self.ATTM_Gra_LCP[i] > 0. : self.ATTM_Gra_LCP[i] = self.ATTM_Gra_LCP[i]*adjustment
            if self.ATTM_Gra_FCP[i] > 0. : self.ATTM_Gra_FCP[i] = self.ATTM_Gra_FCP[i]*adjustment
            if self.ATTM_Gra_HCP[i] > 0. : self.ATTM_Gra_HCP[i] = self.ATTM_Gra_HCP[i]*adjustment
            if self.ATTM_Shr_NPG[i] > 0. : self.ATTM_Shr_NPG[i] = self.ATTM_Shr_NPG[i]*adjustment
            if self.ATTM_Shr_LCP[i] > 0. : self.ATTM_Shr_LCP[i] = self.ATTM_Shr_LCP[i]*adjustment
            if self.ATTM_Shr_FCP[i] > 0. : self.ATTM_Shr_FCP[i] = self.ATTM_Shr_FCP[i]*adjustment
            if self.ATTM_Shr_HCP[i] > 0. : self.ATTM_Shr_HCP[i] = self.ATTM_Shr_HCP[i]*adjustment
            if self.ATTM_Urban[i]   > 0. : self.ATTM_Urban[i]   = self.ATTM_Urban[i]*adjustment
            if self.ATTM_Rivers[i]  > 0. : self.ATTM_Rivers[i]  = self.ATTM_Rivers[i]*adjustment
            if self.ATTM_Lakes[i]   > 0. : self.ATTM_Lakes[i]   = self.ATTM_Lakes[i]*adjustment
            if self.ATTM_Ponds[i]   > 0. : self.ATTM_Ponds[i]   = self.ATTM_Ponds[i]*adjustment

    # Convert all land surface cohorts into fractional area of element
    self.ATTM_Wet_NPG = np.round((self.ATTM_Wet_NPG) / cohorts_required, decimals = 6)
    self.ATTM_Wet_LCP = np.round((self.ATTM_Wet_LCP) / cohorts_required, decimals = 6)
    self.ATTM_Wet_CLC = np.round((self.ATTM_Wet_CLC) / cohorts_required, decimals = 6)
    self.ATTM_Wet_FCP = np.round((self.ATTM_Wet_FCP) / cohorts_required, decimals = 6)
    self.ATTM_Wet_HCP = np.round((self.ATTM_Wet_HCP) / cohorts_required, decimals = 6)
    self.ATTM_Gra_NPG = np.round((self.ATTM_Gra_NPG) / cohorts_required, decimals = 6)
    self.ATTM_Gra_LCP = np.round((self.ATTM_Gra_LCP) / cohorts_required, decimals = 6)
    self.ATTM_Gra_FCP = np.round((self.ATTM_Gra_FCP) / cohorts_required, decimals = 6)
    self.ATTM_Gra_HCP = np.round((self.ATTM_Gra_HCP) / cohorts_required, decimals = 6)
    self.ATTM_Shr_NPG = np.round((self.ATTM_Shr_NPG) / cohorts_required, decimals = 6)
    self.ATTM_Shr_LCP = np.round((self.ATTM_Shr_LCP) / cohorts_required, decimals = 6)
    self.ATTM_Shr_FCP = np.round((self.ATTM_Shr_FCP) / cohorts_required, decimals = 6)
    self.ATTM_Shr_HCP = np.round((self.ATTM_Shr_HCP) / cohorts_required, decimals = 6)
    self.ATTM_Urban   = np.round((self.ATTM_Urban)   / cohorts_required, decimals = 6)
    self.ATTM_Rivers  = np.round((self.ATTM_Rivers)  / cohorts_required, decimals = 6)
    self.ATTM_Lakes   = np.round((self.ATTM_Lakes)   / cohorts_required, decimals = 6)
    self.ATTM_Ponds   = np.round((self.ATTM_Ponds)   / cohorts_required, decimals = 6)

    self.ATTM_Total_Fractional_Area = np.round( \
                           self.ATTM_Wet_NPG + self.ATTM_Wet_LCP + \
                           self.ATTM_Wet_CLC + self.ATTM_Wet_FCP + \
                           self.ATTM_Wet_HCP + self.ATTM_Gra_NPG + \
                           self.ATTM_Gra_LCP + self.ATTM_Gra_FCP + \
                           self.ATTM_Gra_HCP + self.ATTM_Shr_NPG + \
                           self.ATTM_Shr_LCP + self.ATTM_Shr_FCP + \
                           self.ATTM_Shr_HCP + self.ATTM_Urban   + \
                           self.ATTM_Rivers  + self.ATTM_Lakes   + \
                           self.ATTM_Ponds, decimals = 6)

    for i in range(self.ATTM_nrows * self.ATTM_ncols):
        if np.round(self.ATTM_Total_Fractional_Area[i], decimals = 4) > 1.0:
            print 'There is a mass balance problem in element: ', i
            print 'The total fractional area of all cohorts is greater than 1.0'
            print '[in initial_cohort_check]'
            print ' '
            print 'Wetland Non Polygonal Ground: ',          self.ATTM_Wet_NPG[i]
            print 'Wetland Low Center Polygon: ',            self.ATTM_Wet_LCP[i]
            print 'Wetland Coalescent Low Center Polygon: ', self.ATTM_Wet_CLC[i]
            print 'Wetland Flat Center Polygon: ',           self.ATTM_Wet_FCP[i]
            print 'Wetland High Center Polygon: ',           self.ATTM_Wet_HCP[i]
            print 'Rivers: ' ,                               self.ATTM_Rivers[i]
            print 'Lakes: ',                                 self.ATTM_Lakes[i]
            print 'Ponds: ',                                 self.ATTM_Ponds[i]
            print 'Urban: ',                                 self.ATTM_Urban[i]
            print 'Total Fractions: ',                       self.ATTM_Total_Fractional_Area[i]
            exit()
        if np.round(self.ATTM_Total_Fractional_Area[i], decimals = 4) < 0.0:
            print 'There is a mass balance problem in element: ', i
            print 'The total fractional area of all cohorts is less than 0.0.'
            print '[in initial_cohort_check]'
            print ' '
            print 'Wetland Non Polygonal Ground: ',          self.ATTM_Wet_NPG[i]
            print 'Wetland Low Center Polygon: ',            self.ATTM_Wet_LCP[i]
            print 'Wetland Coalescent Low Center Polygon: ', self.ATTM_Wet_CLC[i]
            print 'Wetland Flat Center Polygon: ',           self.ATTM_Wet_FCP[i]
            print 'Wetland High Center Polygon: ',           self.ATTM_Wet_HCP[i]
            print 'Rivers: ' ,                               self.ATTM_Rivers[i]
            print 'Lakes: ',                                 self.ATTM_Lakes[i]
            print 'Ponds: ',                                 self.ATTM_Ponds[i]
            print 'Urban: ',                                 self.ATTM_Urban[i]
            print 'Total Fractions: ',                       self.ATTM_Total_Fractional_Area[i]
            exit()
    # Statement of what has been done for debugging
    print '      done.'
    print ' '

    if self.initialize['Normalized_Cohort_Distribution_Figure'].lower() == 'yes':    
        cohort_check = np.reshape(self.ATTM_Total_Fractional_Area,  [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # Files for plotting & reference #
        ATTM_Wet_NPG_plot =  np.reshape(self.ATTM_Wet_NPG,      [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Wet_LCP_plot =  np.reshape(self.ATTM_Wet_LCP,      [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Wet_CLC_plot =  np.reshape(self.ATTM_Wet_CLC,      [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Wet_FCP_plot =  np.reshape(self.ATTM_Wet_FCP,      [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Wet_HCP_plot =  np.reshape(self.ATTM_Wet_FCP,      [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Rivers_plot  =  np.reshape(self.ATTM_Rivers,       [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Lakes_plot   =  np.reshape(self.ATTM_Lakes,        [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Ponds_plot   =  np.reshape(self.ATTM_Ponds,        [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Urban_plot   =  np.reshape(self.ATTM_Urban,        [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Total_plot   =  np.reshape(self.ATTM_Total_Fractional_Area,\
                                        [int(self.ATTM_nrows), int(self.ATTM_ncols)])

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
        # -----------------------------------------------------------------------------
        # Return to Run Directory
        #----------------------------------
        os.chdir(self.control['Run_dir'])
