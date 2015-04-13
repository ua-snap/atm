import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def set_protective_layer(self):#, PLOT, FIGURE):
        """
        The purpose of this module is to set the protective layer depth for
        each cohort in each predisposed element.

        The protective layer is going to be set relative to the initial
        active layer depth.

        For Wetland and Graminoid Tundra, the protective layer factors are:
        Non-polygonal ground : 0.8
        Low center polygon : 1.0
        Coalescing Low center polygon : 1.0
        Flat center polygon : 1.25
        High center polygon : 1.50

        For Shrub tundra (assuming little thermokarst takes place) the protective
        layer factors are:
        Non-polygonal ground : 1.5
        Low Center Polygon : 1.7
        Flat Center Polygon : 1.9
        High Center Polygon : 2.1

        The Total Protective Layer = Protective Layer Factor * the Initial ALD
        For Lakes & Ponds, the Total Protective Layer = PLF * Lake/Pond depth
        """

        print '  Setting Protective Layer.'

        # --------------------------------------------------
        # Reading protective layer factors from input file
        # --------------------------------------------------
        ## protective_layer_factor = {}
        ## with open(self.protective_layer, 'r') as f:
        ##     for line in f:
        ##         (key, val) = line.split()
        ##         protective_layer_factor[(key)] = float(val)

        #---------------------------------------------
        # Set protective layer arrays for all cohorts
        #---------------------------------------------
        self.Wet_NPG_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.Wet_LCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.Wet_CLC_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.Wet_FCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.Wet_HCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.Gra_NPG_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.Gra_LCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.Gra_FCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.Gra_HCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.Shr_NPG_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.Shr_LCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.Shr_FCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.Shr_HCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.Lakes_PL    = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.Ponds_PL    = np.zeros(self.ATTM_nrows * self.ATTM_ncols)

        for i in range(self.ATTM_nrows * self.ATTM_ncols):
            self.Wet_NPG_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Wet_NPG_PLF']
            self.Wet_LCP_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Wet_LCP_PLF']
            self.Wet_CLC_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Wet_CLC_PLF']
            self.Wet_FCP_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Wet_FCP_PLF']
            self.Wet_HCP_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Wet_HCP_PLF']
            self.Gra_NPG_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Gra_NPG_PLF']
            self.Gra_LCP_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Gra_LCP_PLF']
            self.Gra_FCP_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Gra_FCP_PLF']
            self.Gra_HCP_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Gra_HCP_PLF']
            self.Shr_NPG_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Shr_NPG_PLF']
            self.Shr_LCP_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Shr_LCP_PLF']
            self.Shr_FCP_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Shr_FCP_PLF']
            self.Shr_HCP_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Shr_HCP_PLF']
            self.Lakes_PL[i]   = self.Lake_Depth[i] * \
              self.Terrestrial['Lakes_PLF']
            self.Ponds_PL[i]   = self.Pond_Depth[i] * \
              self.Terrestrial['Ponds_PLF']

        print '    done. \n  '

        # ######################################
        # Plotting and saving values if wanted
        # ######################################
        if self.Terrestrial['Protective_Layer_Factor_Output'].lower() == 'yes':

            # Move to Output directory
            os.chdir(self.control['Run_dir']+self.Output_directory)

            #--------------------------------------------------------------------------------
            # For Barrow Test Case
            Wet_NPG_PL_plot = np.reshape(self.Wet_NPG_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Wet_LCP_PL_plot = np.reshape(self.Wet_LCP_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Wet_CLC_PL_plot = np.reshape(self.Wet_CLC_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Wet_FCP_PL_plot = np.reshape(self.Wet_FCP_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Wet_HCP_PL_plot = np.reshape(self.Wet_HCP_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Lakes_PL_plot    = np.reshape(self.Lakes_PL,    [self.ATTM_nrows, self.ATTM_ncols])
            Ponds_PL_plot    = np.reshape(self.Ponds_PL,    [self.ATTM_nrows, self.ATTM_ncols])
            #-----------------------------------------------------------------------------------
            ## # For expanded areas
            ## # -------------------------------------------------------------------------------
            ## Gra_NPG_PL_plot = np.reshape(self.Gra_NPG_PL, [self.ATTM_nrows, self.ATTM_ncols])
            ## Gra_LCP_PL_plot = np.reshape(self.Gra_LCP_PL, [self.ATTM_nrows, self.ATTM_ncols])
            ## Gra_FCP_PL_plot = np.reshape(self.Gra_FCP_PL, [self.ATTM_nrows, self.ATTM_ncols])
            ## Gra_HCP_PL_plot = np.reshape(self.Gra_HCP_PL, [self.ATTM_nrows, self.ATTM_ncols])
            ## Shr_NPG_PL_plot = np.reshape(self.Shr_NPG_PL, [self.ATTM_nrows, self.ATTM_ncols])
            ## Shr_LCP_PL_plot = np.reshape(self.Shr_LCP_PL, [self.ATTM_nrows, self.ATTM_ncols])
            ## Shr_FCP_PL_plot = np.reshape(self.Shr_FCP_PL, [self.ATTM_nrows, self.ATTM_ncols])
            ## Shr_HCP_PL_plot = np.reshape(self.Shr_HCP_PL, [self.ATTM_nrows, self.ATTM_ncols])

            # ---------------------------------------------------------------------
            # Create output files, plots, figures
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Non-polygonal Ground Protective Layer')
            pl.imshow(Wet_NPG_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Non-polygonal Ground Protective Layer')
            pl.savefig('./Wet_NPG/Wet_NPG_PL.png', format = 'png')
            Wet_NPG_PL_plot.tofile('./Wet_NPG/Wet_NPG_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Low Center Polygon Protective Layer')
            pl.imshow(Wet_LCP_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Low Center Polygon Protective Layer')
            pl.savefig('./Wet_LCP/Wet_LCP_PL.png', format = 'png')
            Wet_LCP_PL_plot.tofile('./Wet_LCP/Wet_LCP_PL.bin')
            pl.close()    
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Coalescent Low Center Polygon Protective Layer')
            pl.imshow(Wet_CLC_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Coalescent_Low_Center Polygon Protective Layer')
            pl.savefig('./Wet_CLC/Wet_CLC_PL.png', format = 'png')
            Wet_CLC_PL_plot.tofile('./Wet_CLC/Wet_CLC_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Flat Center Polygon Protective Layer')
            pl.imshow(Wet_FCP_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Flat_Center Polygon Protective Layer')
            pl.savefig('./Wet_FCP/Wet_FCP_PL.png', format = 'png')
            Wet_FCP_PL_plot.tofile('./Wet_FCP/Wet_FCP_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland High Center Polygon Protective Layer')
            pl.imshow(Wet_HCP_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland High_Center Polygon Protective Layer')
            pl.savefig('./Wet_HCP/Wet_HCP_PL.png', format = 'png')
            Wet_HCP_PL_plot.tofile('./Wet_HCP/Wet_HCP_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Lake Polygon Protective Layer')
            pl.imshow(Lakes_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Lake Protective Layer')
            pl.savefig('./Lakes/Lakes_PL.png', format = 'png')
            Lakes_PL_plot.tofile('./Lakes/Lakes_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Pond Polygon Protective Layer')
            pl.imshow(Ponds_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Pond Protective Layer')
            pl.savefig('./Ponds/Ponds_PL.png', format = 'png')
            Ponds_PL_plot.tofile('./Ponds/Ponds_PL.bin')		
            pl.close()
            ## #_________________________________________________________________________
            ## # For future use
            ## #_________________________________________________________________________
            ## #-----------------------------------------------------------------------
            ## fig = pl.figure('Graminoid Non-polygonal Ground Protective Layer')
            ## pl.imshow(Gra_NPG_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ## pl.colorbar(extend = 'max', shrink = 0.92)
            ## pl.title('Graminoid Non-polygonal Ground Protective Layer')
            ## if FIGURE == 'TRUE':
            ##     pl.savefig('Graminoid_NPG_PL.png', format = 'png')
            ## if PLOT == 'TRUE':
            ##     pl.show()
            ## #-----------------------------------------------------------------------
            ## fig = pl.figure('Shrub Non-polygonal Ground Protective Layer')
            ## pl.imshow(Shr_NPG_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ## pl.colorbar(extend = 'max', shrink = 0.92)
            ## pl.title('Shrub Non-polygonal Ground Protective Layer')
            ## if FIGURE == 'TRUE':
            ##     pl.savefig('Shrub_NPG_PL.png', format = 'png')
            ## if PLOT == 'TRUE':
            ##     pl.show()
            ## #-----------------------------------------------------------------------
            ## fig = pl.figure('Graminoid Low Center Polygon Protective Layer')
            ## pl.imshow(Gra_LCP_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ## pl.colorbar(extend = 'max', shrink = 0.92)
            ## pl.title('Graminoid Low Center Polygon Protective Layer')
            ## if FIGURE == 'TRUE':
            ##     pl.savefig('Graminoid_LCP_PL.png', format = 'png')
            ## if PLOT == 'TRUE':
            ##     pl.show()
            ## #-----------------------------------------------------------------------
            ## fig = pl.figure('Graminoid Flat Center Polygon Protective Layer')
            ## pl.imshow(Gra_FCP_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ## pl.colorbar(extend = 'max', shrink = 0.92)
            ## pl.title('Graminoid Flat Center Polygon Protective Layer')
            ## if FIGURE == 'TRUE':
            ##     pl.savefig('Graminoid_FCP_PL.png', format = 'png')
            ## if PLOT == 'TRUE':
            ##     pl.show()
            ## #-----------------------------------------------------------------------
            ## fig = pl.figure('Graminoid High Center Polygon Protective Layer')
            ## pl.imshow(Gra_HCP_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ## pl.colorbar(extend = 'max', shrink = 0.92)
            ## pl.title('Graminoid High Center Polygon Protective Layer')
            ## if FIGURE == 'TRUE':
            ##     pl.savefig('Graminoid_HCP_PL.png', format = 'png')
            ## if PLOT == 'TRUE':
            ##     pl.show()
            ## #-----------------------------------------------------------------------
            ## fig = pl.figure('Shrub Low Center Polygon Protective Layer')
            ## pl.imshow(Shr_LCP_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ## pl.colorbar(extend = 'max', shrink = 0.92)
            ## pl.title('Shrub Low Center Polygon Protective Layer')
            ## if FIGURE == 'TRUE':
            ##     pl.savefig('Shrub_LCP_PL.png', format = 'png')
            ## if PLOT == 'TRUE':
            ##     pl.show()
            ## #-----------------------------------------------------------------------
            ## fig = pl.figure('Shrub Flat Center Polygon Protective Layer')
            ## pl.imshow(Shr_FCP_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ## pl.colorbar(extend = 'max', shrink = 0.92)
            ## pl.title('Shrub Flat Center Polygon Protective Layer')
            ## if FIGURE == 'TRUE':
            ##     pl.savefig('Shrub_FCP_PL.png', format = 'png')
            ## if PLOT == 'TRUE':
            ##     pl.show()   
            ## #-----------------------------------------------------------------------
            ## fig = pl.figure('Shrub High Center Polygon Protective Layer')
            ## pl.imshow(Shr_HCP_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ## pl.colorbar(extend = 'max', shrink = 0.92)
            ## pl.title('Shrub High Center Polygon Protective Layer')
            ## if FIGURE == 'TRUE':
            ##     pl.savefig('Shrub_HCP_PL.png', format = 'png')
            ## if PLOT == 'TRUE':
            ##     pl.show()   
            #-----------------------------------------------------------------------

        # Change back to Run Directory
            os.chdir(self.control['Run_dir'])


