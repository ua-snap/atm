#! /usr/bin/env python

"""
This is a script to read the geotiff layers into a raster 
in order the relative proportions of each layer (there are
currently 9 layers) for each 1km x 1km grid cell.

If I get fancy, I will try to build this into the main
ATTM code
"""

import gdal
from gdalconst import *
import numpy as np
import os, glob, csv

os.chdir('./Input')


#----------------------------------------------------- 
# Input & define all the data layers or cohort layers
# ----------------------------------------------------
# Meadows
# Low Center Polygons
# Coalescent Low Center Polygons
# Flat Center Polygons
# High Center Polygons
# Rivers
# Ponds
# Lakes
# Urban

layers = {}


with open('Geotif_layers', 'r') as f:
    for line in f:
        (key, val) = line.split()
        layers[(key)] = val

##################################################
# sort of lame not to loop, but doing brute force
# at this point
##################################################
for i in layers:
    ds = gdal.Open(layers[i], gdal.GA_ReadOnly)
    (X, deltaX, rotation, Y, rotation, deltaY) = ds.GetGeoTransform()
    src_wkt = ds.GetProjection()
    Nx = ds.RasterXSize
    Ny = ds.RasterYSize

    myarray = np.array(ds.GetRasterBand(1).ReadAsArray())

    if i == 'Meadow' : Meadow = myarray
    if i == 'LCP'    : LCP    = myarray
    if i == 'CLCP'   ; CLCP   = myarray
    if i == 'FCP'    ; FCP    = myarray
    if i == 'HCP'    : HCP    = myarray
    if i == 'Rivers' : Rivers = myarray
    if i == 'Ponds'  : Ponds  = myarray
    if i == 'Lakes'  : Lakes  = myarray 
    if i == 'Urban'  : Urban  = myarray


print Meadow.shape
    


