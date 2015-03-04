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
            (key, val) = line.split()
            self.control[(key)] = val

    """ Input and Output Directories """
    self.Run_directory    = self.control['Run_dir']
    self.Input_directory  = self.control['Input_dir']
    self.Output_directory = self.control['Output_dir']

    """ Flag for Geotiff Layer Input & Output """
    self.Read_Geotiff     = self.control['Read_Geotiff']
    self.Write_Geotiff    = self.control['Write_Geotiff']

    """ Read ATTM model resolution """
    self.X_resolution            = self.control['X_model_resolution']             # Col dimension
    self.Y_resolution            = self.control['Y_model_resolution']             # Row dimension

    """ Read Met Data file name """
    self.met_distribution        = self.control['met_distribution']               # Spatial or point distribution
    if self.met_distribution.lower() == 'point':
        self.met_file                = self.control['met_file_point']             # Met data file, in xls format
    else:
        self.met_file                = self.control['met_file_distributed'] # List of GeoTiff files

    print '       The meteorologic file to be used is :', self.met_file

    """ Read Degree Day Calculation Method and Files """
    self.degree_day_method       = self.control['degree_day_method']
    self.TDD_file                = self.control['TDD_file']
    self.FDD_file                = self.control['FDD_file']

    """ Read Archiving / Reporting Material """
    self.archive_simulation      = self.control['Archive_simulation']
    self.archive_data            = self.control['Archive_data']
    self.simulation_name         = self.control['Simulation_name']
    self.notes_file              = self.control['Notes_file']

    """ Code Testing Simulations """
    self.test_code               = self.control['Test_code']
 
    #
    # Finished Reading Control File
    # 
    print '    done.'
    print ' '
