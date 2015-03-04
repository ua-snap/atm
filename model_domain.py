import numpy as np

def model_domain(self):
    """
    The purpose of this module is to create the model domain at a 1km x 1km
    resolution.

    A check to make sure all the cohort arrays have the same
    dimensions.
    """
    print '    Initialize model domain.'
    
    print '      In the model domain - checking dimensions'
    if (np.size(self.LCP) == np.size(self.Rivers) == np.size(self.Ponds) == \
        np.size(self.Lakes) == np.size(self.FCP) == np.size(self.Urban) == \
        np.size(self.NPG) == np.size(self.CLC) == np.size(self.HCP)):
        print '      All data arrays have the same dimensions'
    else:
        print '      Initial data array sizes are not all equal.'
        exit()

    
    print '         number of ATTM rows   : ', int((self.nrows * self.y_res) / float(self.Y_resolution))
    print '         number of ATTM columns: ', int((self.ncols * self.x_res) / float(self.X_resolution))
    self.ATTM_nrows = int((self.nrows * self.y_res) / float(self.Y_resolution))
    self.ATTM_ncols = int((self.ncols * self.x_res) / float(self.X_resolution))
# ---------------------------
    print '      done.'
    print ' '
