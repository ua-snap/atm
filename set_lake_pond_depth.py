import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def set_lake_pond_depth(self, PLOT, FIGURE):
    
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

    
#    self.initial_Lake_depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
#    self.initial_Pond_depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)

    self.Lake_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    self.Pond_Depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)

    for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
        Lake_Depth = random.uniform(2.2, 5.0)
        Pond_Depth = random.uniform(1.25, 1.7)
        if self.ATTM_Lakes[i] > 0. :
#            self.initial_Lake_depth[i] = Lake_Depth
            self.Lake_Depth[i] = Lake_Depth
        if self.ATTM_Ponds[i] > 0. :
#            self.initial_Pond_depth[i] = Pond_Depth
            self.Pond_Depth[i] = Pond_Depth

    print '    done. \n  '
    
    # ------------------------------------------------
    # Create output files, plots, figures if desired
    # ------------------------------------------------
    if FIGURE == 'TRUE' or PLOT == 'TRUE':

        lake_depth = np.reshape(self.Lake_Depth, [self.ATTM_nrows, self.ATTM_ncols])
        pond_depth = np.reshape(self.Pond_Depth, [self.ATTM_nrows, self.ATTM_ncols])

        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory)

        # Lakes output
        fig = pl.figure()
        pl.imshow(lake_depth, interpolation = 'nearest', cmap = 'bone')
        pl.colorbar( extend = 'max', shrink = 0.92)
        pl.title('Initial Lake Depths')
        if FIGURE == 'TRUE':
            pl.savefig('./Lakes/Initial_Lake_Depth.png', format = 'png')
            lake_depth.tofile('./Lakes/Initial_Lake_Depth.bin')
        if PLOT == 'TRUE':
            pl.show()
        pl.close()

        # Ponds Output
        fig = pl.figure()
        pl.imshow(pond_depth, interpolation = 'nearest', cmap = 'bone')
        pl.colorbar( extend = 'max', shrink = 0.92)
        pl.title('Initial Pond (shallow lake) Depths')
        if FIGURE == 'TRUE':
            pl.savefig('./Ponds/Initial_Pond_Depth.png', format = 'png')
            pond_depth.tofile('./Ponds/Initial_Pond_Depth.bin')
        if PLOT == 'TRUE':
            pl.show()
        pl.close()
        
        # Return to Run Directory
        os.chdir(self.control['Run_dir'])
