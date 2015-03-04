import numpy as np
import gdal, os, sys, glob, random
from gdalconst import *
from osgeo import *

def read_layers(self):
    """
    The purpose of this module is to read the input files that reflect
    the land cover type.  The information from this process will be used
    to create the model domain.

    ==========================================================
    Note: 20 May 2014 - Bolton
    ----------------------------------------------------------
    Input files (data layers) are assumed to be geotiff. If  
    data layers are in another format, there needs to be an
    additional method of reading data into the arrays.
    ==========================================================

    -------------------------------------------
    The land cover (not-ecotype) cohorts are:
    -------------------------------------------
    Shallow Lakes (ponds)
    Deep Lakes
    Non-polygonal (meadow)
    Low Center Polygon
    Coalescing Low Center Polygon
    Flat Center Polygon
    High Center Polygon
    Rivers
    Urban

    --------------------------
    The ecotype cohorts are:
    --------------------------
    Wetland Tundra
    Graminoid Tundra
    Shrub Tundra

    -------------------------------------------------------------------------
    Combining cohorts that are subject to thermokarst (what we are modeling:
    -------------------------------------------------------------------------
    Shallow Lakes
    Deep Lakes

    Wetland Tundra - Non-polygonal
    Wetland Tundra - Low Center Polygon
    Wetland Tundra - Coalescing Low Center Polygon
    Wetland Tundra - Flat Center Polygon
    Wetland Tundra - High Center Polygon

    Graminoid Tundra - Non-polygonal
    Graminoid Tundra - Low Center Polygon
    Graminoid Tundra - Flat Center Polygon
    Graminoid Tundra - High Center Polygon

    Graminoid Tundra - Non-polygonal
    Shrub Tundra - Low Center Polygon
    Shrub Tundra - Flat Center Polygon
    Shrub Tundar - High Center Polygon
    """
    print '    Initial Cohort Input'
    if self.Read_Geotiff.lower() == 'yes':

        """ Read files from the input directory """
        os.chdir(self.control['Run_dir']+self.Input_directory)
        geotiff_filenames = glob.glob('*.tif')

        """ Create Layer Dictionaries """
        self.LayerInformation = {}          # Information about each layer
        self.InitialCohorts   = {}          # Data ground-type location in the geotiff files
        self.Ecotypes         = {}          # Eco-type information -- TBD, maybe at a different resolution than
                                            # the initial layers/cohorts.

        for filename in geotiff_filenames:
            print '      reading initial '+str(os.path.splitext(filename)[0])+' cohorts.'
            base = os.path.splitext(filename)[0]
            self.base = base

            ds = gdal.Open(filename, gdal.GA_ReadOnly)
            (X, deltaX, rotation, Y, rotation, deltaY) = ds.GetGeoTransform()

            self.LayerInformation['self.base+str(_transform)']  = ds.GetGeoTransform() # Information needed for writing geotiff
            self.LayerInformation['self.base+str(_projection)'] = ds.GetProjection()   # Information for writing geotiff
            self.LayerInformation['self.base+str(_Nx)']         = ds.RasterXSize       # Number of columns
            self.LayerInformation['self.base+str(_Ny)']         = ds.RasterYSize       # Number of rows
            self.LayerInformation['self.base+str(_deltaX)']     = deltaX               # X-resolution (can be + or -)
            self.LayerInformation['self.base+str(_deltaY)']     = deltaY               # Y-resolution (can be + or -)
            self.LayerInformation['self.base+str(_X_corner)']   = X                    # X-origin of geotiff
            self.LayerInformation['self.base+str(_Y_corner)']   = Y                    # Y-origin of geotiff

            #print self.base, 'number columns (x-dimension): ', self.LayerInformation['self.base+str(_Nx)']
            #print self.base, 'number rows (y-dimension): ', self.LayerInformation['self.base+str(_Ny)']

            """ Assuming that the (0,0) element is located in the Upper Left Corner """
            if self.base == "LowCenter":
                self.nrows = self.LayerInformation['self.base+str(_Ny)']           # number of rows  
                self.ncols = self.LayerInformation['self.base+str(_Nx)']           # number of columns 
                self.x_res = abs(self.LayerInformation['self.base+str(_deltaX)'])  # x-resolution [m, absolute value]
                self.y_res = abs(self.LayerInformation['self.base+str(_deltaY)'])  # y-resolution [m, absolute value]

            """ Read Initial cohort data from geotiff into an array """
            self.InitialCohorts['self.base'] = np.array(ds.GetRasterBand(1).ReadAsArray())
            # Data Arrays Below
            if self.base == "LowCenter":
                self.LCP = self.InitialCohorts['self.base']       # Low Center Polygon
                #print self.LCP[1000:1005, 1000:1005]   # Works
            elif self.base == "Rivers":                           
                self.Rivers = self.InitialCohorts['self.base']    # Rivers
            elif self.base == "Ponds":
                self.Ponds = self.InitialCohorts['self.base']     # Ponds or Shallow Lake
            elif self.base == "Lakes":                       
                self.Lakes = self.InitialCohorts['self.base']     # Lake
            elif self.base == "FlatCenter":
                self.FCP = self.InitialCohorts['self.base']       # Flat Center Polygon
            elif self.base == "Urban":
                self.Urban = self.InitialCohorts['self.base']     # Urban
            elif self.base == "Meadows":
                self.NPG = self.InitialCohorts['self.base']       # Non-Polygonal Ground
            elif self.base == "CoalescentLowCenter":
                self.CLC = self.InitialCohorts['self.base']       # Coalescent Low Center polygon
            elif self.base == "HighCenter":
                self.HCP = self.InitialCohorts['self.base']       # High Center Polygon
            else:
                print '--  ERROR -- '
                print 'There is a problem with the Geotiff File names.' 
                exit()
    else:
        print 'Need an alternative method of reading initial cohorts and other necessary information.'
        exit()

    os.chdir(self.control['Run_dir'])

    print '      done.'
    print ' '
