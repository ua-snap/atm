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
        self.ATTM_CLC_WT_M_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_CLC_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_CLC_WT_Y_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_CoastalWaters_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_CoastalWaters_WT_M_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_CoastalWaters_WT_Y_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_DrainedSlope_WT_M_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_DrainedSlope_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_DrainedSlope_WT_Y_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_FCP_WT_M_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_FCP_WT_Y_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_FCP_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_HCP_WT_Y_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_HCP_WT_M_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_HCP_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_LCP_WT_Y_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_LCP_WT_M_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_LCP_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_Meadow_WT_Y_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_Meadow_WT_M_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_Meadow_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_NoData_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_SandDunes_WT_Y_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_SandDunes_WT_M_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_SandDunes_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_SaturatedBarrens_WT_Y_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_SaturatedBarrens_WT_M_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_SaturatedBarrens_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_Shrubs_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_Urban_WT_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_LargeLakes_WT_Y_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_LargeLakes_WT_M_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_LargeLakes_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_MediumLakes_WT_Y_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_MediumLakes_WT_M_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_MediumLakes_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_SmallLakes_WT_Y_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_SmallLakes_WT_M_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_SmallLakes_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_Ponds_WT_Y_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_Ponds_WT_M_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_Ponds_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_Rivers_WT_Y_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_Rivers_WT_M_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        self.ATTM_Rivers_WT_O_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
        
#        self.Wet_NPG_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#        self.Wet_LCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#        self.Wet_CLC_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#        self.Wet_FCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#        self.Wet_HCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#        self.Gra_NPG_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#        self.Gra_LCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#        self.Gra_FCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#        self.Gra_HCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#        self.Shr_NPG_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#        self.Shr_LCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#        self.Shr_FCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#        self.Shr_HCP_PL = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#        self.Lakes_PL    = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#        self.Ponds_PL    = np.zeros(self.ATTM_nrows * self.ATTM_ncols)

        for i in range(self.ATTM_nrows * self.ATTM_ncols):
            self.ATTM_CLC_WT_Y_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['CLC_WT_Y_PLF']
            self.ATTM_CLC_WT_M_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['CLC_WT_M_PLF']
            self.ATTM_CLC_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['CLC_WT_O_PLF']
            self.ATTM_CoastalWaters_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['CoastalWaters_WT_O_PLF']
            self.ATTM_DrainedSlope_WT_Y_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['DrainedSlope_WT_Y_PLF']           
            self.ATTM_DrainedSlope_WT_M_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['DrainedSlope_WT_M_PLF']           
            self.ATTM_DrainedSlope_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['DrainedSlope_WT_O_PLF']           
            self.ATTM_FCP_WT_Y_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['FCP_WT_Y_PLF']           
            self.ATTM_FCP_WT_M_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['FCP_WT_M_PLF'] 
            self.ATTM_FCP_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['FCP_WT_O_PLF'] 
            self.ATTM_HCP_WT_Y_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['HCP_WT_Y_PLF']           
            self.ATTM_HCP_WT_M_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['HCP_WT_M_PLF'] 
            self.ATTM_HCP_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['HCP_WT_O_PLF'] 
            self.ATTM_LCP_WT_Y_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['LCP_WT_Y_PLF']           
            self.ATTM_LCP_WT_M_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['LCP_WT_M_PLF'] 
            self.ATTM_LCP_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['LCP_WT_O_PLF'] 
            self.ATTM_Meadow_WT_Y_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Meadow_WT_Y_PLF']           
            self.ATTM_Meadow_WT_M_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Meadow_WT_M_PLF'] 
            self.ATTM_Meadow_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Meadow_WT_O_PLF'] 
            self.ATTM_NoData_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['NoData_WT_O_PLF'] 
            self.ATTM_SandDunes_WT_Y_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['SandDunes_WT_Y_PLF']           
            self.ATTM_SandDunes_WT_M_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['SandDunes_WT_M_PLF'] 
            self.ATTM_SandDunes_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['SandDunes_WT_O_PLF'] 
            self.ATTM_SaturatedBarrens_WT_Y_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['SaturatedBarrens_WT_Y_PLF']           
            self.ATTM_SaturatedBarrens_WT_M_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['SaturatedBarrens_WT_M_PLF'] 
            self.ATTM_SaturatedBarrens_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['SaturatedBarrens_WT_O_PLF'] 
            self.ATTM_Shrubs_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Shrubs_WT_O_PLF'] 
            self.ATTM_Urban_WT_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Urban_WT_PLF'] 
            self.ATTM_LargeLakes_WT_Y_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['LargeLakes_WT_Y_PLF']           
            self.ATTM_LargeLakes_WT_M_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['LargeLakes_WT_M_PLF'] 
            self.ATTM_LargeLakes_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['LargeLakes_WT_O_PLF'] 
            self.ATTM_MediumLakes_WT_Y_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['MediumLakes_WT_Y_PLF']           
            self.ATTM_MediumLakes_WT_M_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['MediumLakes_WT_M_PLF'] 
            self.ATTM_MediumLakes_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['MediumLakes_WT_O_PLF'] 
            self.ATTM_SmallLakes_WT_Y_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['SmallLakes_WT_Y_PLF']           
            self.ATTM_SmallLakes_WT_M_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['SmallLakes_WT_M_PLF'] 
            self.ATTM_SmallLakes_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['SmallLakes_WT_O_PLF'] 
            self.ATTM_Ponds_WT_Y_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Ponds_WT_Y_PLF']           
            self.ATTM_Ponds_WT_M_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Ponds_WT_M_PLF'] 
            self.ATTM_Ponds_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Ponds_WT_O_PLF'] 
            self.ATTM_Rivers_WT_Y_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Rivers_WT_Y_PLF']           
            self.ATTM_Rivers_WT_M_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Rivers_WT_M_PLF'] 
            self.ATTM_Rivers_WT_O_PL[i] = self.initial_ALD_depth[i] * \
              self.Terrestrial['Rivers_WT_O_PLF'] 

#            self.Wet_NPG_PL[i] = self.initial_ALD_depth[i] * \
#              self.Terrestrial['Wet_NPG_PLF']
#            self.Wet_LCP_PL[i] = self.initial_ALD_depth[i] * \
#              self.Terrestrial['Wet_LCP_PLF']
#            self.Wet_CLC_PL[i] = self.initial_ALD_depth[i] * \
#              self.Terrestrial['Wet_CLC_PLF']
#            self.Wet_FCP_PL[i] = self.initial_ALD_depth[i] * \
#              self.Terrestrial['Wet_FCP_PLF']
#            self.Wet_HCP_PL[i] = self.initial_ALD_depth[i] * \
#              self.Terrestrial['Wet_HCP_PLF']
#            self.Gra_NPG_PL[i] = self.initial_ALD_depth[i] * \
#              self.Terrestrial['Gra_NPG_PLF']
#            self.Gra_LCP_PL[i] = self.initial_ALD_depth[i] * \
#              self.Terrestrial['Gra_LCP_PLF']
#            self.Gra_FCP_PL[i] = self.initial_ALD_depth[i] * \
#              self.Terrestrial['Gra_FCP_PLF']
#            self.Gra_HCP_PL[i] = self.initial_ALD_depth[i] * \
#              self.Terrestrial['Gra_HCP_PLF']
#            self.Shr_NPG_PL[i] = self.initial_ALD_depth[i] * \
#              self.Terrestrial['Shr_NPG_PLF']
#            self.Shr_LCP_PL[i] = self.initial_ALD_depth[i] * \
#              self.Terrestrial['Shr_LCP_PLF']
#            self.Shr_FCP_PL[i] = self.initial_ALD_depth[i] * \
#              self.Terrestrial['Shr_FCP_PLF']
#            self.Shr_HCP_PL[i] = self.initial_ALD_depth[i] * \
#              self.Terrestrial['Shr_HCP_PLF']
#            self.Lakes_PL[i]   = self.Lake_Depth[i] * \
#              self.Terrestrial['Lakes_PLF']
#            self.Ponds_PL[i]   = self.Pond_Depth[i] * \
#              self.Terrestrial['Ponds_PLF']

        print '    done. \n  '

        # ######################################
        # Plotting and saving values if wanted
        # ######################################
        if self.Terrestrial['Protective_Layer_Factor_Output'].lower() == 'yes':

            # Move to Output directory
            os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/')

            #--------------------------------------------------------------------------------
            # For Barrow Test Case
            CLC_WT_Y_PL_plot = np.reshape(self.ATTM_CLC_WT_Y_PL, [self.ATTM_nrows, self.ATTM_ncols])
            CLC_WT_M_PL_plot = np.reshape(self.ATTM_CLC_WT_M_PL, [self.ATTM_nrows, self.ATTM_ncols])
            CLC_WT_O_PL_plot = np.reshape(self.ATTM_CLC_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            CoastalWaters_WT_Y_PL_plot = np.reshape(self.ATTM_CoastalWaters_WT_Y_PL, [self.ATTM_nrows, self.ATTM_ncols])
            CoastalWaters_WT_M_PL_plot = np.reshape(self.ATTM_CoastalWaters_WT_M_PL, [self.ATTM_nrows, self.ATTM_ncols])
            CoastalWaters_WT_O_PL_plot = np.reshape(self.ATTM_CoastalWaters_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            DrainedSlope_WT_Y_PL_plot = np.reshape(self.ATTM_DrainedSlope_WT_Y_PL, [self.ATTM_nrows, self.ATTM_ncols])
            DrainedSlope_WT_M_PL_plot = np.reshape(self.ATTM_DrainedSlope_WT_M_PL, [self.ATTM_nrows, self.ATTM_ncols])
            DrainedSlope_WT_O_PL_plot = np.reshape(self.ATTM_DrainedSlope_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            FCP_WT_Y_PL_plot = np.reshape(self.ATTM_FCP_WT_Y_PL, [self.ATTM_nrows, self.ATTM_ncols])
            FCP_WT_M_PL_plot = np.reshape(self.ATTM_FCP_WT_M_PL, [self.ATTM_nrows, self.ATTM_ncols])
            FCP_WT_O_PL_plot = np.reshape(self.ATTM_FCP_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            HCP_WT_Y_PL_plot = np.reshape(self.ATTM_HCP_WT_Y_PL, [self.ATTM_nrows, self.ATTM_ncols])
            HCP_WT_M_PL_plot = np.reshape(self.ATTM_HCP_WT_M_PL, [self.ATTM_nrows, self.ATTM_ncols])
            HCP_WT_O_PL_plot = np.reshape(self.ATTM_HCP_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            LCP_WT_Y_PL_plot = np.reshape(self.ATTM_LCP_WT_Y_PL, [self.ATTM_nrows, self.ATTM_ncols])
            LCP_WT_M_PL_plot = np.reshape(self.ATTM_LCP_WT_M_PL, [self.ATTM_nrows, self.ATTM_ncols])
            LCP_WT_O_PL_plot = np.reshape(self.ATTM_LCP_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Meadow_WT_Y_PL_plot = np.reshape(self.ATTM_Meadow_WT_Y_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Meadow_WT_M_PL_plot = np.reshape(self.ATTM_Meadow_WT_M_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Meadow_WT_O_PL_plot = np.reshape(self.ATTM_Meadow_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            NoData_WT_O_PL_plot = np.reshape(self.ATTM_NoData_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            SandDunes_WT_Y_PL_plot = np.reshape(self.ATTM_SandDunes_WT_Y_PL, [self.ATTM_nrows, self.ATTM_ncols])
            SandDunes_WT_M_PL_plot = np.reshape(self.ATTM_SandDunes_WT_M_PL, [self.ATTM_nrows, self.ATTM_ncols])
            SandDunes_WT_O_PL_plot = np.reshape(self.ATTM_SandDunes_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            SaturatedBarrens_WT_Y_PL_plot = np.reshape(self.ATTM_SaturatedBarrens_WT_Y_PL, [self.ATTM_nrows, self.ATTM_ncols])
            SaturatedBarrens_WT_M_PL_plot = np.reshape(self.ATTM_SaturatedBarrens_WT_M_PL, [self.ATTM_nrows, self.ATTM_ncols])
            SaturatedBarrens_WT_O_PL_plot = np.reshape(self.ATTM_SaturatedBarrens_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Shrubs_WT_O_PL_plot = np.reshape(self.ATTM_Shrubs_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Urban_WT_PL_plot = np.reshape(self.ATTM_Urban_WT_PL, [self.ATTM_nrows, self.ATTM_ncols])
            LargeLakes_WT_Y_PL_plot = np.reshape(self.ATTM_LargeLakes_WT_Y_PL, [self.ATTM_nrows, self.ATTM_ncols])
            LargeLakes_WT_M_PL_plot = np.reshape(self.ATTM_LargeLakes_WT_M_PL, [self.ATTM_nrows, self.ATTM_ncols])
            LargeLakes_WT_O_PL_plot = np.reshape(self.ATTM_LargeLakes_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            MediumLakes_WT_Y_PL_plot = np.reshape(self.ATTM_MediumLakes_WT_Y_PL, [self.ATTM_nrows, self.ATTM_ncols])
            MediumLakes_WT_M_PL_plot = np.reshape(self.ATTM_MediumLakes_WT_M_PL, [self.ATTM_nrows, self.ATTM_ncols])
            MediumLakes_WT_O_PL_plot = np.reshape(self.ATTM_MediumLakes_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            SmallLakes_WT_Y_PL_plot = np.reshape(self.ATTM_SmallLakes_WT_Y_PL, [self.ATTM_nrows, self.ATTM_ncols])
            SmallLakes_WT_M_PL_plot = np.reshape(self.ATTM_SmallLakes_WT_M_PL, [self.ATTM_nrows, self.ATTM_ncols])
            SmallLakes_WT_O_PL_plot = np.reshape(self.ATTM_SmallLakes_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Ponds_WT_Y_PL_plot = np.reshape(self.ATTM_Ponds_WT_Y_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Ponds_WT_M_PL_plot = np.reshape(self.ATTM_Ponds_WT_M_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Ponds_WT_O_PL_plot = np.reshape(self.ATTM_Ponds_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Rivers_WT_Y_PL_plot = np.reshape(self.ATTM_Rivers_WT_Y_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Rivers_WT_M_PL_plot = np.reshape(self.ATTM_Rivers_WT_M_PL, [self.ATTM_nrows, self.ATTM_ncols])
            Rivers_WT_O_PL_plot = np.reshape(self.ATTM_Rivers_WT_O_PL, [self.ATTM_nrows, self.ATTM_ncols])
            
#            Wet_NPG_PL_plot = np.reshape(self.Wet_NPG_PL, [self.ATTM_nrows, self.ATTM_ncols])
#            Wet_LCP_PL_plot = np.reshape(self.Wet_LCP_PL, [self.ATTM_nrows, self.ATTM_ncols])
#            Wet_CLC_PL_plot = np.reshape(self.Wet_CLC_PL, [self.ATTM_nrows, self.ATTM_ncols])
#            Wet_FCP_PL_plot = np.reshape(self.Wet_FCP_PL, [self.ATTM_nrows, self.ATTM_ncols])
#            Wet_HCP_PL_plot = np.reshape(self.Wet_HCP_PL, [self.ATTM_nrows, self.ATTM_ncols])
#            Lakes_PL_plot    = np.reshape(self.Lakes_PL,    [self.ATTM_nrows, self.ATTM_ncols])
#            Ponds_PL_plot    = np.reshape(self.Ponds_PL,    [self.ATTM_nrows, self.ATTM_ncols])
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
            fig = pl.figure('Wetland Tundra Coalescent Low Center Polygon Protective Layer - Young Age ')
            pl.imshow(CLC_WT_Y_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Coalescent Low Center Polygon\n Protective Layer - Young age')
            pl.savefig('./CLC_WT_Y/CLC_WT_Y_PL.png', format = 'png')
            CLC_WT_Y_PL_plot.tofile('./CLC_WT_Y/CLC_WT_Y_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Coalescent Low Center Polygon Protective Layer - Medium age ')
            pl.imshow(CLC_WT_M_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Coalescent Low Center Polygon\n Protective Layer - Medium Age')
            pl.savefig('./CLC_WT_M/CLC_WT_M_PL.png', format = 'png')
            CLC_WT_Y_PL_plot.tofile('./CLC_WT_M/CLC_WT_M_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Coalescent Low Center Polygon Protective Layer - Old age ')
            pl.imshow(CLC_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Coalescent Low Center Polygon\n Protective Layer - Old Age')
            pl.savefig('./CLC_WT_O/CLC_WT_O_PL.png', format = 'png')
            CLC_WT_Y_PL_plot.tofile('./CLC_WT_O/CLC_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Coastal Waters Protective Layer - Old age ')
            pl.imshow(CoastalWaters_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Coastal Waters\n Protective Layer - Old Age')
            pl.savefig('./CoastalWaters_WT_O/CoastalWaters_WT_O_PL.png', format = 'png')
            CoastalWaters_WT_O_PL_plot.tofile('./CoastalWaters_WT_O/CoastalWaters_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Drained Slope Protective Layer - Young age ')
            pl.imshow(DrainedSlope_WT_Y_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra DrainedSlope\n Protective Layer - Young Age')
            pl.savefig('./DrainedSlope_WT_Y/DrainedSlope_WT_Y_PL.png', format = 'png')
            DrainedSlope_WT_Y_PL_plot.tofile('./DrainedSlope_WT_Y/DrainedSlope_WT_Y_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Drained Slope Protective Layer - Medium age ')
            pl.imshow(DrainedSlope_WT_M_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra DrainedSlope\n Protective Layer - Medium Age')
            pl.savefig('./DrainedSlope_WT_M/DrainedSlope_WT_M_PL.png', format = 'png')
            DrainedSlope_WT_M_PL_plot.tofile('./DrainedSlope_WT_M/DrainedSlope_WT_M_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Drained Slope Protective Layer - Old age ')
            pl.imshow(DrainedSlope_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra DrainedSlope\n Protective Layer - Old Age')
            pl.savefig('./DrainedSlope_WT_O/DrainedSlope_WT_O_PL.png', format = 'png')
            DrainedSlope_WT_O_PL_plot.tofile('./DrainedSlope_WT_O/DrainedSlope_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Flat Center Polygon Protective Layer - Young age ')
            pl.imshow(FCP_WT_Y_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Flat Centered Polygon\n Protective Layer - Young Age')
            pl.savefig('./FCP_WT_Y/FCP_WT_Y_PL.png', format = 'png')
            FCP_WT_Y_PL_plot.tofile('./FCP_WT_Y/FCP_WT_Y_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Flat Center Polygon Protective Layer - Medium age ')
            pl.imshow(FCP_WT_M_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Flat Centered Polygon\n Protective Layer - Medium Age')
            pl.savefig('./FCP_WT_M/FCP_WT_M_PL.png', format = 'png')
            FCP_WT_M_PL_plot.tofile('./FCP_WT_M/FCP_WT_M_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Flat Center Polygon Protective Layer - Old age ')
            pl.imshow(FCP_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Flat Centered Polygon\n Protective Layer - Old Age')
            pl.savefig('./FCP_WT_O/FCP_WT_O_PL.png', format = 'png')
            FCP_WT_O_PL_plot.tofile('./FCP_WT_O/FCP_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra High Center Polygon Protective Layer - Young age ')
            pl.imshow(HCP_WT_Y_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra High Centered Polygon\n Protective Layer - Young Age')
            pl.savefig('./HCP_WT_Y/HCP_WT_Y_PL.png', format = 'png')
            HCP_WT_Y_PL_plot.tofile('./HCP_WT_Y/HCP_WT_Y_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra High Center Polygon Protective Layer - Medium age ')
            pl.imshow(HCP_WT_M_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra High Centered Polygon\n Protective Layer - Medium Age')
            pl.savefig('./HCP_WT_M/HCP_WT_M_PL.png', format = 'png')
            HCP_WT_M_PL_plot.tofile('./HCP_WT_M/HCP_WT_M_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra High Center Polygon Protective Layer - Old age ')
            pl.imshow(HCP_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra High Centered Polygon\n Protective Layer - Old Age')
            pl.savefig('./HCP_WT_O/HCP_WT_O_PL.png', format = 'png')
            HCP_WT_O_PL_plot.tofile('./HCP_WT_O/HCP_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Low Center Polygon Protective Layer - Young age ')
            pl.imshow(LCP_WT_Y_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Low Centered Polygon\n Protective Layer - Young Age')
            pl.savefig('./LCP_WT_Y/LCP_WT_Y_PL.png', format = 'png')
            LCP_WT_Y_PL_plot.tofile('./LCP_WT_Y/LCP_WT_Y_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Low Center Polygon Protective Layer - Medium age ')
            pl.imshow(LCP_WT_M_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Low Centered Polygon\n Protective Layer - Medium Age')
            pl.savefig('./LCP_WT_M/LCP_WT_M_PL.png', format = 'png')
            LCP_WT_M_PL_plot.tofile('./LCP_WT_M/LCP_WT_M_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Low Center Polygon Protective Layer - Old age ')
            pl.imshow(LCP_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Low Centered Polygon\n Protective Layer - Old Age')
            pl.savefig('./LCP_WT_O/LCP_WT_O_PL.png', format = 'png')
            LCP_WT_O_PL_plot.tofile('./LCP_WT_O/LCP_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Meadow Protective Layer - Young age ')
            pl.imshow(Meadow_WT_Y_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Meadow\n Protective Layer - Young Age')
            pl.savefig('./Meadow_WT_Y/Meadow_WT_Y_PL.png', format = 'png')
            Meadow_WT_Y_PL_plot.tofile('./Meadow_WT_Y/Meadow_WT_Y_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Meadow Protective Layer - Medium age ')
            pl.imshow(Meadow_WT_M_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Meadow\n Protective Layer - Medium Age')
            pl.savefig('./Meadow_WT_M/Meadow_WT_M_PL.png', format = 'png')
            Meadow_WT_M_PL_plot.tofile('./Meadow_WT_M/Meadow_WT_M_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Meadow Protective Layer - Old age ')
            pl.imshow(Meadow_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Meadow\n Protective Layer - Old Age')
            pl.savefig('./Meadow_WT_O/Meadow_WT_O_PL.png', format = 'png')
            Meadow_WT_O_PL_plot.tofile('./Meadow_WT_O/Meadow_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra No Data Protective Layer')
            pl.imshow(NoData_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra No Data\n Protective Layer')
            pl.savefig('./Other_Cohorts/NoData_WT_O_PL.png', format = 'png')
            NoData_WT_O_PL_plot.tofile('./Other_Cohorts/NoData_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Sand Dunes Protective Layer - Young age ')
            pl.imshow(SandDunes_WT_Y_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Sand Dunes\n Protective Layer - Young Age')
            pl.savefig('./SandDunes_WT_Y/SandDunes_WT_Y_PL.png', format = 'png')
            SandDunes_WT_Y_PL_plot.tofile('./SandDunes_WT_Y/SandDunes_WT_Y_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Sand Dunes Protective Layer - Medium age ')
            pl.imshow(SandDunes_WT_M_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Sand Dunes\n Protective Layer - Medium Age')
            pl.savefig('./SandDunes_WT_M/SandDunes_WT_M_PL.png', format = 'png')
            SandDunes_WT_M_PL_plot.tofile('./SandDunes_WT_M/SandDunes_WT_M_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Sand Dunes Protective Layer - Old age ')
            pl.imshow(SandDunes_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Sand Dunes\n Protective Layer - Old Age')
            pl.savefig('./SandDunes_WT_O/SandDunes_WT_O_PL.png', format = 'png')
            SandDunes_WT_O_PL_plot.tofile('./SandDunes_WT_O/SandDunes_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Saturated Barrens Protective Layer - Young age ')
            pl.imshow(SaturatedBarrens_WT_Y_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Saturated Barrens\n Protective Layer - Young Age')
            pl.savefig('./SaturatedBarrens_WT_Y/SaturatedBarrens_WT_Y_PL.png', format = 'png')
            SaturatedBarrens_WT_Y_PL_plot.tofile('./SaturatedBarrens_WT_Y/SaturatedBarrens_WT_Y_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Saturated Barrens Protective Layer - Medium age ')
            pl.imshow(SaturatedBarrens_WT_M_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Saturated Barrens\n Protective Layer - Medium Age')
            pl.savefig('./SaturatedBarrens_WT_M/SaturatedBarrens_WT_M_PL.png', format = 'png')
            SaturatedBarrens_WT_M_PL_plot.tofile('./SaturatedBarrens_WT_M/SaturatedBarrens_WT_M_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Saturated Barrens Protective Layer - Old age ')
            pl.imshow(SaturatedBarrens_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Saturated Barrens\n Protective Layer - Old Age')
            pl.savefig('./SaturatedBarrens_WT_O/SaturatedBarrens_WT_O_PL.png', format = 'png')
            SaturatedBarrens_WT_O_PL_plot.tofile('./SaturatedBarrens_WT_O/SaturatedBarrens_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Shrubs Protective Layer - Old age ')
            pl.imshow(Shrubs_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Shrubs\n Protective Layer - Old Age')
            pl.savefig('./Shrubs_WT_O/Shrubs_WT_O_PL.png', format = 'png')
            Shrubs_WT_O_PL_plot.tofile('./Shrubs_WT_O/Shrubs_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Urban Protective Layer')
            pl.imshow(Urban_WT_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Urban\n Protective Layer')
            pl.savefig('./Urban_WT/Urban_WT_PL.png', format = 'png')
            Urban_WT_PL_plot.tofile('./Urban_WT/Urban_WT_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Large Lakes Protective Layer - Young age ')
            pl.imshow(LargeLakes_WT_Y_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Large Lakes\n Protective Layer - Young Age')
            pl.savefig('./LargeLakes_WT_Y/LargeLakes_WT_Y_PL.png', format = 'png')
            LargeLakes_WT_Y_PL_plot.tofile('./LargeLakes_WT_Y/LargeLakes_WT_Y_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Large Lakes Protective Layer - Medium age ')
            pl.imshow(LargeLakes_WT_M_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Large Lakes\n Protective Layer - Medium Age')
            pl.savefig('./LargeLakes_WT_M/LargeLakes_WT_M_PL.png', format = 'png')
            LargeLakes_WT_M_PL_plot.tofile('./LargeLakes_WT_M/LargeLakes_WT_M_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Large Lakes Protective Layer - Old age ')
            pl.imshow(LargeLakes_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Large Lakes\n Protective Layer - Old Age')
            pl.savefig('./LargeLakes_WT_O/LargeLakes_WT_O_PL.png', format = 'png')
            LargeLakes_WT_O_PL_plot.tofile('./LargeLakes_WT_O/LargeLakes_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Medium Lakes Protective Layer - Young age ')
            pl.imshow(MediumLakes_WT_Y_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Medium Lakes\n Protective Layer - Young Age')
            pl.savefig('./MediumLakes_WT_Y/MediumLakes_WT_Y_PL.png', format = 'png')
            MediumLakes_WT_Y_PL_plot.tofile('./MediumLakes_WT_Y/MediumLakes_WT_Y_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Medium Lakes Protective Layer - Medium age ')
            pl.imshow(MediumLakes_WT_M_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Medium Lakes\n Protective Layer - Medium Age')
            pl.savefig('./MediumLakes_WT_M/MediumLakes_WT_M_PL.png', format = 'png')
            MediumLakes_WT_M_PL_plot.tofile('./MediumLakes_WT_M/MediumLakes_WT_M_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Medium Lakes Protective Layer - Old age ')
            pl.imshow(MediumLakes_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Medium Lakes\n Protective Layer - Old Age')
            pl.savefig('./MediumLakes_WT_O/MediumLakes_WT_O_PL.png', format = 'png')
            MediumLakes_WT_O_PL_plot.tofile('./MediumLakes_WT_O/MediumLakes_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Small Lakes Protective Layer - Young age ')
            pl.imshow(SmallLakes_WT_Y_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Small Lakes\n Protective Layer - Young Age')
            pl.savefig('./SmallLakes_WT_Y/SmallLakes_WT_Y_PL.png', format = 'png')
            SmallLakes_WT_Y_PL_plot.tofile('./SmallLakes_WT_Y/SmallLakes_WT_Y_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Small Lakes Protective Layer - Medium age ')
            pl.imshow(SmallLakes_WT_M_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Small Lakes\n Protective Layer - Medium Age')
            pl.savefig('./SmallLakes_WT_M/SmallLakes_WT_M_PL.png', format = 'png')
            SmallLakes_WT_M_PL_plot.tofile('./SmallLakes_WT_M/SmallLakes_WT_M_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Small Lakes Protective Layer - Old age ')
            pl.imshow(SmallLakes_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Small Lakes\n Protective Layer - Old Age')
            pl.savefig('./SmallLakes_WT_O/SmallLakes_WT_O_PL.png', format = 'png')
            SmallLakes_WT_O_PL_plot.tofile('./SmallLakes_WT_O/SmallLakes_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Ponds Protective Layer - Young age ')
            pl.imshow(Ponds_WT_Y_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Ponds\n Protective Layer - Young Age')
            pl.savefig('./Ponds_WT_Y/Ponds_WT_Y_PL.png', format = 'png')
            Ponds_WT_Y_PL_plot.tofile('./Ponds_WT_Y/Ponds_WT_Y_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Ponds Protective Layer - Medium age ')
            pl.imshow(Ponds_WT_M_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Ponds\n Protective Layer - Medium Age')
            pl.savefig('./Ponds_WT_M/Ponds_WT_M_PL.png', format = 'png')
            Ponds_WT_M_PL_plot.tofile('./Ponds_WT_M/Ponds_WT_M_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Ponds Protective Layer - Old age ')
            pl.imshow(Ponds_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Ponds\n Protective Layer - Old Age')
            pl.savefig('./Ponds_WT_O/Ponds_WT_O_PL.png', format = 'png')
            Ponds_WT_O_PL_plot.tofile('./Ponds_WT_O/Ponds_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Rivers Protective Layer - Young age ')
            pl.imshow(Rivers_WT_Y_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Rivers\n Protective Layer - Young Age')
            pl.savefig('./Rivers_WT_Y/Rivers_WT_Y_PL.png', format = 'png')
            Rivers_WT_Y_PL_plot.tofile('./Rivers_WT_Y/Rivers_WT_Y_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Rivers Protective Layer - Medium age ')
            pl.imshow(Rivers_WT_M_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Rivers\n Protective Layer - Medium Age')
            pl.savefig('./Rivers_WT_M/Rivers_WT_M_PL.png', format = 'png')
            Rivers_WT_M_PL_plot.tofile('./Rivers_WT_M/Rivers_WT_M_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            fig = pl.figure('Wetland Tundra Rivers Protective Layer - Old age ')
            pl.imshow(Rivers_WT_O_PL_plot, interpolation = 'nearest', cmap = 'bone')
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Tundra Rivers\n Protective Layer - Old Age')
            pl.savefig('./Rivers_WT_O/Rivers_WT_O_PL.png', format = 'png')
            Rivers_WT_O_PL_plot.tofile('./Rivers_WT_O/Rivers_WT_O_PL.bin')
            pl.close()
            #-----------------------------------------------------------------------
            ##fig = pl.figure('Wetland Non-polygonal Ground Protective Layer')
            ##pl.imshow(Wet_NPG_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ##pl.colorbar(extend = 'max', shrink = 0.92)
            ##pl.title('Wetland Non-polygonal Ground Protective Layer')
            ##pl.savefig('./Wet_NPG/Wet_NPG_PL.png', format = 'png')
            ##Wet_NPG_PL_plot.tofile('./Wet_NPG/Wet_NPG_PL.bin')
            ##pl.close()
            ##-----------------------------------------------------------------------
            ##fig = pl.figure('Wetland Low Center Polygon Protective Layer')
            ##pl.imshow(Wet_LCP_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ##pl.colorbar(extend = 'max', shrink = 0.92)
            ##pl.title('Wetland Low Center Polygon Protective Layer')
            ##pl.savefig('./Wet_LCP/Wet_LCP_PL.png', format = 'png')
            ##Wet_LCP_PL_plot.tofile('./Wet_LCP/Wet_LCP_PL.bin')
            ##pl.close()    
            ###-----------------------------------------------------------------------
            ##fig = pl.figure('Wetland Coalescent Low Center Polygon Protective Layer')
            ##pl.imshow(Wet_CLC_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ##pl.colorbar(extend = 'max', shrink = 0.92)
            ##pl.title('Wetland Coalescent_Low_Center Polygon Protective Layer')
            ##pl.savefig('./Wet_CLC/Wet_CLC_PL.png', format = 'png')
            ##Wet_CLC_PL_plot.tofile('./Wet_CLC/Wet_CLC_PL.bin')
            ##pl.close()
            ###-----------------------------------------------------------------------
            ##fig = pl.figure('Wetland Flat Center Polygon Protective Layer')
            ##pl.imshow(Wet_FCP_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ##pl.colorbar(extend = 'max', shrink = 0.92)
            ##pl.title('Wetland Flat_Center Polygon Protective Layer')
            ##pl.savefig('./Wet_FCP/Wet_FCP_PL.png', format = 'png')
            ##Wet_FCP_PL_plot.tofile('./Wet_FCP/Wet_FCP_PL.bin')
            ##pl.close()
            ###-----------------------------------------------------------------------
            ##fig = pl.figure('Wetland High Center Polygon Protective Layer')
            ##pl.imshow(Wet_HCP_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ##pl.colorbar(extend = 'max', shrink = 0.92)
            ##pl.title('Wetland High_Center Polygon Protective Layer')
            ##pl.savefig('./Wet_HCP/Wet_HCP_PL.png', format = 'png')
            ##Wet_HCP_PL_plot.tofile('./Wet_HCP/Wet_HCP_PL.bin')
            ##pl.close()
            ###-----------------------------------------------------------------------
            ##fig = pl.figure('Lake Polygon Protective Layer')
            ##pl.imshow(Lakes_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ##pl.colorbar(extend = 'max', shrink = 0.92)
            ##pl.title('Lake Protective Layer')
            ##pl.savefig('./Lakes/Lakes_PL.png', format = 'png')
            ##Lakes_PL_plot.tofile('./Lakes/Lakes_PL.bin')
            ##pl.close()
            ###-----------------------------------------------------------------------
            ##fig = pl.figure('Pond Polygon Protective Layer')
            ##pl.imshow(Ponds_PL_plot, interpolation = 'nearest', cmap = 'bone')
            ##pl.colorbar(extend = 'max', shrink = 0.92)
            ##pl.title('Pond Protective Layer')
            ##pl.savefig('./Ponds/Ponds_PL.png', format = 'png')
            ##Ponds_PL_plot.tofile('./Ponds/Ponds_PL.bin')		
            ##pl.close()
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


