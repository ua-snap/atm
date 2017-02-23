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
    The purpose of this module is to populate ATM with the initial cohorts.
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
        ################################################################################################
        # New cohorts replacing former (above) cohorts. These cohorts will be use for both the Alaska  #
        # Arctic Coastal Plain and Barrow projects/products.                                           #
        # 2 June 2016, Bolton                                                                          #
        ################################################################################################
        self.ATTM_Total                 = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Cohort check (cohort fractional
                                                                                                         # areas sum to 1.0)
        self.ATTM_CLC_WT_Y              = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  #                                                                      
        self.ATTM_CLC_WT_M              = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Coalescent Low Center Polygon, Wetland Tundra, Medium age
        self.ATTM_CLC_WT_O              = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Coalescent Low Center Polygon, Wetland Tundra, Old age
        self.ATTM_CoastalWaters_WT_O    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Coastal Waters, Wetland Tundra, Old age
        self.ATTM_DrainedSlope_WT_Y     = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Drained Slope, Wetland Tundra, Young age
        self.ATTM_DrainedSlope_WT_M     = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Drained Slope, Wetland Tundra, Medium age
        self.ATTM_DrainedSlope_WT_O     = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Drianed Slope, Wetland Tundra, Old age
        self.ATTM_FCP_WT_Y              = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Flat Center Polygon, Wetland Tundra, Young age
        self.ATTM_FCP_WT_M              = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Flat Center Polygon, Wetland Tundra, Medium age
        self.ATTM_FCP_WT_O              = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Flat Center Polygon, Wetland Tundra, Old age
        self.ATTM_HCP_WT_Y              = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # High Center Polygon, Wetland Tundra, Young age
        self.ATTM_HCP_WT_M              = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # High Center Polygon, Wetland Tundra, Medium age
        self.ATTM_HCP_WT_O              = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # High Center Polygon, Wetland Tundra, Old age
        self.ATTM_LargeLakes_WT_Y       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Large Lakes, Wetland Tundra, Young age
        self.ATTM_LargeLakes_WT_M       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Large Lakes, Wetland Tundra, Medium age
        self.ATTM_LargeLakes_WT_O       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Large Lakes, Wetland Tundra, Old age
        self.ATTM_LCP_WT_Y              = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Low Center Polygons, Wetland Tundra, Young age
        self.ATTM_LCP_WT_M              = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Low Center Polygons, Wetland Tundra, Medium age
        self.ATTM_LCP_WT_O              = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Low Center Polygons, Wetland Tundra, Old age
        self.ATTM_Meadow_WT_Y           = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Meadows, Wetland Tundra, young age
        self.ATTM_Meadow_WT_M           = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Meadows, Wetland Tundra, medium age
        self.ATTM_Meadow_WT_O           = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Meadows, Wetland Tundra, old age
        self.ATTM_MediumLakes_WT_Y      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Medium Lakes, Wetland Tundra, young age
        self.ATTM_MediumLakes_WT_M      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Medium Lakes, Wetland Tundra, medium age
        self.ATTM_MediumLakes_WT_O      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Medium Lakes, Wetland Tundra, old age
        self.ATTM_NoData_WT_O           = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # No Data, Wetland Tundra, old age
        self.ATTM_Ponds_WT_Y            = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Ponds, Wetland Tundra, young age
        self.ATTM_Ponds_WT_M            = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Ponds, Wetland Tundra, medium age
        self.ATTM_Ponds_WT_O            = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Ponds, Wetland Tundra, old age
        self.ATTM_Rivers_WT_Y           = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Rivers, Wetland Tundra, young age
        self.ATTM_Rivers_WT_M           = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Rivers, Wetland Tundra, medium age
        self.ATTM_Rivers_WT_O           = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Rivers, Wetland Tundra, old age
        self.ATTM_SandDunes_WT_Y        = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Sand Dunes, Wetland Tundra, young age
        self.ATTM_SandDunes_WT_M        = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Sand Dunes, Wetland Tundra, medium age
        self.ATTM_SandDunes_WT_O        = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Sand Dunes, Wetland Tundra, old age
        self.ATTM_SaturatedBarrens_WT_Y = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Saturated Barrens, Wetland Tundra, young age
        self.ATTM_SaturatedBarrens_WT_M = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Saturated Barrens, Wetland Tundra, medium age
        self.ATTM_SaturatedBarrens_WT_O = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Saturated Barrens, Wetland Tundra, old age
        self.ATTM_Shrubs_WT_O           = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Shrubs, Wetland Tundra, old age
        self.ATTM_SmallLakes_WT_Y       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Small Lakes, Wetland Tundra, young age
        self.ATTM_SmallLakes_WT_M       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Small Lakes, Wetland Tunrda, medium age
        self.ATTM_SmallLakes_WT_O       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Small Lakes, Wetland Tundra, old age
        self.ATTM_Urban_WT              = np.zeros([self.ATTM_nrows * self.ATTM_ncols])  # Urban area, wetland tundra
    #==================================================================================================================
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
    #===========================================================================================
    elif self.Simulation_area.lower() == 'yukon':
        self.ATTM_Barren_Yukon          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon             = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_DeciduousForest_Yukon = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_DwarfShrub_Yukon      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_EvergreenForest_Yukon = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon             = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Lake_Yukon            = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Pond_Yukon            = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_River_Yukon           = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_ShrubScrub_Yukon      = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Unclassified_Yukon    = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Total                 = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_00          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_01          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_02          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_03          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_04          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_05          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_06          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_07          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_08          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_09          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_10          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_11          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_12          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_13          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_14          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_15          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_16          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_17          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_18          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_19          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_20          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_21          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_22          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_23          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_24          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_25          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_26          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_27          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_28          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_29          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_30          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_31          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_32          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_33          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_34          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_35          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_36          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_37          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_38          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_39          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_40          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_41          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_42          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_43          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_44          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_45          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_46          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_47          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_48          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_49          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_50          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_51          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_52          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_53          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_54          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_55          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_56          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_57          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_58          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_59          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_60          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_61          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_62          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_63          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_64          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_65          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_66          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_67          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_68          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_69          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_70          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_71          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_72          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_73          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_74          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_75          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_76          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_77          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_78          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_79          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_80          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_81          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_82          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_83          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_84          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_85          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_86          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_87          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_88          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_89          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_90          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_91          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_92          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_93          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_94          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_95          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_96          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_97          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_98          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_99          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        #-------------------------------------------------------------------------------
        self.ATTM_Fen_Yukon_00          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_01          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_02          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_03          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_04          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_05          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_06          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_07          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_08          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_09          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_10          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_11          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_12          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_13          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_14          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_15          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_16          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_17          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_18          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_19          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_20          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_21          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_22          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_23          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_24          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_25          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_26          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_27          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_28          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_29          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_30          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_31          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_32          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_33          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_34          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_35          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_36          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_37          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_38          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_39          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_40          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_41          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_42          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_43          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_44          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_45          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_46          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_47          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_48          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_49          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_50          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_51          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_52          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_53          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_54          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_55          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_56          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_57          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_58          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_59          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_60          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_61          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_62          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_63          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_64          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_65          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_66          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_67          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_68          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_69          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_70          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_71          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_72          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_73          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_74          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_75          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_76          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_77          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_78          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_79          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_80          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_81          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_82          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_83          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_84          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_85          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_86          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_87          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_88          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_89          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_90          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_91          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_92          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_93          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_94          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_95          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_96          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_97          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_98          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_99          = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        #------------------------------------------------------------------------------
        self.ATTM_Bog_Yukon_00_09       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_10_19       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_20_29       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_30_39       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_40_49       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_50_59       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_60_69       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_70_79       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_80_89       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Bog_Yukon_90_99       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        #------------------------------------------------------------------------------
        self.ATTM_Fen_Yukon_00_09       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_10_19       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_20_29       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_30_39       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_40_49       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_50_59       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_60_69       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_70_79       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_80_89       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
        self.ATTM_Fen_Yukon_90_99       = np.zeros([self.ATTM_nrows * self.ATTM_ncols])
    #===========================================================================================
    print '      done.'
    print ' '
