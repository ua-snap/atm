def read_degree_days(self, FIGURE):

    """
    The purpose of this module is to read the Thawing Degree
    Days and Freezing Degree Days from a series of binary
    files (one for each year). This is opposed to having
    the TDD and FDD calculated from geotiff files (long
    computer intensive effort).

    The TDD and FDD are then placed into an array, with
    each row representing one year and each column
    for each element.

    This method is only to be used when the meterologic
    data is spatially distributed.
    """

    # ========================
    # Required python modules
    import xlrd, xlwt
    import numpy as np
    import os, re
    from osgeo import gdal
    import gdalconst
    import pylab as pl
    from scipy import interpolate
    from scipy import integrate
    # =======================

    ################################
    # Read Thawing Degree Day Files
    ################################
    print ' '
    print 'Reading Thawing Degree Days'

    os.chdir(self.control['Run_dir']+self.Input_directory+'/Degree_Days')

    # Define output directory if figures are wanted
    dd_out_dir = self.control['Run_dir']+self.Output_directory+'/Initialization/Degree_Days/'

    """ NOTE: The TDD_file is located in the Input/Degree_Days/ directory """

    num_lines = sum(1 for line in open(self.TDD_file))

    # Set up TDD array
    self.TDD = np.zeros([num_lines, self.ATTM_nrows * self.ATTM_ncols])

    # Set counter
    count = 0
    year = np.arange(min(self.Year), max(self.Year), dtype = np.int16)
    
    # Read TDD Data
    with open(self.TDD_file) as f:
        for line in f:
            line = line.rstrip()          # removes \n at line end

            data = np.fromfile(str(line), dtype=float, count=-1, sep='')

            # Place TDD data into array
            self.TDD[count,:] = data.flatten()

            # Create plots if required
            if FIGURE == 'TRUE':
                TDD_plot = np.reshape(self.TDD[count,:], [int(self.ATTM_nrows), int(self.ATTM_ncols)])
                year_plot = year[count]
                #--------------------------------------------------------
                # Thawing Degree Days
                #--------------------------------------------------------
                fig = pl.figure()
                pl.imshow(TDD_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1000.0)
                pl.title('Thawing Degree-Days - '+str(year_plot))
                pl.colorbar(extend = 'neither', shrink = 0.92)
                pl.savefig(dd_out_dir+'Thawing_Degree_Days_'+str(year_plot)+'.jpg', format = 'jpg')
                pl.close()

            # Moving to the next line
            count = count + 1


    ################################
    # Read Freezing Degree Day Files
    ################################
    print 'Reading Freezing Degree Days'
    print ' '

    """ NOTE: The FDD_file is located in the Input/Degree_Days/ directory """

    # Set up TDD array
    self.FDD = np.zeros([num_lines, self.ATTM_nrows * self.ATTM_ncols])

    # Set counter
    count = 0
    year = np.arange(min(self.Year), max(self.Year), dtype = np.int16)
    
    # Read FDD Data
    with open(self.FDD_file) as f:
        for line in f:
            line = line.rstrip()          # removes \n at line end

            data = np.fromfile(str(line), dtype=float, count=-1, sep='')

            # Place TDD data into array
            self.FDD[count,:] = data.flatten()

            # Create Plots if required 
            if FIGURE == 'TRUE':
                FDD_plot = np.reshape(self.FDD[count,:], [int(self.ATTM_nrows), int(self.ATTM_ncols)])
                year_plot = year[count]
                #--------------------------------------------------------
                # Thawing Degree Days
                #--------------------------------------------------------
                fig = pl.figure()
                pl.imshow(FDD_plot, interpolation = 'nearest', cmap = 'spectral', vmin = -6000.0, vmax = -3500.0)
                pl.title('Freezing Degree-Days - '+str(year_plot))
                pl.colorbar(extend = 'neither', shrink = 0.92)
                pl.savefig(dd_out_dir+'Freezing_Degree_Days_'+str(year_plot)+'.jpg', format = 'jpg')
                pl.close()

            # Moving to the next line
            count = count + 1


    #---------------------------
    # RETURN TO RUN DIRECTORY
    #---------------------------
    os.chdir(self.control['Run_dir'])

    

