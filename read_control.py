def read_control(self):
    """
    The purpose of this module is to open and read the control file into a
    control dictionary. The control file contains information such as Input
    directory, Output directory, file names, etc.

    The name of the control file is specified at the command line as
    the first option following the program name. See example below.
    ------------------------------
    python ATM.py Control
    ------------------------------
    In this case, the file named 'Control' is the control file, located in
    the same directory as this file.

    ##################################
    NTB!  Fill more here as needed
    ##################################
    """
    print '    Reading control file: ', self.Control_file
    self.control = {}
    with open(self.Control_file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.control[(key)] = val

    """ Run, Input and Output Directories """
    self.Run_directory      = self.control['Run_dir']
    self.Input_directory    = self.control['Input_dir']
    self.Output_directory   = self.control['Output_dir']
    self.Control_directory  = self.control['Control_dir']
    """ Simulation area """
    self.Simulation_area    = self.control['Simulation_area']

    """ Start Initialization Process """
    if self.Simulation_area.lower() == 'barrow':
        self.Initialize_Control = self.control['Run_dir']+self.Input_directory+\
                                  '/Barrow/'+self.Control_directory+\
                                  '/'+self.control['Initialize_Control']
        self.Terrestrial_Control = self.control['Run_dir']+self.Input_directory+\
                                   '/Barrow/'+self.Control_directory+'/'+\
                                   self.control['Terrestrial_Control']
    elif self.Simulation_area.lower() == 'tanana':
        self.Initialize_Control = self.control['Run_dir']+self.Input_directory+\
                                  '/Tanana/'+self.control['Initialize_Control']
        self.Terrestrial_Control = self.control['Run_dir']+self.Input_directory+\
                                   '/Tanana/'+self.control['Terrestrial_Control']
    elif self.Simulation_area.lower() == 'yukon':
        self.Initialize_Control = self.control['Run_dir']+self.Input_directory+ \
                                  '/Yukon/'+self.control['Initialize_Control']
        self.Terrestrial_Control = self.control['Run_dir']+self.Input_directory+ \
                                  '/Yukon/'+self.control['Terrestrial_Control']

    """ Flag for Geotiff Layer Input & Output """
    self.Read_Geotiff     = self.control['Read_Geotiff']
    self.Write_Geotiff    = self.control['Write_Geotiff']
    self.Initial_Cohort_List = self.control['Initial_Cohort_List']

    """ Read ATTM model resolution """
    self.X_resolution            = self.control['X_model_resolution']             # Col dimension
    self.Y_resolution            = self.control['Y_model_resolution']             # Row dimension

    """ Read Met Data file name """
    self.Met_Control		 = self.control['Met_Control']

    """ Read Archiving / Reporting Material """
    self.results_onscreen        = self.control['Results_onscreen']
    self.archive_simulation      = self.control['Archive_simulation']
    self.archive_data            = self.control['Archive_data']
    self.simulation_name         = self.control['Simulation_name']
    self.notes_file              = self.control['Notes_file']

    """ Code Testing Simulations """
    self.test_code               = self.control['Test_code']
    self.test_code_duration      = int(self.control['Test_code_duration'])

    """ File containing Terrestrial Cohorts Variables & Parameters """
    #    self.Terrestrial_Control     = self.control['Terrestrial_Control']
    if self.Simulation_area.lower() == 'barrow':
        self.Wet_NPG_Control         = self.control['Wet_NPG_Control']
        self.Wet_LCP_Control         = self.control['Wet_LCP_Control']
        self.Wet_CLC_Control         = self.control['Wet_CLC_Control']
        self.Wet_FCP_Control         = self.control['Wet_FCP_Control']
        self.Wet_HCP_Control         = self.control['Wet_HCP_Control']
        # Below are new cohorts that will be used for Barrow/AK_ACP products
        self.CLC_WT_M_Control           = self.control['CLC_WT_M_Control']                     # Coalescent Low Center Polygon, Wetland Tundra, Medium age
        self.CLC_WT_O_Control           = self.control['CLC_WT_O_Control']                     # Coalescent Low Center Polygon, Wetland Tundra, Old age
        self.CLC_WT_Y_Control           = self.control['CLC_WT_Y_Control']                     # Coalescent Low Center Polygon, Wetland Tundra, Young age
        self.CoastalWaters_WT_O_Control = self.control['CoastalWaters_WT_O_Control']           # Coastal Waters, Wetland Tundra, Old age
        self.DrainedSlope_WT_M_Control  = self.control['DrainedSlope_WT_M_Control']            # Coastal Waters, Wetland Tundra, Medium age
        self.DrainedSlope_WT_O_Control  = self.control['DrainedSlope_WT_O_Control']            # Drained slope, Wetland Tundra, Old age
        self.DrainedSlope_WT_Y_Control  = self.control['DrainedSlope_WT_Y_Control']            # Drained slope, Wetland Tundra, Young age
        self.FCP_WT_M_Control           = self.control['FCP_WT_M_Control']                     # Flat Center Polygon, Wetland Tundra, Medium age
        self.FCP_WT_O_Control           = self.control['FCP_WT_O_Control']                     # Flat Center Polygon, Wetland Tundra, Old age
        self.FCP_WT_Y_Control           = self.control['FCP_WT_Y_Control']                     # Flat Center Polygon, Wetland Tundra, Young age
        self.HCP_WT_M_Control           = self.control['HCP_WT_M_Control']                     # High Center Polygon, Wetland Tundra, Medium age
        self.HCP_WT_O_Control           = self.control['HCP_WT_O_Control']                     # High Center Polygon, Wetland Tundra, Old age
        self.HCP_WT_Y_Control           = self.control['HCP_WT_Y_Control']                     # High Center Polygon, Wetland Tundra, Young age
        self.LCP_WT_M_Control           = self.control['LCP_WT_M_Control']                     # Low Center Polygon, Wetland Tundra, Medium age
        self.LCP_WT_O_Control           = self.control['LCP_WT_O_Control']                     # Low Center Polygon, Wetland Tundra, Old age
        self.LCP_WT_Y_Control           = self.control['LCP_WT_Y_Control']                     # Low Center Polygon, Wetland Tundra, Young age
        self.Meadow_WT_M_Control        = self.control['Meadow_WT_M_Control']                  # Meadow, Wetland Tundra, Medium age
        self.Meadow_WT_O_Control        = self.control['Meadow_WT_O_Control']                  # Meadow, Wetland Tundra, Old age
        self.Meadow_WT_Y_Control        = self.control['Meadow_WT_Y_Control']                  # Meadow, Wetland Tundra, Young age
        self.NoData_WT_O_Control        = self.control['NoData_WT_O_Control']                  # No Data, Wetland Tundra, Old age
        self.SandDunes_WT_M_Control     = self.control['SandDunes_WT_M_Control']               # Sand Dunes, Wetland Tundra, Medium age
        self.SandDunes_WT_O_Control     = self.control['SandDunes_WT_O_Control']               # Sand Dunes, Wetland Tundra, Old age
        self.SandDunes_WT_Y_Control     = self.control['SandDunes_WT_Y_Control']               # Sand Dunes, Wetland Tundra, Young age
        self.SaturatedBarrens_WT_M_Control = self.control['SaturatedBarrens_WT_M_Control']     # Saturated Barrens, Wetland Tundra, Medium age
        self.SaturatedBarrens_WT_O_Control = self.control['SaturatedBarrens_WT_O_Control']     # Saturated Barrens, Wetland Tundra, Old age
        self.SaturatedBarrens_WT_Y_Control = self.control['SaturatedBarrens_WT_Y_Control']     # Saturated Barrens, Wetland Tundra, Young age
        self.Shrubs_WT_O_Control           = self.control['Shrubs_WT_O_Control']               # Shrubs, Wetland Tundra, Old age
        self.Urban_WT_Control              = self.control['Urban_WT_Control']                # Urban, Wetland Tundra, Old age
        """ File containing information about Lake and Pond Variables and Parameters """
        self.Lake_Pond_Control        = self.control['Lake_Pond_Control']
        self.LargeLakes_WT_M_Control  = self.control['LargeLakes_WT_M_Control']                # Large Lakes, Wetland Tundra, Medium age
        self.LargeLakes_WT_O_Control  = self.control['LargeLakes_WT_O_Control']                # Large Lakes, Wetland Tundra, Old age
        self.LargeLakes_WT_Y_Control  = self.control['LargeLakes_WT_Y_Control']                # Large Lakes, Wetland Tundra, Young age
        self.MediumLakes_WT_M_Control = self.control['MediumLakes_WT_M_Control']               # Medium Lakes, Wetland Tundra, Medium age
        self.MediumLakes_WT_O_Control = self.control['MediumLakes_WT_O_Control']               # Medium Lakes, Wetland Tundra, Old age
        self.MediumLakes_WT_Y_Control = self.control['MediumLakes_WT_Y_Control']               # Medium Lakes, Wetland Tundra, Young age
        self.SmallLakes_WT_M_Control  = self.control['SmallLakes_WT_M_Control']                # Small Lakes, Wetland Tundra, Medium age
        self.SmallLakes_WT_O_Control  = self.control['SmallLakes_WT_O_Control']                # Small Lakes, Wetland Tundra, Old age
        self.SmallLakes_WT_Y_Control  = self.control['SmallLakes_WT_Y_Control']                # Small Lakes, Wetland Tundra, Young age
        self.Ponds_WT_M_Control       = self.control['Ponds_WT_M_Control']                     # Ponds, Wetland Tundra, Medium age
        self.Ponds_WT_O_Control       = self.control['Ponds_WT_O_Control']                     # Ponds, Wetland Tundra, Old age
        self.Ponds_WT_Y_Control       = self.control['Ponds_WT_Y_Control']                     # Ponds, Wetland Tundra, Young age
        self.Rivers_WT_M_Control      = self.control['Rivers_WT_M_Control']                    # Rivers, Wetland Tundra, Medium age
        self.Rivers_WT_O_Control      = self.control['Rivers_WT_O_Control']                    # Rivers, Wetland Tundra, Old age
        self.Rivers_WT_Y_Control      = self.control['Rivers_WT_Y_Control']                    # Rivers, Wetland Tundra, Young age
        """ File containing information about Yukon River Test area Variables  and Parameters """
    elif self.Simulation_area.lower() == 'yukon':
        self.Barren_Yukon_Control          = self.control['Barren_Yukon_Control']                   #
        self.Bog_Yukon_Control             = self.control['Bog_Yukon_Control']
        self.DeciduousForest_Yukon_Control = self.control['DeciduousForest_Yukon_Control']
        self.DwarfShrub_Yukon_Control      = self.control['DwarfShrub_Yukon_Control']
        self.Fen_Yukon_Control             = self.control['Fen_Yukon_Control']
        self.EvergreenForest_Yukon_Control = self.control['EvergreenForest_Yukon_Control']
        self.Lake_Yukon_Control            = self.control['Lake_Yukon_Control']
        self.Pond_Yukon_Control            = self.control['Pond_Yukon_Control']
        self.River_Yukon_Control           = self.control['River_Yukon_Control']
        self.ShrubScrub_Yukon_Control      = self.control['ShrubScrub_Yukon_Control']
        self.Unclassified_Yukon_Control    = self.control['Unclassified_Yukon_Control']
        self.Young_Bog_Flag                = self.control['Young_Bog_Flag']
        self.Young_Fen_Flag                = self.control['Young_Fen_Flag']
        self.Lower_Bog_Percentage          = self.control['Lower_Bog_Percentage']
        self.Upper_Bog_Percentage          = self.control['Upper_Bog_Percentage']
        self.Lower_Fen_Percentage          = self.control['Lower_Fen_Percentage']
        self.Upper_Fen_Percentage          = self.control['Upper_Fen_Percentage']

        # Convert string variables if necessary
        self.Lower_Bog_Percentage          = float(self.Lower_Bog_Percentage)
        self.Upper_Bog_Percentage          = float(self.Upper_Bog_Percentage)
        self.Lower_Fen_Percentage          = float(self.Lower_Fen_Percentage)
        self.Upper_Fen_Percentage          = float(self.Upper_Fen_Percentage)
    # ------------------------------
    # Finished Reading Control File
    # ------------------------------
    print '    done.'
    print ' '
