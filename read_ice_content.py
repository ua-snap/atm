import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def read_ice_content(self):
    """
    The purpose of this module is to read (input) the ground ice
    content of each predisposed element.

    If the fractional area of cohorts is > 0.0, then there will be
    an assigned ice content. The possible ice content values are:
    Poor, Pore, Wedge, and Massive

    If there is no input file, ice content will be randomly assigned.
    """
    print '    Reading ground ice content.'
    ice_content = ('poor', 'pore', 'wedge', 'massive')
    self.ice = {}
    ice = np.zeros(self.ATTM_nrows * self.ATTM_ncols)

    for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
        if self.ATTM_Total_Fractional_Area[i] == 0.0 :
            self.ice[i] = 'none'
            ice[i] = 0.0          # redundant, but explicit
        else:
            if self.Terrestrial['Ice_Distribution'].lower() == 'poor':
                self.ice[i] = 'poor'
                ice[i] = 1.
            elif self.Terrestrial['Ice_Distribution'].lower() == 'pore':
                self.ice[i] = 'poor'
                ice[i] = 2.
            elif self.Terrestrial['Ice_Distribution'].lower() == 'wedge':
                self.ice[i] = 'wedge'
                ice[i] = 3.
            elif self.Terrestrial['Ice_Distribution'].lower() == 'massive':
                self.ice[i] = 'massive'
                ice[i] = 4.
            elif self.Terrestrial['Ice_Distribution'].lower() == 'random':
                self.ice[i] = random.choice(ice_content)  
                if self.ice[i] == 'poor'    : ice[i] = 1.
                if self.ice[i] == 'pore'    : ice[i] = 2.
                if self.ice[i] == 'wedge'   : ice[i] = 3.
                if self.ice[i] == 'massive' : ice[i] = 4.
            
    print '    done.'
    print ' '

    #=================================================================
    # Output figures, files, plots
    #=================================================================
#    if PLOT == 'TRUE' or FIGURE == 'TRUE':
    if self.Terrestrial['Ice_Distribution_Figure'].lower() == 'yes':    
        ice_plot = np.reshape(ice, [self.ATTM_nrows, self.ATTM_ncols])
        # ---------------------------
        # Change to output directory
        # --------------------------
        if self.Simulation_area.lower() == 'barrow':
            os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow')

        # --------------------------
        # Figure / file creation
        # --------------------------
        fig = pl.figure()
        pl.imshow(ice_plot, interpolation='nearest', cmap='bone')
        pl.colorbar( extend = 'max', shrink = 0.92)
        pl.title('Ground Ice Content')
        pl.savefig('./Initialization/Ground_Ice_Content.png', format = 'png')
        ice_plot.tofile('./Initialization/Ground_Ice_Content.bin')
        pl.close()

        # ----------------------------
        # Move back to run directory
        # ----------------------------
        os.chdir(self.control['Run_dir'])
