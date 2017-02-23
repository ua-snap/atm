import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def set_lake_pond_depth(self):
    
    """
    The purpose of this module is to set the lake and pond depths for each
    element that has a lake or pond cohort within the element of interest.

    Paper by Jeffries et al (1996) indicate (rough reading) that the max
    ice thickness in this region is 2.2m. This will be the pond-lake threshold.

    The pond depth is typically between 1.4-1.5 m (from paper). 60% of ponds
    are in this range (around barrow).

    Until we have better data, will use random function.
    Lakes ~ 2.2 -> 5 m
    Ponds ~ 1.25 - 1.7 m
    """

    print '    Setting Lake and Pond Depths'

    #self.pond_count = 0.0       # For use in check_ponds.
    self.Pond_WT_Y_count = 0.0  # Not sure if needed, but adding just in case
    self.Pond_WT_M_count = 0.0
    self.Pond_WT_O_count = 0.0

    #self.Lake_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.LargeLake_WT_Y_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.LargeLake_WT_M_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.LargeLake_WT_O_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.MediumLake_WT_Y_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.MediumLake_WT_M_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.MediumLake_WT_O_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.SmallLake_WT_Y_Depth  = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.SmallLake_WT_M_Depth  = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.SmallLake_WT_O_Depth  = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    
    #self.Pond_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.Pond_WT_Y_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.Pond_WT_M_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.Pond_WT_O_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)

    for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
        #------------------------------------
        # Determine Lake Depth Distribution
        #------------------------------------
        if self.LakePond['Lake_Distribution'].lower() == 'random':
            #Lake_Depth = random.uniform(self.LakePond['Lower_Lake_Depth'], \
            #                            self.LakePond['Upper_Lake_Depth'])
            LargeLake_WT_Y_Depth = random.uniform(self.LakePond['Lower_LargeLake_WT_Y_Depth'] , \
                                                  self.LakePond['Upper_LargeLake_WT_Y_Depth'])
            LargeLake_WT_M_Depth = random.uniform(self.LakePond['Lower_LargeLake_WT_M_Depth'] , \
                                                  self.LakePond['Upper_LargeLake_WT_M_Depth'])
            LargeLake_WT_O_Depth = random.uniform(self.LakePond['Lower_LargeLake_WT_O_Depth'] , \
                                                  self.LakePond['Upper_LargeLake_WT_O_Depth'])
            MediumLake_WT_Y_Depth = random.uniform(self.LakePond['Lower_MediumLake_WT_Y_Depth'] , \
                                                   self.LakePond['Upper_MediumLake_WT_Y_Depth'])
            MediumLake_WT_M_Depth = random.uniform(self.LakePond['Lower_MediumLake_WT_M_Depth'], \
                                                   self.LakePond['Upper_MediumLake_WT_M_Depth'])
            MediumLake_WT_O_Depth = random.uniform(self.LakePond['Lower_MediumLake_WT_O_Depth'], \
                                                   self.LakePond['Upper_MediumLake_WT_O_Depth'])
            SmallLake_WT_Y_Depth  = random.uniform(self.LakePond['Lower_SmallLake_WT_Y_Depth'], \
                                                   self.LakePond['Upper_SmallLake_WT_Y_Depth'])
            SmallLake_WT_M_Depth  = random.uniform(self.LakePond['Lower_SmallLake_WT_M_Depth'], \
                                                   self.LakePond['Upper_SmallLake_WT_M_Depth'])
            SmallLake_WT_O_Depth  = random.uniform(self.LakePond['Lower_SmallLake_WT_O_Depth'], \
                                                   self.LakePond['Upper_SmallLake_WT_O_Depth'])
                                        
        elif self.LakePond['Lake_Distribution'].lower() == 'uniform':
            #Lake_Depth = self.LakePond['Uniform_Lake_Depth']
            LargeLake_WT_Y_Depth  = self.LakePond['Uniform_Lake_Depth']
            LargeLake_WT_M_Depth  = self.LakePond['Uniform_Lake_Depth']
            LargeLake_WT_O_Depth  = self.LakePond['Uniform_Lake_Depht']
            MediumLake_WT_Y_Depth = self.LakePond['Uniform_Lake_Depth']
            MediumLake_WT_M_Depth = self.LakePond['Uniform_Lake_Depth']
            MediumLake_WT_O_Depth = self.LakePond['Uniform_Lake_Depth']
            SmallLake_WT_Y_Depth  = self.LakePond['Uniform_Lake_Depth']
            SmallLake_WT_M_Depth  = self.LakePond['Uniform_Lake_Depth']
            SmallLake_WT_O_Depth  = self.LakePond['Uniform_Lake_Depth']
        #------------------------------------
        # Determine Pond Depth Distribution
        #------------------------------------
        if self.LakePond['Pond_Distribution'].lower() == 'random':
            #Pond_Depth = random.uniform(self.LakePond['Lower_Pond_Depth'],\
            #                            self.LakePond['Upper_Pond_Depth'])
            Pond_WT_Y_Depth = random.uniform(self.LakePond['Lower_Pond_WT_Y_Depth'], \
                                             self.LakePond['Upper_Pond_WT_Y_Depth'])
            Pond_WT_M_Depth = random.uniform(self.LakePond['Lower_Pond_WT_M_Depth'], \
                                             self.LakePond['Upper_Pond_WT_M_Depth'])
            Pond_WT_O_Depth = random.uniform(self.LakePond['Lower_Pond_WT_O_Depth'], \
                                             self.LakePond['Upper_Pond_WT_O_Depth'])
        elif self.LakePond['Pond_Distribution'].lower() == 'uniform':
            #Pond_Depth = self.LakePond['Uniform_Pond_Depth']
            Pond_WT_Y_Depth = self.LakePond['Uniform_Pond_Depth']
            Pond_WT_M_Depth = self.LakePond['Uniform_Pond_Depth']
            Pond_WT_O_Depth = self.LakePond['Uniform_Pond_Depth']
            
        #--------------------------
        # Set Lake and Pond Depths
        # -------------------------
        #if self.ATTM_Lakes[i] > 0. :
        #    self.Lake_Depth[i] = Lake_Depth
        #if self.ATTM_Ponds[i] > 0. :
        #    self.Pond_Depth[i] = Pond_Depth
        if self.ATTM_LargeLakes_WT_Y[i] > 0.  : self.LargeLake_WT_Y_Depth[i] = LargeLake_WT_Y_Depth
        if self.ATTM_LargeLakes_WT_M[i] > 0.  : self.LargeLake_WT_M_Depth[i] = LargeLake_WT_M_Depth
        if self.ATTM_LargeLakes_WT_O[i] > 0.  : self.LargeLake_WT_O_Depth[i] = LargeLake_WT_O_Depth
        if self.ATTM_MediumLakes_WT_Y[i] > 0. : self.MediumLake_WT_Y_Depth[i] = MediumLake_WT_Y_Depth
        if self.ATTM_MediumLakes_WT_M[i] > 0. : self.MediumLake_WT_M_Depth[i] = MediumLake_WT_M_Depth
        if self.ATTM_MediumLakes_WT_O[i] > 0. : self.MediumLake_WT_O_Depth[i] = MediumLake_WT_O_Depth
        if self.ATTM_SmallLakes_WT_Y[i] > 0.  : self.SmallLake_WT_Y_Depth[i] = SmallLake_WT_Y_Depth
        if self.ATTM_SmallLakes_WT_M[i] > 0.  : self.SmallLake_WT_M_Depth[i] = SmallLake_WT_M_Depth
        if self.ATTM_SmallLakes_WT_O[i] > 0.  : self.SmallLake_WT_O_Depth[i] = SmallLake_WT_O_Depth
        if self.ATTM_Ponds_WT_Y[i] > 0.       : self.Pond_WT_Y_Depth[i] = Pond_WT_Y_Depth
        if self.ATTM_Ponds_WT_M[i] > 0.       : self.Pond_WT_M_Depth[i] = Pond_WT_M_Depth
        if self.ATTM_Ponds_WT_O[i] > 0.       : self.Pond_WT_O_Depth[i] = Pond_WT_O_Depth
            
    print '    done. \n  '
    
    # ------------------------------------------------
    # Create output files, plots, figures if desired
    # Update: 18 January 2018, Bolton
    #         Assuming that if 'Lake Depth Figure' Flag
    #         is set to 'yes', then all lakes regardless
    #         of size and age will be have a figure
    #         created in this section. This will reduce
    #         the number of flags that need to be set
    #         in the control file as well as the number
    #         of if/then statements required in this
    #         section.
    # ------------------------------------------------
    if self.LakePond['Lake_Depth_Figure'].lower() == 'yes':
        # Small Lakes, Wetland Tundra, Young age
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_Y/')
        lake_depth = np.reshape(self.SmallLake_WT_Y_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        fig = pl.figure
        pl.imshow(lake_depth, interpolation = 'nearest', cmap = 'spectral')
        pl.colorbar(extend = 'max', shrink = 0.92)
        pl.title('Inital Lake Depth \n Small Lakes, Wetland Tundra, Young age')
        pl.savefig('Initial_SmallLake_WT_Y_Depth.jpg', format = 'jpg')
        lake_depth.tofile('Initial_SmallLake_WT_Y_Depth.bin')
        pl.close()
        # Small Lakes, Wetland Tundra, Medium age
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_M/')
        lake_depth = np.reshape(self.SmallLake_WT_M_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        fig = pl.figure
        pl.imshow(lake_depth, interpolation = 'nearest', cmap = 'spectral')
        pl.colorbar(extend = 'max', shrink = 0.92)
        pl.title('Inital Lake Depth \n Small Lakes, Wetland Tundra, Medium age')
        pl.savefig('Initial_SmallLake_WT_M_Depth.jpg', format = 'jpg')
        lake_depth.tofile('Initial_SmallLake_WT_M_Depth.bin')
        pl.close()
        # Small Lakes, Wetland Tundra, Old age
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_O/')
        lake_depth = np.reshape(self.SmallLake_WT_O_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        fig = pl.figure
        pl.imshow(lake_depth, interpolation = 'nearest', cmap = 'spectral')
        pl.colorbar(extend = 'max', shrink = 0.92)
        pl.title('Inital Lake Depth \n Small Lakes, Wetland Tundra, Old age')
        pl.savefig('Initial_SmallLake_WT_O_Depth.jpg', format = 'jpg')
        lake_depth.tofile('Initial_SmallLake_WT_O_Depth.bin')
        pl.close()        
        # Medium Lakes, Wetland Tundra, Young age
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_Y/')
        lake_depth = np.reshape(self.MediumLake_WT_Y_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        fig = pl.figure
        pl.imshow(lake_depth, interpolation = 'nearest', cmap = 'spectral')
        pl.colorbar(extend = 'max', shrink = 0.92)
        pl.title('Inital Lake Depth \n Medium Lakes, Wetland Tundra, Young age')
        pl.savefig('Initial_MediumLake_WT_Y_Depth.jpg', format = 'jpg')
        lake_depth.tofile('Initial_MediumLake_WT_Y_Depth.bin')
        pl.close()
        # Medium Lakes, Wetland Tundra, Medium age
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_M/')
        lake_depth = np.reshape(self.MediumLake_WT_M_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        fig = pl.figure
        pl.imshow(lake_depth, interpolation = 'nearest', cmap = 'spectral')
        pl.colorbar(extend = 'max', shrink = 0.92)
        pl.title('Inital Lake Depth \n Medium Lakes, Wetland Tundra, Medium age')
        pl.savefig('Initial_MediumLake_WT_M_Depth.jpg', format = 'jpg')
        lake_depth.tofile('Initial_MediumLake_WT_M_Depth.bin')
        pl.close()  
        # Medium Lakes, Wetland Tundra, Old age
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_O/')
        lake_depth = np.reshape(self.MediumLake_WT_O_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        fig = pl.figure
        pl.imshow(lake_depth, interpolation = 'nearest', cmap = 'spectral')
        pl.colorbar(extend = 'max', shrink = 0.92)
        pl.title('Inital Lake Depth \n Medium Lakes, Wetland Tundra, Old age')
        pl.savefig('Initial_MediumLake_WT_O_Depth.jpg', format = 'jpg')
        lake_depth.tofile('Initial_MediumLake_WT_O_Depth.bin')
        pl.close()  
        # Large Lakes, Wetland Tundra, Young age
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_Y/')
        lake_depth = np.reshape(self.LargeLake_WT_Y_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        fig = pl.figure
        pl.imshow(lake_depth, interpolation = 'nearest', cmap = 'spectral')
        pl.colorbar(extend = 'max', shrink = 0.92)
        pl.title('Inital Lake Depth \n Large Lakes, Wetland Tundra, Young age')
        pl.savefig('Initial_LargeLake_WT_Y_Depth.jpg', format = 'jpg')
        lake_depth.tofile('Initial_LargeLake_WT_Y_Depth.bin')
        pl.close()
        # Large Lakes, Wetland Tundra, Medium age
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_M/')
        lake_depth = np.reshape(self.LargeLake_WT_M_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        fig = pl.figure
        pl.imshow(lake_depth, interpolation = 'nearest', cmap = 'spectral')
        pl.colorbar(extend = 'max', shrink = 0.92)
        pl.title('Inital Lake Depth \n Large Lakes, Wetland Tundra, Medium age')
        pl.savefig('Initial_LargeLake_WT_M_Depth.jpg', format = 'jpg')
        lake_depth.tofile('Initial_LargeLake_WT_M_Depth.bin')
        pl.close()
        # Large Lakes, Wetland Tundra, Old age
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_O/')
        lake_depth = np.reshape(self.LargeLake_WT_O_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        fig = pl.figure
        pl.imshow(lake_depth, interpolation = 'nearest', cmap = 'spectral')
        pl.colorbar(extend = 'max', shrink = 0.92)
        pl.title('Inital Lake Depth \n Large Lakes, Wetland Tundra, Old age')
        pl.savefig('Initial_LargeLake_WT_O_Depth.jpg', format = 'jpg')
        lake_depth.tofile('Initial_LargeLake_WT_O_Depth.bin')
        pl.close()

        # Return to Run Directory
        os.chdir(self.control['Run_dir'])
    # -----------------------------------------------------------------------------
    if self.LakePond['Lake_Depth_Figure'].lower() == 'yes':
        # Ponds, Wetland Tundra, Young age
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_Y/')
        pond_depth = np.reshape(self.Pond_WT_Y_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        fig = pl.figure
        pl.imshow(pond_depth, interpolation = 'nearest', cmap = 'spectral')
        pl.colorbar(extend = 'max', shrink = 0.92)
        pl.title('Inital Depth \n Ponds, Wetland Tundra, Young age')
        pl.savefig('Initial_Pond_WT_Y_Depth.jpg', format = 'jpg')
        lake_depth.tofile('Initial_Pond_WT_Y_Depth.bin')
        pl.close()
        # Ponds, Wetland Tundra, Medium age
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_M/')
        pond_depth = np.reshape(self.Pond_WT_Y_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        fig = pl.figure
        pl.imshow(pond_depth, interpolation = 'nearest', cmap = 'spectral')
        pl.colorbar(extend = 'max', shrink = 0.92)
        pl.title('Inital Depth \n Ponds, Wetland Tundra, Medium age')
        pl.savefig('Initial_Pond_WT_M_Depth.jpg', format = 'jpg')
        lake_depth.tofile('Initial_Pond_WT_M_Depth.bin')
        pl.close()
        # Ponds, Wetland Tundra, Old age
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_O/')
        pond_depth = np.reshape(self.Pond_WT_Y_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        fig = pl.figure
        pl.imshow(pond_depth, interpolation = 'nearest', cmap = 'spectral')
        pl.colorbar(extend = 'max', shrink = 0.92)
        pl.title('Inital Depth \n Ponds, Wetland Tundra, Old age')
        pl.savefig('Initial_Pond_WT_O_Depth.jpg', format = 'jpg')
        lake_depth.tofile('Initial_Pond_WT_O_Depth.bin')
        pl.close()        
        
        # Return to Run Directory
        os.chdir(self.control['Run_dir'])
