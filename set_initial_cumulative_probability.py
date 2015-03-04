import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def set_initial_cumulative_probability(self):
        
    """
    Setting the cumulative probability array and initializing all cohorts in
    all elements to 0.0.
    
    """

    print '    Initializing Cumulative Probability of Initiation'
    # ---------------------------------------------------------------------
    # Array format is row = element, col = Probability of initiation value.
    #----------------------------------------------------------------------
    self.Wet_NPG_POI = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Wet_LCP_POI = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Wet_CLC_POI = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Wet_FCP_POI = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Wet_HCP_POI = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Gra_NPG_POI = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Gra_LCP_POI = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Gra_FCP_POI = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Gra_HCP_POI = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Shr_NPG_POI = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Shr_LCP_POI = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Shr_FCP_POI = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Shr_HCP_POI = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Lakes_POI   = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])
    self.Ponds_POI   = np.zeros([self.ATTM_nrows * self.ATTM_ncols, self.ATTM_time_steps])

    print '    done. \n  '
