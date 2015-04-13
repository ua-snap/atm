import numpy as np
import gdal, os, sys, glob, random
import pylab as pl


def set_ALD_constant(self):
    """
    The purpose of this module is basically to serve as a place-holder
    until I am able to read in the calculated active layer depths from
    the GIPL model output.

    The active layer will be determined based upon the initial thawing
    degree value at time 0.

    Each element is initialized with an active layer depth (random function
    now).  At each time step, a new active layer depth will be calculated
    by:

    ALD_initial / Thawing_Degree_Day(T=0)) = ALD_new (T=n) / Thawing_Degree_Day(T=n)

    ALD_new(T=n) = (ALD_initial/TDD(T=0)) * Thawing Degree Day (T=n)

    The term ALD_initial/TDD(T=0) will be constant for this place holder
    module.  This module is meant to calculate that constant so the
    new ALD will be the ALD factor * TDD at each time step.
    """

    print '    Determining Active Layer Constant'
    # set array
    self.ALD_Factor = np.zeros(self.ATTM_nrows * self.ATTM_ncols)

    if self.Met['met_distribution'].lower() == 'point':
        # populate array
        for i in range(0,(self.ATTM_nrows * self.ATTM_ncols)):
            self.ALD_Factor[i] = self.initial_ALD_depth[i] / self.degree_days[0,1]
    else:
        for i in range(0,(self.ATTM_nrows * self.ATTM_ncols)):
            self.ALD_Factor[i] = self.initial_ALD_depth[i] / self.TDD[0,i]
 
    print '    done. \n  '

    # ---------------------------------------
    # Output plots, figure, files if desired
    # ---------------------------------------
    ALD_Factor = np.reshape(self.ALD_Factor, [self.ATTM_nrows, self.ATTM_ncols])

    if self.Terrestrial['ALD_Factor_Output'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory)
        # Create output
        fig = pl.figure()
        pl.imshow(ALD_Factor, interpolation = 'nearest', cmap = 'bone')
        pl.colorbar( extend = 'max', shrink = 0.92)
        pl.savefig("./Initialization/Active_Layer_Factor.jpg", format = 'jpg')
        ALD_Factor.tofile('./Initialization/Active_Layer_Factor.bin')

        pl.close()

    # Return to Run Directory
    os.chdir(self.control['Run_dir'])

