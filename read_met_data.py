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
    import datetime
    # =======================

    if self.Met['met_distribution'].lower() == 'point':
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

        if self.Simulation_area.lower() == 'barrow':
            os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/Met/')
        elif self.Simulation_area.lower() == 'tanana':
            os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/Met/')
        elif self.Simulation_area.lower() == 'yukon':
            os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/Met/')
            
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
                
                if self.Met['met_file_distributed'] == 'BarrowAT_1901-2006':
                        # Calculate JD
                    if count == 0 : 
                        self.JD[count] = 1
                        d1 = datetime.datetime(int(re.split('[_ .]', line)[3]), \
                                               int(re.split('[_ .]', line)[2]), 1)
                    else:
                        d2 = datetime.datetime(int(re.split('[_ .]', line)[3]), \
                                               int(re.split('[_ .]', line)[2]), 1)
                        self.JD[count] = (d2-d1).days

                    # Month and Year Arrays
                    self.Month[count] = re.split('[_ .]', line)[2]
                    self.Year[count]  = re.split('[_ .]', line)[3]

                    # Temperature Array
                    dataset = gdal.Open(line, gdalconst.GA_ReadOnly)
                    myarray = np.array(dataset.GetRasterBand(1).ReadAsArray())

                    self.Temp[count,:] = myarray.flatten()

                    # Moving on to the next line
                    count = count + 1
                
                #####
                # New Barrow historical - 1901 - 2009
                #####   
                elif self.Met['met_file_distributed'].lower() == "barrow_at_1901-2009_v1":
                    os.chdir(self.control['Run_dir']+self.Input_directory+\
                             '/Temperature/Barrow_Peninsula_Air_Temp_1901-2009/Processed/')
                    if count == 0 : 
                        self.JD[count] = 1
                        d1 = datetime.datetime(int(re.split('[_ .]', line)[3]), \
                                               int(re.split('[_ .]', line)[2]), 1)
                    else:
                        d2 = datetime.datetime(int(re.split('[_ .]', line)[3]), \
                                               int(re.split('[_ .]', line)[2]), 1)
                        self.JD[count] = (d2-d1).days

                    # Month and Year Arrays
                    if count < num_lines:
                        self.Month[count] = re.split('[_ .]', line)[2]
                        self.Year[count]  = re.split('[_ .]', line)[3]

                    # Temperature Array
                    dataset = gdal.Open(line, gdalconst.GA_ReadOnly)
                    myarray = np.array(dataset.GetRasterBand(1).ReadAsArray())

                    self.Temp[count,:] = myarray.flatten()

                    # Moving on to the next line
                    count = count + 1

                #####
                # New Yukon Flats historical - 1901 - 2009
                #####   
                elif self.Met['met_file_distributed'].lower() == "yukon_flats_at_1901-2009_v1":
                    os.chdir(self.control['Run_dir']+self.Input_directory+\
                             '/Temperature/Yukon_Flats_Air_Temp_1901-2009/')
                    if count == 0 : 
                        self.JD[count] = 1
                        d1 = datetime.datetime(int(re.split('[_ .]', line)[3]), \
                                               int(re.split('[_ .]', line)[2]), 1)
                    else:
                        d2 = datetime.datetime(int(re.split('[_ .]', line)[3]), \
                                               int(re.split('[_ .]', line)[2]), 1)
                        self.JD[count] = (d2-d1).days

                    # Month and Year Arrays
                    if count < num_lines:
                        self.Month[count] = re.split('[_ .]', line)[2]
                        self.Year[count]  = re.split('[_ .]', line)[3]

                    # Temperature Array
                    dataset = gdal.Open(line, gdalconst.GA_ReadOnly)
                    myarray = np.array(dataset.GetRasterBand(1).ReadAsArray())

                    self.Temp[count,:] = myarray.flatten()

                    # Moving on to the next line
                    count = count + 1


                    
                elif self.Met['met_file_distributed'] == 'BarrowAT_2001-2100_cccma':
                    # Calculate JD
                    #if count == 0 and re.split('[_ .]', line)[3] == '01':  # assuming January of first year
                    #    self.JD[count] = int(15)
                    if count == 0:
                        self.JD[count] = 1
                        d1 = datetime.datetime(int(re.split('[_ .]', line)[4]), \
                                               int(re.split('[_ .]', line)[3]), 1)
                    else:
                        d2 = datetime.datetime(int(re.split('[_ .]', line)[4]), \
                                               int(re.split('[_ .]', line)[3]), 1)
                        self.JD[count] = (d2-d1).days

                    # Month and Year Arrays
                    self.Month[count] = re.split('[_ .]', line)[3]
                    self.Year[count] = re.split('[_ .]', line)[4]

                    # Temperature Array
                    dataset = gdal.Open(line, gdalconst.GA_ReadOnly)
                    myarray = np.array(dataset.GetRasterBand(1).ReadAsArray())

                    self.Temp[count,:] = myarray.flatten()

                    # Moving on to the next line
                    count = count + 1

                elif self.Met['met_file_distributed'] == 'BarrowAT_2001-2100_echam5':
                    if count == 0:
                        self.JD[count] = 1
                        d1 = datetime.datetime(int(re.split('[_ .]', line)[4]), \
                                               int(re.split('[_ .]', line)[3]), 1)
                    else:
                        d2 = datetime.datetime(int(re.split('[_ .]', line)[4]), \
                                               int(re.split('[_ .]', line)[3]), 1)
                        self.JD[count] = (d2-d1).days

                    # Month and Year Arrays
                    self.Month[count] = re.split('[_ .]', line)[3]
                    self.Year[count] = re.split('[_ .]', line)[4]

                    # Temperature Array
                    dataset = gdal.Open(line, gdalconst.GA_ReadOnly)
                    myarray = np.array(dataset.GetRasterBand(1).ReadAsArray())

                    self.Temp[count,:] = myarray.flatten()

                    # Moving on to the next line
                    count = count + 1
                    
                elif self.Met['met_file_distributed'] == 'BarrowAT_1901-2100_CCCMA':
                    # Calculate JD
                    #if count == 0 and re.split('[_ .]', line)[3] == '01':  # assuming January of first year
                    #    self.JD[count] = int(15)
                    if count == 0:
                        self.JD[count] = 1
                        d1 = datetime.datetime(int(re.split('[_ .]', line)[3]), \
                                               int(re.split('[_ .]', line)[2]), 1)
                    else:
                        if count < 1:  # Number of lines in the file listing geotifs to read
                            d2 = datetime.datetime(int(re.split('[_ .]', line)[3]), \
                                               int(re.split('[_ .]', line)[2]), 1)
                            self.JD[count] = (d2-d1).days
                        else:
                            d2 = datetime.datetime(int(re.split('[_ .]', line)[4]), \
                                               int(re.split('[_ .]', line)[3]), 1)

                    # Month and Year Arrays
                    if count < 1272:
                        self.Month[count] = re.split('[_ .]', line)[2]
                        self.Year[count] = re.split('[_ .]', line)[3]
                    else:
                        self.Month[count] = re.split('[_ .]', line)[3]
                        self.Year[count] = re.split('[_ .]', line)[4]
                    # Temperature Array
                    dataset = gdal.Open(line, gdalconst.GA_ReadOnly)
                    myarray = np.array(dataset.GetRasterBand(1).ReadAsArray())

                    self.Temp[count,:] = myarray.flatten()

                    # Moving on to the next line
                    count = count + 1
                
                elif self.Met['met_file_distributed'] == 'BarrowAT_1901-2100_ECHAM5':
                    # Calculate JD
                    #if count == 0 and re.split('[_ .]', line)[3] == '01':  # assuming January of first year
                    #    self.JD[count] = int(15)
                    if count == 0:
                        self.JD[count] = 1
                        d1 = datetime.datetime(int(re.split('[_ .]', line)[3]), \
                                               int(re.split('[_ .]', line)[2]), 1)
                    else:
                        if count < 1272:
                            d2 = datetime.datetime(int(re.split('[_ .]', line)[3]), \
                                               int(re.split('[_ .]', line)[2]), 1)
                            self.JD[count] = (d2-d1).days
                        else:
                            d2 = datetime.datetime(int(re.split('[_ .]', line)[4]), \
                                               int(re.split('[_ .]', line)[3]), 1)

                    # Month and Year Arrays
                    if count < 1272:
                        self.Month[count] = re.split('[_ .]', line)[2]
                        self.Year[count] = re.split('[_ .]', line)[3]
                    else:
                        self.Month[count] = re.split('[_ .]', line)[3]
                        self.Year[count] = re.split('[_ .]', line)[4]
                    # Temperature Array
                    dataset = gdal.Open(line, gdalconst.GA_ReadOnly)
                    myarray = np.array(dataset.GetRasterBand(1).ReadAsArray())

                    self.Temp[count,:] = myarray.flatten()

                    # Moving on to the next line
                    count = count + 1
            
        # Determine number of model time steps
        self.ATTM_time_steps = int(max(self.Year) - min(self.Year))
        
        # End Statement
        print '    The number of model time steps is '+str(int(self.ATTM_time_steps)) + ' years.'
        print '    done.'
        print ' '

        
