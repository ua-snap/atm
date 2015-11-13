import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def barrow_initial_cohort_population(self):
    # ----------------------------------------------------------------------------
    # Note -- in this Barrow example:
    # ATTM Model domain is 1000m by 1000m (self.Y_resolution, self.X_resolution)
    # Geotiff files are 25m by 25m (self.y_res, self.x_res)
    # Therefore, the # of rows/columns to to read are 40x40 (1000/25, 1000/25)
    # ----------------------------------------------------------------------------
    #def count_cohorts(a, b):
    #    b = a > 0
    #    return len(a[b])
    #-----------------------------------------------------------------------------

    # ------------------------------------------------------------------------------
    # Define the ATTM Land Surface Cohorts
    #      NOTE: Assuming the entire Barrow test site is considered Wetland Tundra
    # ------------------------------------------------------------------------------
    count = 0
    for i in range(0, int(self.nrows), int(float(self.Y_resolution)/(self.y_res))):
        for j in range(0, int(self.ncols), int(float(self.X_resolution)/(self.x_res))):
            # ==================================
            # Wetland Tundra Non-Polygonal Ground
            # ==================================
            A = self.NPG[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                         j:j+int(float(self.X_resolution)/(self.x_res))-1]

            b = A > 0
            self.ATTM_Wet_NPG[count] = len(A[b])
            # ==================================
            # Wetland Tundra Low Center Polygon
            # ==================================
            A = self.LCP[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                         j:j+int(float(self.X_resolution)/(self.x_res))-1]

            b = A > 0
            self.ATTM_Wet_LCP[count] = len(A[b])
            # =============================================
            # Wetland Tundra Coalescent Low Center Polygon
            # =============================================
            A = self.CLC[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                         j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Wet_CLC[count] = len(A[b])
            # ===================================
            # Wetland Tundra Flat Center Polygon
            # ===================================
            A = self.FCP[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                         j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Wet_FCP[count] = len(A[b])
            # ===================================
            # Wetland Tundra High Center Polygon
            # ===================================
            A = self.HCP[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                         j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Wet_HCP[count] = len(A[b])
            # ===================================
            # Rivers
            # ===================================
            A = self.Rivers[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                            j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Rivers[count] = len(A[b])
            # ===================================
            # Lakes
            # ===================================
            A = self.Lakes[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                           j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Lakes[count] = len(A[b])
            # ===================================
            # Ponds
            # ===================================
            A = self.Ponds[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                           j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Ponds[count] = len(A[b])
            # ===================================
            # Urban
            # ===================================
            A = self.Urban[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                           j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Urban[count] = len(A[b])
            # ===================================
            # Total
            # ===================================
            self.ATTM_Total = self.ATTM_Wet_NPG + self.ATTM_Wet_LCP + \
                              self.ATTM_Wet_CLC + self.ATTM_Wet_FCP + \
                              self.ATTM_Wet_HCP + self.ATTM_Gra_NPG + \
                              self.ATTM_Gra_LCP + self.ATTM_Gra_FCP + \
                              self.ATTM_Gra_HCP + self.ATTM_Shr_NPG + \
                              self.ATTM_Shr_LCP + self.ATTM_Shr_FCP + \
                              self.ATTM_Shr_HCP + self.ATTM_Rivers  + \
                              self.ATTM_Lakes   + self.ATTM_Ponds   + \
                              self.ATTM_Urban
            # ===================================
            # Move to the next element
            # ===================================
            count = count +1

#    if PLOT == 'TRUE' or FIGURE == 'TRUE':
    if self.initialize['Initial_Cohort_Distribution_Figure'].lower() == 'yes':
    
        # Files for plotting & reference #
        ATTM_Wet_NPG_plot =  np.reshape(self.ATTM_Wet_NPG, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Wet_LCP_plot =  np.reshape(self.ATTM_Wet_LCP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Wet_CLC_plot =  np.reshape(self.ATTM_Wet_CLC, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Wet_FCP_plot =  np.reshape(self.ATTM_Wet_FCP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Wet_HCP_plot =  np.reshape(self.ATTM_Wet_HCP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Rivers_plot  =  np.reshape(self.ATTM_Rivers,  [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Lakes_plot   =  np.reshape(self.ATTM_Lakes,   [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Ponds_plot   =  np.reshape(self.ATTM_Ponds,   [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Urban_plot   =  np.reshape(self.ATTM_Urban,   [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Total_plot   =  np.reshape(self.ATTM_Total,   [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # Move to output directory #
        os.chdir(self.control['Run_dir']+self.Output_directory)
        
        #-----------------------------------------------------------------------
        # Create Figures, Plots, and Binary files for each cohort
        # ----------------------------------------------------------------------
        if self.initialize['WetNPG_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_NPG_plot, interpolation = 'nearest', cmap= 'spectral', vmin=0.0, vmax=1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Non-Polygonal Ground Initial Cohort Distribution')
            pl.savefig('./Wet_NPG/Initial_Wet_NPG.png', format = 'png')
            self.ATTM_Wet_NPG.tofile('./Wet_NPG/Wet_NPG_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['WetLCP_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_LCP_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Low Center Polygon Initial Cohort Distribution')
            pl.savefig('./Wet_LCP/Initial_Wet_LCP.png', format = 'png')
            self.ATTM_Wet_LCP.tofile('./Wet_LCP/Wet_LCP_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['WetCLC_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_CLC_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Coalescent Low Center Polygon Initial Cohort Distribution')
            pl.savefig('./Wet_CLC/Initial_Wet_CLC.png', format = 'png')
            self.ATTM_Wet_CLC.tofile('./Wet_CLC/Wet_CLC_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['WetFCP_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_FCP_plot, interpolation = 'nearest', cmap= 'spectral', vmin= 1.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Flat Center Polygon Initial Cohort Distribution')
            pl.savefig('./Wet_FCP/Initial_Wet_FCP.png', format = 'png')
            self.ATTM_Wet_FCP.tofile('./Wet_FCP/Wet_FCP_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['WetHCP_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_HCP_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland High Center Polygon Initial Cohort Distribution')
            pl.savefig('./Wet_HCP/Initial_Wet_HCP.png', format = 'png')
            self.ATTM_Wet_HCP.tofile('./Wet_HCP/Wet_HCP_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Ponds_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Ponds_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Ponds Initial Cohort Distribution')
            pl.savefig('./Ponds/Initial_Ponds.png', format = 'png')
            self.ATTM_Ponds.tofile('./Ponds/Ponds_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Lakes_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Lakes_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Lakes Initial Cohort Distribution')
            pl.savefig('./Lakes/Initial_Lakes.png', format = 'png')
            self.ATTM_Lakes.tofile('./Lakes/Lakes_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Rivers_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Rivers_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Rivers Initial Cohort Distribution')
            pl.savefig('./Other_Cohorts/Initial_Rivers.png', format = 'png')
            self.ATTM_Rivers.tofile('./Other_Cohorts/Rivers_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Urban_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Urban_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Urban Area Initial Cohort Distribution')
            pl.savefig('./Other_Cohorts/Initial_Urban.png', format = 'png')
            self.ATTM_Urban.tofile('./Other_Cohorts/Urban_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['All_Cohorts_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Total_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 0.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('All Cohorts Combined Distribution')
            pl.savefig('./All_Cohorts/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Total.tofile('./All_Cohorts/Total_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        # Return to Run Directory
        os.chdir(self.control['Run_dir'])

def tanana_initial_cohort_population(self):
    # ----------------------------------------------------------------------------
    # Note -- in this Barrow example:
    # ATTM Model domain is 1000m by 1000m (self.Y_resolution, self.X_resolution)
    # Geotiff files are 25m by 25m (self.y_res, self.x_res)
    # Therefore, the # of rows/columns to to read are 40x40 (1000/25, 1000/25)
    # ----------------------------------------------------------------------------
    #def count_cohorts(a, b):
    #    b = a > 0
    #    return len(a[b])
    #-----------------------------------------------------------------------------

    # ------------------------------------------------------------------------------
    # Define the ATTM Land Surface Cohorts
    #      NOTE: Assuming the entire Barrow test site is considered Wetland Tundra
    # ------------------------------------------------------------------------------
    count = 0
    for i in range(0, int(self.nrows), int(float(self.Y_resolution)/(self.y_res))):
        for j in range(0, int(self.ncols), int(float(self.X_resolution)/(self.x_res))):
            # ==================================
            # Tanana Flats - Old Bog
            # ==================================
            A = self.TF_OB[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                           j:j+int(float(self.X_resolution)/(self.x_res))-1]

            b = A > 0
            self.ATTM_TF_OB[count] = len(A[b])
            # ==================================
            # Tanana Flats - Young Bog
            # ==================================
            A = self.TF_YB[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                           j:j+int(float(self.X_resolution)/(self.x_res))-1]

            b = A > 0
            self.ATTM_TF_YB[count] = len(A[b])
            # =============================================
            # Tanana Flats - Old Fen
            # =============================================
            A = self.TF_YF[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                           j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_TF_YF[count] = len(A[b])
            # ===================================
            # Tanana Flats - Young Fen
            # ===================================
            A = self.TF_YF[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                           j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_TF_YF[count] = len(A[b])
            # ===================================
            # Tanana Flats - Coniferous Permafrost Plateau
            # ===================================
            A = self.TF_Con_PP[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                               j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_TF_Con_PP[count] = len(A[b])
            # ===================================
            # Tanana Flats - Deciduous Permafrost Plateau
            # ===================================
            A = self.TF_Dec_PP[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                               j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_TF_Dec_PP[count] = len(A[b])
            # ===================================
            # Tanana Flats - Thermokarst Lakes
            # ===================================
            A = self.TF_TL[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                           j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_TF_TL[count] = len(A[b])
            # ===================================
            # Total
            # ===================================
            self.ATTM_Total = self.ATTM_TF_OB + self.ATTM_TF_YB + \
                              self.ATTM_TF_OF + self.ATTM_TF_YF + \
                              self.ATTM_TF_Con_PP + self.ATTM_TF_Dec_PP + \
                              self.ATTM_TF_TL
            # ===================================
            # Move to the next element
            # ===================================
            count = count +1

    if self.initialize['Initial_Cohort_Distribution_Figure'].lower() == 'yes':
    
        # Files for plotting & reference #
        ATTM_TF_OB_plot     =  np.reshape(self.ATTM_TF_OB, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_YB_plot     =  np.reshape(self.ATTM_TF_YB, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_OF_plot     =  np.reshape(self.ATTM_TF_OF, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_YF_plot     =  np.reshape(self.ATTM_TF_YF, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_Con_PP_plot =  np.reshape(self.ATTM_TF_Con_PP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_Dec_PP_plot =  np.reshape(self.ATTM_TF_Dec_PP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_TL_plot     =  np.reshape(self.ATTM_TF_TL, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Total_plot     =  np.reshape(self.ATTM_Total,   [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # Move to output directory #
        os.chdir(self.control['Run_dir']+self.Output_directory)
        
        #-----------------------------------------------------------------------
        # Create Figures, Plots, and Binary files for each cohort
        # ----------------------------------------------------------------------
        if self.initialize['TF_OB_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_OB_plot, interpolation = 'nearest', cmap= 'spectral', vmin=0.0, vmax=1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Tanana Flats - Old Bog Initial Cohort Distribution')
            pl.savefig('./TF_OB/Initial_TF_OB.png', format = 'png')
            self.ATTM_TF_OB.tofile('./TF_OB/TF_OB_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['TF_YB_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_YB_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Tanana Flats Young Bog Initial Cohort Distribution')
            pl.savefig('./TF_YB/Initial_TF_YB.png', format = 'png')
            self.ATTM_TF_YB.tofile('./TF_YB/TF_YB_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['TF_OF_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_OF_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Tanana Flats Old Fen Initial Cohort Distribution')
            pl.savefig('./TF_OF/Initial_TF_OF.png', format = 'png')
            self.ATTM_TF_OF.tofile('./TF_OF/TF_OF_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['TF_YF_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_YF_plot, interpolation = 'nearest', cmap= 'spectral', vmin= 1.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Tanana Flats Young Fen Initial Cohort Distribution')
            pl.savefig('./TF_YF/Initial_TF_YF.png', format = 'png')
            self.ATTM_TF_YF.tofile('./TF_YF/TF_YF_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['TF_Con_PP_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_Con_PP_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Tanana Flats Coniferous Permafrost Plateau Initial Cohort Distribution')
            pl.savefig('./TF_Con_PP/Initial_TF_Con_PP.png', format = 'png')
            self.ATTM_TF_Con_PP.tofile('./TF_Con_PP/TF_Con_PP_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['TF_Dec_PP_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_Dec_PP_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Tanana Flats Deciduous Permafrost Plateau Initial Cohort Distribution')
            pl.savefig('./TF_Dec_PP/Initial_TF_Con_PP.png', format = 'png')
            self.ATTM_TF_Dec_PP.tofile('./TF_Dec_PP/TF_Dec_PP_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------       
        if self.initialize['TF_TL_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_TL_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Tanana Flats Thermokarst Lake Initial Cohort Distribution')
            pl.savefig('./TF_TL/Initial_Ponds.png', format = 'png')
            self.ATTM_TF_TL.tofile('./TF_TL/TF_TL_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['TF_All_Cohorts_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Total_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 0.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('All Cohorts Combined Distribution')
            pl.savefig('./TF_All_Cohorts/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Total.tofile('./TF_All_Cohorts/Total_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        # Return to Run Directory
        os.chdir(self.control['Run_dir'])
