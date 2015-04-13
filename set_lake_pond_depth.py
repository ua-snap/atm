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

    self.pond_count = 0.0       # For use in check_ponds.


    self.Lake_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.Pond_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)

    for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
        #------------------------------------
        # Determine Lake Depth Distribution
        #------------------------------------
        if self.LakePond['Lake_Distribution'].lower() == 'random':
            Lake_Depth = random.uniform(self.LakePond['Lower_Lake_Depth'], \
                                        self.LakePond['Upper_Lake_Depth'])
        elif self.LakePond['Lake_Distribution'].lower() == 'uniform':
            Lake_Depth = self.LakePond['Uniform_Lake_Depth']
        #------------------------------------
        # Determine Pond Depth Distribution
        #------------------------------------
        if self.LakePond['Pond_Distribution'].lower() == 'random':
            Pond_Depth = random.uniform(self.LakePond['Lower_Pond_Depth'],\
                                        self.LakePond['Upper_Pond_Depth'])
        elif self.LakePon['Pond_Distribution'].lower() == 'uniform':
            Pond_Depth = self.LakePond['Uniform_Pond_Depth']
        
        #--------------------------
        # Set Lake and Pond Depths
        # -------------------------
        if self.ATTM_Lakes[i] > 0. :
            self.Lake_Depth[i] = Lake_Depth
        if self.ATTM_Ponds[i] > 0. :
            self.Pond_Depth[i] = Pond_Depth

    print '    done. \n  '
    
    # ------------------------------------------------
    # Create output files, plots, figures if desired
    # ------------------------------------------------
    if self.LakePond['Lake_Depth_Figure'].lower() == 'yes':
        
        lake_depth = np.reshape(self.Lake_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        os.chdir(self.control['Run_dir']+self.Output_directory)

        # Lakes Figure
        fig = pl.figure()
        pl.imshow(lake_depth, interpolation = 'nearest', cmap = 'bone')
        pl.colorbar( extend = 'max', shrink = 0.92)
        pl.title('Initial Lake Depths')
        pl.savefig('./Lakes/Initial_Lake_Depth.jpg', format = 'jpg')
        lake_depth.tofile('./Lakes/Initial_Lake_Depth.bin')
        pl.close()

        os.chdir(self.control['Run_dir'])
    # -----------------------------------------------------------------------------
    if self.LakePond['Pond_Depth_Figure'].lower() == 'yes':

        pond_depth = np.reshape(self.Pond_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory)
        # Ponds Figure
        fig = pl.figure()
        pl.imshow(pond_depth, interpolation = 'nearest', cmap = 'bone')
        pl.colorbar( extend = 'max', shrink = 0.92)
        pl.title('Initial Pond (shallow lake) Depths')
        pl.savefig('./Ponds/Initial_Pond_Depth.jpg', format = 'jpg')
        pond_depth.tofile('./Ponds/Initial_Pond_Depth.bin')
        pl.close()
        
        # Return to Run Directory
        os.chdir(self.control['Run_dir'])
