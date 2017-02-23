import numpy as np
import os, sys
import datetime, time
from matplotlib.dates import date2num
from matplotlib.dates import num2date


def on_screen(self):
    """
    The purpose of this module is to compile simulation results
    and output to the terminal screen.
    """
    ########################################################################
    print ' '
    print ' '
    print '====================================================='
    print '       Simulation Results         '
    print '====================================================='
    print 'Simulation name: ', self.simulation_name
    print 'Start Date / Time : ', self.start_time
    print 'End Date / Time : ', self.finish_time
    print 'Total Simulation Time (minutes): ', (self.finish - self.start)/60.0
    if self.archive_simulation.lower() == 'yes':
        print 'Archive Status: Active'
        print 'Archive Name : ', self.simulation_name
    else:
        print 'Archive Status: Inactive'
    print ' '
    print 'Number of time steps in the simulation: ', self.stop
    print ' '
    print '-----------------------------------'
    print ' Initial Cohort Information'
    print '-----------------------------------'
    print 'Outputs of Initial Cohort Distribution:'
    if self.initialize['Initial_Cohort_Distribution_Figure'].lower() != 'yes':
        print '  No outputs generated.'
    else:
        if self.initialize['Meadow_WT_Y_Figure'].lower() == 'yes':
            print '  Inital Meadow, Wetland Tundra, Young age Figure [Output/Barrow/Meadow_WT_Y]'
        if self.initialize['Meadow_WT_M_Figure'].lower() == 'yes':
            print '  Initial Meadow, Wetland Tundra, Medium age Figure [Output/Barrow/Meadow_WT_M]'
        if self.initialize['Meadow_WT_O_Figure'].lower() == 'yes':
            print '  Initial Meadow, Wetland Tundra, Old age Figure [Output/Barrow/Meadow_WT_O]'
        if self.initialize['LCP_WT_Y_Figure'].lower() == 'yes':
            print '  Initial Low Center Polygon, Wetland Tundra, Young age Figure [Output/Barrow/LCP_WT_Y]'
        if self.initialize['LCP_WT_M_Figure'].lower() == 'yes':
            print '  Initial Low Center Polygon, Wetland Tundra, Medium age Figure [Output/Barrow/LCP_WT_M]'
        if self.initialize['LCP_WT_O_Figure'].lower() == 'yes':
            print '  Initial Low Center Polygon, Wetland Tundra, Old age Figure [Output/Barrow/LCP_WT_O]'
        if self.initialize['CLC_WT_Y_Figure'].lower() == 'yes':
            print '  Initial Coalescent Low Center Polygon, Wetland Tundra, Young age Figure [Output/Barrow/CLC_WT_Y]'
        if self.initialize['CLC_WT_M_Figure'].lower() == 'yes':
            print '  Initial Coalescent Low Center Polygon, Wetland Tundra, Medium age Figure [Output/Barrow/CLC_WT_M]'
        if self.initialize['CLC_WT_O_Figure'].lower() == 'yes':
            print '  Initial Coalescent Low Center Polygon, Wetland Tundra, Old age Figure [Output/Barrow/CLC_WT_O]'
        if self.initialize['FCP_WT_Y_Figure'].lower() == 'yes':
            print '  Initial Flat Center Polygon, Wetland Tundra, Young age Figure [Output/Barrow/FCP_WT_Y]'
        if self.initialize['FCP_WT_M_Figure'].lower() == 'yes':
            print '  Initial Flat Center Polygon, Wetland Tundra, Medium age Figure [Output/Barrow/FCP_WT_M]'
        if self.initialize['FCP_WT_O_Figure'].lower() == 'yes':
            print '  Initial Flat Center Polygon, Wetland Tundra, Old age Figure [Output/Barrow/FCP_WT_O]'
        if self.initialize['HCP_WT_Y_Figure'].lower() == 'yes':
            print '  Initial High Center Polygon, Wetland Tundra, Young age Figure [Output/Barrow/HCP_WT_Y]'
        if self.initialize['HCP_WT_M_Figure'].lower() == 'yes':
            print '  Initial High Center Polygon, Wetland Tundra, Medium age Figure [Output/Barrow/HCP_WT_M]'
        if self.initialize['HCP_WT_O_Figure'].lower() == 'yes':
            print '  Initial High Center Polygon, Wetland Tundra, Old age Figure [Output/Barrow/HCP_WT_O]'
        if self.initialize['LargeLakes_WT_Y_Figure'].lower() == 'yes':
            print '  Initial Large (size) Lakes, Wetland Tundra, Young age Figure [Output/Barrow/LargeLakes_WT_Y]'
        if self.initialize['LargeLakes_WT_M_Figure'].lower() == 'yes':
            print '  Initial Large (size) Lakes, Wetland Tundra, Medium age Figure [Output/Barrow/LargeLakes_WT_M]'
        if self.initialize['LargeLakes_WT_O_Figure'].lower() == 'yes':
            print '  Initial Large (size) Lakes, Wetland Tundra, Old age Figure [Output/Barrow/LargeLakes_WT_O]'
        if self.initialize['MediumLakes_WT_Y_Figure'].lower() == 'yes':
            print '  Initial Medium (size) Lakes, Wetland Tundra, Young age Figure [Output/Barrow/MediumLakes_WT_Y]'
        if self.initialize['MediumLakes_WT_M_Figure'].lower() == 'yes':
            print '  Initial Medium (size) Lakes, Wetland Tundra, Medium age Figure [Output/Barrow/MediumLakes_WT_M]'
        if self.initialize['MediumLakes_WT_O_Figure'].lower() == 'yes':
            print '  Initial Medium (size) Lakes, Wetland Tundra, Old age Figure [Output/Barrow/MediumLakes_WT_O]'
        if self.initialize['SmallLakes_WT_Y_Figure'].lower() == 'yes':
            print '  Initial Small (size) Lakes, Wetland Tundra, Young age Figure [Output/Barrow/SmallLakes_WT_Y]'
        if self.initialize['SmallLakes_WT_M_Figure'].lower() == 'yes':
            print '  Initial Small (size) Lakes, Wetland Tundra, Medium age Figure [Output/Barrow/SmallLakes_WT_M]'
        if self.initialize['SmallLakes_WT_O_Figure'].lower() == 'yes':
            print '  Initial Small (size) Lakes, Wetland Tundra, Old age Figure [Output/Barrow/SmallLakes_WT_O]'
        if self.initialize['Ponds_WT_Y_Figure'].lower() == 'yes':
            print '  Initial Ponds, Wetland Tundra, Young age Figure [Output/Barrow/Ponds_WT_Y]'
        if self.initialize['Ponds_WT_M_Figure'].lower() == 'yes':
            print '  Initial Ponds, Wetland Tundra, Medium age Figure [Output/Barrow/Ponds_WT_M]'
        if self.initialize['Ponds_WT_O_Figure'].lower() == 'yes':
            print '  Initial Ponds, Wetland Tundra, Old age Figure [Output/Barrow/Ponds_WT_O]'
        if self.initialize['CoastalWaters_WT_O_Figure'].lower() == 'yes':
            print '  Initial Coastal Waters, Wetland Tundra, Old age Figure [Output/Barrow/CoastalWaters_WT_O]'
        if self.initialize['DrainedSlope_WT_Y_Figure'].lower() == 'yes':
            print '  Initial Drained Slope, Wetland Tundra, Young age Figure [Output/Barrow/DrainedSlope_WT_Y]'
        if self.initialize['DrainedSlope_WT_M_Figure'].lower() == 'yes':
            print '  Initial Drained Slope, Wetland Tundra, Medium age Figure [Output/Barrow/DrainedSlope_WT_M]'
        if self.initialize['DrainedSlope_WT_O_Figure'].lower() == 'yes':
            print '  Initial Drained Slope, Wetland Tundra, Old age Figure [Output/Barrow/DrainedSlope_WT_O]'
        if self.initialize['SandDunes_WT_Y_Figure'].lower() == 'yes':
            print '  Initial Sand Dunes, Wetland Tundra, Young age Figure [Output/Barrow/SandDunes/WT_Y]'
        if self.initialize['SandDunes_WT_M_Figure'].lower() == 'yes':
            print '  Initial Sand Dunes, Wetland Tundra, Medium age Figure [Ouput/Barrow/SandDunes_WT_M]'
        if self.initialize['SandDunes_WT_O_Figure'].lower() == 'yes':
            print '  Initial Sand Dunes, Wetland Tundra, Old age Figure [Output/Barrow/SandDunes_WT_O]'
        if self.initialize['SaturatedBarrens_WT_Y_Figure'].lower()  == 'yes':
            print '  Initial Saturated Barrens, Wetland Tundra, Young age Figure [Output/Barrow/SaturatedBarrens_WT_Y]'
        if self.initialize['SaturatedBarrens_WT_M_Figure'].lower() == 'yes':
            print '  Initial Saturated Barrens, Wetland Tundra, Medium age Figure [Output/Barrow/SaturatedBarrens_WT_M]'
        if self.initialize['SaturatedBarrens_WT_O_Figure'].lower() == 'yes':
            print '  Initial Saturated Barrens, Wetland Tundra, Old age Figure [Output/Barrow/SaturatedBarrens_WT_O]'
        if self.initialize['Shrubs_WT_O_Figure'].lower() == 'yes':
            print '  Initial Shrubs, Wetland Tundra, Old age Figure [Output/Barrow/Shrubs_WT_O]'
        if self.initialize['Urban_WT_Figure'].lower() == 'yes':
            print '  Initial Urban area, Wetland Tundra, Figure [Output/Barrow/Urban_WT]'
        if self.initialize['Rivers_WT_Y_Figure'].lower() == 'yes':
            print '  Initial Rivers, Wetland Tundra, Young age Figure [Output/Barrow/Rivers_WT_Y]'
        if self.initialize['Rivers_WT_M_Figure'].lower() == 'yes':
            print '  Initial Rivers, Wetland Tundra, Medium age Figure [Output/Barrow/Rivers_WT_M]'
        if self.initialize['Rivers_WT_O_Figure'].lower() == 'yes':
            print '  Initial Rivers, Wetland Tunrda, old age Figure [Output/Barrow/Rivers_WT_O]'
        
#        if self.initialize['WetNPG_Figure'].lower() == 'yes':
#            print '  Initial Wetland Non-polygonal Ground Figure [Output/Wet_NPG]'
#        if self.initialize['WetLCP_Figure'].lower() == 'yes':
#            print '  Initial Wetland Low Center Polygon Figure [Output/Wet_LCP]'
#        if self.initialize['WetCLC_Figure'].lower() == 'yes':
#            print '  Initial Wetland Coalescent Low Center Polygon Figure [Output/Wet_CLC]'
#        if self.initialize['WetFCP_Figure'].lower() == 'yes':
#            print '  Initial Wetland Flat Center Polygon Figure [Output/Wet_FCP]'
#        if self.initialize['WetHCP_Figure'].lower() == 'yes':
#            print '  Initial Wetland High Center Polygon Figure [Output/Wet_HCP]'
#        if self.initialize['Lakes_Figure'].lower() == 'yes':
#            print '  Initial Lakes Figure [Output/Lakes]'
#        if self.initialize['Ponds_Figure'].lower() == 'yes':
#            print '  Initial Ponds Figure [Output/Ponds]'
#        if self.initialize['Rivers_Figure'].lower() == 'yes':
#            print '  Initial Rivers Figure [Output/Other_Cohorts]'
#        if self.initialize['Urban_Figure'].lower() == 'yes':
#            print '  Initial Ubran Figure [Output/Other_Cohorts]'
        if self.initialize['All_Cohorts_Figure'].lower() == 'yes':
            print '  Total Cohorts Figure [Output/Barrow/All_Cohorts]'
    print ' '

    print 'Outputs of Normalized Cohort Distribution:'
    if self.initialize['Normalized_Cohort_Distribution_Figure'].lower() != 'yes':
        print '  No outputs generated.'
    else:
        if self.initialize['Meadow_WT_Y_Normal'].lower() == 'yes':
            print '  Inital Meadow, Wetland Tundra, Young age Normalized [Output/Barrow/Meadow_WT_Y]'
        if self.initialize['Meadow_WT_M_Normal'].lower() == 'yes':
            print '  Initial Meadow, Wetland Tundra, Medium age Normalized [Output/Barrow/Meadow_WT_M]'
        if self.initialize['Meadow_WT_O_Normal'].lower() == 'yes':
            print '  Initial Meadow, Wetland Tundra, Old age Normalized [Output/Barrow/Meadow_WT_O]'
        if self.initialize['LCP_WT_Y_Normal'].lower() == 'yes':
            print '  Initial Low Center Polygon, Wetland Tundra, Young age Normalized [Output/Barrow/LCP_WT_Y]'
        if self.initialize['LCP_WT_M_Normal'].lower() == 'yes':
            print '  Initial Low Center Polygon, Wetland Tundra, Medium age Normalized [Output/Barrow/LCP_WT_M]'
        if self.initialize['LCP_WT_O_Normal'].lower() == 'yes':
            print '  Initial Low Center Polygon, Wetland Tundra, Old age Normalized [Output/Barrow/LCP_WT_O]'
        if self.initialize['CLC_WT_Y_Normal'].lower() == 'yes':
            print '  Initial Coalescent Low Center Polygon, Wetland Tundra, Young age Normalized [Output/Barrow/CLC_WT_Y]'
        if self.initialize['CLC_WT_M_Normal'].lower() == 'yes':
            print '  Initial Coalescent Low Center Polygon, Wetland Tundra, Medium age Normalized [Output/Barrow/CLC_WT_M]'
        if self.initialize['CLC_WT_O_Normal'].lower() == 'yes':
            print '  Initial Coalescent Low Center Polygon, Wetland Tundra, Old age Normalized [Output/Barrow/CLC_WT_O]'
        if self.initialize['FCP_WT_Y_Normal'].lower() == 'yes':
            print '  Initial Flat Center Polygon, Wetland Tundra, Young age Normalized [Output/Barrow/FCP_WT_Y]'
        if self.initialize['FCP_WT_M_Normal'].lower() == 'yes':
            print '  Initial Flat Center Polygon, Wetland Tundra, Medium age Normalized [Output/Barrow/FCP_WT_M]'
        if self.initialize['FCP_WT_O_Normal'].lower() == 'yes':
            print '  Initial Flat Center Polygon, Wetland Tundra, Old age Normalized [Output/Barrow/FCP_WT_O]'
        if self.initialize['HCP_WT_Y_Normal'].lower() == 'yes':
            print '  Initial High Center Polygon, Wetland Tundra, Young age Normalized [Output/Barrow/HCP_WT_Y]'
        if self.initialize['HCP_WT_M_Normal'].lower() == 'yes':
            print '  Initial High Center Polygon, Wetland Tundra, Medium age Normalized [Output/Barrow/HCP_WT_M]'
        if self.initialize['HCP_WT_O_Normal'].lower() == 'yes':
            print '  Initial High Center Polygon, Wetland Tundra, Old age Normalized [Output/Barrow/HCP_WT_O]'
        if self.initialize['LargeLakes_WT_Y_Normal'].lower() == 'yes':
            print '  Initial Large (size) Lakes, Wetland Tundra, Young age Normalized [Output/Barrow/LargeLakes_WT_Y]'
        if self.initialize['LargeLakes_WT_M_Normal'].lower() == 'yes':
            print '  Initial Large (size) Lakes, Wetland Tundra, Medium age Normalized [Output/Barrow/LargeLakes_WT_M]'
        if self.initialize['LargeLakes_WT_O_Normal'].lower() == 'yes':
            print '  Initial Large (size) Lakes, Wetland Tundra, Old age Normalized [Output/Barrow/LargeLakes_WT_O]'
        if self.initialize['MediumLakes_WT_Y_Normal'].lower() == 'yes':
            print '  Initial Medium (size) Lakes, Wetland Tundra, Young age Normalized [Output/Barrow/MediumLakes_WT_Y]'
        if self.initialize['MediumLakes_WT_M_Normal'].lower() == 'yes':
            print '  Initial Medium (size) Lakes, Wetland Tundra, Medium age Normalized [Output/Barrow/MediumLakes_WT_M]'
        if self.initialize['MediumLakes_WT_O_Normal'].lower() == 'yes':
            print '  Initial Medium (size) Lakes, Wetland Tundra, Old age Normalized [Output/Barrow/MediumLakes_WT_O]'
        if self.initialize['SmallLakes_WT_Y_Normal'].lower() == 'yes':
            print '  Initial Small (size) Lakes, Wetland Tundra, Young age Normalized [Output/Barrow/SmallLakes_WT_Y]'
        if self.initialize['SmallLakes_WT_M_Normal'].lower() == 'yes':
            print '  Initial Small (size) Lakes, Wetland Tundra, Medium age Normalized [Output/Barrow/SmallLakes_WT_M]'
        if self.initialize['SmallLakes_WT_O_Normal'].lower() == 'yes':
            print '  Initial Small (size) Lakes, Wetland Tundra, Old age Normalized [Output/Barrow/SmallLakes_WT_O]'
        if self.initialize['Ponds_WT_Y_Normal'].lower() == 'yes':
            print '  Initial Ponds, Wetland Tundra, Young age Normalized [Output/Barrow/Ponds_WT_Y]'
        if self.initialize['Ponds_WT_M_Normal'].lower() == 'yes':
            print '  Initial Ponds, Wetland Tundra, Medium age Normalized [Output/Barrow/Ponds_WT_M]'
        if self.initialize['Ponds_WT_O_Normal'].lower() == 'yes':
            print '  Initial Ponds, Wetland Tundra, Old age Normalized [Output/Barrow/Ponds_WT_O]'
        if self.initialize['CoastalWaters_WT_O_Normal'].lower() == 'yes':
            print '  Initial Coastal Waters, Wetland Tundra, Old age Normalized [Output/Barrow/CoastalWaters_WT_O]'
        if self.initialize['DrainedSlope_WT_Y_Normal'].lower() == 'yes':
            print '  Initial Drained Slope, Wetland Tundra, Young age Normalized [Output/Barrow/DrainedSlope_WT_Y]'
        if self.initialize['DrainedSlope_WT_M_Normal'].lower() == 'yes':
            print '  Initial Drained Slope, Wetland Tundra, Medium age Normalized [Output/Barrow/DrainedSlope_WT_M]'
        if self.initialize['DrainedSlope_WT_O_Normal'].lower() == 'yes':
            print '  Initial Drained Slope, Wetland Tundra, Old age Normalized [Output/Barrow/DrainedSlope_WT_O]'
        if self.initialize['SandDunes_WT_Y_Normal'].lower() == 'yes':
            print '  Initial Sand Dunes, Wetland Tundra, Young age Normalized [Output/Barrow/SandDunes/WT_Y]'
        if self.initialize['SandDunes_WT_M_Normal'].lower() == 'yes':
            print '  Initial Sand Dunes, Wetland Tundra, Medium age Normalized [Ouput/Barrow/SandDunes_WT_M]'
        if self.initialize['SandDunes_WT_O_Normal'].lower() == 'yes':
            print '  Initial Sand Dunes, Wetland Tundra, Old age Normalized [Output/Barrow/SandDunes_WT_O]'
        if self.initialize['SaturatedBarrens_WT_Y_Normal'].lower()  == 'yes':
            print '  Initial Saturated Barrens, Wetland Tundra, Young age Normalized [Output/Barrow/SaturatedBarrens_WT_Y]'
        if self.initialize['SaturatedBarrens_WT_M_Normal'].lower() == 'yes':
            print '  Initial Saturated Barrens, Wetland Tundra, Medium age Normalized [Output/Barrow/SaturatedBarrens_WT_M]'
        if self.initialize['SaturatedBarrens_WT_O_Normal'].lower() == 'yes':
            print '  Initial Saturated Barrens, Wetland Tundra, Old age Normalized [Output/Barrow/SaturatedBarrens_WT_O]'
        if self.initialize['Shrubs_WT_O_Normal'].lower() == 'yes':
            print '  Initial Shrubs, Wetland Tundra, Old age Normalized [Output/Barrow/Shrubs_WT_O]'
        if self.initialize['Urban_WT_Normal'].lower() == 'yes':
            print '  Initial Urban area, Wetland Tundra, Normal [Output/Barrow/Urban_WT]'
        if self.initialize['Rivers_WT_Y_Normal'].lower() == 'yes':
            print '  Initial Rivers, Wetland Tundra, Young age Normalized [Output/Barrow/Rivers_WT_Y]'
        if self.initialize['Rivers_WT_M_Normal'].lower() == 'yes':
            print '  Initial Rivers, Wetland Tundra, Medium age Normalized [Output/Barrow/Rivers_WT_M]'
        if self.initialize['Rivers_WT_O_Normal'].lower() == 'yes':
            print '  Initial Rivers, Wetland Tunrda, old age Normalized [Output/Barrow/Rivers_WT_O]'
        
        
#        if self.initialize['WetNPG_Normal'].lower() == 'yes':
#            print '  Normalized Wetland Non-polygonal Ground Figure [Output/Wet_NPG]'
#        if self.initialize['WetLCP_Normal'].lower() == 'yes':
#            print '  Normalized Wetland Low Center Polygon Figure [Output/Wet_LCP]'
#        if self.initialize['WetCLC_Normal'].lower() == 'yes':
#            print '  Normalized Wetland Coalescent Low Center Polygon Figure [Output/Wet_CLC]'
#        if self.initialize['WetFCP_Normal'].lower() == 'yes':
#            print '  Normalized Wetland Flat Center Polygon Figure [Output/Wet_FCP]'
#        if self.initialize['WetHCP_Normal'].lower() == 'yes':
#            print '  Normalized Wetland High Center Polygon Figure [Output/Wet_HCP]'
#        if self.initialize['Lakes_Normal'].lower() == 'yes':
#            print '  Normalized Lakes Figure [Output/Lakes]'
#        if self.initialize['Ponds_Normal'].lower() == 'yes':
#            print '  Normalized Ponds Figure [Output/Ponds]'
#        if self.initialize['Rivers_Normal'].lower() == 'yes':
#            print '  Normalized Rivers Figure [Output/Other_Cohorts]'
#        if self.initialize['Urban_Normal'].lower() == 'yes':
#            print '  Normalized Ubran Figure [Output/Other_Cohorts]'
        if self.initialize['Total_Cohorts_Normal'].lower() == 'yes':
            print '  Normalize Total Cohorts [Output/All_Cohorts]'
    print ' '

    print 'Outputs of Cohort Ages:'
    if self.initialize['Initial_Cohort_Age_Figure'].lower() != 'yes':
        print '  No outputs generated.'
    else:
        if self.initialize['Meadow_WT_Y_Age'].lower() == 'yes':
            print '  Inital Meadow, Wetland Tundra, Young age distribution [Output/Barrow/Meadow_WT_Y]'
        if self.initialize['Meadow_WT_M_Age'].lower() == 'yes':
            print '  Initial Meadow, Wetland Tundra, Medium age distribution [Output/Barrow/Meadow_WT_M]'
        if self.initialize['Meadow_WT_O_Age'].lower() == 'yes':
            print '  Initial Meadow, Wetland Tundra, Old age distribution [Output/Barrow/Meadow_WT_O]'
        if self.initialize['LCP_WT_Y_Age'].lower() == 'yes':
            print '  Initial Low Center Polygon, Wetland Tundra, Young age distribution [Output/Barrow/LCP_WT_Y]'
        if self.initialize['LCP_WT_M_Age'].lower() == 'yes':
            print '  Initial Low Center Polygon, Wetland Tundra, Medium age distribution [Output/Barrow/LCP_WT_M]'
        if self.initialize['LCP_WT_O_Age'].lower() == 'yes':
            print '  Initial Low Center Polygon, Wetland Tundra, Old age distribution [Output/Barrow/LCP_WT_O]'
        if self.initialize['CLC_WT_Y_Age'].lower() == 'yes':
            print '  Initial Coalescent Low Center Polygon, Wetland Tundra, Young age distribution [Output/Barrow/CLC_WT_Y]'
        if self.initialize['CLC_WT_M_Age'].lower() == 'yes':
            print '  Initial Coalescent Low Center Polygon, Wetland Tundra, Medium age distribution [Output/Barrow/CLC_WT_M]'
        if self.initialize['CLC_WT_O_Age'].lower() == 'yes':
            print '  Initial Coalescent Low Center Polygon, Wetland Tundra, Old age distribution [Output/Barrow/CLC_WT_O]'
        if self.initialize['FCP_WT_Y_Age'].lower() == 'yes':
            print '  Initial Flat Center Polygon, Wetland Tundra, Young age distribution [Output/Barrow/FCP_WT_Y]'
        if self.initialize['FCP_WT_M_Age'].lower() == 'yes':
            print '  Initial Flat Center Polygon, Wetland Tundra, Medium age distribution [Output/Barrow/FCP_WT_M]'
        if self.initialize['FCP_WT_O_Age'].lower() == 'yes':
            print '  Initial Flat Center Polygon, Wetland Tundra, Old age distribution [Output/Barrow/FCP_WT_O]'
        if self.initialize['HCP_WT_Y_Age'].lower() == 'yes':
            print '  Initial High Center Polygon, Wetland Tundra, Young age distribution [Output/Barrow/HCP_WT_Y]'
        if self.initialize['HCP_WT_M_Age'].lower() == 'yes':
            print '  Initial High Center Polygon, Wetland Tundra, Medium age distribution [Output/Barrow/HCP_WT_M]'
        if self.initialize['HCP_WT_O_Age'].lower() == 'yes':
            print '  Initial High Center Polygon, Wetland Tundra, Old age distribution [Output/Barrow/HCP_WT_O]'
        if self.initialize['LargeLakes_WT_Y_Age'].lower() == 'yes':
            print '  Initial Large (size) Lakes, Wetland Tundra, Young age distribution [Output/Barrow/LargeLakes_WT_Y]'
        if self.initialize['LargeLakes_WT_M_Age'].lower() == 'yes':
            print '  Initial Large (size) Lakes, Wetland Tundra, Medium age distribution [Output/Barrow/LargeLakes_WT_M]'
        if self.initialize['LargeLakes_WT_O_Age'].lower() == 'yes':
            print '  Initial Large (size) Lakes, Wetland Tundra, Old age distribution [Output/Barrow/LargeLakes_WT_O]'
        if self.initialize['MediumLakes_WT_Y_Age'].lower() == 'yes':
            print '  Initial Medium (size) Lakes, Wetland Tundra, Young age distribution [Output/Barrow/MediumLakes_WT_Y]'
        if self.initialize['MediumLakes_WT_M_Age'].lower() == 'yes':
            print '  Initial Medium (size) Lakes, Wetland Tundra, Medium age distribution [Output/Barrow/MediumLakes_WT_M]'
        if self.initialize['MediumLakes_WT_O_Age'].lower() == 'yes':
            print '  Initial Medium (size) Lakes, Wetland Tundra, Old age distribution [Output/Barrow/MediumLakes_WT_O]'
        if self.initialize['SmallLakes_WT_Y_Age'].lower() == 'yes':
            print '  Initial Small (size) Lakes, Wetland Tundra, Young age distribution [Output/Barrow/SmallLakes_WT_Y]'
        if self.initialize['SmallLakes_WT_M_Age'].lower() == 'yes':
            print '  Initial Small (size) Lakes, Wetland Tundra, Medium age distribution [Output/Barrow/SmallLakes_WT_M]'
        if self.initialize['SmallLakes_WT_O_Age'].lower() == 'yes':
            print '  Initial Small (size) Lakes, Wetland Tundra, Old age distribution [Output/Barrow/SmallLakes_WT_O]'
        if self.initialize['Ponds_WT_Y_Age'].lower() == 'yes':
            print '  Initial Ponds, Wetland Tundra, Young age distribution [Output/Barrow/Ponds_WT_Y]'
        if self.initialize['Ponds_WT_M_Age'].lower() == 'yes':
            print '  Initial Ponds, Wetland Tundra, Medium age distribution [Output/Barrow/Ponds_WT_M]'
        if self.initialize['Ponds_WT_O_Age'].lower() == 'yes':
            print '  Initial Ponds, Wetland Tundra, Old age distribution [Output/Barrow/Ponds_WT_O]'
        if self.initialize['CoastalWaters_WT_O_Age'].lower() == 'yes':
            print '  Initial Coastal Waters, Wetland Tundra, Old age distribution [Output/Barrow/CoastalWaters_WT_O]'
        if self.initialize['DrainedSlope_WT_Y_Age'].lower() == 'yes':
            print '  Initial Drained Slope, Wetland Tundra, Young age distribution [Output/Barrow/DrainedSlope_WT_Y]'
        if self.initialize['DrainedSlope_WT_M_Age'].lower() == 'yes':
            print '  Initial Drained Slope, Wetland Tundra, Medium age distribution [Output/Barrow/DrainedSlope_WT_M]'
        if self.initialize['DrainedSlope_WT_O_Age'].lower() == 'yes':
            print '  Initial Drained Slope, Wetland Tundra, Old age distribution [Output/Barrow/DrainedSlope_WT_O]'
        if self.initialize['SandDunes_WT_Y_Age'].lower() == 'yes':
            print '  Initial Sand Dunes, Wetland Tundra, Young age distribution [Output/Barrow/SandDunes/WT_Y]'
        if self.initialize['SandDunes_WT_M_Age'].lower() == 'yes':
            print '  Initial Sand Dunes, Wetland Tundra, Medium age distribution [Ouput/Barrow/SandDunes_WT_M]'
        if self.initialize['SandDunes_WT_O_Age'].lower() == 'yes':
            print '  Initial Sand Dunes, Wetland Tundra, Old age distribution [Output/Barrow/SandDunes_WT_O]'
        if self.initialize['SaturatedBarrens_WT_Y_Age'].lower()  == 'yes':
            print '  Initial Saturated Barrens, Wetland Tundra, Young age distribution [Output/Barrow/SaturatedBarrens_WT_Y]'
        if self.initialize['SaturatedBarrens_WT_M_Age'].lower() == 'yes':
            print '  Initial Saturated Barrens, Wetland Tundra, Medium age distribution [Output/Barrow/SaturatedBarrens_WT_M]'
        if self.initialize['SaturatedBarrens_WT_O_Age'].lower() == 'yes':
            print '  Initial Saturated Barrens, Wetland Tundra, Old age distribution [Output/Barrow/SaturatedBarrens_WT_O]'
        if self.initialize['Shrubs_WT_O_Age'].lower() == 'yes':
            print '  Initial Shrubs, Wetland Tundra, Old age distribution [Output/Barrow/Shrubs_WT_O]'
        if self.initialize['Urban_WT_Age'].lower() == 'yes':
            print '  Initial Urban area, Wetland Tundra, Normal [Output/Barrow/Urban_WT]'
        if self.initialize['Rivers_WT_Y_Age'].lower() == 'yes':
            print '  Initial Rivers, Wetland Tundra, Young age distribution [Output/Barrow/Rivers_WT_Y]'
        if self.initialize['Rivers_WT_M_Age'].lower() == 'yes':
            print '  Initial Rivers, Wetland Tundra, Medium age distribution [Output/Barrow/Rivers_WT_M]'
        if self.initialize['Rivers_WT_O_Age'].lower() == 'yes':
            print '  Initial Rivers, Wetland Tunrda, old age distribution [Output/Barrow/Rivers_WT_O]'

#        if self.initialize['WetNPG_Age'].lower() == 'yes':
#            print '  Wetland Non-polygonal Ground Age [Output/Wet_NPG]'
#        if self.initialize['WetLCP_Age'].lower() == 'yes':
#            print '  Wetland Low Center Polygon Age [Output/Wet_LCP]'
#        if self.initialize['WetCLC_Age'].lower() == 'yes':
#            print '  Wetland Coalescent Low Center Polygon Age [Output/Wet_CLC]'
#        if self.initialize['WetFCP_Age'].lower() == 'yes':
#            print '  Wetland Flat Center Polygon Age [Output/Wet_FCP]'
#        if self.initialize['WetHCP_Age'].lower() == 'yes':
#            print '  Wetland High Center Polygon Age [Output/Wet_HCP]'
#        if self.initialize['Lakes_Age'].lower() == 'yes':
#            print '  Lakes Age [Output/Lakes]'
#        if self.initialize['Ponds_Age'].lower() == 'yes':
#            print '  Normalized Ponds Age [Output/Ponds]'
    print ' '
    ##########################################################################
    print '-----------------------------------'
    print '   Meteorologic Data Information   '
    print '-----------------------------------'
    if self.Met['met_distribution'].lower() == 'point':
        print 'Point meteorologic data is used.'
    else:
        print 'Meterologic data is distributed.'
    print 'Meteorologic Data File: ', self.met_file
    if self.Met['degree_day_method'].lower() == 'read':
        print 'Degree Days read from files: ',self.Met['TDD_file'] +' and '+self.Met['FDD_file']
    else:
        print 'Degree Days calculated during simulation.'
    print ' '

    print 'Outputs:'
    if self.Met['Degree_Day_Output'].lower() == 'yes':
        print '  Degree-Days are output.'
        
    # Note: Might want to add climatic event probability and block size here
    ############################################################################
    print '------------------------------------'
    print '   General Terrestrial Information   '
    print '------------------------------------'
    print 'Ground Ice Distribution: ', self.Terrestrial['Ice_Distribution']
    print 'Drainage Efficiency Distribution: ', self.Terrestrial['Drainage_Efficiency_Distribution']
    print 'Initial Active Layer Depth Distribution: ',self.Terrestrial['ALD_Distribution']
    print ' '
    ## #________________________________________________________
    ## # Setting Protective Layer Factor Shorthand for results
    ## #________________________________________________________
    ## WNPG = self.Terrestrial['Wet_NPG_PLF']
    ## WLCP = self.Terrestrial['Wet_LCP_PLF']
    ## WCLC = self.Terrestrial['Wet_CLC_PLF']
    ## WFCP = self.Terrestrial['Wet_FCP_PLF']
    ## WHCP = self.Terrestrial['Wet_HCP_PLF']
    ## GNPG = self.Terrestrial['Gra_NPG_PLF']
    ## GLCP = self.Terrestrial['Gra_LCP_PLF']
    ## GFCP = self.Terrestrial['Gra_FCP_PLF']
    ## GHCP = self.Terrestrial['Gra_HCP_PLF']
    ## SNPG = self.Terrestrial['Shr_NPG_PLF']
    ## SLCP = self.Terrestrial['Shr_LCP_PLF']
    ## SFCP = self.Terrestrial['Shr_FCP_PLF']
    ## SHCP = self.Terrestrial['Shr_HCP_PLF']
    ## LPLF = self.Terrestrial['Lakes_PLF']
    ## PPLF = self.Terrestrial['Ponds_PLF']
    ## #_________________________________________________________
    ## print '__________________________________________________'
    ## print '              Protective Layer Factors            '
    ## print '__________________________________________________'
    ## print '     | Wetland | Graminoid | Shrub | Lake | Pond |'
    ## print '__________________________________________________'
    ## print ' NPG |  '+str(WNPG)+'    |   '+str(GNPG)+'     | '+str(SNPG)+'   |  '+\
    ##   str(LPLF)+' | '+str(PPLF)+'  |'
    ## print ' LCP |  '+str(WLCP)+'    |   '+str(GLCP)+'     | '+str(SLCP)+'   |  '+\
    ##   '--  | --   |'
    ## print ' CLC |  '+str(WCLC)+'    |    --     |  --   |  '+\
    ##   '--  | --   |'
    ## print ' FCP |  '+str(WFCP)+'   |   '+str(GFCP)+'    | '+str(SFCP)+'   |  '+\
    ##   '--  | --   |'
    ## print ' HCP |  '+str(WHCP)+'    |   '+str(GHCP)+'     | '+str(SHCP)+'   |  '+\
    ##   '--  | --   |'
    ## print '__________________________________________________'
    ## print ' '
    ############################################################################
    print '==========================================================='
    print '----------------------------------- '
    print ' Meadows, Wetland Tundra, All ages'
    print '-----------------------------------'
    init_total = self.Init_Meadow_WT_Y + self.Init_Meadow_WT_M + self.Init_Meadow_WT_O
    final_total = self.Final_Meadow_WT_Y + self.Final_Meadow_WT_M + self.Final_Meadow_WT_O
    print 'Initial Fractional Area (km2): ', init_total 
    print 'Final Fractional Area (km2): ',  final_total
    print 'Total Fractional Change (km2): ', final_total - init_total
    print 'Percent difference: ', ((final_total - init_total)/init_total)*100.
    print ' '    
    print '----------------------------------- '
    print ' Meadows, Wetland Tundra Young age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_Meadow_WT_Y
    print 'Final Fractional Area (km2): ', self.Final_Meadow_WT_Y
    print 'Total Fractional Change (km2): ', self.Final_Meadow_WT_Y - self.Init_Meadow_WT_Y
    print 'Percent difference: ', ((self.Final_Meadow_WT_Y - self.Init_Meadow_WT_Y)/self.Init_Meadow_WT_Y)*100.
    print ' '
    print '----------------------------------- '
    print ' Meadows, Wetland Tundra Medium age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_Meadow_WT_M
    print 'Final Fractional Area (km2): ', self.Final_Meadow_WT_M
    print 'Total Fractional Change (km2): ', self.Final_Meadow_WT_M - self.Init_Meadow_WT_M
    print 'Percent difference: ', ((self.Final_Meadow_WT_M - self.Init_Meadow_WT_M)/self.Init_Meadow_WT_M)*100.
    print ' '
    print '----------------------------------- '
    print ' Meadows, Wetland Tundra Old age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_Meadow_WT_O
    print 'Final Fractional Area (km2): ', self.Final_Meadow_WT_O
    print 'Total Fractional Change (km2): ', self.Final_Meadow_WT_O - self.Init_Meadow_WT_O
    print 'Percent difference: ', ((self.Final_Meadow_WT_O - self.Init_Meadow_WT_O)/self.Init_Meadow_WT_O)*100.
    print ' '
    print '==========================================================='
    print '----------------------------------- '
    print ' Low Center Polygons, Wetland Tundra, All ages'
    print '-----------------------------------'
    init_total = self.Init_LCP_WT_Y + self.Init_LCP_WT_M + self.Init_LCP_WT_O
    final_total = self.Final_LCP_WT_Y + self.Final_LCP_WT_M + self.Final_LCP_WT_O
    print 'Initial Fractional Area (km2): ', init_total 
    print 'Final Fractional Area (km2): ',  final_total
    print 'Total Fractional Change (km2): ', final_total - init_total
    print 'Percent difference: ', ((final_total - init_total)/init_total)*100.
    print ' '    
    print '----------------------------------- '
    print ' Low Center Polygons, Wetland Tundra Young age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_LCP_WT_Y
    print 'Final Fractional Area (km2): ', self.Final_LCP_WT_Y
    print 'Total Fractional Change (km2): ', self.Final_LCP_WT_Y - self.Init_LCP_WT_Y
    print 'Percent difference: ', ((self.Final_LCP_WT_Y - self.Init_LCP_WT_Y)/self.Init_LCP_WT_Y)*100.
    print ' '
    print '----------------------------------- '
    print ' Low Center Polygons, Wetland Tundra Medium age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_LCP_WT_M
    print 'Final Fractional Area (km2): ', self.Final_LCP_WT_M
    print 'Total Fractional Change (km2): ', self.Final_LCP_WT_M - self.Init_LCP_WT_M
    print 'Percent difference: ', ((self.Final_LCP_WT_M - self.Init_LCP_WT_M)/self.Init_LCP_WT_M)*100.
    print ' '
    print '----------------------------------- '
    print ' Low Center Polygons, Wetland Tundra Old age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_LCP_WT_O
    print 'Final Fractional Area (km2): ', self.Final_LCP_WT_O
    print 'Total Fractional Change (km2): ', self.Final_LCP_WT_O - self.Init_LCP_WT_O
    print 'Percent difference: ', ((self.Final_LCP_WT_O - self.Init_LCP_WT_O)/self.Init_LCP_WT_O)*100.
    print ' '
    print '==========================================================='    
    print '----------------------------------- '
    print ' Coalescent Low Center Polygons, Wetland Tundra, All ages'
    print '-----------------------------------'
    init_total = self.Init_CLC_WT_Y + self.Init_CLC_WT_M + self.Init_CLC_WT_O
    final_total = self.Final_CLC_WT_Y + self.Final_CLC_WT_M + self.Final_CLC_WT_O
    print 'Initial Fractional Area (km2): ', init_total 
    print 'Final Fractional Area (km2): ',  final_total
    print 'Total Fractional Change (km2): ', final_total - init_total
    print 'Percent difference: ', ((final_total - init_total)/init_total)*100.
    print ' '    
    print '----------------------------------- '
    print ' Coalescent Low Center Polygons, Wetland Tundra Young age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_CLC_WT_Y
    print 'Final Fractional Area (km2): ', self.Final_CLC_WT_Y
    print 'Total Fractional Change (km2): ', self.Final_CLC_WT_Y - self.Init_CLC_WT_Y
    print 'Percent difference: ', ((self.Final_CLC_WT_Y - self.Init_CLC_WT_Y)/self.Init_CLC_WT_Y)*100.
    print ' '
    print '----------------------------------- '
    print ' Coalescent Low Center Polygons, Wetland Tundra Medium age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_CLC_WT_M
    print 'Final Fractional Area (km2): ', self.Final_CLC_WT_M
    print 'Total Fractional Change (km2): ', self.Final_CLC_WT_M - self.Init_CLC_WT_M
    print 'Percent difference: ', ((self.Final_CLC_WT_M - self.Init_CLC_WT_M)/self.Init_CLC_WT_M)*100.
    print ' '
    print '----------------------------------- '
    print ' Coalescent Low Center Polygons, Wetland Tundra Old age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_CLC_WT_O
    print 'Final Fractional Area (km2): ', self.Final_CLC_WT_O
    print 'Total Fractional Change (km2): ', self.Final_CLC_WT_O - self.Init_CLC_WT_O
    print 'Percent difference: ', ((self.Final_CLC_WT_O - self.Init_CLC_WT_O)/self.Init_CLC_WT_O)*100.
    print ' '
    print '==========================================================='
    print '----------------------------------- '
    print ' Flat Center Polygons, Wetland Tundra, All ages'
    print '-----------------------------------'
    init_total = self.Init_FCP_WT_Y + self.Init_FCP_WT_M + self.Init_FCP_WT_O
    final_total = self.Final_FCP_WT_Y + self.Final_FCP_WT_M + self.Final_FCP_WT_O
    print 'Initial Fractional Area (km2): ', init_total 
    print 'Final Fractional Area (km2): ',  final_total
    print 'Total Fractional Change (km2): ', final_total - init_total
    print 'Percent difference: ', ((final_total - init_total)/init_total)*100.
    print ' '    
    print '----------------------------------- '
    print ' Flat Center Polygons, Wetland Tundra Young age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_FCP_WT_Y
    print 'Final Fractional Area (km2): ', self.Final_FCP_WT_Y
    print 'Total Fractional Change (km2): ', self.Final_FCP_WT_Y - self.Init_FCP_WT_Y
    print 'Percent difference: ', ((self.Final_FCP_WT_Y - self.Init_FCP_WT_Y)/self.Init_FCP_WT_Y)*100.
    print ' '
    print '----------------------------------- '
    print ' Flat Center Polygons, Wetland Tundra Medium age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_FCP_WT_M
    print 'Final Fractional Area (km2): ', self.Final_FCP_WT_M
    print 'Total Fractional Change (km2): ', self.Final_FCP_WT_M - self.Init_FCP_WT_M
    print 'Percent difference: ', ((self.Final_FCP_WT_M - self.Init_FCP_WT_M)/self.Init_FCP_WT_M)*100.
    print ' '
    print '----------------------------------- '
    print ' Flat Center Polygons, Wetland Tundra Old age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_FCP_WT_O
    print 'Final Fractional Area (km2): ', self.Final_FCP_WT_O
    print 'Total Fractional Change (km2): ', self.Final_FCP_WT_O - self.Init_FCP_WT_O
    print 'Percent difference: ', ((self.Final_FCP_WT_O - self.Init_FCP_WT_O)/self.Init_FCP_WT_O)*100.
    print ' '
    print '==========================================================='    
    print '----------------------------------- '
    print ' High Center Polygons, Wetland Tundra, All ages'
    print '-----------------------------------'
    init_total = self.Init_HCP_WT_Y + self.Init_HCP_WT_M + self.Init_HCP_WT_O
    final_total = self.Final_HCP_WT_Y + self.Final_HCP_WT_M + self.Final_HCP_WT_O
    print 'Initial Fractional Area (km2): ', init_total 
    print 'Final Fractional Area (km2): ',  final_total
    print 'Total Fractional Change (km2): ', final_total - init_total
    print 'Percent difference: ', ((final_total - init_total)/init_total)*100.
    print ' '    
    print '----------------------------------- '
    print ' High Center Polygons, Wetland Tundra Young age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_HCP_WT_Y
    print 'Final Fractional Area (km2): ', self.Final_HCP_WT_Y
    print 'Total Fractional Change (km2): ', self.Final_HCP_WT_Y - self.Init_HCP_WT_Y
    print 'Percent difference: ', ((self.Final_HCP_WT_Y - self.Init_HCP_WT_Y)/self.Init_HCP_WT_Y)*100.
    print ' '
    print '----------------------------------- '
    print ' High Center Polygons, Wetland Tundra Medium age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_HCP_WT_M
    print 'Final Fractional Area (km2): ', self.Final_HCP_WT_M
    print 'Total Fractional Change (km2): ', self.Final_HCP_WT_M - self.Init_HCP_WT_M
    print 'Percent difference: ', ((self.Final_HCP_WT_M - self.Init_HCP_WT_M)/self.Init_HCP_WT_M)*100.
    print ' '
    print '----------------------------------- '
    print ' High Center Polygons, Wetland Tundra Old age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_HCP_WT_O
    print 'Final Fractional Area (km2): ', self.Final_HCP_WT_O
    print 'Total Fractional Change (km2): ', self.Final_HCP_WT_O - self.Init_HCP_WT_O
    print 'Percent difference: ', ((self.Final_HCP_WT_O - self.Init_HCP_WT_O)/self.Init_HCP_WT_O)*100.
    print ' '
    print '==========================================================='  
    print '------------------------------------------ '
    print ' Lakes, Wetland Tundra, All sizes and ages'
    print '-------------------------------------------'
    init_total = self.Init_LargeLakes_WT_Y + self.Init_LargeLakes_WT_M + self.Init_LargeLakes_WT_O + \
                 self.Init_MediumLakes_WT_Y + self.Init_MediumLakes_WT_M + self.Init_MediumLakes_WT_O + \
                 self.Init_SmallLakes_WT_Y + self.Init_SmallLakes_WT_M + self.Init_SmallLakes_WT_O
    final_total = self.Final_LargeLakes_WT_Y + self.Final_LargeLakes_WT_M + self.Final_LargeLakes_WT_O + \
                  self.Final_MediumLakes_WT_Y + self.Final_MediumLakes_WT_M + self.Final_MediumLakes_WT_O + \
                  self.Final_SmallLakes_WT_Y + self.Final_SmallLakes_WT_M + self.Final_SmallLakes_WT_O
    print 'Initial Fractional Area (km2): ', init_total 
    print 'Final Fractional Area (km2): ',  final_total
    print 'Total Fractional Change (km2): ', final_total - init_total
    print 'Percent difference: ', ((final_total - init_total)/init_total)*100.
    print ' '    
    print '----------------------------------- '
    print ' Large Lakes, Wetland Tundra Young age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_LargeLakes_WT_Y
    print 'Final Fractional Area (km2): ', self.Final_LargeLakes_WT_Y
    print 'Total Fractional Change (km2): ', self.Final_LargeLakes_WT_Y - self.Init_LargeLakes_WT_Y
    print 'Percent difference: ', ((self.Final_LargeLakes_WT_Y - self.Init_LargeLakes_WT_Y)/self.Init_LargeLakes_WT_Y)*100.
    print ' '
    print '----------------------------------- '
    print ' Large lakes, Wetland Tundra Medium age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_LargeLakes_WT_M
    print 'Final Fractional Area (km2): ', self.Final_LargeLakes_WT_M
    print 'Total Fractional Change (km2): ', self.Final_LargeLakes_WT_M - self.Init_LargeLakes_WT_M
    print 'Percent difference: ', ((self.Final_LargeLakes_WT_M - self.Init_LargeLakes_WT_M)/self.Init_LargeLakes_WT_M)*100.
    print ' '
    print '----------------------------------- '
    print ' Large Lakes, Wetland Tundra Old age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_LargeLakes_WT_O
    print 'Final Fractional Area (km2): ', self.Final_LargeLakes_WT_O
    print 'Total Fractional Change (km2): ', self.Final_LargeLakes_WT_O - self.Init_LargeLakes_WT_O
    print 'Percent difference: ', ((self.Final_LargeLakes_WT_O - self.Init_LargeLakes_WT_O)/self.Init_LargeLakes_WT_O)*100.
    print ' '
    print '----------------------------------- '
    print ' Medium Lakes, Wetland Tundra Young age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_MediumLakes_WT_Y
    print 'Final Fractional Area (km2): ', self.Final_MediumLakes_WT_Y
    print 'Total Fractional Change (km2): ', self.Final_MediumLakes_WT_Y - self.Init_MediumLakes_WT_Y
    print 'Percent difference: ', ((self.Final_MediumLakes_WT_Y - self.Init_MediumLakes_WT_Y)/self.Init_MediumLakes_WT_Y)*100.
    print ' '
    print '----------------------------------- '
    print ' Medium lakes, Wetland Tundra Medium age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_MediumLakes_WT_M
    print 'Final Fractional Area (km2): ', self.Final_MediumLakes_WT_M
    print 'Total Fractional Change (km2): ', self.Final_MediumLakes_WT_M - self.Init_MediumLakes_WT_M
    print 'Percent difference: ', ((self.Final_MediumLakes_WT_M - self.Init_MediumLakes_WT_M)/self.Init_MediumLakes_WT_M)*100.
    print ' '
    print '----------------------------------- '
    print ' Medium Lakes, Wetland Tundra Old age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_MediumLakes_WT_O
    print 'Final Fractional Area (km2): ', self.Final_MediumLakes_WT_O
    print 'Total Fractional Change (km2): ', self.Final_MediumLakes_WT_O - self.Init_MediumLakes_WT_O
    print 'Percent difference: ', ((self.Final_MediumLakes_WT_O - self.Init_MediumLakes_WT_O)/self.Init_MediumLakes_WT_O)*100.
    print ' '
    print '----------------------------------- '
    print ' Small Lakes, Wetland Tundra Young age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_SmallLakes_WT_Y
    print 'Final Fractional Area (km2): ', self.Final_SmallLakes_WT_Y
    print 'Total Fractional Change (km2): ', self.Final_SmallLakes_WT_Y - self.Init_SmallLakes_WT_Y
    print 'Percent difference: ', ((self.Final_SmallLakes_WT_Y - self.Init_SmallLakes_WT_Y)/self.Init_SmallLakes_WT_Y)*100.
    print ' '
    print '----------------------------------- '
    print ' Small lakes, Wetland Tundra Medium age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_SmallLakes_WT_M
    print 'Final Fractional Area (km2): ', self.Final_SmallLakes_WT_M
    print 'Total Fractional Change (km2): ', self.Final_SmallLakes_WT_M - self.Init_SmallLakes_WT_M
    print 'Percent difference: ', ((self.Final_SmallLakes_WT_M - self.Init_SmallLakes_WT_M)/self.Init_SmallLakes_WT_M)*100.
    print ' '
    print '----------------------------------- '
    print ' Small Lakes, Wetland Tundra Old age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_SmallLakes_WT_O
    print 'Final Fractional Area (km2): ', self.Final_SmallLakes_WT_O
    print 'Total Fractional Change (km2): ', self.Final_SmallLakes_WT_O - self.Init_SmallLakes_WT_O
    print 'Percent difference: ', ((self.Final_SmallLakes_WT_O - self.Init_SmallLakes_WT_O)/self.Init_SmallLakes_WT_O)*100.
    print ' '
    print '==========================================================='  
    print '------------------------------------------ '
    print ' Ponds, Wetland Tundra, All  ages'
    print '-------------------------------------------'
    init_total = self.Init_Ponds_WT_Y + self.Init_Ponds_WT_M + self.Init_Ponds_WT_O 
    final_total = self.Final_Ponds_WT_Y + self.Final_Ponds_WT_M + self.Final_Ponds_WT_O 
    print 'Initial Fractional Area (km2): ', init_total 
    print 'Final Fractional Area (km2): ',  final_total
    print 'Total Fractional Change (km2): ', final_total - init_total
    print 'Percent difference: ', ((final_total - init_total)/init_total)*100.
    print ' '    
    print '----------------------------------- '
    print ' Ponds, Wetland Tundra Young age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_Ponds_WT_Y
    print 'Final Fractional Area (km2): ', self.Final_Ponds_WT_Y
    print 'Total Fractional Change (km2): ', self.Final_Ponds_WT_Y - self.Init_Ponds_WT_Y
    print 'Percent difference: ', ((self.Final_Ponds_WT_Y - self.Init_Ponds_WT_Y)/self.Init_Ponds_WT_Y)*100.
    print ' '
    print '----------------------------------- '
    print ' Ponds, Wetland Tundra Medium age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_Ponds_WT_M
    print 'Final Fractional Area (km2): ', self.Final_Ponds_WT_M
    print 'Total Fractional Change (km2): ', self.Final_Ponds_WT_M - self.Init_Ponds_WT_M
    print 'Percent difference: ', ((self.Final_Ponds_WT_M - self.Init_Ponds_WT_M)/self.Init_Ponds_WT_M)*100.
    print ' '
    print '----------------------------------- '
    print ' Ponds, Wetland Tundra Old age'
    print '-----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_Ponds_WT_O
    print 'Final Fractional Area (km2): ', self.Final_Ponds_WT_O
    print 'Total Fractional Change (km2): ', self.Final_Ponds_WT_O - self.Init_Ponds_WT_O
    print 'Percent difference: ', ((self.Final_Ponds_WT_O - self.Init_Ponds_WT_O)/self.Init_Ponds_WT_O)*100.
    print '===========================================================' 


############################################################################
###    print '----------------------------------'
###    print '        Simulation Notes '
###    print '----------------------------------'
###    file = open(self.control['Run_dir']+self.Input_directory+str('/Notes/')+self.notes_file, 'r')
###    print file.read()
###    file.close()
###    print '----------------------------------'
###    print ' '
#============================================================================================
#============================================================================================
def on_file(self):
    if self.Simulation_area.lower() == 'barrow':
        file = open(self.control['Run_dir']+self.Output_directory+str('/Barrow/Archive/')+ \
            self.archive_time+str('_')+self.simulation_name+str('.txt'), 'a')
    elif self.Simulation_area.lower() == 'yukon':
         file = open(self.control['Run_dir']+self.Output_directory+str('/Yukon/Archive/')+ \
            self.archive_time+str('_')+self.simulation_name+str('.txt'), 'a')       
    elif self.Simulation_area.lower() == 'tanana':
         file = open(self.control['Run_dir']+self.Output_directory+str('/Tanana/Archive/')+ \
            self.archive_time+str('_')+self.simulation_name+str('.txt'), 'a')     
    

    file.write('=====================================================\n')
    file.write('       Simulation Results        \n')
    file.write('=====================================================\n')
    file.write('Simulation name: '+ self.simulation_name +str('\n'))
    file.write('Start Date / Time : ' + self.start_time +str('\n'))
    file.write('End Date / Time : '+ self.finish_time +str('\n'))
    file.write('Total Simulation Time (minutes): '+ str((self.finish - self.start)/60.0) + str('\n'))
    if self.archive_simulation.lower() == 'yes':
        file.write('Archive Status: Active \n')
        file.write('Archive Name : '+ self.simulation_name + str('\n'))
    else:
        file.write('Archive Status: Inactive \n')

    file.write('Number of time-steps in the simulation: '+str(self.stop)+str('\n'))
    file.write(' \n')
    ##########################################################################
    file.write( '-----------------------------------\n')
    file.write( ' Initial Cohort Information \n')
    file.write( '-----------------------------------\n')
    file.write( 'Outputs of Initial Cohort Distribution:\n')
    if self.initialize['Initial_Cohort_Distribution_Figure'].lower() != 'yes':
        file.write( '  No outputs generated. \n')
    else:
        if self.initialize['Meadow_WT_Y_Figure'].lower() == 'yes':
            file.write( '  Inital Meadow, Wetland Tundra, Young age Figure [Output/Barrow/Meadow_WT_Y] \n')
        if self.initialize['Meadow_WT_M_Figure'].lower() == 'yes':
            file.write( '  Initial Meadow, Wetland Tundra, Medium age Figure [Output/Barrow/Meadow_WT_M] \n')
        if self.initialize['Meadow_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial Meadow, Wetland Tundra, Old age Figure [Output/Barrow/Meadow_WT_O] \n')
        if self.initialize['LCP_WT_Y_Figure'].lower() == 'yes':
            file.write( '  Initial Low Center Polygon, Wetland Tundra, Young age Figure [Output/Barrow/LCP_WT_Y] \n')
        if self.initialize['LCP_WT_M_Figure'].lower() == 'yes':
            file.write( '  Initial Low Center Polygon, Wetland Tundra, Medium age Figure [Output/Barrow/LCP_WT_M] \n')
        if self.initialize['LCP_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial Low Center Polygon, Wetland Tundra, Old age Figure [Output/Barrow/LCP_WT_O] \n')
        if self.initialize['CLC_WT_Y_Figure'].lower() == 'yes':
            file.write( '  Initial Coalescent Low Center Polygon, Wetland Tundra, Young age Figure [Output/Barrow/CLC_WT_Y] \n')
        if self.initialize['CLC_WT_M_Figure'].lower() == 'yes':
            file.write( '  Initial Coalescent Low Center Polygon, Wetland Tundra, Medium age Figure [Output/Barrow/CLC_WT_M] \n')
        if self.initialize['CLC_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial Coalescent Low Center Polygon, Wetland Tundra, Old age Figure [Output/Barrow/CLC_WT_O] \n')
        if self.initialize['FCP_WT_Y_Figure'].lower() == 'yes':
            file.write( '  Initial Flat Center Polygon, Wetland Tundra, Young age Figure [Output/Barrow/FCP_WT_Y] \n')
        if self.initialize['FCP_WT_M_Figure'].lower() == 'yes':
            file.write( '  Initial Flat Center Polygon, Wetland Tundra, Medium age Figure [Output/Barrow/FCP_WT_M] \n')
        if self.initialize['FCP_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial Flat Center Polygon, Wetland Tundra, Old age Figure [Output/Barrow/FCP_WT_O] \n')
        if self.initialize['HCP_WT_Y_Figure'].lower() == 'yes':
            file.write( '  Initial High Center Polygon, Wetland Tundra, Young age Figure [Output/Barrow/HCP_WT_Y] \n')
        if self.initialize['HCP_WT_M_Figure'].lower() == 'yes':
            file.write( '  Initial High Center Polygon, Wetland Tundra, Medium age Figure [Output/Barrow/HCP_WT_M] \n')
        if self.initialize['HCP_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial High Center Polygon, Wetland Tundra, Old age Figure [Output/Barrow/HCP_WT_O] \n')
        if self.initialize['LargeLakes_WT_Y_Figure'].lower() == 'yes':
            file.write( '  Initial Large (size) Lakes, Wetland Tundra, Young age Figure [Output/Barrow/LargeLakes_WT_Y] \n')
        if self.initialize['LargeLakes_WT_M_Figure'].lower() == 'yes':
            file.write( '  Initial Large (size) Lakes, Wetland Tundra, Medium age Figure [Output/Barrow/LargeLakes_WT_M] \n')
        if self.initialize['LargeLakes_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial Large (size) Lakes, Wetland Tundra, Old age Figure [Output/Barrow/LargeLakes_WT_O] \n')
        if self.initialize['MediumLakes_WT_Y_Figure'].lower() == 'yes':
            file.write( '  Initial Medium (size) Lakes, Wetland Tundra, Young age Figure [Output/Barrow/MediumLakes_WT_Y] \n')
        if self.initialize['MediumLakes_WT_M_Figure'].lower() == 'yes':
            file.write( '  Initial Medium (size) Lakes, Wetland Tundra, Medium age Figure [Output/Barrow/MediumLakes_WT_M] \n')
        if self.initialize['MediumLakes_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial Medium (size) Lakes, Wetland Tundra, Old age Figure [Output/Barrow/MediumLakes_WT_O] \n')
        if self.initialize['SmallLakes_WT_Y_Figure'].lower() == 'yes':
            file.write( '  Initial Small (size) Lakes, Wetland Tundra, Young age Figure [Output/Barrow/SmallLakes_WT_Y] \n')
        if self.initialize['SmallLakes_WT_M_Figure'].lower() == 'yes':
            file.write( '  Initial Small (size) Lakes, Wetland Tundra, Medium age Figure [Output/Barrow/SmallLakes_WT_M] \n')
        if self.initialize['SmallLakes_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial Small (size) Lakes, Wetland Tundra, Old age Figure [Output/Barrow/SmallLakes_WT_O] \n')
        if self.initialize['Ponds_WT_Y_Figure'].lower() == 'yes':
            file.write( '  Initial Ponds, Wetland Tundra, Young age Figure [Output/Barrow/Ponds_WT_Y] \n')
        if self.initialize['Ponds_WT_M_Figure'].lower() == 'yes':
            file.write( '  Initial Ponds, Wetland Tundra, Medium age Figure [Output/Barrow/Ponds_WT_M] \n')
        if self.initialize['Ponds_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial Ponds, Wetland Tundra, Old age Figure [Output/Barrow/Ponds_WT_O] \n')
        if self.initialize['CoastalWaters_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial Coastal Waters, Wetland Tundra, Old age Figure [Output/Barrow/CoastalWaters_WT_O] \n')
        if self.initialize['DrainedSlope_WT_Y_Figure'].lower() == 'yes':
            file.write( '  Initial Drained Slope, Wetland Tundra, Young age Figure [Output/Barrow/DrainedSlope_WT_Y] \n')
        if self.initialize['DrainedSlope_WT_M_Figure'].lower() == 'yes':
            file.write( '  Initial Drained Slope, Wetland Tundra, Medium age Figure [Output/Barrow/DrainedSlope_WT_M] \n')
        if self.initialize['DrainedSlope_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial Drained Slope, Wetland Tundra, Old age Figure [Output/Barrow/DrainedSlope_WT_O] \n')
        if self.initialize['SandDunes_WT_Y_Figure'].lower() == 'yes':
            file.write( '  Initial Sand Dunes, Wetland Tundra, Young age Figure [Output/Barrow/SandDunes/WT_Y] \n')
        if self.initialize['SandDunes_WT_M_Figure'].lower() == 'yes':
            file.write( '  Initial Sand Dunes, Wetland Tundra, Medium age Figure [Ouput/Barrow/SandDunes_WT_M] \n')
        if self.initialize['SandDunes_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial Sand Dunes, Wetland Tundra, Old age Figure [Output/Barrow/SandDunes_WT_O] \n')
        if self.initialize['SaturatedBarrens_WT_Y_Figure'].lower()  == 'yes':
            file.write( '  Initial Saturated Barrens, Wetland Tundra, Young age Figure [Output/Barrow/SaturatedBarrens_WT_Y] \n')
        if self.initialize['SaturatedBarrens_WT_M_Figure'].lower() == 'yes':
            file.write( '  Initial Saturated Barrens, Wetland Tundra, Medium age Figure [Output/Barrow/SaturatedBarrens_WT_M] \n')
        if self.initialize['SaturatedBarrens_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial Saturated Barrens, Wetland Tundra, Old age Figure [Output/Barrow/SaturatedBarrens_WT_O] \n')
        if self.initialize['Shrubs_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial Shrubs, Wetland Tundra, Old age Figure [Output/Barrow/Shrubs_WT_O] \n')
        if self.initialize['Urban_WT_Figure'].lower() == 'yes':
            file.write( '  Initial Urban area, Wetland Tundra, Figure [Output/Barrow/Urban_WT] \n')
        if self.initialize['Rivers_WT_Y_Figure'].lower() == 'yes':
            file.write( '  Initial Rivers, Wetland Tundra, Young age Figure [Output/Barrow/Rivers_WT_Y] \n')
        if self.initialize['Rivers_WT_M_Figure'].lower() == 'yes':
            file.write( '  Initial Rivers, Wetland Tundra, Medium age Figure [Output/Barrow/Rivers_WT_M] \n')
        if self.initialize['Rivers_WT_O_Figure'].lower() == 'yes':
            file.write( '  Initial Rivers, Wetland Tunrda, old age Figure [Output/Barrow/Rivers_WT_O] \n')
        if self.initialize['All_Cohorts_Figure'].lower() == 'yes':
            file.write( '  Total Cohorts Figure [Output/All_Cohorts] \n \n')
        
 #       if self.initialize['WetNPG_Figure'].lower() == 'yes':
 #           file.write( '  Initial Wetland Non-polygonal Ground Figure [Output/Wet_NPG] \n')
 #       if self.initialize['WetLCP_Figure'].lower() == 'yes':
 #           file.write( '  Initial Wetland Low Center Polygon Figure [Output/Wet_LCP] \n')
 #       if self.initialize['WetCLC_Figure'].lower() == 'yes':
 #           file.write( '  Initial Wetland Coalescent Low Center Polygon Figure [Output/Wet_CLC] \n')
 #       if self.initialize['WetFCP_Figure'].lower() == 'yes':
 #           file.write( '  Initial Wetland Flat Center Polygon Figure [Output/Wet_FCP] \n')
 #       if self.initialize['WetHCP_Figure'].lower() == 'yes':
 #           file.write( '  Initial Wetland High Center Polygon Figure [Output/Wet_HCP] \n')
 #       if self.initialize['Lakes_Figure'].lower() == 'yes':
 #           file.write( '  Initial Lakes Figure [Output/Lakes] \n')
 #       if self.initialize['Ponds_Figure'].lower() == 'yes':
 #           file.write( '  Initial Ponds Figure [Output/Ponds] \n')
 #       if self.initialize['Rivers_Figure'].lower() == 'yes':
 #           file.write( '  Initial Rivers Figure [Output/Other_Cohorts] \n')
 #       if self.initialize['Urban_Figure'].lower() == 'yes':
 #           file.write( '  Initial Ubran Figure [Output/Other_Cohorts] \n')

    
    file.write( 'Outputs of Initial Cohort Fractional Distribution:\n')
        
    if self.initialize['Normalized_Cohort_Distribution_Figure'].lower() != 'yes':
        file.write( '  No outputs generated. \n')
    else:
        if self.initialize['Meadow_WT_Y_Normal'].lower() == 'yes':
            file.write( '  Inital Meadow, Wetland Tundra, Young age Normalized [Output/Barrow/Meadow_WT_Y] \n')
        if self.initialize['Meadow_WT_M_Normal'].lower() == 'yes':
            file.write( '  Initial Meadow, Wetland Tundra, Medium age Normalized [Output/Barrow/Meadow_WT_M] \n')
        if self.initialize['Meadow_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial Meadow, Wetland Tundra, Old age Normalized [Output/Barrow/Meadow_WT_O] \n')
        if self.initialize['LCP_WT_Y_Normal'].lower() == 'yes':
            file.write( '  Initial Low Center Polygon, Wetland Tundra, Young age Normalized [Output/Barrow/LCP_WT_Y] \n')
        if self.initialize['LCP_WT_M_Normal'].lower() == 'yes':
            file.write( '  Initial Low Center Polygon, Wetland Tundra, Medium age Normalized [Output/Barrow/LCP_WT_M] \n')
        if self.initialize['LCP_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial Low Center Polygon, Wetland Tundra, Old age Normalized [Output/Barrow/LCP_WT_O] \n')
        if self.initialize['CLC_WT_Y_Normal'].lower() == 'yes':
            file.write( '  Initial Coalescent Low Center Polygon, Wetland Tundra, Young age Normalized [Output/Barrow/CLC_WT_Y] \n')
        if self.initialize['CLC_WT_M_Normal'].lower() == 'yes':
            file.write( '  Initial Coalescent Low Center Polygon, Wetland Tundra, Medium age Normalized [Output/Barrow/CLC_WT_M] \n')
        if self.initialize['CLC_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial Coalescent Low Center Polygon, Wetland Tundra, Old age Normalized [Output/Barrow/CLC_WT_O] \n')
        if self.initialize['FCP_WT_Y_Normal'].lower() == 'yes':
            file.write( '  Initial Flat Center Polygon, Wetland Tundra, Young age Normalized [Output/Barrow/FCP_WT_Y] \n')
        if self.initialize['FCP_WT_M_Normal'].lower() == 'yes':
            file.write( '  Initial Flat Center Polygon, Wetland Tundra, Medium age Normalized [Output/Barrow/FCP_WT_M] \n')
        if self.initialize['FCP_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial Flat Center Polygon, Wetland Tundra, Old age Normalized [Output/Barrow/FCP_WT_O] \n')
        if self.initialize['HCP_WT_Y_Normal'].lower() == 'yes':
            file.write( '  Initial High Center Polygon, Wetland Tundra, Young age Normalized [Output/Barrow/HCP_WT_Y] \n')
        if self.initialize['HCP_WT_M_Normal'].lower() == 'yes':
            file.write( '  Initial High Center Polygon, Wetland Tundra, Medium age Normalized [Output/Barrow/HCP_WT_M] \n')
        if self.initialize['HCP_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial High Center Polygon, Wetland Tundra, Old age Normalized [Output/Barrow/HCP_WT_O] \n')
        if self.initialize['LargeLakes_WT_Y_Normal'].lower() == 'yes':
            file.write( '  Initial Large (size) Lakes, Wetland Tundra, Young age Normalized [Output/Barrow/LargeLakes_WT_Y] \n')
        if self.initialize['LargeLakes_WT_M_Normal'].lower() == 'yes':
            file.write( '  Initial Large (size) Lakes, Wetland Tundra, Medium age Normalized [Output/Barrow/LargeLakes_WT_M] \n')
        if self.initialize['LargeLakes_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial Large (size) Lakes, Wetland Tundra, Old age Normalized [Output/Barrow/LargeLakes_WT_O] \n')
        if self.initialize['MediumLakes_WT_Y_Normal'].lower() == 'yes':
            file.write( '  Initial Medium (size) Lakes, Wetland Tundra, Young age Normalized [Output/Barrow/MediumLakes_WT_Y] \n')
        if self.initialize['MediumLakes_WT_M_Normal'].lower() == 'yes':
            file.write( '  Initial Medium (size) Lakes, Wetland Tundra, Medium age Normalized [Output/Barrow/MediumLakes_WT_M] \n')
        if self.initialize['MediumLakes_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial Medium (size) Lakes, Wetland Tundra, Old age Normalized [Output/Barrow/MediumLakes_WT_O] \n')
        if self.initialize['SmallLakes_WT_Y_Normal'].lower() == 'yes':
            file.write( '  Initial Small (size) Lakes, Wetland Tundra, Young age Normalized [Output/Barrow/SmallLakes_WT_Y] \n')
        if self.initialize['SmallLakes_WT_M_Normal'].lower() == 'yes':
            file.write( '  Initial Small (size) Lakes, Wetland Tundra, Medium age Normalized [Output/Barrow/SmallLakes_WT_M] \n')
        if self.initialize['SmallLakes_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial Small (size) Lakes, Wetland Tundra, Old age Normalized [Output/Barrow/SmallLakes_WT_O] \n')
        if self.initialize['Ponds_WT_Y_Normal'].lower() == 'yes':
            file.write( '  Initial Ponds, Wetland Tundra, Young age Normalized [Output/Barrow/Ponds_WT_Y] \n')
        if self.initialize['Ponds_WT_M_Normal'].lower() == 'yes':
            file.write( '  Initial Ponds, Wetland Tundra, Medium age Normalized [Output/Barrow/Ponds_WT_M] \n')
        if self.initialize['Ponds_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial Ponds, Wetland Tundra, Old age Normalized [Output/Barrow/Ponds_WT_O] \n')
        if self.initialize['CoastalWaters_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial Coastal Waters, Wetland Tundra, Old age Normalized [Output/Barrow/CoastalWaters_WT_O] \n')
        if self.initialize['DrainedSlope_WT_Y_Normal'].lower() == 'yes':
            file.write( '  Initial Drained Slope, Wetland Tundra, Young age Normalized [Output/Barrow/DrainedSlope_WT_Y] \n')
        if self.initialize['DrainedSlope_WT_M_Normal'].lower() == 'yes':
            file.write( '  Initial Drained Slope, Wetland Tundra, Medium age Normalized [Output/Barrow/DrainedSlope_WT_M] \n')
        if self.initialize['DrainedSlope_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial Drained Slope, Wetland Tundra, Old age Normalized [Output/Barrow/DrainedSlope_WT_O] \n')
        if self.initialize['SandDunes_WT_Y_Normal'].lower() == 'yes':
            file.write( '  Initial Sand Dunes, Wetland Tundra, Young age Normalized [Output/Barrow/SandDunes/WT_Y] \n')
        if self.initialize['SandDunes_WT_M_Normal'].lower() == 'yes':
            file.write( '  Initial Sand Dunes, Wetland Tundra, Medium age Normalized [Ouput/Barrow/SandDunes_WT_M] \n')
        if self.initialize['SandDunes_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial Sand Dunes, Wetland Tundra, Old age Normalized [Output/Barrow/SandDunes_WT_O] \n')
        if self.initialize['SaturatedBarrens_WT_Y_Normal'].lower()  == 'yes':
            file.write( '  Initial Saturated Barrens, Wetland Tundra, Young age Normalized [Output/Barrow/SaturatedBarrens_WT_Y] \n')
        if self.initialize['SaturatedBarrens_WT_M_Normal'].lower() == 'yes':
            file.write( '  Initial Saturated Barrens, Wetland Tundra, Medium age Normalized [Output/Barrow/SaturatedBarrens_WT_M] \n')
        if self.initialize['SaturatedBarrens_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial Saturated Barrens, Wetland Tundra, Old age Normalized [Output/Barrow/SaturatedBarrens_WT_O] \n')
        if self.initialize['Shrubs_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial Shrubs, Wetland Tundra, Old age Normalized [Output/Barrow/Shrubs_WT_O] \n')
        if self.initialize['Urban_WT_Normal'].lower() == 'yes':
            file.write( '  Initial Urban area, Wetland Tundra, Normal [Output/Barrow/Urban_WT] \n')
        if self.initialize['Rivers_WT_Y_Normal'].lower() == 'yes':
            file.write( '  Initial Rivers, Wetland Tundra, Young age Normalized [Output/Barrow/Rivers_WT_Y] \n')
        if self.initialize['Rivers_WT_M_Normal'].lower() == 'yes':
            file.write( '  Initial Rivers, Wetland Tundra, Medium age Normalized [Output/Barrow/Rivers_WT_M] \n')
        if self.initialize['Rivers_WT_O_Normal'].lower() == 'yes':
            file.write( '  Initial Rivers, Wetland Tunrda, old age Normalized [Output/Barrow/Rivers_WT_O] \n')        

#        if self.initialize['WetNPG_Normal'].lower() == 'yes':
#            file.write( '  Normalized Wetland Non-polygonal Ground Figure [Output/Wet_NPG] \n')
#        if self.initialize['WetLCP_Normal'].lower() == 'yes':
#            file.write( '  Normalized Wetland Low Center Polygon Figure [Output/Wet_LCP] \n')
#        if self.initialize['WetCLC_Normal'].lower() == 'yes':
#            file.write( '  Normalized Wetland Coalescent Low Center Polygon Figure [Output/Wet_CLC] \n')
#        if self.initialize['WetFCP_Normal'].lower() == 'yes':
#            file.write( '  Normalized Wetland Flat Center Polygon Figure [Output/Wet_FCP] \n')
#        if self.initialize['WetHCP_Normal'].lower() == 'yes':
#            file.write( '  Normalized Wetland High Center Polygon Figure [Output/Wet_HCP] \n')
#        if self.initialize['Lakes_Normal'].lower() == 'yes':
#            file.write( '  Normalized Lakes Figure [Output/Lakes] \n')
#        if self.initialize['Ponds_Normal'].lower() == 'yes':
#            file.write( '  Normalized Ponds Figure [Output/Ponds] \n')
#        if self.initialize['Rivers_Normal'].lower() == 'yes':
#            file.write( '  Normalized Rivers Figure [Output/Other_Cohorts] \n')
#        if self.initialize['Urban_Normal'].lower() == 'yes':
#            file.write( '  Normalized Ubran Figure [Output/Other_Cohorts] \n')
#        if self.initialize['Total_Cohorts_Normal'].lower() == 'yes':
#            file.write( '  Normalized Total Cohorts [Output/All_Cohorts] \n \n')

    file.write( 'Outputs of Initial Cohort Age:\n')
        
    if self.initialize['Initial_Cohort_Age_Figure'].lower() != 'yes':
        file.write( '  No outputs generated. \n')
    else:
        if self.initialize['Meadow_WT_Y_Age'].lower() == 'yes':
            file.write( '  Inital Meadow, Wetland Tundra, Young age distribution [Output/Barrow/Meadow_WT_Y] \n')
        if self.initialize['Meadow_WT_M_Age'].lower() == 'yes':
            file.write( '  Initial Meadow, Wetland Tundra, Medium age distribution [Output/Barrow/Meadow_WT_M] \n')
        if self.initialize['Meadow_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial Meadow, Wetland Tundra, Old age distribution [Output/Barrow/Meadow_WT_O] \n')
        if self.initialize['LCP_WT_Y_Age'].lower() == 'yes':
            file.write( '  Initial Low Center Polygon, Wetland Tundra, Young age distribution [Output/Barrow/LCP_WT_Y] \n')
        if self.initialize['LCP_WT_M_Age'].lower() == 'yes':
            file.write( '  Initial Low Center Polygon, Wetland Tundra, Medium age distribution [Output/Barrow/LCP_WT_M] \n')
        if self.initialize['LCP_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial Low Center Polygon, Wetland Tundra, Old age distribution [Output/Barrow/LCP_WT_O] \n')
        if self.initialize['CLC_WT_Y_Age'].lower() == 'yes':
            file.write( '  Initial Coalescent Low Center Polygon, Wetland Tundra, Young age distribution [Output/Barrow/CLC_WT_Y] \n')
        if self.initialize['CLC_WT_M_Age'].lower() == 'yes':
            file.write( '  Initial Coalescent Low Center Polygon, Wetland Tundra, Medium age distribution [Output/Barrow/CLC_WT_M] \n')
        if self.initialize['CLC_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial Coalescent Low Center Polygon, Wetland Tundra, Old age distribution [Output/Barrow/CLC_WT_O] \n')
        if self.initialize['FCP_WT_Y_Age'].lower() == 'yes':
            file.write( '  Initial Flat Center Polygon, Wetland Tundra, Young age distribution [Output/Barrow/FCP_WT_Y] \n')
        if self.initialize['FCP_WT_M_Age'].lower() == 'yes':
            file.write( '  Initial Flat Center Polygon, Wetland Tundra, Medium age distribution [Output/Barrow/FCP_WT_M] \n')
        if self.initialize['FCP_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial Flat Center Polygon, Wetland Tundra, Old age distribution [Output/Barrow/FCP_WT_O] \n')
        if self.initialize['HCP_WT_Y_Age'].lower() == 'yes':
            file.write( '  Initial High Center Polygon, Wetland Tundra, Young age distribution [Output/Barrow/HCP_WT_Y] \n')
        if self.initialize['HCP_WT_M_Age'].lower() == 'yes':
            file.write( '  Initial High Center Polygon, Wetland Tundra, Medium age distribution [Output/Barrow/HCP_WT_M] \n')
        if self.initialize['HCP_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial High Center Polygon, Wetland Tundra, Old age distribution [Output/Barrow/HCP_WT_O] \n')
        if self.initialize['LargeLakes_WT_Y_Age'].lower() == 'yes':
            file.write( '  Initial Large (size) Lakes, Wetland Tundra, Young age distribution [Output/Barrow/LargeLakes_WT_Y] \n')
        if self.initialize['LargeLakes_WT_M_Age'].lower() == 'yes':
            file.write( '  Initial Large (size) Lakes, Wetland Tundra, Medium age distribution [Output/Barrow/LargeLakes_WT_M] \n')
        if self.initialize['LargeLakes_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial Large (size) Lakes, Wetland Tundra, Old age distribution [Output/Barrow/LargeLakes_WT_O] \n')
        if self.initialize['MediumLakes_WT_Y_Age'].lower() == 'yes':
            file.write( '  Initial Medium (size) Lakes, Wetland Tundra, Young age distribution [Output/Barrow/MediumLakes_WT_Y] \n')
        if self.initialize['MediumLakes_WT_M_Age'].lower() == 'yes':
            file.write( '  Initial Medium (size) Lakes, Wetland Tundra, Medium age distribution [Output/Barrow/MediumLakes_WT_M] \n')
        if self.initialize['MediumLakes_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial Medium (size) Lakes, Wetland Tundra, Old age distribution [Output/Barrow/MediumLakes_WT_O] \n')
        if self.initialize['SmallLakes_WT_Y_Age'].lower() == 'yes':
            file.write( '  Initial Small (size) Lakes, Wetland Tundra, Young age distribution [Output/Barrow/SmallLakes_WT_Y] \n')
        if self.initialize['SmallLakes_WT_M_Age'].lower() == 'yes':
            file.write( '  Initial Small (size) Lakes, Wetland Tundra, Medium age distribution [Output/Barrow/SmallLakes_WT_M] \n')
        if self.initialize['SmallLakes_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial Small (size) Lakes, Wetland Tundra, Old age distribution [Output/Barrow/SmallLakes_WT_O] \n')
        if self.initialize['Ponds_WT_Y_Age'].lower() == 'yes':
            file.write( '  Initial Ponds, Wetland Tundra, Young age distribution [Output/Barrow/Ponds_WT_Y] \n')
        if self.initialize['Ponds_WT_M_Age'].lower() == 'yes':
            file.write( '  Initial Ponds, Wetland Tundra, Medium age distribution [Output/Barrow/Ponds_WT_M] \n')
        if self.initialize['Ponds_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial Ponds, Wetland Tundra, Old age distribution [Output/Barrow/Ponds_WT_O] \n')
        if self.initialize['CoastalWaters_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial Coastal Waters, Wetland Tundra, Old age distribution [Output/Barrow/CoastalWaters_WT_O] \n')
        if self.initialize['DrainedSlope_WT_Y_Age'].lower() == 'yes':
            file.write( '  Initial Drained Slope, Wetland Tundra, Young age distribution [Output/Barrow/DrainedSlope_WT_Y] \n')
        if self.initialize['DrainedSlope_WT_M_Age'].lower() == 'yes':
            file.write( '  Initial Drained Slope, Wetland Tundra, Medium age distribution [Output/Barrow/DrainedSlope_WT_M] \n')
        if self.initialize['DrainedSlope_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial Drained Slope, Wetland Tundra, Old age distribution [Output/Barrow/DrainedSlope_WT_O] \n')
        if self.initialize['SandDunes_WT_Y_Age'].lower() == 'yes':
            file.write( '  Initial Sand Dunes, Wetland Tundra, Young age distribution [Output/Barrow/SandDunes/WT_Y] \n')
        if self.initialize['SandDunes_WT_M_Age'].lower() == 'yes':
            file.write( '  Initial Sand Dunes, Wetland Tundra, Medium age distribution [Ouput/Barrow/SandDunes_WT_M] \n')
        if self.initialize['SandDunes_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial Sand Dunes, Wetland Tundra, Old age distribution [Output/Barrow/SandDunes_WT_O] \n')
        if self.initialize['SaturatedBarrens_WT_Y_Age'].lower()  == 'yes':
            file.write( '  Initial Saturated Barrens, Wetland Tundra, Young age distribution [Output/Barrow/SaturatedBarrens_WT_Y] \n')
        if self.initialize['SaturatedBarrens_WT_M_Age'].lower() == 'yes':
            file.write( '  Initial Saturated Barrens, Wetland Tundra, Medium age distribution [Output/Barrow/SaturatedBarrens_WT_M] \n')
        if self.initialize['SaturatedBarrens_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial Saturated Barrens, Wetland Tundra, Old age distribution [Output/Barrow/SaturatedBarrens_WT_O] \n')
        if self.initialize['Shrubs_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial Shrubs, Wetland Tundra, Old age distribution [Output/Barrow/Shrubs_WT_O] \n')
        if self.initialize['Urban_WT_Age'].lower() == 'yes':
            file.write( '  Initial Urban area, Wetland Tundra, Normal [Output/Barrow/Urban_WT] \n')
        if self.initialize['Rivers_WT_Y_Age'].lower() == 'yes':
            file.write( '  Initial Rivers, Wetland Tundra, Young age distribution [Output/Barrow/Rivers_WT_Y] \n')
        if self.initialize['Rivers_WT_M_Age'].lower() == 'yes':
            file.write( '  Initial Rivers, Wetland Tundra, Medium age distribution [Output/Barrow/Rivers_WT_M] \n')
        if self.initialize['Rivers_WT_O_Age'].lower() == 'yes':
            file.write( '  Initial Rivers, Wetland Tunrda, old age distribution [Output/Barrow/Rivers_WT_O] \n')        
        
#        if self.initialize['WetNPG_Age'].lower() == 'yes':
#            file.write( '  Wetland Non-polygonal Ground Age [Output/Wet_NPG] \n')
#        if self.initialize['WetLCP_Age'].lower() == 'yes':
#            file.write( '  Wetland Low Center Polygon Age [Output/Wet_LCP] \n')
#        if self.initialize['WetCLC_Age'].lower() == 'yes':
#            file.write( '  Wetland Coalescent Low Center Polygon Age [Output/Wet_CLC] \n')
#        if self.initialize['WetFCP_Age'].lower() == 'yes':
#            file.write( '  Wetland Flat Center Polygon Age [Output/Wet_FCP] \n')
#        if self.initialize['WetHCP_Age'].lower() == 'yes':
#            file.write( '  Wetland High Center Polygon Age [Output/Wet_HCP] \n')
#        if self.initialize['Lakes_Age'].lower() == 'yes':
#            file.write( '  Lakes Age [Output/Lakes] \n')
#        if self.initialize['Ponds_Age'].lower() == 'yes':
#            file.write( '  Ponds Age [Output/Ponds] \n \n')
    
    ##########################################################################    
    file.write( '====================================================\n')
    file.write( '        Meteorologic Data Information               \n')
    file.write( '====================================================\n')
    if self.Met['met_distribution'].lower() == 'point':
        file.write( 'Point meteorologic data is used. \n')
    else:
        file.write( 'Meterologic data is distributed. \n')
    file.write( 'Meteorologic Data File: '+ self.met_file +str('\n'))
    if self.Met['degree_day_method'].lower() == 'read':
        file.write('Degree Days read from files: '+ self.Met['TDD_file'] +' and '+ \
                   self.Met['FDD_file'] +str('\n'))
    else:
        file.write( 'Degree Days calculated during simulation. \n')
    file.write( ' \n')
    
    file.write( 'Output: \n')
    if self.Met['Degree_Day_Output'].lower() == 'yes':
        file.write('  Degree-days are output. \n')
        
    # Note: Might want to add climatic event probability and block size here
    ############################################################################
    file.write( '====================================================\n')
    file.write( '           General Terrestrial Information          \n')
    file.write( '====================================================\n')
    file.write( 'Ground Ice distribution: '+str(self.Terrestrial['Ice_Distribution'])+str('\n'))
    file.write( 'Drainage efficiency distribution: '+ \
                str(self.Terrestrial['Drainage_Efficiency_Distribution'])+str('\n'))
    file.write( 'Initial Active Layer Depth Distribution: '+ \
                str(self.Terrestrial['ALD_Distribution'])+str('\n \n'))
    #-------------------------------------------------------------------------
    file.write( '- - - - - - - - - - - - - - - - - - - - - - - - - -\n')
    file.write( 'Protective Layer Factors        \n')
    file.write( '  Meadow, Wetland Tundra, Young age:   ' + str(self.Terrestrial['Meadow_WT_Y_PLF']) + str(' \n'))
    file.write( '  Meadow, Wetland Tundra, Medium age:  ' + str(self.Terrestrial['Meadow_WT_M_PLF']) + str(' \n'))
    file.write( '  Meadow, Wetland Tundra, Old age:     ' + str(self.Terrestrial['Meadow_WT_O_PLF']) + str(' \n'))
    file.write( '  Low Center Polygon, Wetland Tundra, Young age:  ' + str(self.Terrestrial['LCP_WT_Y_PLF']) + str(' \n'))
    file.write( '  Low Center Polygon, Wetland Tundra, Medium age: ' + str(self.Terrestrial['LCP_WT_M_PLF']) + str(' \n'))
    file.write( '  Low Center Polygon, Wetland Tundra, Old age:    ' + str(self.Terrestrial['LCP_WT_O_PLF']) + str(' \n'))
    file.write( '  Coalescent Low Center Polygon, Wetland Tundra, Young age: ' + str(self.Terrestrial['CLC_WT_Y_PLF']) + str('\n'))
    file.write( '  Coalescent Low Center Polygon, Wetland Tundra, Medium age: ' + str(self.Terrestrial['CLC_WT_M_PLF'])+ str('\n'))
    file.write( '  Coalescent Low Center Polygon, Wetland Tundra, Old age: ' + str(self.Terrestrial['CLC_WT_O_PLF']) + str('\n'))
    file.write( '  Flat Center Polygon, Wetland Tundra, Young age: ' + str(self.Terrestrial['FCP_WT_Y_PLF']) + str('\n'))
    file.write( '  Flat Center Polygon, Wetland Tundra, Medium age: ' + str(self.Terrestrial['FCP_WT_M_PLF']) + str('\n'))
    file.write( '  Flat Center Polygon, Wetland Tundra, Old age: ' +str(self.Terrestrial['FCP_WT_O_PLF']) + str('\n'))
    file.write( '  High Center Polygon, Wetland Tundra, Young age: ' + str(self.Terrestrial['HCP_WT_Y_PLF'])+str('\n'))
    file.write( '  High Center Polygon, Wetland Tundra, Medium age: ' + str(self.Terrestrial['HCP_WT_M_PLF'])+str('\n'))
    file.write( '  High Center Polygon, Wetland Tundra, Old age: '+ str(self.Terrestrial['HCP_WT_O_PLF'])+str('\n'))
    file.write( '  Large Lakes, Wetland Tundra, Young age: ' + str(self.Terrestrial['LargeLakes_WT_Y_PLF']) + str('\n'))
    file.write( '  Large Lakes, Wetland Tundra, Medium age: ' + str(self.Terrestrial['LargeLakes_WT_M_PLF']) + str('\n'))
    file.write( '  Large Lakes, Wetland Tundra, Old age: '+str(self.Terrestrial['LargeLakes_WT_O_PLF'])+str('\n'))
    file.write( '  Medium Lakes, Wetland Tundra, Young age: '+str(self.Terrestrial['MediumLakes_WT_Y_PLF'])+str('\n'))
    file.write( '  Medium Lakes, Wetland Tundra, Medium age: '+str(self.Terrestrial['MediumLakes_WT_M_PLF'])+str('\n'))
    file.write( '  Medium Lakes, Wetland Tundra, Old age: '+str(self.Terrestrial['MediumLakes_WT_O_PLF'])+str('\n'))
    file.write( '  Small Lakes, Wetland Tundra, Young age: '+str(self.Terrestrial['SmallLakes_WT_Y_PLF'])+str('\n'))
    file.write( '  Small Lakes, Wetland Tundra, Medium age: '+str(self.Terrestrial['SmallLakes_WT_M_PLF'])+str('\n'))
    file.write( '  Small Lakes, Wetland Tundra, Old age: '+str(self.Terrestrial['SmallLakes_WT_O_PLF'])+str('\n'))
    file.write( '  Ponds, Wetland Tundra, Young age: '+str(self.Terrestrial['Ponds_WT_Y_PLF'])+str('\n'))
    file.write( '  Ponds, Wetland Tundra, Medium age: '+str(self.Terrestrial['Ponds_WT_M_PLF'])+str('\n'))
    file.write( '  Ponds, Wetland Tundra, Old age: '+str(self.Terrestrial['Ponds_WT_O_PLF'])+str('\n'))
    file.write( '  Rivers, Wetland Tundra, Young age: '+str(self.Terrestrial['Rivers_WT_Y_PLF'])+str('\n'))
    file.write( '  Rivers, Wetland Tundra, Medium age: '+str(self.Terrestrial['Rivers_WT_M_PLF'])+str('\n'))
    file.write( '  Rivers, Wetland Tundra, Old age: '+str(self.Terrestrial['Rivers_WT_O_PLF'])+str('\n'))
    file.write( '  Drained Slope, Wetland Tundra, Young age: '+str(self.Terrestrial['DrainedSlope_WT_Y_PLF'])+str('\n'))
    file.write( '  Drained Slope, Wetland Tundra, Medium age: '+str(self.Terrestrial['DrainedSlope_WT_M_PLF'])+str('\n'))
    file.write( '  Drained Slope, Wetland Tundra, Old age: '+str(self.Terrestrial['DrainedSlope_WT_O_PLF'])+str('\n'))
    file.write( '  Coastal Waters, Wetland Tundra, Old age: '+str(self.Terrestrial['CoastalWaters_WT_O_PLF'])+str('\n'))
    file.write( '  Sand Dunes, Wetland Tunda, Young age: '+str(self.Terrestrial['SandDunes_WT_Y_PLF'])+str('\n'))
    file.write( '  Sand Dunes, Wetland Tundra, Medium age: '+str(self.Terrestrial['SandDunes_WT_M_PLF'])+str('\n'))
    file.write( '  Sand Dunes, Wetland Tundra, Old age: '+str(self.Terrestrial['SandDunes_WT_O_PLF'])+str('\n'))
    file.write( '  Saturated Barrens, Wetland Tundra, Young age: '+str(self.Terrestrial['SaturatedBarrens_WT_Y_PLF'])+str('\n'))
    file.write( '  Saturated Barrens, Wetland Tundra, Medium age: '+str(self.Terrestrial['SaturatedBarrens_WT_M_PLF'])+str('\n'))
    file.write( '  Saturated Barrens, Wetland Tundra, Old age: '+str(self.Terrestrial['SaturatedBarrens_WT_O_PLF'])+str('\n'))
    file.write( '  Shrubs, Wetland Tundra, Old age: '+str(self.Terrestrial['Shrubs_WT_O_PLF'])+str('\n'))
    file.write( '  No Data, Wetland Tundra, Old age: '+str(self.Terrestrial['NoData_WT_O_PLF'])+str('\n'))
    file.write( '  Urban, Wetland Tundra: '+str(self.Terrestrial['Urban_WT_PLF'])+str('\n'))

    file.write( '- - - - - - - - - - - - - - - - - - - - - - - - - -\n')

        
    file.write( '\nOutput: \n')
    if self.Terrestrial['Ice_Distribution_Figure'].lower() == 'yes':
        file.write('  Initial Ice Distribution Figure \n')
    if self.Terrestrial['Drainage_Efficiency_Figure'].lower() == 'yes':
        file.write('  Drainage Efficiency Figure \n')
    if self.Terrestrial['ALD_Distribution_Output'].lower() == 'yes':
        file.write('  Initial Active Layer Depth Figure \n')
    if self.Terrestrial['ALD_Factor_Output'].lower() == 'yes':
        file.write('  Active Layer Factor Figure \n')
    file.write( '- - - - - - - - - - - - - - - - - - - - - - - - - -\n \n')
    
    ############################################################################
        
    file.write( '=============================================================\n')
    file.write( '       Wetland Tundra, Meadows (Non polygonal ground) \n')
    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' Meadows, Wetland Tundra, All ages \n')
    file.write( '----------------------------------- \n')
    init_total = self.Init_Meadow_WT_Y + self.Init_Meadow_WT_M + self.Init_Meadow_WT_O
    final_total = self.Final_Meadow_WT_Y + self.Final_Meadow_WT_M + self.Final_Meadow_WT_O
    file.write( 'Initial Fractional Area (km2): ' +str( init_total )+str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str(  final_total) +str('\n'))
    file.write( 'Total Fractional Change (km2):' + str( final_total - init_total) +str('\n'))
    file.write( 'Percent difference: ' + str( ((final_total - init_total)/init_total)*100.) +str('\n'))
    file.write( ' \n'    )
    file.write( '----------------------------------- \n')
    file.write( ' Meadows, Wetland Tundra Young age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Meadow_WT_Y ) + str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_Meadow_WT_Y) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_Meadow_WT_Y - self.Init_Meadow_WT_Y) + str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_Meadow_WT_Y - self.Init_Meadow_WT_Y)/self.Init_Meadow_WT_Y)*100.) + str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.Meadow_WT_Y['POI_Function']) + str('\n'))
    if self.Meadow_WT_Y['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.Meadow_WT_Y['A1_above'])+\
                   ' | '+str(self.Meadow_WT_Y['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.Meadow_WT_Y['A2_above'])+\
                   ' | '+str(self.Meadow_WT_Y['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.Meadow_WT_Y['x0_above'])+\
                   ' | '+str(self.Meadow_WT_Y['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.Meadow_WT_Y['dx_above'])+\
                   ' | '+str(self.Meadow_WT_Y['dx_below'])+str('\n \n'))
    elif self.Meadow_WT_Y['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.Meadow_WT_Y['a_above'])+\
                   str(' | ')+str(self.Meadow_WT_Y['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.Meadow_WT_Y['b_above']) +\
                   str(' | ')+str(self.Meadow_WT_Y['b_below'])+str('\n \n'))
    elif self.Meadow_WT_Y['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.Meadow_WT_Y['K_above'])+ \
                   str(' | ')+str(self.Meadow_WT_Y['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.Meadow_WT_Y['C_above'])+ \
                   str(' | ')+str(self.Meadow_WT_Y['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.Meadow_WT_Y['A_above'])+ \
                   str(' | ')+str(self.Meadow_WT_Y['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.Meadow_WT_Y['B_above'])+ \
                   str(' | ')+str(self.Meadow_WT_Y['B_below'])+str('\n \n'))
    elif self.Meadow_WT_Y['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.Meadow_WT_Y['HillB_above'])+ \
                   str(' | ')+str(self.Meadow_WT_Y['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.Meadow_WT_Y['HillN_above'])+ \
                   str(' | ')+str(self.Meadow_WT_Y['HillN_below'])+str('\n \n'))
                   
    file.write(' Maximum rate of terrain transition: '+str(self.Meadow_WT_Y['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.Meadow_WT_Y['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.Meadow_WT_Y['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.Meadow_WT_Y['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.Meadow_WT_Y['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.Meadow_WT_Y['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.Meadow_WT_Y['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.Meadow_WT_Y['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.Meadow_WT_Y['Figures'].lower() == 'no' and self.Meadow_WT_Y['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')

    file.write( '===========================================================\n')
    file.write('\n')
    file.write( '----------------------------------- \n')
    file.write( ' Meadows, Wetland Tundra Medium age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): ' +str( self.Init_Meadow_WT_M) +str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_Meadow_WT_M) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_Meadow_WT_M - self.Init_Meadow_WT_M)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_Meadow_WT_M - self.Init_Meadow_WT_M)/self.Init_Meadow_WT_M)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.Meadow_WT_M['POI_Function']) + str('\n'))
    if self.Meadow_WT_M['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.Meadow_WT_M['A1_above'])+\
                   ' | '+str(self.Meadow_WT_M['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.Meadow_WT_M['A2_above'])+\
                   ' | '+str(self.Meadow_WT_M['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.Meadow_WT_M['x0_above'])+\
                   ' | '+str(self.Meadow_WT_M['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.Meadow_WT_M['dx_above'])+\
                   ' | '+str(self.Meadow_WT_M['dx_below'])+str('\n \n'))
    elif self.Meadow_WT_M['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.Meadow_WT_M['a_above'])+\
                   str(' | ')+str(self.Meadow_WT_M['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.Meadow_WT_M['b_above']) +\
                   str(' | ')+str(self.Meadow_WT_M['b_below'])+str('\n \n'))
    elif self.Meadow_WT_M['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.Meadow_WT_M['K_above'])+ \
                   str(' | ')+str(self.Meadow_WT_M['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.Meadow_WT_M['C_above'])+ \
                   str(' | ')+str(self.Meadow_WT_M['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.Meadow_WT_M['A_above'])+ \
                   str(' | ')+str(self.Meadow_WT_M['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.Meadow_WT_M['B_above'])+ \
                   str(' | ')+str(self.Meadow_WT_M['B_below'])+str('\n \n'))
    elif self.Meadow_WT_M['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.Meadow_WT_M['HillB_above'])+ \
                   str(' | ')+str(self.Meadow_WT_M['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.Meadow_WT_M['HillN_above'])+ \
                   str(' | ')+str(self.Meadow_WT_M['HillN_below'])+str('\n \n'))
                   
    file.write(' Maximum rate of terrain transition: '+str(self.Meadow_WT_M['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.Meadow_WT_M['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.Meadow_WT_M['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.Meadow_WT_M['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.Meadow_WT_M['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.Meadow_WT_M['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.Meadow_WT_M['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.Meadow_WT_M['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.Meadow_WT_M['Figures'].lower() == 'no' and self.Meadow_WT_M['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')
    file.write( '----------------------------------- \n')
    file.write( ' Meadows, Wetland Tundra Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Meadow_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_Meadow_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Meadow_WT_O - self.Init_Meadow_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_Meadow_WT_O - self.Init_Meadow_WT_O)/self.Init_Meadow_WT_O)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.Meadow_WT_O['POI_Function']) + str('\n'))
    if self.Meadow_WT_O['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.Meadow_WT_O['A1_above'])+\
                   ' | '+str(self.Meadow_WT_O['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.Meadow_WT_O['A2_above'])+\
                   ' | '+str(self.Meadow_WT_O['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.Meadow_WT_O['x0_above'])+\
                   ' | '+str(self.Meadow_WT_O['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.Meadow_WT_O['dx_above'])+\
                   ' | '+str(self.Meadow_WT_O['dx_below'])+str('\n \n'))
    elif self.Meadow_WT_O['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.Meadow_WT_O['a_above'])+\
                   str(' | ')+str(self.Meadow_WT_O['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.Meadow_WT_O['b_above']) +\
                   str(' | ')+str(self.Meadow_WT_O['b_below'])+str('\n \n'))
    elif self.Meadow_WT_O['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.Meadow_WT_O['K_above'])+ \
                   str(' | ')+str(self.Meadow_WT_O['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.Meadow_WT_O['C_above'])+ \
                   str(' | ')+str(self.Meadow_WT_O['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.Meadow_WT_O['A_above'])+ \
                   str(' | ')+str(self.Meadow_WT_O['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.Meadow_WT_O['B_above'])+ \
                   str(' | ')+str(self.Meadow_WT_O['B_below'])+str('\n \n'))
    elif self.Meadow_WT_O['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.Meadow_WT_O['HillB_above'])+ \
                   str(' | ')+str(self.Meadow_WT_O['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.Meadow_WT_O['HillN_above'])+ \
                   str(' | ')+str(self.Meadow_WT_O['HillN_below'])+str('\n \n'))


    file.write(' Maximum rate of terrain transition: '+str(self.Meadow_WT_O['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.Meadow_WT_O['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.Meadow_WT_O['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.Meadow_WT_O['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.Meadow_WT_O['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.Meadow_WT_O['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.Meadow_WT_O['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.Meadow_WT_O['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.Meadow_WT_O['Figures'].lower() == 'no' and self.Meadow_WT_O['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')
        
    file.write( '=============================================================\n')
    file.write( '       Wetland Tundra, Low Center Polgyons \n')
    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' Low Center Polygons, Wetland Tundra, All ages \n')
    file.write( '----------------------------------- \n')
    init_total = self.Init_LCP_WT_Y + self.Init_LCP_WT_M + self.Init_LCP_WT_O
    final_total = self.Final_LCP_WT_Y + self.Final_LCP_WT_M + self.Final_LCP_WT_O
    file.write( 'Initial Fractional Area (km2): ' +str( init_total )+str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str(  final_total) +str('\n'))
    file.write( 'Total Fractional Change (km2):' + str( final_total - init_total) +str('\n'))
    file.write( 'Percent difference: ' + str( ((final_total - init_total)/init_total)*100.) +str('\n'))
    file.write( ' \n'    )
    file.write( '----------------------------------- \n')
    file.write( ' Low Center Polygons, Wetland Tundra Young age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_LCP_WT_Y ) + str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_LCP_WT_Y) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_LCP_WT_Y - self.Init_LCP_WT_Y) + str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_LCP_WT_Y - self.Init_LCP_WT_Y)/self.Init_LCP_WT_Y)*100.) + str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.LCP_WT_Y['POI_Function']) + str('\n'))
    if self.LCP_WT_Y['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.LCP_WT_Y['A1_above'])+\
                   ' | '+str(self.LCP_WT_Y['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.LCP_WT_Y['A2_above'])+\
                   ' | '+str(self.LCP_WT_Y['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.LCP_WT_Y['x0_above'])+\
                   ' | '+str(self.LCP_WT_Y['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.LCP_WT_Y['dx_above'])+\
                   ' | '+str(self.LCP_WT_Y['dx_below'])+str('\n \n'))
    elif self.LCP_WT_Y['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.LCP_WT_Y['a_above'])+\
                   str(' | ')+str(self.LCP_WT_Y['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.LCP_WT_Y['b_above']) +\
                   str(' | ')+str(self.LCP_WT_Y['b_below'])+str('\n \n'))
    elif self.LCP_WT_Y['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.LCP_WT_Y['K_above'])+ \
                   str(' | ')+str(self.LCP_WT_Y['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.LCP_WT_Y['C_above'])+ \
                   str(' | ')+str(self.LCP_WT_Y['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.LCP_WT_Y['A_above'])+ \
                   str(' | ')+str(self.LCP_WT_Y['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.LCP_WT_Y['B_above'])+ \
                   str(' | ')+str(self.LCP_WT_Y['B_below'])+str('\n \n'))
    elif self.LCP_WT_Y['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.LCP_WT_Y['HillB_above'])+ \
                   str(' | ')+str(self.LCP_WT_Y['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.LCP_WT_Y['HillN_above'])+ \
                   str(' | ')+str(self.LCP_WT_Y['HillN_below'])+str('\n \n'))

    file.write(' Maximum rate of terrain transition: '+str(self.LCP_WT_Y['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.LCP_WT_Y['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.LCP_WT_Y['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.LCP_WT_Y['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.LCP_WT_Y['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.LCP_WT_Y['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.LCP_WT_Y['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.LCP_WT_Y['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.LCP_WT_Y['Figures'].lower() == 'no' and self.LCP_WT_Y['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')


        
    file.write( '----------------------------------- \n')
    file.write( ' Low Center Polygons, Wetland Tundra Medium age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): ' +str( self.Init_LCP_WT_M) +str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_LCP_WT_M) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_LCP_WT_M - self.Init_LCP_WT_M)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_LCP_WT_M - self.Init_LCP_WT_M)/self.Init_LCP_WT_M)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.LCP_WT_M['POI_Function']) + str('\n'))
    if self.LCP_WT_M['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.LCP_WT_M['A1_above'])+\
                   ' | '+str(self.LCP_WT_M['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.LCP_WT_M['A2_above'])+\
                   ' | '+str(self.LCP_WT_M['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.LCP_WT_M['x0_above'])+\
                   ' | '+str(self.LCP_WT_M['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.LCP_WT_M['dx_above'])+\
                   ' | '+str(self.LCP_WT_M['dx_below'])+str('\n \n'))
    elif self.LCP_WT_M['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.LCP_WT_M['a_above'])+\
                   str(' | ')+str(self.LCP_WT_M['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.LCP_WT_M['b_above']) +\
                   str(' | ')+str(self.LCP_WT_M['b_below'])+str('\n \n'))
    elif self.LCP_WT_M['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.LCP_WT_M['K_above'])+ \
                   str(' | ')+str(self.LCP_WT_M['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.LCP_WT_M['C_above'])+ \
                   str(' | ')+str(self.LCP_WT_M['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.LCP_WT_M['A_above'])+ \
                   str(' | ')+str(self.LCP_WT_M['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.LCP_WT_M['B_above'])+ \
                   str(' | ')+str(self.LCP_WT_M['B_below'])+str('\n \n'))
    elif self.LCP_WT_M['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.LCP_WT_M['HillB_above'])+ \
                   str(' | ')+str(self.LCP_WT_M['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.LCP_WT_M['HillN_above'])+ \
                   str(' | ')+str(self.LCP_WT_M['HillN_below'])+str('\n \n'))

    file.write(' Maximum rate of terrain transition: '+str(self.LCP_WT_M['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.LCP_WT_M['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.LCP_WT_M['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.LCP_WT_M['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.LCP_WT_M['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.LCP_WT_M['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.LCP_WT_M['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.LCP_WT_M['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.LCP_WT_M['Figures'].lower() == 'no' and self.LCP_WT_M['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')

        
    file.write( '----------------------------------- \n')
    file.write( ' Low Center Polygons, Wetland Tundra Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_LCP_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_LCP_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_LCP_WT_O - self.Init_LCP_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_LCP_WT_O - self.Init_LCP_WT_O)/self.Init_LCP_WT_O)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.LCP_WT_O['POI_Function']) + str('\n'))
    if self.LCP_WT_O['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.LCP_WT_O['A1_above'])+\
                   ' | '+str(self.LCP_WT_O['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.LCP_WT_O['A2_above'])+\
                   ' | '+str(self.LCP_WT_O['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.LCP_WT_O['x0_above'])+\
                   ' | '+str(self.LCP_WT_O['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.LCP_WT_O['dx_above'])+\
                   ' | '+str(self.LCP_WT_O['dx_below'])+str('\n \n'))
    elif self.LCP_WT_O['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.LCP_WT_O['a_above'])+\
                   str(' | ')+str(self.LCP_WT_O['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.LCP_WT_O['b_above']) +\
                   str(' | ')+str(self.LCP_WT_O['b_below'])+str('\n \n'))
    elif self.LCP_WT_O['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.LCP_WT_O['K_above'])+ \
                   str(' | ')+str(self.LCP_WT_O['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.LCP_WT_O['C_above'])+ \
                   str(' | ')+str(self.LCP_WT_O['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.LCP_WT_O['A_above'])+ \
                   str(' | ')+str(self.LCP_WT_O['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.LCP_WT_O['B_above'])+ \
                   str(' | ')+str(self.LCP_WT_O['B_below'])+str('\n \n'))
    elif self.LCP_WT_O['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.LCP_WT_O['HillB_above'])+ \
                   str(' | ')+str(self.LCP_WT_O['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.LCP_WT_O['HillN_above'])+ \
                   str(' | ')+str(self.LCP_WT_O['HillN_below'])+str('\n \n'))


    file.write(' Maximum rate of terrain transition: '+str(self.LCP_WT_O['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.LCP_WT_O['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.LCP_WT_O['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.LCP_WT_O['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.LCP_WT_O['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.LCP_WT_O['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.LCP_WT_O['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.LCP_WT_O['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.LCP_WT_O['Figures'].lower() == 'no' and self.LCP_WT_O['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')
        
    file.write( '=============================================================\n')
    file.write( '       Wetland Tundra, Coalescent Low Center Polgyons \n')
    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' Coalescent Low Center Polygons, Wetland Tundra, All ages \n')
    file.write( '----------------------------------- \n')
    init_total = self.Init_CLC_WT_Y + self.Init_CLC_WT_M + self.Init_CLC_WT_O
    final_total = self.Final_CLC_WT_Y + self.Final_CLC_WT_M + self.Final_CLC_WT_O
    file.write( 'Initial Fractional Area (km2): ' +str( init_total )+str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str(  final_total) +str('\n'))
    file.write( 'Total Fractional Change (km2):' + str( final_total - init_total) +str('\n'))
    file.write( 'Percent difference: ' + str( ((final_total - init_total)/init_total)*100.) +str('\n'))
    file.write( ' \n'    )
    file.write( '----------------------------------- \n')
    file.write( ' Coalescent Low Center Polygons, Wetland Tundra Young age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_CLC_WT_Y ) + str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_CLC_WT_Y) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_CLC_WT_Y - self.Init_CLC_WT_Y) + str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_CLC_WT_Y - self.Init_CLC_WT_Y)/self.Init_CLC_WT_Y)*100.) + str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.CLC_WT_Y['POI_Function']) + str('\n'))
    if self.CLC_WT_Y['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.CLC_WT_Y['A1_above'])+\
                   ' | '+str(self.CLC_WT_Y['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.CLC_WT_Y['A2_above'])+\
                   ' | '+str(self.CLC_WT_Y['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.CLC_WT_Y['x0_above'])+\
                   ' | '+str(self.CLC_WT_Y['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.CLC_WT_Y['dx_above'])+\
                   ' | '+str(self.CLC_WT_Y['dx_below'])+str('\n \n'))
    elif self.CLC_WT_Y['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.CLC_WT_Y['a_above'])+\
                   str(' | ')+str(self.CLC_WT_Y['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.CLC_WT_Y['b_above']) +\
                   str(' | ')+str(self.CLC_WT_Y['b_below'])+str('\n \n'))
    elif self.CLC_WT_Y['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.CLC_WT_Y['K_above'])+ \
                   str(' | ')+str(self.CLC_WT_Y['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.CLC_WT_Y['C_above'])+ \
                   str(' | ')+str(self.CLC_WT_Y['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.CLC_WT_Y['A_above'])+ \
                   str(' | ')+str(self.CLC_WT_Y['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.CLC_WT_Y['B_above'])+ \
                   str(' | ')+str(self.CLC_WT_Y['B_below'])+str('\n \n'))
    elif self.CLC_WT_Y['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.CLC_WT_Y['HillB_above'])+ \
                   str(' | ')+str(self.CLC_WT_Y['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.CLC_WT_Y['HillN_above'])+ \
                   str(' | ')+str(self.CLC_WT_Y['HillN_below'])+str('\n \n'))

    file.write(' Maximum rate of terrain transition: '+str(self.CLC_WT_Y['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.CLC_WT_Y['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.CLC_WT_Y['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.CLC_WT_Y['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.CLC_WT_Y['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.CLC_WT_Y['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.CLC_WT_Y['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.CLC_WT_Y['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.CLC_WT_Y['Figures'].lower() == 'no' and self.CLC_WT_Y['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')
        
    file.write( '----------------------------------- \n')
    file.write( ' Coalescent Low Center Polygons, Wetland Tundra Medium age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): ' +str( self.Init_CLC_WT_M) +str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_CLC_WT_M) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_CLC_WT_M - self.Init_CLC_WT_M)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_CLC_WT_M - self.Init_CLC_WT_M)/self.Init_CLC_WT_M)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.CLC_WT_M['POI_Function']) + str('\n'))
    if self.CLC_WT_M['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.CLC_WT_M['A1_above'])+\
                   ' | '+str(self.CLC_WT_M['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.CLC_WT_M['A2_above'])+\
                   ' | '+str(self.CLC_WT_M['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.CLC_WT_M['x0_above'])+\
                   ' | '+str(self.CLC_WT_M['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.CLC_WT_M['dx_above'])+\
                   ' | '+str(self.CLC_WT_M['dx_below'])+str('\n \n'))
    elif self.CLC_WT_M['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.CLC_WT_M['a_above'])+\
                   str(' | ')+str(self.CLC_WT_M['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.CLC_WT_M['b_above']) +\
                   str(' | ')+str(self.CLC_WT_M['b_below'])+str('\n \n'))
    elif self.CLC_WT_M['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.CLC_WT_M['K_above'])+ \
                   str(' | ')+str(self.CLC_WT_M['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.CLC_WT_M['C_above'])+ \
                   str(' | ')+str(self.CLC_WT_M['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.CLC_WT_M['A_above'])+ \
                   str(' | ')+str(self.CLC_WT_M['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.CLC_WT_M['B_above'])+ \
                   str(' | ')+str(self.CLC_WT_M['B_below'])+str('\n \n'))
    elif self.CLC_WT_M['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.CLC_WT_M['HillB_above'])+ \
                   str(' | ')+str(self.CLC_WT_M['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.CLC_WT_M['HillN_above'])+ \
                   str(' | ')+str(self.CLC_WT_M['HillN_below'])+str('\n \n'))
                   
    file.write(' Maximum rate of terrain transition: '+str(self.CLC_WT_M['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.CLC_WT_M['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.CLC_WT_M['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.CLC_WT_M['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.CLC_WT_M['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.CLC_WT_M['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.CLC_WT_M['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.CLC_WT_M['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.CLC_WT_M['Figures'].lower() == 'no' and self.CLC_WT_M['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')
        
    file.write( '----------------------------------- \n')
    file.write( ' Coalescent Low Center Polygons, Wetland Tundra Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_CLC_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_CLC_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_CLC_WT_O - self.Init_CLC_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_CLC_WT_O - self.Init_CLC_WT_O)/self.Init_CLC_WT_O)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.CLC_WT_O['POI_Function']) + str('\n'))
    if self.CLC_WT_O['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.CLC_WT_O['A1_above'])+\
                   ' | '+str(self.CLC_WT_O['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.CLC_WT_O['A2_above'])+\
                   ' | '+str(self.CLC_WT_O['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.CLC_WT_O['x0_above'])+\
                   ' | '+str(self.CLC_WT_O['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.CLC_WT_O['dx_above'])+\
                   ' | '+str(self.CLC_WT_O['dx_below'])+str('\n \n'))
    elif self.CLC_WT_O['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.CLC_WT_O['a_above'])+\
                   str(' | ')+str(self.CLC_WT_O['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.CLC_WT_O['b_above']) +\
                   str(' | ')+str(self.CLC_WT_O['b_below'])+str('\n \n'))
    elif self.CLC_WT_O['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.CLC_WT_O['K_above'])+ \
                   str(' | ')+str(self.CLC_WT_O['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.CLC_WT_O['C_above'])+ \
                   str(' | ')+str(self.CLC_WT_O['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.CLC_WT_O['A_above'])+ \
                   str(' | ')+str(self.CLC_WT_O['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.CLC_WT_O['B_above'])+ \
                   str(' | ')+str(self.CLC_WT_O['B_below'])+str('\n \n'))
    elif self.CLC_WT_O['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.CLC_WT_O['HillB_above'])+ \
                   str(' | ')+str(self.CLC_WT_O['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.CLC_WT_O['HillN_above'])+ \
                   str(' | ')+str(self.CLC_WT_O['HillN_below'])+str('\n \n'))

                   
    file.write(' Maximum rate of terrain transition: '+str(self.CLC_WT_O['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.CLC_WT_O['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.CLC_WT_O['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.CLC_WT_O['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.CLC_WT_O['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.CLC_WT_O['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.CLC_WT_O['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.CLC_WT_O['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.CLC_WT_O['Figures'].lower() == 'no' and self.CLC_WT_O['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')
        

    file.write( '=============================================================\n')
    file.write( '       Wetland Tundra, Flat Center Polgyons \n')
    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' Flat Center Polygons, Wetland Tundra, All ages \n')
    file.write( '----------------------------------- \n')
    init_total = self.Init_FCP_WT_Y + self.Init_FCP_WT_M + self.Init_FCP_WT_O
    final_total = self.Final_FCP_WT_Y + self.Final_FCP_WT_M + self.Final_FCP_WT_O
    file.write( 'Initial Fractional Area (km2): ' +str( init_total )+str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str(  final_total) +str('\n'))
    file.write( 'Total Fractional Change (km2):' + str( final_total - init_total) +str('\n'))
    file.write( 'Percent difference: ' + str( ((final_total - init_total)/init_total)*100.) +str('\n'))
    file.write( ' \n'    )
    file.write( '----------------------------------- \n')
    file.write( ' Flat Center Polygons, Wetland Tundra Young age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_FCP_WT_Y ) + str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_FCP_WT_Y) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_FCP_WT_Y - self.Init_FCP_WT_Y) + str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_FCP_WT_Y - self.Init_FCP_WT_Y)/self.Init_FCP_WT_Y)*100.) + str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.FCP_WT_Y['POI_Function']) + str('\n'))
    if self.FCP_WT_Y['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.FCP_WT_Y['A1_above'])+\
                   ' | '+str(self.FCP_WT_Y['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.FCP_WT_Y['A2_above'])+\
                   ' | '+str(self.FCP_WT_Y['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.FCP_WT_Y['x0_above'])+\
                   ' | '+str(self.FCP_WT_Y['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.FCP_WT_Y['dx_above'])+\
                   ' | '+str(self.FCP_WT_Y['dx_below'])+str('\n \n'))
    elif self.FCP_WT_Y['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.FCP_WT_Y['a_above'])+\
                   str(' | ')+str(self.FCP_WT_Y['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.FCP_WT_Y['b_above']) +\
                   str(' | ')+str(self.FCP_WT_Y['b_below'])+str('\n \n'))
    elif self.FCP_WT_Y['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.FCP_WT_Y['K_above'])+ \
                   str(' | ')+str(self.FCP_WT_Y['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.FCP_WT_Y['C_above'])+ \
                   str(' | ')+str(self.FCP_WT_Y['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.FCP_WT_Y['A_above'])+ \
                   str(' | ')+str(self.FCP_WT_Y['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.FCP_WT_Y['B_above'])+ \
                   str(' | ')+str(self.FCP_WT_Y['B_below'])+str('\n \n'))
    elif self.FCP_WT_Y['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.FCP_WT_Y['HillB_above'])+ \
                   str(' | ')+str(self.FCP_WT_Y['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.FCP_WT_Y['HillN_above'])+ \
                   str(' | ')+str(self.FCP_WT_Y['HillN_below'])+str('\n \n'))

                   
    file.write(' Maximum rate of terrain transition: '+str(self.FCP_WT_Y['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.FCP_WT_Y['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.FCP_WT_Y['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.FCP_WT_Y['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.FCP_WT_Y['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.FCP_WT_Y['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.FCP_WT_Y['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.FCP_WT_Y['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.FCP_WT_Y['Figures'].lower() == 'no' and self.FCP_WT_Y['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')
        



    file.write( '----------------------------------- \n')
    file.write( ' Flat Center Polygons, Wetland Tundra Medium age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): ' +str( self.Init_FCP_WT_M) +str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_FCP_WT_M) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_FCP_WT_M - self.Init_FCP_WT_M)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_FCP_WT_M - self.Init_FCP_WT_M)/self.Init_FCP_WT_M)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.FCP_WT_M['POI_Function']) + str('\n'))
    if self.FCP_WT_M['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.FCP_WT_M['A1_above'])+\
                   ' | '+str(self.FCP_WT_M['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.FCP_WT_M['A2_above'])+\
                   ' | '+str(self.FCP_WT_M['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.FCP_WT_M['x0_above'])+\
                   ' | '+str(self.FCP_WT_M['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.FCP_WT_M['dx_above'])+\
                   ' | '+str(self.FCP_WT_M['dx_below'])+str('\n \n'))
    elif self.FCP_WT_M['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.FCP_WT_M['a_above'])+\
                   str(' | ')+str(self.FCP_WT_M['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.FCP_WT_M['b_above']) +\
                   str(' | ')+str(self.FCP_WT_M['b_below'])+str('\n \n'))
    elif self.FCP_WT_M['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.FCP_WT_M['K_above'])+ \
                   str(' | ')+str(self.FCP_WT_M['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.FCP_WT_M['C_above'])+ \
                   str(' | ')+str(self.FCP_WT_M['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.FCP_WT_M['A_above'])+ \
                   str(' | ')+str(self.FCP_WT_M['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.FCP_WT_M['B_above'])+ \
                   str(' | ')+str(self.FCP_WT_M['B_below'])+str('\n \n'))
    elif self.FCP_WT_M['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.FCP_WT_M['HillB_above'])+ \
                   str(' | ')+str(self.FCP_WT_M['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.FCP_WT_M['HillN_above'])+ \
                   str(' | ')+str(self.FCP_WT_M['HillN_below'])+str('\n \n'))

    file.write(' Maximum rate of terrain transition: '+str(self.FCP_WT_M['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.FCP_WT_M['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.FCP_WT_M['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.FCP_WT_M['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.FCP_WT_M['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.FCP_WT_M['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.FCP_WT_M['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.FCP_WT_M['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.FCP_WT_M['Figures'].lower() == 'no' and self.FCP_WT_M['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')
        
    file.write( '----------------------------------- \n')
    file.write( ' Flat Center Polygons, Wetland Tundra Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_FCP_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_FCP_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_FCP_WT_O - self.Init_FCP_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_FCP_WT_O - self.Init_FCP_WT_O)/self.Init_FCP_WT_O)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.FCP_WT_O['POI_Function']) + str('\n'))
    if self.FCP_WT_O['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.FCP_WT_O['A1_above'])+\
                   ' | '+str(self.FCP_WT_O['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.FCP_WT_O['A2_above'])+\
                   ' | '+str(self.FCP_WT_O['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.FCP_WT_O['x0_above'])+\
                   ' | '+str(self.FCP_WT_O['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.FCP_WT_O['dx_above'])+\
                   ' | '+str(self.FCP_WT_O['dx_below'])+str('\n \n'))
    elif self.FCP_WT_O['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.FCP_WT_O['a_above'])+\
                   str(' | ')+str(self.FCP_WT_O['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.FCP_WT_O['b_above']) +\
                   str(' | ')+str(self.FCP_WT_O['b_below'])+str('\n \n'))
    elif self.FCP_WT_O['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.FCP_WT_O['K_above'])+ \
                   str(' | ')+str(self.FCP_WT_O['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.FCP_WT_O['C_above'])+ \
                   str(' | ')+str(self.FCP_WT_O['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.FCP_WT_O['A_above'])+ \
                   str(' | ')+str(self.FCP_WT_O['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.FCP_WT_O['B_above'])+ \
                   str(' | ')+str(self.FCP_WT_O['B_below'])+str('\n \n'))
    elif self.FCP_WT_O['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.FCP_WT_O['HillB_above'])+ \
                   str(' | ')+str(self.FCP_WT_O['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.FCP_WT_O['HillN_above'])+ \
                   str(' | ')+str(self.FCP_WT_O['HillN_below'])+str('\n \n'))

    file.write(' Maximum rate of terrain transition: '+str(self.FCP_WT_O['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.FCP_WT_O['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.FCP_WT_O['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.FCP_WT_O['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.FCP_WT_O['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.FCP_WT_O['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.FCP_WT_O['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.FCP_WT_O['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.FCP_WT_O['Figures'].lower() == 'no' and self.FCP_WT_O['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')
        
    file.write( '=============================================================\n')
    file.write( '       Wetland Tundra, High Center Polgyons \n')
    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' High Center Polygons, Wetland Tundra, All ages \n')
    file.write( '----------------------------------- \n')
    init_total = self.Init_HCP_WT_Y + self.Init_HCP_WT_M + self.Init_HCP_WT_O
    final_total = self.Final_HCP_WT_Y + self.Final_HCP_WT_M + self.Final_HCP_WT_O
    file.write( 'Initial Fractional Area (km2): ' +str( init_total )+str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str(  final_total) +str('\n'))
    file.write( 'Total Fractional Change (km2):' + str( final_total - init_total) +str('\n'))
    file.write( 'Percent difference: ' + str( ((final_total - init_total)/init_total)*100.) +str('\n'))
    file.write( ' \n'    )
    file.write( '----------------------------------- \n')
    file.write( ' High Center Polygons, Wetland Tundra Young age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_HCP_WT_Y ) + str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_HCP_WT_Y) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_HCP_WT_Y - self.Init_HCP_WT_Y) + str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_HCP_WT_Y - self.Init_HCP_WT_Y)/self.Init_HCP_WT_Y)*100.) + str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.HCP_WT_Y['POI_Function']) + str('\n'))
    if self.HCP_WT_Y['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.HCP_WT_Y['A1_above'])+\
                   ' | '+str(self.HCP_WT_Y['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.HCP_WT_Y['A2_above'])+\
                   ' | '+str(self.HCP_WT_Y['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.HCP_WT_Y['x0_above'])+\
                   ' | '+str(self.HCP_WT_Y['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.HCP_WT_Y['dx_above'])+\
                   ' | '+str(self.HCP_WT_Y['dx_below'])+str('\n \n'))
    elif self.HCP_WT_Y['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.HCP_WT_Y['a_above'])+\
                   str(' | ')+str(self.HCP_WT_Y['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.HCP_WT_Y['b_above']) +\
                   str(' | ')+str(self.HCP_WT_Y['b_below'])+str('\n \n'))
    elif self.HCP_WT_Y['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.HCP_WT_Y['K_above'])+ \
                   str(' | ')+str(self.HCP_WT_Y['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.HCP_WT_Y['C_above'])+ \
                   str(' | ')+str(self.HCP_WT_Y['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.HCP_WT_Y['A_above'])+ \
                   str(' | ')+str(self.HCP_WT_Y['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.HCP_WT_Y['B_above'])+ \
                   str(' | ')+str(self.HCP_WT_Y['B_below'])+str('\n \n'))
    elif self.HCP_WT_Y['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.HCP_WT_Y['HillB_above'])+ \
                   str(' | ')+str(self.HCP_WT_Y['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.HCP_WT_Y['HillN_above'])+ \
                   str(' | ')+str(self.HCP_WT_Y['HillN_below'])+str('\n \n'))

    file.write(' Maximum rate of terrain transition: '+str(self.HCP_WT_Y['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.HCP_WT_Y['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.HCP_WT_Y['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.HCP_WT_Y['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.HCP_WT_Y['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.HCP_WT_Y['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.HCP_WT_Y['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.HCP_WT_Y['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.HCP_WT_Y['Figures'].lower() == 'no' and self.HCP_WT_Y['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')


    file.write( '----------------------------------- \n')
    file.write( ' High Center Polygons, Wetland Tundra Medium age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): ' +str( self.Init_HCP_WT_M) +str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_HCP_WT_M) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_HCP_WT_M - self.Init_HCP_WT_M)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_HCP_WT_M - self.Init_HCP_WT_M)/self.Init_HCP_WT_M)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.HCP_WT_M['POI_Function']) + str('\n'))
    if self.HCP_WT_M['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.HCP_WT_M['A1_above'])+\
                   ' | '+str(self.HCP_WT_M['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.HCP_WT_M['A2_above'])+\
                   ' | '+str(self.HCP_WT_M['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.HCP_WT_M['x0_above'])+\
                   ' | '+str(self.HCP_WT_M['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.HCP_WT_M['dx_above'])+\
                   ' | '+str(self.HCP_WT_M['dx_below'])+str('\n \n'))
    elif self.HCP_WT_M['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.HCP_WT_M['a_above'])+\
                   str(' | ')+str(self.HCP_WT_M['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.HCP_WT_M['b_above']) +\
                   str(' | ')+str(self.HCP_WT_M['b_below'])+str('\n \n'))
    elif self.HCP_WT_M['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.HCP_WT_M['K_above'])+ \
                   str(' | ')+str(self.HCP_WT_M['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.HCP_WT_M['C_above'])+ \
                   str(' | ')+str(self.HCP_WT_M['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.HCP_WT_M['A_above'])+ \
                   str(' | ')+str(self.HCP_WT_M['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.HCP_WT_M['B_above'])+ \
                   str(' | ')+str(self.HCP_WT_M['B_below'])+str('\n \n'))
    elif self.HCP_WT_M['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.HCP_WT_M['HillB_above'])+ \
                   str(' | ')+str(self.HCP_WT_M['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.HCP_WT_M['HillN_above'])+ \
                   str(' | ')+str(self.HCP_WT_M['HillN_below'])+str('\n \n'))


    file.write(' Maximum rate of terrain transition: '+str(self.HCP_WT_M['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.HCP_WT_M['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.HCP_WT_M['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.HCP_WT_M['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.HCP_WT_M['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.HCP_WT_M['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.HCP_WT_M['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.HCP_WT_M['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.HCP_WT_M['Figures'].lower() == 'no' and self.HCP_WT_M['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')


    
    file.write( '----------------------------------- \n')
    file.write( ' High Center Polygons, Wetland Tundra Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_HCP_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_HCP_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_HCP_WT_O - self.Init_HCP_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_HCP_WT_O - self.Init_HCP_WT_O)/self.Init_HCP_WT_O)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.HCP_WT_O['POI_Function']) + str('\n'))
    if self.HCP_WT_O['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.HCP_WT_O['A1_above'])+\
                   ' | '+str(self.HCP_WT_O['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.HCP_WT_O['A2_above'])+\
                   ' | '+str(self.HCP_WT_O['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.HCP_WT_O['x0_above'])+\
                   ' | '+str(self.HCP_WT_O['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.HCP_WT_O['dx_above'])+\
                   ' | '+str(self.HCP_WT_O['dx_below'])+str('\n \n'))
    elif self.HCP_WT_O['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.HCP_WT_O['a_above'])+\
                   str(' | ')+str(self.HCP_WT_O['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.HCP_WT_O['b_above']) +\
                   str(' | ')+str(self.HCP_WT_O['b_below'])+str('\n \n'))
    elif self.HCP_WT_O['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.HCP_WT_O['K_above'])+ \
                   str(' | ')+str(self.HCP_WT_O['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.HCP_WT_O['C_above'])+ \
                   str(' | ')+str(self.HCP_WT_O['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.HCP_WT_O['A_above'])+ \
                   str(' | ')+str(self.HCP_WT_O['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.HCP_WT_O['B_above'])+ \
                   str(' | ')+str(self.HCP_WT_O['B_below'])+str('\n \n'))
    elif self.HCP_WT_O['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.HCP_WT_O['HillB_above'])+ \
                   str(' | ')+str(self.HCP_WT_O['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.HCP_WT_O['HillN_above'])+ \
                   str(' | ')+str(self.HCP_WT_O['HillN_below'])+str('\n \n'))

    file.write(' Maximum rate of terrain transition: '+str(self.HCP_WT_O['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.HCP_WT_O['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.HCP_WT_O['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.HCP_WT_O['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.HCP_WT_O['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.HCP_WT_O['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.HCP_WT_O['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.HCP_WT_O['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.HCP_WT_O['Figures'].lower() == 'no' and self.HCP_WT_O['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')

    #-------------------------------------------------------------------------------------------
    file.write( '===========================================================\n' )
    file.write( '       Lake and Pond Ice Information  \n')
    file.write( '===========================================================\n')
    if self.LakePond['ice_thickness_distribution'].lower() == 'random':
        file.write('Ice thickness alpha value is RANDOM. \n')
        file.write('  Lower | Upper bounds of alpha values are: ' +\
                   str(self.LakePond['Lower_ice_thickness_alpha']) +str(' | ') +\
                   str(self.LakePond['Upper_ice_thickness_alpha']) +str(' \n \n'))
    elif self.LakePond['ice_thickness_distribution'].lower() == 'uniform':
        file.write('Ice thickness alpha value is UNIFORM. \n')
        file.write('  The alpha value is: '+str(self.LakePond['ice_thickness_uniform_alpha']) +\
                   str(' \n \n'))

    file.write( '=============================================================\n')
    file.write( '       Wetland Tundra, Lakes \n')
    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' Lakes, Wetland Tundra, Small, Medium, Large, All ages \n')
    file.write( '----------------------------------- \n')
    init_total = self.Init_LargeLakes_WT_Y + self.Init_LargeLakes_WT_M + self.Init_LargeLakes_WT_O + \
                 self.Init_MediumLakes_WT_Y + self.Init_MediumLakes_WT_M + self.Init_MediumLakes_WT_O + \
                 self.Init_SmallLakes_WT_Y + self.Init_SmallLakes_WT_M + self.Init_SmallLakes_WT_O
    final_total = self.Final_LargeLakes_WT_Y + self.Final_LargeLakes_WT_M + self.Final_LargeLakes_WT_O + \
                  self.Final_MediumLakes_WT_Y + self.Final_MediumLakes_WT_M + self.Final_MediumLakes_WT_O + \
                  self.Final_SmallLakes_WT_Y + self.Final_SmallLakes_WT_M + self.Final_SmallLakes_WT_O
    file.write( 'Initial Fractional Area (km2): ' +str( init_total )+str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str(  final_total) +str('\n'))
    file.write( 'Total Fractional Change (km2):' + str( final_total - init_total) +str('\n'))
    file.write( 'Percent difference: ' + str( ((final_total - init_total)/init_total)*100.) +str('\n'))
    file.write( '\n'  )
    file.write( '----------------------------------- \n')
    file.write( ' Large Lakes, Wetland Tundra Young age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_LargeLakes_WT_Y ) + str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_LargeLakes_WT_Y) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_LargeLakes_WT_Y - self.Init_LargeLakes_WT_Y) + str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_LargeLakes_WT_Y - self.Init_LargeLakes_WT_Y)/\
                                                 self.Init_LargeLakes_WT_Y)*100.) + str('\n'))
    file.write( ' \n')
    file.write( 'Large Lake, Wetland Tundra, Young age expansion constant is set to: ' \
                +str(self.LakePond['LargeLake_WT_Y_Expansion'])+str('\n\n'))
    #--------------------------------------------------------------------------------------------
    if self.LakePond['Lake_Distribution'].lower() == 'random':
        file.write('Large Lake, Wetland Tundra, Young age lake depth distribution is RANDOM.\n')
        file.write('   Lower | Upper bounds of the random function are: ' \
                   +str(self.LakePond['Lower_LargeLake_WT_Y_Depth']) + str(' | ') + \
                   str(self.LakePond['Upper_LargeLake_WT_Y_Depth']))
    elif self.LakePond['Lake_Distribution'].lower() == 'uniform':
        file.write('Large Lake, Wetland Tundra, Young age lake depth distribution is UNIFORM. \n')
        file.write('   The initial lake depth is : ' + str(self.LakePond['Uniform_Lake_Depth'])+str('\n \n'))
    #-------------------------------------------------------------------------------------------
    if self.LakePond['ice_thickness_distribution'].lower() == 'random':
        file.write('Ice thickness alpha value is RANDOM. \n')
        file.write('  Lower | Upper bounds of alpha values are: ' +\
                   str(self.LakePond['Lower_ice_thickness_alpha']) +str(' | ') +\
                   str(self.LakePond['Upper_ice_thickness_alpha']) +str(' \n \n'))
    elif self.LakePond['ice_thickness_distribution'].lower() == 'uniform':
        file.write('Ice thickness alpha value is UNIFORM. \n')
        file.write('  The alpha value is: '+str(self.LakePond['ice_thickness_uniform_alpha']) +\
                   str(' \n \n'))
    #---------------------------------------------------------------------------------------------

                
    file.write( ' \n \n')
    file.write( '----------------------------------- \n')
    file.write( ' Large Lakes, Wetland Tundra Medium age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): ' +str( self.Init_LargeLakes_WT_M) +str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_LargeLakes_WT_M) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_LargeLakes_WT_M - self.Init_LargeLakes_WT_M)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_LargeLakes_WT_M - self.Init_LargeLakes_WT_M)/\
                                                 self.Init_LargeLakes_WT_M)*100.)+str('\n'))
    file.write( ' \n')
    file.write( '----------------------------------- \n')
    file.write( ' Large Lakes, Wetland Tundra Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_LargeLakes_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_LargeLakes_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_LargeLakes_WT_O - self.Init_LargeLakes_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_LargeLakes_WT_O - self.Init_LargeLakes_WT_O)/\
                                                 self.Init_LargeLakes_WT_O)*100.)+str('\n'))
    file.write( ' \n')
    file.write( '----------------------------------- \n')
    file.write( ' Medium Lakes, Wetland Tundra Young age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_MediumLakes_WT_Y ) + str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_MediumLakes_WT_Y) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_MediumLakes_WT_Y - self.Init_MediumLakes_WT_Y) + str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_MediumLakes_WT_Y - self.Init_MediumLakes_WT_Y)/\
                                                 self.Init_MediumLakes_WT_Y)*100.) + str('\n'))
    file.write( ' \n')
    file.write( '----------------------------------- \n')
    file.write( ' Medium Lakes, Wetland Tundra Medium age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): ' +str( self.Init_MediumLakes_WT_M) +str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_MediumLakes_WT_M) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_MediumLakes_WT_M - self.Init_MediumLakes_WT_M)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_MediumLakes_WT_M - self.Init_MediumLakes_WT_M)/\
                                                 self.Init_MediumLakes_WT_M)*100.)+str('\n'))
    file.write( ' \n')
    file.write( '----------------------------------- \n')
    file.write( ' Small Lakes, Wetland Tundra Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_SmallLakes_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_SmallLakes_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_SmallLakes_WT_O - self.Init_SmallLakes_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_SmallLakes_WT_O - self.Init_SmallLakes_WT_O)/\
                                                 self.Init_SmallLakes_WT_O)*100.)+str('\n'))
    file.write( ' \n')    
    file.write( '----------------------------------- \n')
    file.write( ' Small Lakes, Wetland Tundra Young age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_SmallLakes_WT_Y ) + str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_SmallLakes_WT_Y) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_SmallLakes_WT_Y - self.Init_SmallLakes_WT_Y) + str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_SmallLakes_WT_Y - self.Init_SmallLakes_WT_Y)/\
                                                 self.Init_SmallLakes_WT_Y)*100.) + str('\n'))
    file.write( ' \n')
    file.write( '----------------------------------- \n')
    file.write( ' Small Lakes, Wetland Tundra Medium age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): ' +str( self.Init_SmallLakes_WT_M) +str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_SmallLakes_WT_M) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_SmallLakes_WT_M - self.Init_SmallLakes_WT_M)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_SmallLakes_WT_M - self.Init_SmallLakes_WT_M)/\
                                                 self.Init_SmallLakes_WT_M)*100.)+str('\n'))
    file.write( ' \n')
    file.write( '----------------------------------- \n')
    file.write( ' Small Lakes, Wetland Tundra Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_SmallLakes_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_SmallLakes_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_SmallLakes_WT_O - self.Init_SmallLakes_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_SmallLakes_WT_O - self.Init_SmallLakes_WT_O)/\
                                                 self.Init_SmallLakes_WT_O)*100.)+str('\n'))
    file.write( ' \n')

    file.write( '=============================================================\n')
    file.write( '       Wetland Tundra, Ponds \n')
    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' Ponds, Wetland Tundra, All ages \n')
    file.write( '----------------------------------- \n')
    init_total = self.Init_Ponds_WT_Y + self.Init_Ponds_WT_M + self.Init_Ponds_WT_O
    final_total = self.Final_Ponds_WT_Y + self.Final_Ponds_WT_M + self.Final_Ponds_WT_O
    file.write( 'Initial Fractional Area (km2): ' +str( init_total )+str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str(  final_total) +str('\n'))
    file.write( 'Total Fractional Change (km2):' + str( final_total - init_total) +str('\n'))
    file.write( 'Percent difference: ' + str( ((final_total - init_total)/init_total)*100.) +str('\n'))
    file.write( ' \n'    )
    file.write( '----------------------------------- \n')
    file.write( ' Ponds, Wetland Tundra Young age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Ponds_WT_Y ) + str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_Ponds_WT_Y) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_Ponds_WT_Y - self.Init_Ponds_WT_Y) + str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_Ponds_WT_Y - self.Init_Ponds_WT_Y)/\
                                                 self.Init_Ponds_WT_Y)*100.) + str('\n'))
    if self.LakePond['Pond_Distribution'].lower() == 'random':
        file.write(' Pond Depth Distribution is RANDOM function. \n')
        file.write('  Lower | Upper bounds of the random functions are: '+\
                       str(self.LakePond['Lower_Pond_WT_Y_Depth']) + str(' | ') + \
                       str(self.LakePond['Upper_Pond_WT_Y_Depth']) + str('\n'))
    else:
        file.write(' Pond Depth Distribution is initialized as UNIFORM. \n')
        file.write('  The initial pond depth (wetland tundra, young age) is: '+\
                       str(self.LakePond['Uniform_Pond_Depth'])+str('\n'))
    file.write(' The Pond (Wetland Tundra, Young age) expansion constant is: ' +\
                   str(self.LakePond['Pond_WT_Y_Expansion']) + str('\n'))
    file.write(' The Pond (Wetland Tundra, Young age) infilling constant is: ' +\
                   str(self.LakePond['Pond_WT_Y_Infill_Constant']) + str('\n'))
    file.write(' The Pond (Wetland Tundra, Young age) depth control constant is: ' +\
                   str(self.LakePond['Pond_WT_Y_depth_control']) + str('\n'))
    file.write(' Number of consecutive years of pond growth (depth) before lake transition is allowed: '\
                   +str(self.LakePond['Pond_WT_Y_growth_time_required']))
    file.write('Output Results: \n')
    if self.LakePond['Pond_WT_Y_Depth_Figure'].lower() == 'yes':
        file.write('  Initial pond depth (wetland tundra, young age) output as figure. \n')
    
    if self.LakePond['Pond_WT_Y_Figures'].lower() == 'yes':
        file.write('  Yearly Figures output. \n')
    if self.LakePond['Pond_WT_Y_Movie'].lower() == 'yes':
        file.write('  Animation output. \n')
    file.write( ' \n')

    file.write( '----------------------------------- \n')
    file.write( ' Ponds, Wetland Tundra Medium age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): ' +str( self.Init_Ponds_WT_M) +str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_Ponds_WT_M) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_Ponds_WT_M - self.Init_Ponds_WT_M)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_Ponds_WT_M - self.Init_Ponds_WT_M)/\
                                                 self.Init_Ponds_WT_M)*100.)+str('\n'))
    if self.LakePond['Pond_Distribution'].lower() == 'random':
        file.write(' Pond Depth Distribution is RANDOM function. \n')
        file.write('  Lower | Upper bounds of the random functions are: '+\
                       str(self.LakePond['Lower_Pond_WT_M_Depth']) + str(' | ') + \
                       str(self.LakePond['Upper_Pond_WT_M_Depth']) + str('\n'))
    else:
        file.write(' Pond Depth Distribution is initialized as UNIFORM. \n')
        file.write('  The initial pond depth (wetland tundra, medium age) is: '+\
                       str(self.LakePond['Uniform_Pond_Depth'])+str('\n'))
    file.write(' The Pond (Wetland Tundra, Medium age) expansion constant is: ' +\
                   str(self.LakePond['Pond_WT_M_Expansion']) + str('\n'))
    file.write(' The Pond (Wetland Tundra, Medium age) infilling constant is: ' +\
                   str(self.LakePond['Pond_WT_M_Infill_Constant']) + str('\n'))
    file.write(' The Pond (Wetland Tundra, Medium age) depth control constant is: ' +\
                   str(self.LakePond['Pond_WT_M_depth_control']) + str('\n'))
    file.write(' Number of consecutive years of pond growth (depth) before lake transition is allowed: '\
                   +str(self.LakePond['Pond_WT_M_growth_time_required']))
    file.write('Output Results: \n')
    if self.LakePond['Pond_WT_M_Depth_Figure'].lower() == 'yes':
        file.write('  Initial pond depth (wetland tundra, medium age) output as figure. \n')
    
    if self.LakePond['Pond_WT_M_Figures'].lower() == 'yes':
        file.write('  Yearly Figures output. \n')
    if self.LakePond['Pond_WT_M_Movie'].lower() == 'yes':
        file.write('  Animation output. \n')    
    file.write( ' \n')
    file.write( '----------------------------------- \n')
    file.write( ' Ponds, Wetland Tundra Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Ponds_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_Ponds_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Ponds_WT_O - self.Init_Ponds_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_Ponds_WT_O - self.Init_Ponds_WT_O)/\
                                                 self.Init_Ponds_WT_O)*100.)+str('\n'))
    if self.LakePond['Pond_Distribution'].lower() == 'random':
        file.write(' Pond Depth Distribution is RANDOM function. \n')
        file.write('  Lower | Upper bounds of the random functions are: '+\
                       str(self.LakePond['Lower_Pond_WT_O_Depth']) + str(' | ') + \
                       str(self.LakePond['Upper_Pond_WT_O_Depth']) + str('\n'))
    else:
        file.write(' Pond Depth Distribution is initialized as UNIFORM. \n')
        file.write('  The initial pond depth (wetland tundra, old age) is: '+\
                       str(self.LakePond['Uniform_Pond_Depth'])+str('\n'))
    file.write(' The Pond (Wetland Tundra, Old age) expansion constant is: ' +\
                   str(self.LakePond['Pond_WT_O_Expansion']) + str('\n'))
    file.write(' The Pond (Wetland Tundra, Old age) infilling constant is: ' +\
                   str(self.LakePond['Pond_WT_O_Infill_Constant']) + str('\n'))
    file.write(' The Pond (Wetland Tundra, Old age) depth control constant is: ' +\
                   str(self.LakePond['Pond_WT_O_depth_control']) + str('\n'))
    file.write(' Number of consecutive years of pond growth (depth) before lake transition is allowed: '\
                   +str(self.LakePond['Pond_WT_O_growth_time_required']))
    file.write('Output Results: \n')
    if self.LakePond['Pond_WT_O_Depth_Figure'].lower() == 'yes':
        file.write('  Initial pond depth (wetland tundra, old age) output as figure. \n')
    
    if self.LakePond['Pond_WT_O_Figures'].lower() == 'yes':
        file.write('  Yearly Figures output. \n')
    if self.LakePond['Pond_WT_O_Movie'].lower() == 'yes':
        file.write('  Animation output. \n')   
    file.write( ' \n')
    file.write( '=============================================================\n')
    file.write( '       Wetland Tundra, Drained Slopes \n')
    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' Drained Slopes, Wetland Tundra, All ages \n')
    file.write( '----------------------------------- \n')
    init_total = self.Init_DrainedSlope_WT_Y + self.Init_DrainedSlope_WT_M + self.Init_DrainedSlope_WT_O
    final_total = self.Final_DrainedSlope_WT_Y + self.Final_DrainedSlope_WT_M + self.Final_DrainedSlope_WT_O
    file.write( 'Initial Fractional Area (km2): ' +str( init_total )+str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str(  final_total) +str('\n'))
    file.write( 'Total Fractional Change (km2):' + str( final_total - init_total) +str('\n'))
    file.write( 'Percent difference: ' + str( ((final_total - init_total)/init_total)*100.) +str('\n'))
    file.write( ' \n'    )
    file.write( '----------------------------------- \n')
    file.write( ' Drained Slopes, Wetland Tundra Young age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_DrainedSlope_WT_Y ) + str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_DrainedSlope_WT_Y) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_DrainedSlope_WT_Y - self.Init_DrainedSlope_WT_Y) + str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_DrainedSlope_WT_Y - self.Init_DrainedSlope_WT_Y)/\
                                                 self.Init_DrainedSlope_WT_Y)*100.) + str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.DrainedSlope_WT_Y['POI_Function']) + str('\n'))
    if self.DrainedSlope_WT_Y['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.DrainedSlope_WT_Y['A1_above'])+\
                   ' | '+str(self.DrainedSlope_WT_Y['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.DrainedSlope_WT_Y['A2_above'])+\
                   ' | '+str(self.DrainedSlope_WT_Y['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.DrainedSlope_WT_Y['x0_above'])+\
                   ' | '+str(self.DrainedSlope_WT_Y['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.DrainedSlope_WT_Y['dx_above'])+\
                   ' | '+str(self.DrainedSlope_WT_Y['dx_below'])+str('\n \n'))
    elif self.DrainedSlope_WT_Y['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.DrainedSlope_WT_Y['a_above'])+\
                   str(' | ')+str(self.DrainedSlope_WT_Y['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.DrainedSlope_WT_Y['b_above']) +\
                   str(' | ')+str(self.DrainedSlope_WT_Y['b_below'])+str('\n \n'))
    elif self.DrainedSlope_WT_Y['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.DrainedSlope_WT_Y['K_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_Y['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.DrainedSlope_WT_Y['C_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_Y['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.DrainedSlope_WT_Y['A_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_Y['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.DrainedSlope_WT_Y['B_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_Y['B_below'])+str('\n \n'))
    elif self.DrainedSlope_WT_Y['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.DrainedSlope_WT_Y['HillB_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_Y['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.DrainedSlope_WT_Y['HillN_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_Y['HillN_below'])+str('\n \n'))


    file.write(' Maximum rate of terrain transition: '+str(self.DrainedSlope_WT_Y['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.DrainedSlope_WT_Y['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.DrainedSlope_WT_Y['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.DrainedSlope_WT_Y['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.DrainedSlope_WT_Y['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.DrainedSlope_WT_Y['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.DrainedSlope_WT_Y['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.DrainedSlope_WT_Y['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.DrainedSlope_WT_Y['Figures'].lower() == 'no' and self.DrainedSlope_WT_Y['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')

    file.write( '----------------------------------- \n')
    file.write( ' Drained Slopes, Wetland Tundra Medium age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): ' +str( self.Init_DrainedSlope_WT_M) +str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_DrainedSlope_WT_M) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_DrainedSlope_WT_M - self.Init_DrainedSlope_WT_M)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_DrainedSlope_WT_M - self.Init_DrainedSlope_WT_M)/\
                                                 self.Init_DrainedSlope_WT_M)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.DrainedSlope_WT_M['POI_Function']) + str('\n'))
    if self.DrainedSlope_WT_M['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.DrainedSlope_WT_M['A1_above'])+\
                   ' | '+str(self.DrainedSlope_WT_M['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.DrainedSlope_WT_M['A2_above'])+\
                   ' | '+str(self.DrainedSlope_WT_M['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.DrainedSlope_WT_M['x0_above'])+\
                   ' | '+str(self.DrainedSlope_WT_M['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.DrainedSlope_WT_M['dx_above'])+\
                   ' | '+str(self.DrainedSlope_WT_M['dx_below'])+str('\n \n'))
    elif self.DrainedSlope_WT_M['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.DrainedSlope_WT_M['a_above'])+\
                   str(' | ')+str(self.DrainedSlope_WT_M['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.DrainedSlope_WT_M['b_above']) +\
                   str(' | ')+str(self.DrainedSlope_WT_M['b_below'])+str('\n \n'))
    elif self.DrainedSlope_WT_M['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.DrainedSlope_WT_M['K_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_M['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.DrainedSlope_WT_M['C_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_M['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.DrainedSlope_WT_M['A_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_M['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.DrainedSlope_WT_M['B_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_M['B_below'])+str('\n \n'))
    elif self.DrainedSlope_WT_M['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.DrainedSlope_WT_M['HillB_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_M['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.DrainedSlope_WT_M['HillN_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_M['HillN_below'])+str('\n \n'))

    file.write(' Maximum rate of terrain transition: '+str(self.DrainedSlope_WT_M['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.DrainedSlope_WT_M['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.DrainedSlope_WT_M['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.DrainedSlope_WT_M['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.DrainedSlope_WT_M['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.DrainedSlope_WT_M['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.DrainedSlope_WT_M['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.DrainedSlope_WT_M['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.DrainedSlope_WT_M['Figures'].lower() == 'no' and self.DrainedSlope_WT_M['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')

                   
    file.write( '----------------------------------- \n')
    file.write( ' Drained Slope, Wetland Tundra Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_DrainedSlope_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_DrainedSlope_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_DrainedSlope_WT_O - self.Init_DrainedSlope_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_DrainedSlope_WT_O - self.Init_DrainedSlope_WT_O)/\
                                                 self.Init_DrainedSlope_WT_O)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.DrainedSlope_WT_O['POI_Function']) + str('\n'))
    if self.DrainedSlope_WT_O['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.DrainedSlope_WT_O['A1_above'])+\
                   ' | '+str(self.DrainedSlope_WT_O['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.DrainedSlope_WT_O['A2_above'])+\
                   ' | '+str(self.DrainedSlope_WT_O['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.DrainedSlope_WT_O['x0_above'])+\
                   ' | '+str(self.DrainedSlope_WT_O['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.DrainedSlope_WT_O['dx_above'])+\
                   ' | '+str(self.DrainedSlope_WT_O['dx_below'])+str('\n \n'))
    elif self.DrainedSlope_WT_O['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.DrainedSlope_WT_O['a_above'])+\
                   str(' | ')+str(self.DrainedSlope_WT_O['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.DrainedSlope_WT_O['b_above']) +\
                   str(' | ')+str(self.DrainedSlope_WT_O['b_below'])+str('\n \n'))
    elif self.DrainedSlope_WT_O['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.DrainedSlope_WT_O['K_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_O['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.DrainedSlope_WT_O['C_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_O['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.DrainedSlope_WT_O['A_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_O['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.DrainedSlope_WT_O['B_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_O['B_below'])+str('\n \n'))
    elif self.DrainedSlope_WT_O['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.DrainedSlope_WT_O['HillB_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_O['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.DrainedSlope_WT_O['HillN_above'])+ \
                   str(' | ')+str(self.DrainedSlope_WT_O['HillN_below'])+str('\n \n'))


    file.write(' Maximum rate of terrain transition: '+str(self.DrainedSlope_WT_O['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.DrainedSlope_WT_O['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.DrainedSlope_WT_O['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.DrainedSlope_WT_O['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.DrainedSlope_WT_O['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.DrainedSlope_WT_O['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.DrainedSlope_WT_O['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.DrainedSlope_WT_O['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.DrainedSlope_WT_O['Figures'].lower() == 'no' and self.DrainedSlope_WT_O['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')

    file.write( '=============================================================\n')
    file.write( '       Wetland Tundra, Sand Dunes \n')
    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' Sand Dunes, Wetland Tundra, All ages \n')
    file.write( '----------------------------------- \n')
    init_total = self.Init_SandDunes_WT_Y + self.Init_SandDunes_WT_M + self.Init_SandDunes_WT_O
    final_total = self.Final_SandDunes_WT_Y + self.Final_SandDunes_WT_M + self.Final_SandDunes_WT_O
    file.write( 'Initial Fractional Area (km2): ' +str( init_total )+str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str(  final_total) +str('\n'))
    file.write( 'Total Fractional Change (km2):' + str( final_total - init_total) +str('\n'))
    file.write( 'Percent difference: ' + str( ((final_total - init_total)/init_total)*100.) +str('\n'))
    file.write( ' \n'    )
    file.write( '----------------------------------- \n')
    file.write( ' Sand Dunes, Wetland Tundra Young age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_SandDunes_WT_Y ) + str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_SandDunes_WT_Y) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_SandDunes_WT_Y - self.Init_SandDunes_WT_Y) + str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_SandDunes_WT_Y - self.Init_SandDunes_WT_Y)/\
                                                 self.Init_SandDunes_WT_Y)*100.) + str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.SandDunes_WT_Y['POI_Function']) + str('\n'))
    if self.SandDunes_WT_Y['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.SandDunes_WT_Y['A1_above'])+\
                   ' | '+str(self.SandDunes_WT_Y['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.SandDunes_WT_Y['A2_above'])+\
                   ' | '+str(self.SandDunes_WT_Y['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.SandDunes_WT_Y['x0_above'])+\
                   ' | '+str(self.SandDunes_WT_Y['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.SandDunes_WT_Y['dx_above'])+\
                   ' | '+str(self.SandDunes_WT_Y['dx_below'])+str('\n \n'))
    elif self.SandDunes_WT_Y['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.SandDunes_WT_Y['a_above'])+\
                   str(' | ')+str(self.SandDunes_WT_Y['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.SandDunes_WT_Y['b_above']) +\
                   str(' | ')+str(self.SandDunes_WT_Y['b_below'])+str('\n \n'))
    elif self.SandDunes_WT_Y['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.SandDunes_WT_Y['K_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_Y['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.SandDunes_WT_Y['C_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_Y['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.SandDunes_WT_Y['A_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_Y['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.SandDunes_WT_Y['B_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_Y['B_below'])+str('\n \n'))
    elif self.SandDunes_WT_Y['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.SandDunes_WT_Y['HillB_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_Y['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.SandDunes_WT_Y['HillN_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_Y['HillN_below'])+str('\n \n'))


    file.write(' Maximum rate of terrain transition: '+str(self.SandDunes_WT_Y['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.SandDunes_WT_Y['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.SandDunes_WT_Y['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.SandDunes_WT_Y['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.SandDunes_WT_Y['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.SandDunes_WT_Y['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.SandDunes_WT_Y['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.SandDunes_WT_Y['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.SandDunes_WT_Y['Figures'].lower() == 'no' and self.SandDunes_WT_Y['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')

    file.write( '----------------------------------- \n')
    file.write( ' Sand Dunes, Wetland Tundra Medium age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): ' +str( self.Init_SandDunes_WT_M) +str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_SandDunes_WT_M) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_SandDunes_WT_M - self.Init_SandDunes_WT_M)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_SandDunes_WT_M - self.Init_SandDunes_WT_M)/\
                                                 self.Init_SandDunes_WT_M)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.SandDunes_WT_M['POI_Function']) + str('\n'))
    if self.SandDunes_WT_M['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.SandDunes_WT_M['A1_above'])+\
                   ' | '+str(self.SandDunes_WT_M['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.SandDunes_WT_M['A2_above'])+\
                   ' | '+str(self.SandDunes_WT_M['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.SandDunes_WT_M['x0_above'])+\
                   ' | '+str(self.SandDunes_WT_M['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.SandDunes_WT_M['dx_above'])+\
                   ' | '+str(self.SandDunes_WT_M['dx_below'])+str('\n \n'))
    elif self.SandDunes_WT_M['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.SandDunes_WT_M['a_above'])+\
                   str(' | ')+str(self.SandDunes_WT_M['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.SandDunes_WT_M['b_above']) +\
                   str(' | ')+str(self.SandDunes_WT_M['b_below'])+str('\n \n'))
    elif self.SandDunes_WT_M['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.SandDunes_WT_M['K_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_M['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.SandDunes_WT_M['C_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_M['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.SandDunes_WT_M['A_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_M['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.SandDunes_WT_M['B_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_M['B_below'])+str('\n \n'))
    elif self.SandDunes_WT_M['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.SandDunes_WT_M['HillB_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_M['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.SandDunes_WT_M['HillN_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_M['HillN_below'])+str('\n \n'))

    file.write(' Maximum rate of terrain transition: '+str(self.SandDunes_WT_M['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.SandDunes_WT_M['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.SandDunes_WT_M['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.SandDunes_WT_M['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.SandDunes_WT_M['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.SandDunes_WT_M['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.SandDunes_WT_M['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.SandDunes_WT_M['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.SandDunes_WT_M['Figures'].lower() == 'no' and self.SandDunes_WT_M['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')


    file.write( '----------------------------------- \n')
    file.write( ' Sand Dunes, Wetland Tundra Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_SandDunes_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_SandDunes_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_SandDunes_WT_O - self.Init_SandDunes_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_SandDunes_WT_O - self.Init_SandDunes_WT_O)/\
                                                 self.Init_SandDunes_WT_O)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.SandDunes_WT_O['POI_Function']) + str('\n'))
    if self.SandDunes_WT_O['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.SandDunes_WT_O['A1_above'])+\
                   ' | '+str(self.SandDunes_WT_O['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.SandDunes_WT_O['A2_above'])+\
                   ' | '+str(self.SandDunes_WT_O['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.SandDunes_WT_O['x0_above'])+\
                   ' | '+str(self.SandDunes_WT_O['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.SandDunes_WT_O['dx_above'])+\
                   ' | '+str(self.SandDunes_WT_O['dx_below'])+str('\n \n'))
    elif self.SandDunes_WT_O['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.SandDunes_WT_O['a_above'])+\
                   str(' | ')+str(self.SandDunes_WT_O['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.SandDunes_WT_O['b_above']) +\
                   str(' | ')+str(self.SandDunes_WT_O['b_below'])+str('\n \n'))
    elif self.SandDunes_WT_O['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.SandDunes_WT_O['K_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_O['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.SandDunes_WT_O['C_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_O['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.SandDunes_WT_O['A_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_O['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.SandDunes_WT_O['B_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_O['B_below'])+str('\n \n'))
    elif self.SandDunes_WT_O['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.SandDunes_WT_O['HillB_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_O['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.SandDunes_WT_O['HillN_above'])+ \
                   str(' | ')+str(self.SandDunes_WT_O['HillN_below'])+str('\n \n'))


    file.write(' Maximum rate of terrain transition: '+str(self.SandDunes_WT_O['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.SandDunes_WT_O['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.SandDunes_WT_O['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.SandDunes_WT_O['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.SandDunes_WT_O['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.SandDunes_WT_O['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.SandDunes_WT_O['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.SandDunes_WT_O['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.SandDunes_WT_O['Figures'].lower() == 'no' and self.SandDunes_WT_O['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')


    file.write( '=============================================================\n')
    file.write( '       Wetland Tundra, Saturated Barrens \n')
    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' Saturated Barrens, Wetland Tundra, All ages \n')
    file.write( '----------------------------------- \n')
    init_total = self.Init_SaturatedBarrens_WT_Y + self.Init_SaturatedBarrens_WT_M + self.Init_SaturatedBarrens_WT_O
    final_total = self.Final_SaturatedBarrens_WT_Y + self.Final_SaturatedBarrens_WT_M + self.Final_SaturatedBarrens_WT_O
    file.write( 'Initial Fractional Area (km2): ' +str( init_total )+str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str(  final_total) +str('\n'))
    file.write( 'Total Fractional Change (km2):' + str( final_total - init_total) +str('\n'))
    file.write( 'Percent difference: ' + str( ((final_total - init_total)/init_total)*100.) +str('\n'))
    file.write( ' \n'    )
    file.write( '----------------------------------- \n')
    file.write( ' Saturated Barrens, Wetland Tundra Young age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_SaturatedBarrens_WT_Y ) + str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_SaturatedBarrens_WT_Y) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_SaturatedBarrens_WT_Y - self.Init_SaturatedBarrens_WT_Y) + str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_SaturatedBarrens_WT_Y - self.Init_SaturatedBarrens_WT_Y)/\
                                                 self.Init_SaturatedBarrens_WT_Y)*100.) + str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.SaturatedBarrens_WT_Y['POI_Function']) + str('\n'))
    if self.SaturatedBarrens_WT_Y['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_Y['A1_above'])+\
                   ' | '+str(self.SaturatedBarrens_WT_Y['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_Y['A2_above'])+\
                   ' | '+str(self.SaturatedBarrens_WT_Y['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_Y['x0_above'])+\
                   ' | '+str(self.SaturatedBarrens_WT_Y['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_Y['dx_above'])+\
                   ' | '+str(self.SaturatedBarrens_WT_Y['dx_below'])+str('\n \n'))
    elif self.SaturatedBarrens_WT_Y['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_Y['a_above'])+\
                   str(' | ')+str(self.SaturatedBarrens_WT_Y['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.SaturatedBarrens_WT_Y['b_above']) +\
                   str(' | ')+str(self.SaturatedBarrens_WT_Y['b_below'])+str('\n \n'))
    elif self.SaturatedBarrens_WT_Y['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_Y['K_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_Y['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_Y['C_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_Y['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_Y['A_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_Y['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_Y['B_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_Y['B_below'])+str('\n \n'))
    elif self.SaturatedBarrens_WT_Y['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_Y['HillB_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_Y['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_Y['HillN_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_Y['HillN_below'])+str('\n \n'))


    file.write(' Maximum rate of terrain transition: '+str(self.SaturatedBarrens_WT_Y['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.SaturatedBarrens_WT_Y['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.SaturatedBarrens_WT_Y['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.SaturatedBarrens_WT_Y['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.SaturatedBarrens_WT_Y['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.SaturatedBarrens_WT_Y['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.SaturatedBarrens_WT_Y['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.SaturatedBarrens_WT_Y['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.SaturatedBarrens_WT_Y['Figures'].lower() == 'no' and self.SaturatedBarrens_WT_Y['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')

    file.write( '----------------------------------- \n')
    file.write( ' Saturated Barrens, Wetland Tundra Medium age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): ' +str( self.Init_SaturatedBarrens_WT_M) +str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_SaturatedBarrens_WT_M) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_SaturatedBarrens_WT_M - self.Init_SaturatedBarrens_WT_M)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_SaturatedBarrens_WT_M - self.Init_SaturatedBarrens_WT_M)/\
                                                 self.Init_SaturatedBarrens_WT_M)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.SaturatedBarrens_WT_M['POI_Function']) + str('\n'))
    if self.SaturatedBarrens_WT_M['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_M['A1_above'])+\
                   ' | '+str(self.SaturatedBarrens_WT_M['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_M['A2_above'])+\
                   ' | '+str(self.SaturatedBarrens_WT_M['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_M['x0_above'])+\
                   ' | '+str(self.SaturatedBarrens_WT_M['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_M['dx_above'])+\
                   ' | '+str(self.SaturatedBarrens_WT_M['dx_below'])+str('\n \n'))
    elif self.SaturatedBarrens_WT_M['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_M['a_above'])+\
                   str(' | ')+str(self.SaturatedBarrens_WT_M['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.SaturatedBarrens_WT_M['b_above']) +\
                   str(' | ')+str(self.SaturatedBarrens_WT_M['b_below'])+str('\n \n'))
    elif self.SaturatedBarrens_WT_M['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_M['K_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_M['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_M['C_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_M['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_M['A_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_M['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_M['B_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_M['B_below'])+str('\n \n'))
    elif self.SaturatedBarrens_WT_M['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_M['HillB_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_M['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_M['HillN_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_M['HillN_below'])+str('\n \n'))


    file.write(' Maximum rate of terrain transition: '+str(self.SaturatedBarrens_WT_M['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.SaturatedBarrens_WT_M['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.SaturatedBarrens_WT_M['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.SaturatedBarrens_WT_M['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.SaturatedBarrens_WT_M['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.SaturatedBarrens_WT_M['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.SaturatedBarrens_WT_M['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.SaturatedBarrens_WT_M['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.SaturatedBarrens_WT_M['Figures'].lower() == 'no' and self.SaturatedBarrens_WT_M['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')


    file.write( '----------------------------------- \n')
    file.write( ' Saturated Barrens, Wetland Tundra Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_SaturatedBarrens_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_SaturatedBarrens_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_SaturatedBarrens_WT_O - self.Init_SaturatedBarrens_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_SaturatedBarrens_WT_O - self.Init_SaturatedBarrens_WT_O)/\
                                                 self.Init_SaturatedBarrens_WT_O)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.SaturatedBarrens_WT_O['POI_Function']) + str('\n'))
    if self.SaturatedBarrens_WT_O['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_O['A1_above'])+\
                   ' | '+str(self.SaturatedBarrens_WT_O['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_O['A2_above'])+\
                   ' | '+str(self.SaturatedBarrens_WT_O['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_O['x0_above'])+\
                   ' | '+str(self.SaturatedBarrens_WT_O['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_O['dx_above'])+\
                   ' | '+str(self.SaturatedBarrens_WT_O['dx_below'])+str('\n \n'))
    elif self.SaturatedBarrens_WT_O['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_O['a_above'])+\
                   str(' | ')+str(self.SaturatedBarrens_WT_O['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.SaturatedBarrens_WT_O['b_above']) +\
                   str(' | ')+str(self.SaturatedBarrens_WT_O['b_below'])+str('\n \n'))
    elif self.SaturatedBarrens_WT_O['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_O['K_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_O['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_O['C_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_O['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_O['A_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_O['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_O['B_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_O['B_below'])+str('\n \n'))
    elif self.SaturatedBarrens_WT_O['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_O['HillB_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_O['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.SaturatedBarrens_WT_O['HillN_above'])+ \
                   str(' | ')+str(self.SaturatedBarrens_WT_O['HillN_below'])+str('\n \n'))


    file.write(' Maximum rate of terrain transition: '+str(self.SaturatedBarrens_WT_O['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.SaturatedBarrens_WT_O['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.SaturatedBarrens_WT_O['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.SaturatedBarrens_WT_O['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.SaturatedBarrens_WT_O['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.SaturatedBarrens_WT_O['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.SaturatedBarrens_WT_O['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.SaturatedBarrens_WT_O['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.SaturatedBarrens_WT_O['Figures'].lower() == 'no' and self.SaturatedBarrens_WT_O['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')


    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' Rivers, Wetland Tundra, All ages \n')
    file.write( '----------------------------------- \n')
    init_total = self.Init_Rivers_WT_Y + self.Init_Rivers_WT_M + self.Init_Rivers_WT_O
    final_total = self.Final_Rivers_WT_Y + self.Final_Rivers_WT_M + self.Final_Rivers_WT_O
    file.write( 'Initial Fractional Area (km2): ' +str( init_total )+str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str(  final_total) +str('\n'))
    file.write( 'Total Fractional Change (km2):' + str( final_total - init_total) +str('\n'))
    file.write( 'Percent difference: ' + str( ((final_total - init_total)/init_total)*100.) +str('\n'))
    file.write( ' \n'    )
    file.write( '----------------------------------- \n')
    file.write( ' Rivers, Wetland Tundra Young age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Rivers_WT_Y ) + str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_Rivers_WT_Y) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_Rivers_WT_Y - self.Init_Rivers_WT_Y) + str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_Rivers_WT_Y - self.Init_Rivers_WT_Y)/\
                                                 self.Init_Rivers_WT_Y)*100.) + str('\n'))
    file.write( ' \n')
    file.write( '----------------------------------- \n')
    file.write( ' Rivers, Wetland Tundra Medium age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): ' +str( self.Init_Rivers_WT_M) +str('\n'))
    file.write( 'Final Fractional Area (km2): ' + str( self.Final_Rivers_WT_M) + str('\n'))
    file.write( 'Total Fractional Change (km2): ' + str( self.Final_Rivers_WT_M - self.Init_Rivers_WT_M)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_Rivers_WT_M - self.Init_Rivers_WT_M)/\
                                                 self.Init_Rivers_WT_M)*100.)+str('\n'))
    file.write( ' \n')
    file.write( '----------------------------------- \n')
    file.write( ' Rivers, Wetland Tundra Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Rivers_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_Rivers_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Rivers_WT_O - self.Init_Rivers_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_Rivers_WT_O - self.Init_Rivers_WT_O)/\
                                                 self.Init_Rivers_WT_O)*100.)+str('\n'))
    file.write( ' \n')
    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' Shrubs, Wetland Tundra, Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Shrubs_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_Shrubs_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Shrubs_WT_O - self.Init_Shrubs_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_Shrubs_WT_O - self.Init_Shrubs_WT_O)/\
                                                 self.Init_Shrubs_WT_O)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.Shrubs_WT_O['POI_Function']) + str('\n'))
    if self.Shrubs_WT_O['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.Shrubs_WT_O['A1_above'])+\
                   ' | '+str(self.Shrubs_WT_O['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.Shrubs_WT_O['A2_above'])+\
                   ' | '+str(self.Shrubs_WT_O['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.Shrubs_WT_O['x0_above'])+\
                   ' | '+str(self.Shrubs_WT_O['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.Shrubs_WT_O['dx_above'])+\
                   ' | '+str(self.Shrubs_WT_O['dx_below'])+str('\n \n'))
    elif self.Shrubs_WT_O['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.Shrubs_WT_O['a_above'])+\
                   str(' | ')+str(self.Shrubs_WT_O['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.Shrubs_WT_O['b_above']) +\
                   str(' | ')+str(self.Shrubs_WT_O['b_below'])+str('\n \n'))
    elif self.Shrubs_WT_O['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.Shrubs_WT_O['K_above'])+ \
                   str(' | ')+str(self.Shrubs_WT_O['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.Shrubs_WT_O['C_above'])+ \
                   str(' | ')+str(self.Shrubs_WT_O['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.Shrubs_WT_O['A_above'])+ \
                   str(' | ')+str(self.Shrubs_WT_O['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.Shrubs_WT_O['B_above'])+ \
                   str(' | ')+str(self.Shrubs_WT_O['B_below'])+str('\n \n'))
    elif self.Shrubs_WT_O['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.Shrubs_WT_O['HillB_above'])+ \
                   str(' | ')+str(self.Shrubs_WT_O['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.Shrubs_WT_O['HillN_above'])+ \
                   str(' | ')+str(self.Shrubs_WT_O['HillN_below'])+str('\n \n'))

    file.write(' Maximum rate of terrain transition: '+str(self.Shrubs_WT_O['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.Shrubs_WT_O['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.Shrubs_WT_O['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.Shrubs_WT_O['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.Shrubs_WT_O['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.Shrubs_WT_O['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.Shrubs_WT_O['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.Shrubs_WT_O['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.Shrubs_WT_O['Figures'].lower() == 'no' and self.Shrubs_WT_O['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')


    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' Coastal Waters, Wetland Tundra, Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_CoastalWaters_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_CoastalWaters_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_CoastalWaters_WT_O - self.Init_CoastalWaters_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_CoastalWaters_WT_O - self.Init_CoastalWaters_WT_O)/\
                                                 self.Init_CoastalWaters_WT_O)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.CoastalWaters_WT_O['POI_Function']) + str('\n'))
    if self.CoastalWaters_WT_O['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.CoastalWaters_WT_O['A1_above'])+\
                   ' | '+str(self.CoastalWaters_WT_O['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.CoastalWaters_WT_O['A2_above'])+\
                   ' | '+str(self.CoastalWaters_WT_O['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.CoastalWaters_WT_O['x0_above'])+\
                   ' | '+str(self.CoastalWaters_WT_O['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.CoastalWaters_WT_O['dx_above'])+\
                   ' | '+str(self.CoastalWaters_WT_O['dx_below'])+str('\n \n'))
    elif self.CoastalWaters_WT_O['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.CoastalWaters_WT_O['a_above'])+\
                   str(' | ')+str(self.CoastalWaters_WT_O['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.CoastalWaters_WT_O['b_above']) +\
                   str(' | ')+str(self.CoastalWaters_WT_O['b_below'])+str('\n \n'))
    elif self.CoastalWaters_WT_O['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.CoastalWaters_WT_O['K_above'])+ \
                   str(' | ')+str(self.CoastalWaters_WT_O['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.CoastalWaters_WT_O['C_above'])+ \
                   str(' | ')+str(self.CoastalWaters_WT_O['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.CoastalWaters_WT_O['A_above'])+ \
                   str(' | ')+str(self.CoastalWaters_WT_O['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.CoastalWaters_WT_O['B_above'])+ \
                   str(' | ')+str(self.CoastalWaters_WT_O['B_below'])+str('\n \n'))
    elif self.CoastalWaters_WT_O['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.CoastalWaters_WT_O['HillB_above'])+ \
                   str(' | ')+str(self.CoastalWaters_WT_O['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.CoastalWaters_WT_O['HillN_above'])+ \
                   str(' | ')+str(self.CoastalWaters_WT_O['HillN_below'])+str('\n \n'))


    file.write(' Maximum rate of terrain transition: '+str(self.CoastalWaters_WT_O['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.CoastalWaters_WT_O['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.CoastalWaters_WT_O['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.CoastalWaters_WT_O['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.CoastalWaters_WT_O['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.CoastalWaters_WT_O['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.CoastalWaters_WT_O['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.CoastalWaters_WT_O['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.CoastalWaters_WT_O['Figures'].lower() == 'no' and self.CoastalWaters_WT_O['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')

    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' Urban Area, Wetland Tundra \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Urban_WT) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_Urban_WT)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Urban_WT - self.Init_Urban_WT)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_Urban_WT - self.Init_Urban_WT)/\
                                                 self.Init_Urban_WT)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' POI Function Used: '+str(self.Urban_WT['POI_Function']) + str('\n'))
    if self.Urban_WT['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.Urban_WT['A1_above'])+\
                   ' | '+str(self.Urban_WT['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.Urban_WT['A2_above'])+\
                   ' | '+str(self.Urban_WT['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.Urban_WT['x0_above'])+\
                   ' | '+str(self.Urban_WT['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.Urban_WT['dx_above'])+\
                   ' | '+str(self.Urban_WT['dx_below'])+str('\n \n'))
    elif self.Urban_WT['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.Urban_WT['a_above'])+\
                   str(' | ')+str(self.Urban_WT['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.Urban_WT['b_above']) +\
                   str(' | ')+str(self.Urban_WT['b_below'])+str('\n \n'))
    elif self.Urban_WT['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.Urban_WT['K_above'])+ \
                   str(' | ')+str(self.Urban_WT['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.Urban_WT['C_above'])+ \
                   str(' | ')+str(self.Urban_WT['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.Urban_WT['A_above'])+ \
                   str(' | ')+str(self.Urban_WT['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.Urban_WT['B_above'])+ \
                   str(' | ')+str(self.Urban_WT['B_below'])+str('\n \n'))
    elif self.Urban_WT['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.Urban_WT['HillB_above'])+ \
                   str(' | ')+str(self.Urban_WT['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.Urban_WT['HillN_above'])+ \
                   str(' | ')+str(self.Urban_WT['HillN_below'])+str('\n \n'))


    file.write(' Maximum rate of terrain transition: '+str(self.Urban_WT['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.Urban_WT['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.Urban_WT['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.Urban_WT['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.Urban_WT['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.Urban_WT['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.Urban_WT['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.Urban_WT['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.Urban_WT['Figures'].lower() == 'no' and self.Urban_WT['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')


    file.write( '=============================================================\n')
    file.write( '-----------------------------------  \n')
    file.write( ' No Data, Wetland Tundra, Old age \n')
    file.write( '----------------------------------- \n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_NoData_WT_O) + str('\n'))
    file.write( 'Final Fractional Area (km2): '+str( self.Final_NoData_WT_O)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_NoData_WT_O - self.Init_NoData_WT_O)+str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_NoData_WT_O - self.Init_NoData_WT_O)/\
                                                 self.Init_NoData_WT_O)*100.)+str('\n'))
    file.write( ' \n')
    file.write( ' Wetland Tundra, No Data, Old age \n')
    file.write( ' POI Function Used: '+str(self.NoData_WT_O['POI_Function']) + str('\n'))
    if self.NoData_WT_O['POI_Function'].lower() == 'sigmoid':
        file.write(' POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.NoData_WT_O['A1_above'])+\
                   ' | '+str(self.NoData_WT_O['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.NoData_WT_O['A2_above'])+\
                   ' | '+str(self.NoData_WT_O['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.NoData_WT_O['x0_above'])+\
                   ' | '+str(self.NoData_WT_O['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.NoData_WT_O['dx_above'])+\
                   ' | '+str(self.NoData_WT_O['dx_below'])+str('\n \n'))
    elif self.NoData_WT_O['POI_Function'].lower() == 'linear':
        file.write(' POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.NoData_WT_O['a_above'])+\
                   str(' | ')+str(self.NoData_WT_O['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.NoData_WT_O['b_above']) +\
                   str(' | ')+str(self.NoData_WT_O['b_below'])+str('\n \n'))
    elif self.NoData_WT_O['POI_Function'].lower() == 'sigmoid2':
        file.write(' POI = K / (C + (A*x**B)) \n')
        file.write('  K [above | below drainage threshold]: '+str(self.NoData_WT_O['K_above'])+ \
                   str(' | ')+str(self.NoData_WT_O['K_below'])+str('\n'))
        file.write('  C [above | below drainage threshold]: '+str(self.NoData_WT_O['C_above'])+ \
                   str(' | ')+str(self.NoData_WT_O['C_below'])+str('\n'))        
        file.write('  A [above | below drainage threshold]: '+str(self.NoData_WT_O['A_above'])+ \
                   str(' | ')+str(self.NoData_WT_O['A_below'])+str('\n'))        
        file.write('  B [above | below drainage threshold]: '+str(self.NoData_WT_O['B_above'])+ \
                   str(' | ')+str(self.NoData_WT_O['B_below'])+str('\n \n'))
    elif self.NoData_WT_O['POI_Function'].lower() == 'hill':
        file.write(' POI = (B * (x^n))/(1+(x^n)) \n')
        file.write('  B [above | below drainage threshold]: '+str(self.NoData_WT_O['HillB_above'])+ \
                   str(' | ')+str(self.NoData_WT_O['HillB_below'])+str('\n'))        
        file.write('  n [above | below drainage threshold]: '+str(self.NoData_WT_O['HillN_above'])+ \
                   str(' | ')+str(self.NoData_WT_O['HillN_below'])+str('\n \n'))

    file.write(' Maximum rate of terrain transition: '+str(self.NoData_WT_O['max_terrain_transition'])+\
               str(' \n \n'))
    file.write(' Soil Porosity: '+str(self.NoData_WT_O['porosity'])+str('\n \n'))

    file.write(' Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.NoData_WT_O['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.NoData_WT_O['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.NoData_WT_O['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.NoData_WT_O['ice_slope_massive'])+str('\n \n'))

    file.write(' Output Results: ' +str('\n'))
    if self.NoData_WT_O['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.NoData_WT_O['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.NoData_WT_O['Figures'].lower() == 'no' and self.NoData_WT_O['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')


    file.write( '============================================================== \n')

    ############################################################################
    file.write( '===================================================\n')
    file.write( '                Simulation Notes                   \n')
    file.write( '===================================================\n')
    sim_notes = open(self.control['Run_dir']+self.Input_directory+str('/Notes/')+self.notes_file, 'r')
    file.write(sim_notes.read())
    sim_notes.close()
    ############################################################################
    file.close()

    #-------------------------
    # Return to Run Directory
    #-------------------------
    os.chdir(self.control['Run_dir'])
