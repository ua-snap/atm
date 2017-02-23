import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def read_drainage_efficiency(self):#, PLOT, FIGURE, DISTRIBUTION):
    """
    The purpose of this module is to read (input) the drainage efficiency
    of each predisposed element.

    If the fractional area of cohorts is > 0.0, then there will be
    an assigned drainage efficiency (Below or Above)

    If there is no input file, drainage efficiency  will be randomly assigned.
    However, since we are working with Barrow, the probabibilty of the
    drainage efficiency of being 'below' the drainage efficiency threshold
    is set to 0.85.
    """

    print '    Reading drainage efficiency'

    self.drainage_efficiency = {}

    drainage = np.zeros(self.ATTM_nrows * self.ATTM_ncols)

    for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
        if self.ATTM_Total_Fractional_Area[i] > 0.0 :
            if self.Terrestrial['Drainage_Efficiency_Distribution'].lower() == 'random':
                chance = random.random()
                if chance > self.Terrestrial['Drainage_Efficiency_Random_Value']:
                    self.drainage_efficiency[i] = 'above'
                    drainage[i] = 1.
                else:
                    self.drainage_efficiency[i] = 'below'
                    drainage[i] = 2.          # redundant, but explicit
            elif self.Terrestrial['Drainage_Efficiency_Distribution'].lower() == 'above':
                self.drainage_efficiency[i] = 'above'
                drainage[i] = 1.
            elif self.Terrestrial['Drainage_Efficiency_Distribution'].lower() == 'below':
                self.drainage_efficiency[i] = 'below'
                drainage[i] = 2.
        else: 
            self.drainage_efficiency[i] = 'none'
            drainage[i] =0.

    print '    done.'
    print ' '

    # ==================================================
    # Create desired output files, figures, and plots
    # ==================================================
    if self.Terrestrial['Drainage_Efficiency_Figure'].lower() == 'yes':
        # -------------------------
        # Move to output directory
        # -------------------------
        if self.Simulation_area.lower() == 'barrow':
            os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow')

        # -----------------------
        # Create desired output
        # -----------------------
        drainage = np.reshape(drainage, [self.ATTM_nrows, self.ATTM_ncols])

        fig = pl.figure()
        pl.imshow(drainage, interpolation='nearest', cmap='bone')
        pl.colorbar( extend = 'max', shrink = 0.92)
        pl.title('Drainage efficiency')
        pl.savefig('./Initialization/Drainage_efficiency.png', format = 'png')
        drainage.tofile('./Initialization/Drainage_efficiency.bin')
        pl.close()

        os.chdir(self.control['Run_dir'])
