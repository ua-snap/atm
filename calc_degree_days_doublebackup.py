import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
from scipy import interpolate
from scipy import integrate

def calc_degree_days(self, PLOT, FIGURE):
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

    if self.met_distribution.lower() == "point":
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
        if PLOT == 'TRUE' or FIGURE == 'TRUE':

            os.chdir(self.control['Run_dir']+self.Output_directory+'/Initialization')

            fig = pl.figure()
            pl.plot(self.degree_days[:,0], self.degree_days[:,1])
            pl.plot(self.degree_days[:,0], self.degree_days[:,2])
            pl.title('Thawing and Freezing Degree Days')
            if FIGURE == 'TRUE':
                pl.savefig("Degree_days_calculation.png", format = 'png')
                np.savetxt('Degree_Day_calculation.csv', self.degree_days, delimiter=', ', newline='\n')
            if PLOT == 'TRUE':
                pl.show()

            os.chdir(self.control['Run_dir'])
    else:
        ###################################################
        # SPATIAL DISTRIBUTION OF TEMPERATURE
        ###################################################
        print '   Calculating Thawing and Freezing Degree Days -- Spatial Distribution'
        
        self.dd_year = np.arange(min(self.Year), max(self.Year))
        self.TDD     = np.zeros([np.size(self.dd_year), (self.ATTM_nrows * self.ATTM_ncols)])
        self.FDD     = np.zeros([np.size(self.dd_year), (self.ATTM_nrows * self.ATTM_ncols)])

                
        print ' '
        print np.arange(min(self.Year), max(self.Year))


        ###################################
        #   Start to Loop over elements   #
        ###################################
 
        ## fig = pl.figure()
        ## pl.plot(self.JD, self.Temp[:,162])
        ## pl.show()

        
 
        for element in range(self.ATTM_nrows * self.ATTM_ncols):

            print '     Processing element '+str(element)
            
            # The spline function
            spline = interpolate.UnivariateSpline(self.JD, self.Temp[:,element], s = 20)

            year = min(self.Year)
            k = 0
            # Main loop in module
            #print np.size(spline.roots())
            if np.size(spline.roots()) == 0:
                self.TDD[k,element] = 0.0
                self.FDD[k,element] = 0.0
            else:
                for i in range(0, np.size(spline.roots())-2, 2):
                    #print 'element, i-value', element, i
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
                    #self.degree_days[k,0] = year

                    #self.TDD[k,0] = year
                    #self.FDD[k,0] = year
                    self.TDD[k,element] = thaw_dd[0]
                    self.FDD[k,element] = freeze_dd[0]

                print element, min(self.TDD[k,element]), max(self.TDD[k,element])
                print element, min(self.FDD[k,element]), max(self.FDD[k,element])

                k = k + 1
                year = year + 1
                    ## print 'Year: '+str(self.TDD[k,0])+' Element: '+str(element)+' TDD: '+\
                    ##       str(self.TDD[k,element+1])+' FDD: '+str(self.FDD[k,element+1])
                     
        ######################################################################################
        #
        # Create plots for animations
        #
        ######################################################################################
        if FIGURE == 'TRUE':

            for k in range(0,np.size(self.dd_year)):
                year_plot =  min(self.Year)

                os.chdir(self.control['Run_dir']+self.Output_directory+'/Initialization/Degree_Days')

                TDD_plot = np.reshape(self.TDD[k,:], [int(self.ATTM_nrows), int(self.ATTM_ncols)])
                FDD_plot = np.reshape(self.FDD[k,:], [int(self.ATTM_nrows), int(self.ATTM_ncols)])

                #--------------------------------------------------------
                # Thawing Degree Days
                #--------------------------------------------------------
                fig = pl.figure()
                pl.imshow(TDD_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1000.0)
                pl.title('Thawing Degree-Days - '+str(year_plot))
                pl.colorbar(extend = 'neither', shrink = 0.92)
                pl.savefig('Thawing_Degree_Days_'+str(year_plot)+'.jpg', format = 'jpg')
                TDD_plot.tofile('Thawing_Degree_Days_'+str(year_plot)+'.bin')
                pl.close()
                #--------------------------------------------------------
                # Freezing Degree Days
                #--------------------------------------------------------
                fig = pl.figure()
                pl.imshow(FDD_plot, interpolation = 'nearest', cmap = 'spectral', vmin = -5000.0, vmax = 0.0)
                pl.title('Freezing Degree-Days - '+str(year_plot))
                pl.colorbar(extend = 'neither', shrink = 0.92)
                pl.savefig('Freezing_Degree_Days_'+str(year_plot)+'.jpg', format = 'jpg')
                TDD_plot.tofile('Freezing_Degree_Days_'+str(year_plot)+'.bin')
                pl.close()

                year_plot = year_plot + 1
                
            os.chdir(self.control['Run_dir'])

        print '    done. \n  '

    print 'Finished calculating thawing and freezing degree days.'

    #print max(self.TDD[:,0:1500:1600])
    #print max(self.FDD[:,0:1500:1600])
    #exit()
