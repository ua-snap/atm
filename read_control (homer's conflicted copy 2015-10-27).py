def read_control(self):
    """
    The purpose of this module is to open and read the control file into a
    control dictionary. The control file contains information such as Input 
    directory, Output directory, file names, etc.

    The name of the control file is specified at the command line as
    the first option following the program name. See example below.
    ------------------------------
    python ATTM.py Control
    ------------------------------
    In this case, the file named "Control" is the control file, located in 
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
    
    """ Simulation area """
    self.Simulation_area    = self.control['Simulation_area']
    
    """ Start Initialization Process """
    if self.Simulation_area.lower() == 'barrow':
        self.Initialize_Control = self.control['Run_dir']+self.Input_directory+\
                                  '/Barrow/'+self.control['Initialize_Control']
        self.Terrestrial_Control = self.control['Run_dir']+self.Input_directory+\
                                   '/Barrow/'+self.control['Terrestrial_Control']
    elif self.Simulation_area.lower() == 'tanana':
        self.Initialize_Control = self.control['Run_dir']+self.Input_directory+\
                                  '/Tanana/'+self.control['Initialize_Control']
        self.Terrestrial_Control = self.control['Run_dir']+self.Input_directory+\
                                   '/Tanana/'+self.control['Terrestrial_Control']
    
    """ Flag for Geotiff Layer Input & Output """
    self.Read_Geotiff     = self.control['Read_Geotiff']
    self.Write_Geotiff    = self.control['Write_Geotiff']

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
    self.Terrestrial_Control     = self.control['Terrestrial_Control']
    self.Wet_NPG_Control         = self.control['Wet_NPG_Control']
    self.Wet_LCP_Control         = self.control['Wet_LCP_Control']
    self.Wet_CLC_Control         = self.control['Wet_CLC_Control']
    self.Wet_FCP_Control         = self.control['Wet_FCP_Control']
    self.Wet_HCP_Control         = self.control['Wet_HCP_Control']

    """ File containing information about Lake and Pond Variables and Parameters """
    self.Lake_Pond_Control       = self.control['Lake_Pond_Control']



    
    # ------------------------------
    # Finished Reading Control File
    # ------------------------------
    print '    done.'
    print ' '
