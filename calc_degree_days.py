import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
from scipy import interpolate
from scipy import integrate

def calc_degree_days(self):
    """
    The purpose of this module is to calculate the number of degree-days,
    both freezing and thawing for each simulation year.

    Data is from the SNAP monthly data used in a previous module.

    A spline is used to fit the data, after which the 'roots' are
    determined. The roots are the location (x-axis) where the spline
    intercects y=0.  The area between the roots will be either positive
    or negative (since basically a sine-function).  The area above
    or below the x-axis is integrated to determine the area (or total
    number of degree days).

    The index [0] indicates the integrated value.  The integration
    function also returns the error (I believe) at location [1].
    """

    if self.Met['met_distribution'].lower() == "point":
        print '   Calculating Thawing and Freezing Degree Days'

        self.dd_year = np.arange(min(self.Year), max(self.Year))
        self.degree_days = np.zeros([np.size(self.dd_year), 3])

        # The spline function
        spline = interpolate.UnivariateSpline(self.JD, self.Temp, s =20)

        # Main loop in module
        year = min(self.Year)
        k = 0
        for i in range(0, np.size(spline.roots())-2, 2):

            # Determine the location where the spline intersects y=0
            # Note: This is based upon looking at data prior to writing module, not
            #       set up for general use.
            tdd_start = spline.roots()[i]             # Thawing degree-days
            tdd_end   = spline.roots()[i+1]           # Thawing degree-day

            fdd_start = spline.roots()[i+1]           # Freezing degree-days
            fdd_end   = spline.roots()[i+2]           # Freezing degree-days

            # Integrate between root points
            thaw_dd = integrate.quad(spline, tdd_start, tdd_end)
            freeze_dd = integrate.quad(spline, fdd_start, fdd_end)

            #print i, year, thaw_dd[0], freeze_dd[0]
            # Place into array.  The
            self.degree_days[k,0] = year
            self.degree_days[k,1] = thaw_dd[0]
            self.degree_days[k,2] = freeze_dd[0]

            year = year + 1
            k = k + 1

        print '    done. \n  '

        """ Save/Show figure if desired """
        if self.Met['Degree_Day_Output'].lower() == 'yes':

            os.chdir(self.control['Run_dir']+self.Output_directory+'/Initialization')

            fig = pl.figure()
            pl.plot(self.degree_days[:,0], self.degree_days[:,1])
            pl.plot(self.degree_days[:,0], self.degree_days[:,2])
            pl.title('Thawing and Freezing Degree Days')
            pl.savefig("Degree_days_calculation.png", format = 'png')
            np.savetxt('Degree_Day_calculation.csv', self.degree_days, delimiter=', ', newline='\n')

            os.chdir(self.control['Run_dir'])
    else:
        ###################################################
        # SPATIAL DISTRIBUTION OF TEMPERATURE
        ###################################################
        print '   Calculating Thawing and Freezing Degree Days -- Spatial Distribution'

        self.dd_year = np.arange(min(self.Year), max(self.Year))
        print np.size(self.dd_year)
        print self.dd_year
        self.TDD     = np.zeros([np.size(self.dd_year), (self.ATTM_nrows * self.ATTM_ncols)])
        self.FDD     = np.zeros([np.size(self.dd_year), (self.ATTM_nrows * self.ATTM_ncols)])

        ###################################
        #   Start to Loop over elements   #
        ###################################

        ## fig = pl.figure()
        ## pl.plot(self.JD, self.Temp[:,162])
        ## pl.show()
        print max(self.Year)-min(self.Year)
        for element in range(self.ATTM_nrows * self.ATTM_ncols):
            print '..... working on element', element
            year = min(self.Year)
            k = 0
            tdd_count = 0
            fdd_count = 1
            
            # The spline function
#            spline = interpolate.UnivariateSpline(self.JD, self.Temp[:,element], s = 20)
#            spline = interpolate.UnivariateSpline(self.JD, self.Temp[:,element], s=20)
            spline = interpolate.UnivariateSpline(self.JD, self.Temp[:,element], s=10)
            # Main loop in module

#            if np.size(spline.roots()) == 0:
            if np.size(spline.roots()) < 50:
                self.TDD[:,element] = 0.0
                self.FDD[:,element] = 0.0
            else:
                for i in range(1, (np.size(self.dd_year)*2)):
#                    if i == 0:   # initial FDD, assuming 1/2 year
#                        fdd_end = spline.roots()[i]
#                        # integrate between 0 and first root point
#                        freeze_dd = integrate.quad(spline, 0, fdd_end)
#                        # put into FDD array
#                        self.FDD[fdd_count, element] = freeze_dd[0]*2.
#                        fdd_count = fdd_count + 1
                    if i % 2 == 0:   # even number = FDD
                        fdd_end = spline.roots()[i]
                        fdd_start = spline.roots()[i-1]
                        # integrate between start and end point
                        freeze_dd = integrate.quad(spline, fdd_start, fdd_end)
                        # put into FDD array
                        self.FDD[fdd_count, element] = freeze_dd[0]
                        # Assuming the 2nd year of freezing degree-days is the
                        # same as the first year.
 #                       print 'in freezing', i, freeze_dd[0], spline.roots()[i], spline.roots()[i-1]
                        if i == 2:
                            self.FDD[0,element] = freeze_dd[0]
                        fdd_count = fdd_count + 1
                    else:  # i is an odd number == TDD
                        tdd_end = spline.roots()[i]
                        tdd_start = spline.roots()[i-1]
                        # integrate between start and end point
                        thaw_dd = integrate.quad(spline, tdd_start, tdd_end)
                        # put into TDD array
                        self.TDD[tdd_count, element] = thaw_dd[0]
#                        print 'in thawing', i, thaw_dd[0], spline.roots()[i], spline.roots()[i-1]
                        tdd_count = tdd_count + 1
                    
                    
#                for i in range(0, np.size(spline.roots())-2, 2):
#
#                    # Determine the location where the spline intersects y=0
#                    # Note: This is based upon looking at data prior to writing module, not
#                    #       set up for general use.
#
#                    tdd_start = spline.roots()[i]             # Thawing degree-days
#                    tdd_end   = spline.roots()[i+1]           # Thawing degree-day

#                    fdd_start = spline.roots()[i+1]           # Freezing degree-days
#                    fdd_end   = spline.roots()[i+2]           # Freezing degree-days

#                    # Integrate between root points
#                    thaw_dd = integrate.quad(spline, tdd_start, tdd_end)
#                    freeze_dd = integrate.quad(spline, fdd_start, fdd_end)
                    
                    
#                    self.TDD[k,element] = thaw_dd[0]
#                    self.FDD[k,element] = freeze_dd[0]

                    year = year + 1


        ######################################################################################
        #
        # Create plots for animations
        #
        ######################################################################################
        if self.Met['Degree_Day_Output'].lower() == 'yes':
            if self.Simulation_area.lower() == 'barrow':
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Initialization/Degree_Days')
            elif self.Simulation_area.lower() == 'yukon':
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Yukon/Initialization/Degree_Days/')
                
            year = np.arange(min(self.Year), max(self.Year), dtype = np.int16)

            for k in range(0,np.size(self.dd_year)):

                TDD_plot = np.reshape(self.TDD[k,:], [int(self.ATTM_nrows), int(self.ATTM_ncols)])
                FDD_plot = np.reshape(self.FDD[k,:], [int(self.ATTM_nrows), int(self.ATTM_ncols)])


                year_plot = year[k]

                #--------------------------------------------------------
                # Thawing Degree Days
                #--------------------------------------------------------
                fig = pl.figure()
                pl.imshow(TDD_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 2500.0)
                pl.title('Thawing Degree-Days - '+str(year_plot))
                pl.colorbar(extend = 'neither', shrink = 0.92)
                pl.savefig(self.Met['TDD_Output']+'_'+str(year_plot)+'.jpg', format = 'jpg')
                TDD_plot.tofile(self.Met['TDD_Output']+'_'+str(year_plot)+'.bin')
                pl.close()
                #--------------------------------------------------------
                # Freezing Degree Days
                #--------------------------------------------------------
                fig = pl.figure()
                pl.imshow(FDD_plot, interpolation = 'nearest', cmap = 'spectral', vmin = -6000.0, vmax = -2000.0)
                pl.title('Freezing Degree-Days -'+str(year_plot))
                pl.colorbar(extend = 'neither', shrink = 0.92)
                pl.savefig(self.Met['FDD_Output']+'_'+str(year_plot)+'.jpg', format = 'jpg')
                FDD_plot.tofile(self.Met['FDD_Output']+'_'+str(year_plot)+'.bin')
                pl.close()

            os.chdir(self.control['Run_dir'])

        print '    done. \n  '

    print 'Finished calculating thawing and freezing degree days.'
