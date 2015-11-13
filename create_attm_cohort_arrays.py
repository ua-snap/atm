import numpy as np
import gdal, os, sys, glob, random
from gdalconst import *
from osgeo import *
import pylab as pl
import xlrd, xlwt
from scipy import interpolate
from scipy import integrate

def create_attm_cohort_arrays(self):
    print '    Initializing ATTM cohort arrays.'
    
    """
    The purpose of this module is to populate ATTM with the initial cohorts.
    """
    if self.Simulation_area.lower() == 'barrow':
        self.ATTM_Wet_NPG    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Wetland Non-polygonal ground (meadow)
        self.ATTM_Wet_LCP    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Wetland Low Center Polygon
        self.ATTM_Wet_CLC    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Wetland Coalescent Low Center Polygon
        self.ATTM_Wet_FCP    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Wetland Flat Center Polygon
        self.ATTM_Wet_HCP    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Wetland High Center Polygon
        self.ATTM_Gra_NPG    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Graminoid Non-polygonal ground
        self.ATTM_Gra_LCP    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Graminoid Low Center Polygon
        self.ATTM_Gra_FCP    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Graminoid Flat Center Polygon
        self.ATTM_Gra_HCP    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Graminoid High Center Polygon
        self.ATTM_Shr_NPG    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Shrub Non-polygonal ground
        self.ATTM_Shr_LCP    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Shrub Low Center Polygon
        self.ATTM_Shr_FCP    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Shrub Tundra Flat Center Polygon
        self.ATTM_Shr_HCP    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Shrub Tundra High Center Polygon
        self.ATTM_Ponds      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Ponds or Shallow Lakes 
        self.ATTM_Lakes      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Lakes or Deep Lakes
        self.ATTM_Rivers     = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Do not change over time
        self.ATTM_Urban      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Do not change over time
        self.ATTM_Total      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Cohort check (cohort fractional
                                                                              # areas sum to 1.0)

    elif self.Simulation_area.lower() == 'tanana':
        self.ATTM_TF_OB      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Tanana Flats Old Bog
        self.ATTM_TF_YB      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Tanana Flats Young Bog
        self.ATTM_TF_OF      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Tanana Flats Old Fen
        self.ATTM_TF_YF      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Tanana Flats Young Fen
        self.ATTM_TF_Con_PP  = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Tanana Flats Coniferous Permafrost Plateau
        self.ATTM_TF_Dec_PP  = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Tanana Flats Deciduous Permafrost Plateua
        self.ATTM_TF_TL      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Tanana Flats Thermokarst Lakes
        self.ATTM_Total      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Cohort check (cohort fractional
                                                                              # areas sum to 1.0?)
    print '      done.'
    print ' '
