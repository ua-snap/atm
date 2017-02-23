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
    if self.Simulation_area.lower() == 'barrow' or self.Simulation_area.lower() == "arctic_coast":
        if (np.size(self.CLC_WT_M) == np.size(self.CLC_WT_O) == np.size(self.CLC_WT_Y) == \
            np.size(self.CoastalWaters_WT_O) == \
            np.size(self.DrainedSlope_WT_M) == np.size(self.DrainedSlope_WT_O) == np.size(self.DrainedSlope_WT_Y) == \
            np.size(self.FCP_WT_M) == np.size(self.FCP_WT_O) == np.size(self.FCP_WT_Y) ==  \
            np.size(self.HCP_WT_M) == np.size(self.HCP_WT_O) == np.size(self.HCP_WT_Y) == \
            np.size(self.LargeLakes_WT_M) == np.size(self.LargeLakes_WT_O) == np.size(self.LargeLakes_WT_Y) == \
            np.size(self.LCP_WT_M) == np.size(self.LCP_WT_O) == np.size(self.LCP_WT_Y) == \
            np.size(self.Meadow_WT_M) == np.size(self.Meadow_WT_O) == np.size(self.Meadow_WT_Y) == \
            np.size(self.MediumLakes_WT_M) == np.size(self.MediumLakes_WT_O) == np.size(self.MediumLakes_WT_Y) == \
            np.size(self.NoData_WT_O) == \
            np.size(self.Ponds_WT_M) == np.size(self.Ponds_WT_O) == np.size(self.Ponds_WT_Y) == \
            np.size(self.Rivers_WT_M) == np.size(self.Rivers_WT_O) == np.size(self.Rivers_WT_Y) == \
            np.size(self.SandDunes_WT_M) == np.size(self.SandDunes_WT_O) == np.size(self.SandDunes_WT_Y) == \
            np.size(self.SaturatedBarrens_WT_M) == np.size(self.SandDunes_WT_O) == np.size(self.SaturatedBarrens_WT_Y) == \
            np.size(self.Shrubs_WT_O) == \
            np.size(self.SmallLakes_WT_M) == np.size(self.SmallLakes_WT_O) == np.size(self.SmallLakes_WT_Y) == \
            np.size(self.Urban_WT)):
                                                 
                                                 
#        if (np.size(self.LCP) == np.size(self.Rivers) == np.size(self.Ponds) == \
#            np.size(self.Lakes) == np.size(self.FCP) == np.size(self.Urban) == \
#            np.size(self.NPG) == np.size(self.CLC) == np.size(self.HCP)):
            print '      All data arrays have the same dimensions'
    elif self.Simulation_area.lower() == 'tanana':
        if (np.size(self.TF_OB) == np.size(self.TF_OF) == np.size(self.TF_Con_PP) == \
            np.size(self.TF_Dec_PP) == np.size(self.TF_TL) == np.size(self.TF_YB) == \
            np.size(self.TF_YF)):
            print '    All data arrays have the same dimensions'
    elif self.Simulation_area.lower() == 'yukon':
        if (np.size(self.Barren_Yukon) == np.size(self.Bog_Yukon) == \
            np.size(self.DeciduousForest_Yukon) == np.size(self.DwarfShrub_Yukon) == \
            np.size(self.EvergreenForest_Yukon) == np.size(self.Fen_Yukon) == \
            np.size(self.Lake_Yukon) == np.size(self.Pond_Yukon) == \
            np.size(self.River_Yukon) == np.size(self.ShrubScrub_Yukon) == \
            np.size(self.Unclassified_Yukon)):
            print '    All data arrays have the same diminsions'
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
