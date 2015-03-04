def read_met_data(self):

    """
    The purpose of this module is to read the monthly mean temperatures
    from for the specific meterologic file defined in the Control file.

    The units for temperature are degrees C.

    Data from SNAP, 5 model average, 2km resolution. pixel represents Barrow.
    (Need to get more specific about data source)

    If the data is a point measurement (i.e. scalar time-series values for
    the entire model domain), an excel file is used as the input.  If the data
    is spatially-distributed over time (i.e. grid stack), the data is derived from
    Geotif files specified in the meterologic file defined in the Control file.
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

    if self.met_distribution.lower() == 'point':
        print '    Reading Meteorologic Data (Monthly T and P)'

        # Work flow
        met = xlrd.open_workbook(self.control['Run_dir']+self.Input_directory+str('/')+self.met_file)

        sh = met.sheet_by_index(0)

        """ Set up data arrays """
        self.JD    = np.zeros(sh.nrows -1)            # Number of days since 1 Jan 2006
        self.Temp  = np.zeros(sh.nrows -1)            # Monthly Temperature [C]
        self.Prec  = np.zeros(sh.nrows -1)            # Monthly Precipitation [mm]
        self.Year  = np.zeros(sh.nrows -1)            # Year of data
        self.Month = np.zeros(sh.nrows -1)            # Month of data

        """ Read data into arrays """
        k = 0
        for j in range(1, sh.nrows):
            self.JD[k]     = float(sh.cell(j,0).value)
            self.Temp[k]   = float(sh.cell(j,1).value)
            self.Prec[k]   = float(sh.cell(j,2).value)
            self.Month[k]  = float(sh.cell(j,3).value)
            self.Year[k]   = float(sh.cell(j,4).value)
            k = k + 1

        # Determine number of model time steps
        self.ATTM_time_steps = max(self.Year) - min(self.Year)

        # End Statement
        print '    The number of model time steps is '+str(int(self.ATTM_time_steps)) + ' years.'
        print '    done.'
        print ' '
    ###################################
    # Spatial Data Sets Read
    ###################################
    else:
        print '   Reading Distributed Temperature Data...'
        print '   '
        
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Met/')
        #print '    Meterologic data used:', self.met_file
        #print ' '

        # Create Data Arrays
        # Format
        # JD (since 1 Jan 1901), MM, YY, AT[0], AT[1] ... AT[n]
        # ...
        # ... num_lines

        num_lines = sum(1 for line in open(self.met_file)) # Number of geotiff files
        print '    .... the number of met files to read is ', num_lines
        # Data arrays
        self.JD    = np.zeros(num_lines)
        self.Temp  = np.zeros([num_lines, self.ATTM_nrows * self.ATTM_ncols])
        self.Prec  = np.zeros([num_lines, self.ATTM_nrows * self.ATTM_ncols])
        self.Month = np.zeros(num_lines)
        self.Year  = np.zeros(num_lines)
        
        count = 0
        with open(self.met_file) as f:
            for line in f:
                #print re.split('[_ .]',line)  # Works -- splitting with multiple delimiters
                line = line.rstrip()           # removes the \n at the end
                
                # Calculate JD
                if count == 0 and re.split('[_ .]', line)[2] == '01':  # assuming January of first year
                    self.JD[count] = int(15)
                    
     #               count = count + 1
                else:
                    if count > 0 and re.split('[_ .]', line)[2] == '01':
                        self.JD[count] = self.JD[count-1] + 30
                    if count > 0 and re.split('[_ .]', line)[2] == '02':
                        self.JD[count] = self.JD[count-1] + 30
                    if count > 0 and re.split('[_ .]', line)[2] == '03':
                        self.JD[count] = self.JD[count-1] + 29
                    if count > 0 and re.split('[_ .]', line)[2] == '04':
                        self.JD[count] = self.JD[count-1] + 31
                    if count > 0 and re.split('[_ .]', line)[2] == '05':
                        self.JD[count] = self.JD[count-1] + 31    
                    if count > 0 and re.split('[_ .]', line)[2] == '06':
                        self.JD[count] = self.JD[count-1] + 30
                    if count > 0 and re.split('[_ .]', line)[2] == '07':
                        self.JD[count] = self.JD[count-1] + 30   
                    if count > 0 and re.split('[_ .]', line)[2] == '08':
                        self.JD[count] = self.JD[count-1] + 32
                    if count > 0 and re.split('[_ .]', line)[2] == '09':
                        self.JD[count] = self.JD[count-1] + 30
                    if count > 0 and re.split('[_ .]', line)[2] == '10':
                        self.JD[count] = self.JD[count-1] + 30
                    if count > 0 and re.split('[_ .]', line)[2] == '11':
                        self.JD[count] = self.JD[count-1] + 31
                    if count > 0 and re.split('[_ .]', line)[2] == '12':
                        self.JD[count] = self.JD[count-1] + 31

                # Month and Year Arrays
                self.Month[count] = re.split('[_ .]', line)[2]
                self.Year[count]  = re.split('[_ .]', line)[3]

                # Temperature Array
                dataset = gdal.Open(line, gdalconst.GA_ReadOnly)
                myarray = np.array(dataset.GetRasterBand(1).ReadAsArray())

                self.Temp[count,:] = myarray.flatten()

                # Moving on to the next line
                count = count + 1

            
        # Determine number of model time steps
        self.ATTM_time_steps = max(self.Year) - min(self.Year)

        # End Statement
        print '    The number of model time steps is '+str(int(self.ATTM_time_steps)) + ' years.'
        print '    done.'
        print ' '

        
