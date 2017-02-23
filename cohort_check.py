import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
from decimal import *

getcontext().prec = 4

def cohort_start(self, element, time):
    """
    The purpose of this module is to define the total fractional areas
    of all the cohorts in each model element.
    """
 #   fraction_start = self.ATTM_Wet_NPG[element] + self.ATTM_Wet_LCP[element] + \
 #                        self.ATTM_Wet_CLC[element] + self.ATTM_Wet_FCP[element] + \
 #                        self.ATTM_Wet_HCP[element] + self.ATTM_Gra_NPG[element] + \
 #                        self.ATTM_Gra_LCP[element] + self.ATTM_Gra_FCP[element] + \
 #                        self.ATTM_Gra_HCP[element] + self.ATTM_Shr_NPG[element] + \
 #                        self.ATTM_Shr_LCP[element] + self.ATTM_Shr_FCP[element] + \
 #                        self.ATTM_Shr_HCP[element] + self.ATTM_Urban[element]   + \
 #                        self.ATTM_Rivers[element]  + self.ATTM_Ponds[element]   + \
 #                        self.ATTM_Lakes[element]
    fraction_start = self.ATTM_CLC_WT_Y[element] + self.ATTM_CLC_WT_M[element] + \
                     self.ATTM_CLC_WT_O[element] + self.ATTM_CoastalWaters_WT_O[element] + \
                     self.ATTM_DrainedSlope_WT_Y[element] + self.ATTM_DrainedSlope_WT_M[element] + \
                     self.ATTM_DrainedSlope_WT_O[element] + self.ATTM_FCP_WT_Y[element] + \
                     self.ATTM_FCP_WT_M[element] + self.ATTM_FCP_WT_O[element] + \
                     self.ATTM_HCP_WT_Y[element] + self.ATTM_HCP_WT_M[element] + \
                     self.ATTM_HCP_WT_O[element] + self.ATTM_LCP_WT_Y[element] + \
                     self.ATTM_LCP_WT_M[element] + self.ATTM_LCP_WT_O[element] + \
                     self.ATTM_Meadow_WT_Y[element] + self.ATTM_Meadow_WT_M[element] + \
                     self.ATTM_Meadow_WT_O[element] + self.ATTM_NoData_WT_O[element] + \
                     self.ATTM_SandDunes_WT_Y[element] + self.ATTM_SandDunes_WT_M[element] + \
                     self.ATTM_SandDunes_WT_O[element] + self.ATTM_SaturatedBarrens_WT_Y[element] + \
                     self.ATTM_SaturatedBarrens_WT_M[element] + self.ATTM_SaturatedBarrens_WT_O[element] + \
                     self.ATTM_Shrubs_WT_O[element] + self.ATTM_Urban_WT[element] + \
                     self.ATTM_LargeLakes_WT_Y[element] + self.ATTM_LargeLakes_WT_M[element] + \
                     self.ATTM_LargeLakes_WT_O[element] + self.ATTM_MediumLakes_WT_Y[element] + \
                     self.ATTM_MediumLakes_WT_M[element] + self.ATTM_MediumLakes_WT_O[element] + \
                     self.ATTM_SmallLakes_WT_Y[element] + self.ATTM_SmallLakes_WT_M[element] + \
                     self.ATTM_SmallLakes_WT_O[element] + self.ATTM_Ponds_WT_Y[element] + \
                     self.ATTM_Ponds_WT_M[element] + self.ATTM_Ponds_WT_O[element] + \
                     self.ATTM_Rivers_WT_Y[element] + self.ATTM_Rivers_WT_M[element] + \
                     self.ATTM_Rivers_WT_O[element]
                     
    ## if element == 700:
    ##     print 'element : ', element
    ##     print 'Wetland Meadow Start: ', self.ATTM_Wet_NPG[element]
    ##     print 'Wetland LCP Start: ', self.ATTM_Wet_LCP[element]
    ##     print 'Wetland CLC Start: ', self.ATTM_Wet_CLC[element]
    ##     print 'Wetland FCP Start: ', self.ATTM_Wet_CLC[element]
    ##     print 'Wetland HCP Start: ', self.ATTM_Wet_HCP[element]
    ##     print 'Lakes Start: ', self.ATTM_Lakes[element]
    ##     print 'Ponds Start: ', self.ATTM_Ponds[element]
    ##     print 'Urban Start: ', self.ATTM_Urban[element]
    ##     print 'Rivers Start: ', self. ATTM_Rivers[element]
    ##     print 'Total: ', fraction_start
    ##     print ' '
    return fraction_start

def cohort_check(self, element, time, cohort_start):
    """
    The purpose of this module is to run a 'mass-balance' of the
    fractional areas of all the cohorts.  After each time step,
    the total fractional area of all the cohorts should equal
    the prior time-step fractional area of cohorts.

    In most elements the total sum of all the fractional cohorts
    should be equal to 1.0. There are a few cases, such elements
    along the edge of the model domain and along the rivers,
    that have a total fractional area that is less than 1.0.
    """

 #   fraction_end = np.round(self.ATTM_Wet_NPG[element] + self.ATTM_Wet_LCP[element] + \
 #                           self.ATTM_Wet_CLC[element] + self.ATTM_Wet_FCP[element] + \
 #                           self.ATTM_Wet_HCP[element] + self.ATTM_Gra_NPG[element] + \
 #                           self.ATTM_Gra_LCP[element] + self.ATTM_Gra_FCP[element] + \
 #                           self.ATTM_Gra_HCP[element] + self.ATTM_Shr_NPG[element] + \
 #                           self.ATTM_Shr_LCP[element] + self.ATTM_Shr_FCP[element] + \
 #                           self.ATTM_Shr_HCP[element] + self.ATTM_Urban[element]   + \
 #                           self.ATTM_Rivers[element]  + self.ATTM_Ponds[element]   + \
 #                           self.ATTM_Lakes[element], decimals = 4)
    fraction_end  =  np.round(self.ATTM_CLC_WT_Y[element] + self.ATTM_CLC_WT_M[element] + \
                     self.ATTM_CLC_WT_O[element] + self.ATTM_CoastalWaters_WT_O[element] + \
                     self.ATTM_DrainedSlope_WT_Y[element] + self.ATTM_DrainedSlope_WT_M[element] + \
                     self.ATTM_DrainedSlope_WT_O[element] + self.ATTM_FCP_WT_Y[element] + \
                     self.ATTM_FCP_WT_M[element] + self.ATTM_FCP_WT_O[element] + \
                     self.ATTM_HCP_WT_Y[element] + self.ATTM_HCP_WT_M[element] + \
                     self.ATTM_HCP_WT_O[element] + self.ATTM_LCP_WT_Y[element] + \
                     self.ATTM_LCP_WT_M[element] + self.ATTM_LCP_WT_O[element] + \
                     self.ATTM_Meadow_WT_Y[element] + self.ATTM_Meadow_WT_M[element] + \
                     self.ATTM_Meadow_WT_O[element] + self.ATTM_NoData_WT_O[element] + \
                     self.ATTM_SandDunes_WT_Y[element] + self.ATTM_SandDunes_WT_M[element] + \
                     self.ATTM_SandDunes_WT_O[element] + self.ATTM_SaturatedBarrens_WT_Y[element] + \
                     self.ATTM_SaturatedBarrens_WT_M[element] + self.ATTM_SaturatedBarrens_WT_O[element] + \
                     self.ATTM_Shrubs_WT_O[element] + self.ATTM_Urban_WT[element] + \
                     self.ATTM_LargeLakes_WT_Y[element] + self.ATTM_LargeLakes_WT_M[element] + \
                     self.ATTM_LargeLakes_WT_O[element] + self.ATTM_MediumLakes_WT_Y[element] + \
                     self.ATTM_MediumLakes_WT_M[element] + self.ATTM_MediumLakes_WT_O[element] + \
                     self.ATTM_SmallLakes_WT_Y[element] + self.ATTM_SmallLakes_WT_M[element] + \
                     self.ATTM_SmallLakes_WT_O[element] + self.ATTM_Ponds_WT_Y[element] + \
                     self.ATTM_Ponds_WT_M[element] + self.ATTM_Ponds_WT_O[element] + \
                     self.ATTM_Rivers_WT_Y[element] + self.ATTM_Rivers_WT_M[element] + \
                     self.ATTM_Rivers_WT_O[element], decimals = 4)
                     
                     
    if abs(cohort_start - fraction_end) > 0.1:
        print 'There is a mass balance problem in element: '+str(element)+' at time: ', time
        print 'start: ', cohort_start
        print 'end: ', fraction_end
        print ' '
        print 'Final land cohort fractions: '
        print '    Wetland Tundra Meadows:'
        print '       Young: ', self.ATTM_Meadow_WT_Y[element]
        print '      Medium: ', self.ATTM_Meadow_WT_M[element]
        print '         Old: ', self.ATTM_Meadow_WT_O[element]
        print '    Wetland Tundra Low Center Polygons:'
        print '       Young: ', self.ATTM_LCP_WT_Y[element]
        print '      Medium: ', self.ATTM_LCP_WT_M[element]
        print '         Old: ', self.ATTM_LCP_WT_O[element]
        print '    Wetland Tundra Coalescent Low Center Polygons:'
        print '       Young: ', self.ATTM_CLC_WT_Y[element]
        print '      Medium: ', self.ATTM_CLC_WT_M[element]
        print '         Old: ', self.ATTM_CLC_WT_O[element]
        print '    Wetland Tundra Flat Center Polygons:'
        print '       Young: ', self.ATTM_FCP_WT_Y[element]
        print '      Medium: ', self.ATTM_FCP_WT_M[element]
        print '         Old: ', self.ATTM_FCP_WT_O[element]
        print '    Wetland Tundra High Center Polygons: '
        print '       Young: ', self.ATTM_HCP_WT_Y[element]
        print '      Medium: ', self.ATTM_HCP_WT_M[element]
        print '         Old: ', self.ATTM_HCP_WT_O[element]
        print '    Wetland Tundra Large Lakes: '
        print '       Young: ', self.ATTM_LargeLakes_WT_Y[element]
        print '      Medium: ', self.ATTM_LargeLakes_WT_M[element]
        print '         Old: ', self.ATTM_LargeLakes_WT_O[element]
        print '    Wetland Tundra Medium Lakes: '
        print '       Young: ', self.ATTM_MediumLakes_WT_Y[element]
        print '      Medium: ', self.ATTM_MediumLakes_WT_M[element]
        print '         Old; ', self.ATTM_MediumLakes_WT_O[element]
        print '    Wetland Tundra Small Lakes: '
        print '       Young: ', self.ATTM_SmallLakes_WT_Y[element]
        print '      Medium: ', self.ATTM_SmallLakes_WT_M[element]
        print '         Old: ', self.ATTM_SmallLakes_WT_O[element]
        print '    Wetland Tundra Ponds: '
        print '       Young: ', self.ATTM_Ponds_WT_Y[element]
        print ',     Medium: ', self.ATTM_Ponds_WT_M[element]
        print ',        Old: ', self.ATTM_Ponds_WT_O[element]
        print ',   Wetland Tundra Rivers: '
        print ',      Young: ', self.ATTM_Rivers_WT_Y[element]
        print ',     Medium: ', self.ATTM_Rivers_WT_M[element]
        print ',        Old: ', self.ATTM_Rivers_WT_O[element]
        print ',   Wetland Tundra Shrubs: '
        print '         Old: ', self.ATTM_Shrubs_WT_O[element]
        print ',   Wetland Tundra Urban: '
        print ',        Old: ', self.ATTM_Urban_WT[element]
        print ' '
        print '    Wetland Tundra Coastal Waters: '
        print '         Old: ', self.ATTM_CoastalWaters_WT_O[element]
        print '    Wetland Tundra Drained Slopes: '
        print '       Young: ', self.ATTM_DrainedSlope_WT_Y[element]
        print '      Medium: ', self.ATTM_DrainedSlope_WT_M[element]
        print '         Old: ', self.ATTM_DrainedSlope_WT_O[element]
        print '    Wetland Tundra No Data: '
        print '         Old: ', self.ATTM_NoData_WT_O[element]
        print '    Wetland Tundra Sand Dunes: '
        print '       Young: ', self.ATTM_SandDunes_WT_Y[element]
        print '      Medium: ', self.ATTM_SandDunes_WT_M[element]
        print '         Old: ', self.ATTM_SandDunes_WT_O[element]
        print '    Wetland Tundra Saturated Barrens: '
        print '       Young: ', self.ATTM_SaturatedBarrens_WT_Y[element]
        print ',     Medium: ', self.ATTM_SaturatedBarrens_WT_M[element]
        print ',        Old: ', self.ATTM_SaturatedBarrens_WT_O[element]
        
        
#        print '    Wet_NPG: ', self.ATTM_Wet_NPG[element]
#        print '    Wet_LCP: ', self.ATTM_Wet_LCP[element]
#        print '    Wet_CLC: ', self.ATTM_Wet_CLC[element]
#        print '    Wet_FCP: ', self.ATTM_Wet_FCP[element]
#        print '    Wet_HCP: ', self.ATTM_Wet_HCP[element]
#        print '      Lakes: ', self.ATTM_Lakes[element]
#        print '      Ponds: ', self.ATTM_Ponds[element]
#        print '     Rivers: ', self.ATTM_Rivers[element]
#        print '      Urban: ', self.ATTM_Urban[element]
#        print ' '
#        print '    Gra_NPG: ', self.ATTM_Gra_NPG[element]
#        print '    Gra_LCP: ', self.ATTM_Gra_LCP[element]
#        print '    Gra_FCP: ', self.ATTM_Gra_FCP[element]
#        print '    Gra_HCP: ', self.ATTM_Gra_HCP[element]
#        print '    Shr_NPG: ', self.ATTM_Shr_NPG[element]
#        print '    Shr_LCP: ', self.ATTM_Shr_LCP[element]
#        print '    Shr_FCP: ', self.ATTM_Shr_FCP[element]
#        print '    Shr_HCP: ', self.ATTM_Shr_HCP[element]
        exit()
        
    if round(fraction_end, 4) > 1.0 :
        print 'There is a mass balance problem in element ', element
        print 'has a total fractional area greater than 1.0'
        print ' '
        print '    Wetland Tundra Meadows:'
        print '       Young: ', self.ATTM_Meadow_WT_Y[element]
        print '      Medium: ', self.ATTM_Meadow_WT_M[element]
        print '         Old: ', self.ATTM_Meadow_WT_O[element]
        print '    Wetland Tundra Low Center Polygons:'
        print '       Young: ', self.ATTM_LCP_WT_Y[element]
        print '      Medium: ', self.ATTM_LCP_WT_M[element]
        print '         Old: ', self.ATTM_LCP_WT_O[element]
        print '    Wetland Tundra Coalescent Low Center Polygons:'
        print '       Young: ', self.ATTM_CLC_WT_Y[element]
        print '      Medium: ', self.ATTM_CLC_WT_M[element]
        print '         Old: ', self.ATTM_CLC_WT_O[element]
        print '    Wetland Tundra Flat Center Polygons:'
        print '       Young: ', self.ATTM_FCP_WT_Y[element]
        print '      Medium: ', self.ATTM_FCP_WT_M[element]
        print '         Old: ', self.ATTM_FCP_WT_O[element]
        print '    Wetland Tundra High Center Polygons: '
        print '       Young: ', self.ATTM_HCP_WT_Y[element]
        print '      Medium: ', self.ATTM_HCP_WT_M[element]
        print '         Old: ', self.ATTM_HCP_WT_O[element]
        print '    Wetland Tundra Large Lakes: '
        print '       Young: ', self.ATTM_LargeLakes_WT_Y[element]
        print '      Medium: ', self.ATTM_LargeLakes_WT_M[element]
        print '         Old: ', self.ATTM_LargeLakes_WT_O[element]
        print '    Wetland Tundra Medium Lakes: '
        print '       Young: ', self.ATTM_MediumLakes_WT_Y[element]
        print '      Medium: ', self.ATTM_MediumLakes_WT_M[element]
        print '         Old; ', self.ATTM_MediumLakes_WT_O[element]
        print '    Wetland Tundra Small Lakes: '
        print '       Young: ', self.ATTM_SmallLakes_WT_Y[element]
        print '      Medium: ', self.ATTM_SmallLakes_WT_M[element]
        print '         Old: ', self.ATTM_SmallLakes_WT_O[element]
        print '    Wetland Tundra Ponds: '
        print '       Young: ', self.ATTM_Ponds_WT_Y[element]
        print ',     Medium: ', self.ATTM_Ponds_WT_M[element]
        print ',        Old: ', self.ATTM_Ponds_WT_O[element]
        print ',   Wetland Tundra Rivers: '
        print ',      Young: ', self.ATTM_Rivers_WT_Y[element]
        print ',     Medium: ', self.ATTM_Rivers_WT_M[element]
        print ',        Old: ', self.ATTM_Rivers_WT_O[element]
        print ',   Wetland Tundra Shrubs: '
        print '         Old: ', self.ATTM_Shrubs_WT_O[element]
        print ',   Wetland Tundra Urban: '
        print ',        Old: ', self.ATTM_Urban_WT[element]
        print ' '
        print '    Wetland Tundra Coastal Waters: '
        print '         Old: ', self.ATTM_CoastalWaters_WT_O[element]
        print '    Wetland Tundra Drained Slopes: '
        print '       Young: ', self.ATTM_DrainedSlope_WT_Y[element]
        print '      Medium: ', self.ATTM_DrainedSlope_WT_M[element]
        print '         Old: ', self.ATTM_DrainedSlope_WT_O[element]
        print '    Wetland Tundra No Data: '
        print '         Old: ', self.ATTM_NoData_WT_O[element]
        print '    Wetland Tundra Sand Dunes: '
        print '       Young: ', self.ATTM_SandDunes_WT_Y[element]
        print '      Medium: ', self.ATTM_SandDunes_WT_M[element]
        print '         Old: ', self.ATTM_SandDunes_WT_O[element]
        print '    Wetland Tundra Saturated Barrens: '
        print '       Young: ', self.ATTM_SaturatedBarrens_WT_Y[element]
        print ',     Medium: ', self.ATTM_SaturatedBarrens_WT_M[element]
        print ',        Old: ', self.ATTM_SaturatedBarrens_WT_O[element]        

#        print 'Wetland Non-polygonal Ground: ',          self.ATTM_Wet_NPG[element]
#        print 'Wetland Low Center Polygon: ',            self.ATTM_Wet_LCP[element]
#        print 'Wetland Coalescent Low Center Polygon: ', self.ATTM_Wet_CLC[element]
#        print 'Wetland Flat Center Polygon: ',           self.ATTM_Wet_FCP[element]
#        print 'Wetland High Center Polygon: ',           self.ATTM_Wet_HCP[element]
#        print 'Lakes: ' ,                                self.ATTM_Lakes[element]
#        print 'Ponds: ',                                 self.ATTM_Ponds[element]
#        print 'Rivers: ',                                self.ATTM_Rivers[element]
#        print 'Urban: ',                                 self.ATTM_Urban[element]
        print 'Total: ',                                 np.float64(fraction_end)
        exit()
    if round(fraction_end, 4) < 0.0 :
        print 'There is a mass balance problem in element ', element
        print 'has a total fractional area less than 0.0 '
        print ' '
        print '    Wetland Tundra Meadows:'
        print '       Young: ', self.ATTM_Meadow_WT_Y[element]
        print '      Medium: ', self.ATTM_Meadow_WT_M[element]
        print '         Old: ', self.ATTM_Meadow_WT_O[element]
        print '    Wetland Tundra Low Center Polygons:'
        print '       Young: ', self.ATTM_LCP_WT_Y[element]
        print '      Medium: ', self.ATTM_LCP_WT_M[element]
        print '         Old: ', self.ATTM_LCP_WT_O[element]
        print '    Wetland Tundra Coalescent Low Center Polygons:'
        print '       Young: ', self.ATTM_CLC_WT_Y[element]
        print '      Medium: ', self.ATTM_CLC_WT_M[element]
        print '         Old: ', self.ATTM_CLC_WT_O[element]
        print '    Wetland Tundra Flat Center Polygons:'
        print '       Young: ', self.ATTM_FCP_WT_Y[element]
        print '      Medium: ', self.ATTM_FCP_WT_M[element]
        print '         Old: ', self.ATTM_FCP_WT_O[element]
        print '    Wetland Tundra High Center Polygons: '
        print '       Young: ', self.ATTM_HCP_WT_Y[element]
        print '      Medium: ', self.ATTM_HCP_WT_M[element]
        print '         Old: ', self.ATTM_HCP_WT_O[element]
        print '    Wetland Tundra Large Lakes: '
        print '       Young: ', self.ATTM_LargeLakes_WT_Y[element]
        print '      Medium: ', self.ATTM_LargeLakes_WT_M[element]
        print '         Old: ', self.ATTM_LargeLakes_WT_O[element]
        print '    Wetland Tundra Medium Lakes: '
        print '       Young: ', self.ATTM_MediumLakes_WT_Y[element]
        print '      Medium: ', self.ATTM_MediumLakes_WT_M[element]
        print '         Old; ', self.ATTM_MediumLakes_WT_O[element]
        print '    Wetland Tundra Small Lakes: '
        print '       Young: ', self.ATTM_SmallLakes_WT_Y[element]
        print '      Medium: ', self.ATTM_SmallLakes_WT_M[element]
        print '         Old: ', self.ATTM_SmallLakes_WT_O[element]
        print '    Wetland Tundra Ponds: '
        print '       Young: ', self.ATTM_Ponds_WT_Y[element]
        print ',     Medium: ', self.ATTM_Ponds_WT_M[element]
        print ',        Old: ', self.ATTM_Ponds_WT_O[element]
        print ',   Wetland Tundra Rivers: '
        print ',      Young: ', self.ATTM_Rivers_WT_Y[element]
        print ',     Medium: ', self.ATTM_Rivers_WT_M[element]
        print ',        Old: ', self.ATTM_Rivers_WT_O[element]
        print ',   Wetland Tundra Shrubs: '
        print '         Old: ', self.ATTM_Shrubs_WT_O[element]
        print ',   Wetland Tundra Urban: '
        print ',        Old: ', self.ATTM_Urban_WT[element]
        print ' '
        print '    Wetland Tundra Coastal Waters: '
        print '         Old: ', self.ATTM_CoastalWaters_WT_O[element]
        print '    Wetland Tundra Drained Slopes: '
        print '       Young: ', self.ATTM_DrainedSlope_WT_Y[element]
        print '      Medium: ', self.ATTM_DrainedSlope_WT_M[element]
        print '         Old: ', self.ATTM_DrainedSlope_WT_O[element]
        print '    Wetland Tundra No Data: '
        print '         Old: ', self.ATTM_NoData_WT_O[element]
        print '    Wetland Tundra Sand Dunes: '
        print '       Young: ', self.ATTM_SandDunes_WT_Y[element]
        print '      Medium: ', self.ATTM_SandDunes_WT_M[element]
        print '         Old: ', self.ATTM_SandDunes_WT_O[element]
        print '    Wetland Tundra Saturated Barrens: '
        print '       Young: ', self.ATTM_SaturatedBarrens_WT_Y[element]
        print ',     Medium: ', self.ATTM_SaturatedBarrens_WT_M[element]
        print ',        Old: ', self.ATTM_SaturatedBarrens_WT_O[element]        

#        print 'Wetland Non-polygonal Ground: ',          self.ATTM_Wet_NPG[element]
#        print 'Wetland Low Center Polygon: ',            self.ATTM_Wet_LCP[element]
#        print 'Wetland Coalescent Low Center Polygon: ', self.ATTM_Wet_CLC[element]
#        print 'Wetland Flat Center Polygon: ',           self.ATTM_Wet_FCP[element]
#        print 'Wetland High Center Polygon: ',           self.ATTM_Wet_HCP[element]
#        print 'Lakes: ' ,                                self.ATTM_Lakes[element]
#        print 'Ponds: ',                                 self.ATTM_Ponds[element]
#        print 'Rivers: ',                                self.ATTM_Rivers[element]
#        print 'Urban: ',                                 self.ATTM_Urban[element]
        print 'Total: ',                                 np.float64(fraction_end)
        exit()
