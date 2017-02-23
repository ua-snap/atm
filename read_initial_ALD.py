import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def read_initial_ALD(self):
    """
    The purpose of this module is to read the initial active layer depth
    for each predisposed element in the model domain.

    Until there is true active layer depth, I am going to generate
    random depths between 0.3 - 0.75m as the input.
    """
    print '    Reading/setting initial active layer depths'

    self.initial_ALD_depth = np.zeros(self.ATTM_nrows * self.ATTM_ncols)
    initial_ALD = np.zeros(self.ATTM_nrows * self.ATTM_ncols)

    for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
        if self.ATTM_Total_Fractional_Area[i] > 0.0 :
            chance = random.uniform(self.Terrestrial['ALD_Distribution_Lower_Bound'],\
                                    self.Terrestrial['ALD_Distribution_Upper_Bound'])
            self.initial_ALD_depth[i] = chance
            initial_ALD[i] = chance

    #-----------------------------------------
    
    print '    done.'
    print '  '

    # ---------------------------------------------
    # Create desired output files, figures, plots
    # --------------------------------------------
    if self.Terrestrial['ALD_Distribution_Output'].lower() == 'yes':
        # -------------------------
        # Move to Output Directory
        # -------------------------
        if self.Simulation_area.lower() == 'barrow':
            os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow')

        # Create desired output
        initial_ALD = np.reshape(initial_ALD, [self.ATTM_nrows, self.ATTM_ncols])

        fig = pl.figure()
        pl.imshow(initial_ALD, interpolation='nearest', cmap='bone')
        pl.colorbar( extend = 'max', shrink = 0.92)
        pl.title('Initial Active Layer Depth')
        pl.savefig('./Initialization/Initial_ALD.jpg', format = 'jpg')
        initial_ALD.tofile('./Initialization/Initial_ALD.bin')
        pl.close()

        # Return to Run directory
        os.chdir(self.control['Run_dir'])
