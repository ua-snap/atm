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
        if self.initialize['WetNPG_Figure'].lower() == 'yes':
            print '  Initial Wetland Non-polygonal Ground Figure [Output/Wet_NPG]'
        if self.initialize['WetLCP_Figure'].lower() == 'yes':
            print '  Initial Wetland Low Center Polygon Figure [Output/Wet_LCP]'
        if self.initialize['WetCLC_Figure'].lower() == 'yes':
            print '  Initial Wetland Coalescent Low Center Polygon Figure [Output/Wet_CLC]'
        if self.initialize['WetFCP_Figure'].lower() == 'yes':
            print '  Initial Wetland Flat Center Polygon Figure [Output/Wet_FCP]'
        if self.initialize['WetHCP_Figure'].lower() == 'yes':
            print '  Initial Wetland High Center Polygon Figure [Output/Wet_HCP]'
        if self.initialize['Lakes_Figure'].lower() == 'yes':
            print '  Initial Lakes Figure [Output/Lakes]'
        if self.initialize['Ponds_Figure'].lower() == 'yes':
            print '  Initial Ponds Figure [Output/Ponds]'
        if self.initialize['Rivers_Figure'].lower() == 'yes':
            print '  Initial Rivers Figure [Output/Other_Cohorts]'
        if self.initialize['Urban_Figure'].lower() == 'yes':
            print '  Initial Ubran Figure [Output/Other_Cohorts]'
        if self.initialize['All_Cohorts_Figure'].lower() == 'yes':
            print '  Total Cohorts Figure [Output/All_Cohorts]'
    print ' '

    print 'Outputs of Normalized Cohort Distribution:'
    if self.initialize['Normalized_Cohort_Distribution_Figure'].lower() != 'yes':
        print '  No outputs generated.'
    else:
        if self.initialize['WetNPG_Normal'].lower() == 'yes':
            print '  Normalized Wetland Non-polygonal Ground Figure [Output/Wet_NPG]'
        if self.initialize['WetLCP_Normal'].lower() == 'yes':
            print '  Normalized Wetland Low Center Polygon Figure [Output/Wet_LCP]'
        if self.initialize['WetCLC_Normal'].lower() == 'yes':
            print '  Normalized Wetland Coalescent Low Center Polygon Figure [Output/Wet_CLC]'
        if self.initialize['WetFCP_Normal'].lower() == 'yes':
            print '  Normalized Wetland Flat Center Polygon Figure [Output/Wet_FCP]'
        if self.initialize['WetHCP_Normal'].lower() == 'yes':
            print '  Normalized Wetland High Center Polygon Figure [Output/Wet_HCP]'
        if self.initialize['Lakes_Normal'].lower() == 'yes':
            print '  Normalized Lakes Figure [Output/Lakes]'
        if self.initialize['Ponds_Normal'].lower() == 'yes':
            print '  Normalized Ponds Figure [Output/Ponds]'
        if self.initialize['Rivers_Normal'].lower() == 'yes':
            print '  Normalized Rivers Figure [Output/Other_Cohorts]'
        if self.initialize['Urban_Normal'].lower() == 'yes':
            print '  Normalized Ubran Figure [Output/Other_Cohorts]'
        if self.initialize['Total_Cohorts_Normal'].lower() == 'yes':
            print '  Normalize Total Cohorts [Output/All_Cohorts]'
    print ' '

    print 'Outputs of Cohort Ages:'
    if self.initialize['Initial_Cohort_Age_Figure'].lower() != 'yes':
        print '  No outputs generated.'
    else:
        if self.initialize['WetNPG_Age'].lower() == 'yes':
            print '  Wetland Non-polygonal Ground Age [Output/Wet_NPG]'
        if self.initialize['WetLCP_Age'].lower() == 'yes':
            print '  Wetland Low Center Polygon Age [Output/Wet_LCP]'
        if self.initialize['WetCLC_Age'].lower() == 'yes':
            print '  Wetland Coalescent Low Center Polygon Age [Output/Wet_CLC]'
        if self.initialize['WetFCP_Age'].lower() == 'yes':
            print '  Wetland Flat Center Polygon Age [Output/Wet_FCP]'
        if self.initialize['WetHCP_Age'].lower() == 'yes':
            print '  Wetland High Center Polygon Age [Output/Wet_HCP]'
        if self.initialize['Lakes_Age'].lower() == 'yes':
            print '  Lakes Age [Output/Lakes]'
        if self.initialize['Ponds_Age'].lower() == 'yes':
            print '  Normalized Ponds Age [Output/Ponds]'
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
    print '----------------------------------'
    print ' Non-polygonal ground - meadows '
    print '----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_Wet_NPG
    print 'Final Fraction Area (km2): ', self.Final_Wet_NPG
    print 'Total Fractional Change (km2): ', self.Final_Wet_NPG - self.Init_Wet_NPG
    print 'Percent difference: ', ((self.Final_Wet_NPG - self.Init_Wet_NPG)/self.Init_Wet_NPG)*100.
    print ' '
    ############################################################################
    print '----------------------------------'
    print ' Low Center Polygons '
    print '----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_Wet_LCP
    print 'Final Fraction Area (km2): ', self.Final_Wet_LCP
    print 'Total Fractional Change (km2): ', self.Final_Wet_LCP - self.Init_Wet_LCP
    print 'Percent change: ', ((self.Final_Wet_LCP - self.Init_Wet_LCP)/self.Init_Wet_LCP)*100.
    print ' '
    ############################################################################
    print '----------------------------------'
    print ' Coalescent Low Center Polygons '
    print '----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_Wet_CLC
    print 'Final Fraction Area (km2): ', self.Final_Wet_CLC
    print 'Total Fractional Change (km2): ', self.Final_Wet_CLC - self.Init_Wet_CLC
    print 'Percent change: ', ((self.Final_Wet_CLC - self.Init_Wet_CLC)/self.Init_Wet_CLC)*100.
    print ' '
    ############################################################################
    print '----------------------------------'
    print ' Flat Center Polygons '
    print '----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_Wet_FCP
    print 'Final Fraction Area (km2): ', self.Final_Wet_FCP
    print 'Total Fractional Change (km2): ', self.Final_Wet_FCP - self.Init_Wet_FCP
    print 'Percent difference: ', ((self.Final_Wet_FCP - self.Init_Wet_FCP)/self.Init_Wet_FCP)*100.
    print ' '
    ############################################################################
    print '----------------------------------'
    print ' High Center Polygons '
    print '----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_Wet_HCP
    print 'Final Fraction Area (km2): ', self.Final_Wet_HCP
    print 'Total Fractional Change (km2): ', self.Final_Wet_HCP - self.Init_Wet_HCP
    print 'Percent change: ', ((self.Final_Wet_HCP - self.Init_Wet_HCP)/self.Init_Wet_HCP)*100.
    print ' '
    ############################################################################
    print '----------------------------------'
    print '          Ponds '
    print '----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_Ponds
    print 'Final Fraction Area (km2): ', self.Final_Ponds
    print 'Total Fractional Change (km2): ', self.Final_Ponds - self.Init_Ponds
    print 'Percent change: ', ((self.Final_Ponds - self.Init_Ponds)/self.Init_Ponds)*100.
    print ' '
    ############################################################################
    print '----------------------------------'
    print '          Lakes '
    print '----------------------------------'
    print 'Initial Fractional Area (km2): ', self.Init_Lakes
    print 'Final Fraction Area (km2): ', self.Final_Lakes
    print 'Total Fractional Change (km2): ', self.Final_Lakes - self.Init_Lakes
    print 'Percent change: ', ((self.Final_Lakes - self.Init_Lakes)/self.Init_Lakes)*100.
    print ' '
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
    file = open(self.control['Run_dir']+self.Output_directory+str('/Archive/')+ \
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
        if self.initialize['WetNPG_Figure'].lower() == 'yes':
            file.write( '  Initial Wetland Non-polygonal Ground Figure [Output/Wet_NPG] \n')
        if self.initialize['WetLCP_Figure'].lower() == 'yes':
            file.write( '  Initial Wetland Low Center Polygon Figure [Output/Wet_LCP] \n')
        if self.initialize['WetCLC_Figure'].lower() == 'yes':
            file.write( '  Initial Wetland Coalescent Low Center Polygon Figure [Output/Wet_CLC] \n')
        if self.initialize['WetFCP_Figure'].lower() == 'yes':
            file.write( '  Initial Wetland Flat Center Polygon Figure [Output/Wet_FCP] \n')
        if self.initialize['WetHCP_Figure'].lower() == 'yes':
            file.write( '  Initial Wetland High Center Polygon Figure [Output/Wet_HCP] \n')
        if self.initialize['Lakes_Figure'].lower() == 'yes':
            file.write( '  Initial Lakes Figure [Output/Lakes] \n')
        if self.initialize['Ponds_Figure'].lower() == 'yes':
            file.write( '  Initial Ponds Figure [Output/Ponds] \n')
        if self.initialize['Rivers_Figure'].lower() == 'yes':
            file.write( '  Initial Rivers Figure [Output/Other_Cohorts] \n')
        if self.initialize['Urban_Figure'].lower() == 'yes':
            file.write( '  Initial Ubran Figure [Output/Other_Cohorts] \n')
        if self.initialize['All_Cohorts_Figure'].lower() == 'yes':
            file.write( '  Total Cohorts Figure [Output/All_Cohorts] \n \n')
    
    file.write( 'Outputs of Initial Cohort Fractional Distribution:\n')
        
    if self.initialize['Normalized_Cohort_Distribution_Figure'].lower() != 'yes':
        file.write( '  No outputs generated. \n')
    else:
        if self.initialize['WetNPG_Normal'].lower() == 'yes':
            file.write( '  Normalized Wetland Non-polygonal Ground Figure [Output/Wet_NPG] \n')
        if self.initialize['WetLCP_Normal'].lower() == 'yes':
            file.write( '  Normalized Wetland Low Center Polygon Figure [Output/Wet_LCP] \n')
        if self.initialize['WetCLC_Normal'].lower() == 'yes':
            file.write( '  Normalized Wetland Coalescent Low Center Polygon Figure [Output/Wet_CLC] \n')
        if self.initialize['WetFCP_Normal'].lower() == 'yes':
            file.write( '  Normalized Wetland Flat Center Polygon Figure [Output/Wet_FCP] \n')
        if self.initialize['WetHCP_Normal'].lower() == 'yes':
            file.write( '  Normalized Wetland High Center Polygon Figure [Output/Wet_HCP] \n')
        if self.initialize['Lakes_Normal'].lower() == 'yes':
            file.write( '  Normalized Lakes Figure [Output/Lakes] \n')
        if self.initialize['Ponds_Normal'].lower() == 'yes':
            file.write( '  Normalized Ponds Figure [Output/Ponds] \n')
        if self.initialize['Rivers_Normal'].lower() == 'yes':
            file.write( '  Normalized Rivers Figure [Output/Other_Cohorts] \n')
        if self.initialize['Urban_Normal'].lower() == 'yes':
            file.write( '  Normalized Ubran Figure [Output/Other_Cohorts] \n')
        if self.initialize['Total_Cohorts_Normal'].lower() == 'yes':
            file.write( '  Normalized Total Cohorts [Output/All_Cohorts] \n \n')

    file.write( 'Outputs of Initial Cohort Age:\n')
        
    if self.initialize['Initial_Cohort_Age_Figure'].lower() != 'yes':
        file.write( '  No outputs generated. \n')
    else:
        if self.initialize['WetNPG_Age'].lower() == 'yes':
            file.write( '  Wetland Non-polygonal Ground Age [Output/Wet_NPG] \n')
        if self.initialize['WetLCP_Age'].lower() == 'yes':
            file.write( '  Wetland Low Center Polygon Age [Output/Wet_LCP] \n')
        if self.initialize['WetCLC_Age'].lower() == 'yes':
            file.write( '  Wetland Coalescent Low Center Polygon Age [Output/Wet_CLC] \n')
        if self.initialize['WetFCP_Age'].lower() == 'yes':
            file.write( '  Wetland Flat Center Polygon Age [Output/Wet_FCP] \n')
        if self.initialize['WetHCP_Age'].lower() == 'yes':
            file.write( '  Wetland High Center Polygon Age [Output/Wet_HCP] \n')
        if self.initialize['Lakes_Age'].lower() == 'yes':
            file.write( '  Lakes Age [Output/Lakes] \n')
        if self.initialize['Ponds_Age'].lower() == 'yes':
            file.write( '  Ponds Age [Output/Ponds] \n \n')
    
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
    WNPG = self.Terrestrial['Wet_NPG_PLF']
    WLCP = self.Terrestrial['Wet_LCP_PLF']
    WCLC = self.Terrestrial['Wet_CLC_PLF']
    WFCP = self.Terrestrial['Wet_FCP_PLF']
    WHCP = self.Terrestrial['Wet_HCP_PLF']
    GNPG = self.Terrestrial['Gra_NPG_PLF']
    GLCP = self.Terrestrial['Gra_LCP_PLF']
    GFCP = self.Terrestrial['Gra_FCP_PLF']
    GHCP = self.Terrestrial['Gra_HCP_PLF']
    SNPG = self.Terrestrial['Shr_NPG_PLF']
    SLCP = self.Terrestrial['Shr_LCP_PLF']
    SFCP = self.Terrestrial['Shr_FCP_PLF']
    SHCP = self.Terrestrial['Shr_HCP_PLF']
    LPLF = self.Terrestrial['Lakes_PLF']
    PPLF = self.Terrestrial['Ponds_PLF']
    #------------------------------------------------------------------------- 
    file.write( '- - - - - - - - - - - - - - - - - - - - - - - - - -\n')
    file.write( '                Protective Layer Factors        \n')
    file.write( '     | Wetland | Graminoid | Shrub | Lake | Pond | \n')
    file.write( '- - - - - - - - - - - - - - - - - - - - - - - - - -\n')
    file.write( ' NPG |  '+str(WNPG)+'    |   '+str(GNPG)+'     | '+str(SNPG)+'   |  '+\
      str(LPLF)+' | '+str(PPLF)+'  |\n')
    file.write( ' LCP |  '+str(WLCP)+'    |   '+str(GLCP)+'     | '+str(SLCP)+'   |  '+\
      '--  | --   |\n')
    file.write( ' CLC |  '+str(WCLC)+'    |    --     |  --   |  '+\
      '--  | --   |\n')
    file.write( ' FCP |  '+str(WFCP)+'   |   '+str(GFCP)+'    | '+str(SFCP)+'   |  '+\
      '--  | --   |\n')
    file.write( ' HCP |  '+str(WHCP)+'    |   '+str(GHCP)+'     | '+str(SHCP)+'   |  '+\
      '--  | --   |\n')
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
    
    
    ############################################################################
    file.write( '====================================================\n')
    file.write( '           Non-polygonal ground - meadows           \n')
    file.write( '====================================================\n')
    file.write( 'Initial Fractional Area (km2): '+ str(self.Init_Wet_NPG) +str('\n'))
    file.write( 'Final Fraction Area (km2): '+ str(self.Final_Wet_NPG) + str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Wet_NPG - self.Init_Wet_NPG) +str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_Wet_NPG - self.Init_Wet_NPG)/self.Init_Wet_NPG)*100.) +\
                str('\n \n'))
                
    file.write( 'POI Function Used: '+str(self.WetNPG['POI_Function']) + str('\n'))
    if self.WetNPG['POI_Function'].lower() == 'sigmoid':
        file.write('POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.WetNPG['A1_above'])+\
                   ' | '+str(self.WetNPG['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.WetNPG['A2_above'])+\
                   ' | '+str(self.WetNPG['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.WetNPG['x0_above'])+\
                   ' | '+str(self.WetNPG['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.WetNPG['dx_above'])+\
                   ' | '+str(self.WetNPG['dx_below'])+str('\n \n'))
    elif self.WetNPG['POI_Function'].lower() == 'linear':
        file.write('POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.WetNPG['a_above'])+\
                   str(' | ')+str(self.WetNPG['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.WetNPG['b_above']) +\
                   str(' | ')+str(self.WetNPG['b_below'])+str('\n \n'))

    file.write('Maximum rate of terrain transition: '+str(self.WetNPG['max_terrain_transition'])+\
               str(' \n \n'))
    file.write('Soil Porosity: '+str(self.WetNPG['porosity'])+str('\n \n'))

    file.write('Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.WetNPG['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.WetNPG['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.WetNPG['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.WetNPG['ice_slope_massive'])+str('\n \n'))

    file.write('Output Results: ' +str('\n'))
    if self.WetNPG['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.WetNPG['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.WetNPG['Figures'].lower() == 'no' and self.WetNPG['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')
    file.write('\n')
                    
    ############################################################################
    file.write( '===================================================\n')
    file.write( '               Low Center Polygons                 \n')
    file.write( '===================================================\n')
    file.write( 'Initial Fractional Area (km2): '+str(self.Init_Wet_LCP) + str('\n'))
    file.write( 'Final Fraction Area (km2): '+ str(self.Final_Wet_LCP) + str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Wet_LCP - self.Init_Wet_LCP)+('\n'))
    file.write( 'Percent change: '+ str(((self.Final_Wet_LCP - self.Init_Wet_LCP)/\
                                             self.Init_Wet_LCP)*100.)+str('\n \n'))

    file.write( 'POI Function Used: '+str(self.WetLCP['POI_Function']) + str('\n'))
    if self.WetLCP['POI_Function'].lower() == 'sigmoid':
        file.write('POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.WetLCP['A1_above'])+\
                   ' | '+str(self.WetLCP['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.WetLCP['A2_above'])+\
                   ' | '+str(self.WetLCP['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.WetLCP['x0_above'])+\
                   ' | '+str(self.WetLCP['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.WetLCP['dx_above'])+\
                   ' | '+str(self.WetLCP['dx_below'])+str('\n \n'))
    elif self.WetLCP['POI_Function'].lower() == 'linear':
        file.write('POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.WetLCP['a_above'])+\
                   str(' | ')+str(self.WetLCP['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.WetLCP['b_above']) +\
                   str(' | ')+str(self.WetLCP['b_below'])+str('\n \n'))

    file.write('Maximum rate of terrain transition: '+str(self.WetLCP['max_terrain_transition'])+\
               str(' \n \n'))
    file.write('Soil Porosity: '+str(self.WetLCP['porosity'])+str(' \n \n'))

    file.write('Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.WetLCP['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.WetLCP['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.WetLCP['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.WetLCP['ice_slope_massive'])+str('\n \n'))

    file.write('Output Results: ' +str('\n'))
    if self.WetLCP['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.WetLCP['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.WetLCP['Figures'].lower() == 'no' and self.WetLCP['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')
    file.write('\n')

    ############################################################################
    file.write( '===================================================\n')
    file.write( '        Coalescent Low Center Polygons             \n')
    file.write( '===================================================\n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Wet_CLC)+str('\n'))
    file.write('Final Fraction Area (km2): '+str( self.Final_Wet_CLC )+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Wet_CLC - self.Init_Wet_CLC)+str( '\n'))
    file.write( 'Percent change: '+str(((self.Final_Wet_CLC - self.Init_Wet_CLC)/self.Init_Wet_CLC)*100.) \
                +str('\n \n'))

    file.write( 'POI Function Used: '+str(self.WetCLC['POI_Function']) + str('\n'))
    if self.WetCLC['POI_Function'].lower() == 'sigmoid':
        file.write('POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.WetCLC['A1_above'])+\
                   ' | '+str(self.WetCLC['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.WetCLC['A2_above'])+\
                   ' | '+str(self.WetCLC['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.WetCLC['x0_above'])+\
                   ' | '+str(self.WetCLC['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.WetCLC['dx_above'])+\
                   ' | '+str(self.WetCLC['dx_below'])+str('\n \n'))
    elif self.WetCLC['POI_Function'].lower() == 'linear':
        file.write('POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.WetCLC['a_above'])+\
                   str(' | ')+str(self.WetCLC['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.WetCLC['b_above']) +\
                   str(' | ')+str(self.WetCLC['b_below'])+str('\n \n'))

    file.write('Maximum rate of terrain transition: '+str(self.WetCLC['max_terrain_transition'])+\
               str('\n \n'))
    file.write('Soil Porosity: '+str(self.WetCLC['porosity'])+str('\n \n'))

    file.write('Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.WetCLC['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.WetCLC['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.WetCLC['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.WetCLC['ice_slope_massive'])+str('\n \n'))

    file.write('Output Results: ' +str('\n'))
    if self.WetCLC['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.WetCLC['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.WetCLC['Figures'].lower() == 'no' and self.WetLCP['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')
    file.write('\n')

    ############################################################################
    file.write( '===================================================\n')
    file.write( '              Flat Center Polygons                 \n')
    file.write( '===================================================\n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Wet_FCP)+str('\n'))
    file.write( 'Final Fraction Area (km2): '+str( self.Final_Wet_FCP)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Wet_FCP - self.Init_Wet_FCP)+str('\n'))
    file.write( 'Percent change: '+str( ((self.Final_Wet_FCP - self.Init_Wet_FCP)/self.Init_Wet_FCP)*100.)\
                +str('\n \n'))

    file.write( 'POI Function Used: '+str(self.WetFCP['POI_Function']) + str('\n'))
    if self.WetFCP['POI_Function'].lower() == 'sigmoid':
        file.write('POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.WetFCP['A1_above'])+\
                   ' | '+str(self.WetFCP['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.WetFCP['A2_above'])+\
                   ' | '+str(self.WetFCP['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.WetFCP['x0_above'])+\
                   ' | '+str(self.WetFCP['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.WetFCP['dx_above'])+\
                   ' | '+str(self.WetFCP['dx_below'])+str('\n \n'))
    elif self.WetFCP['POI_Function'].lower() == 'linear':
        file.write('POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.WetFCP['a_above'])+\
                   str(' | ')+str(self.WetFCP['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.WetFCP['b_above']) +\
                   str(' | ')+str(self.WetFCP['b_below'])+str('\n \n'))

    file.write('Maximum rate of terrain transition: '+str(self.WetFCP['max_terrain_transition'])+\
               str('\n \n'))
    file.write('Soil Porosity: '+str(self.WetFCP['porosity'])+str('\n \n'))

    file.write('Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.WetFCP['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.WetFCP['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.WetFCP['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.WetFCP['ice_slope_massive'])+str('\n \n'))

    file.write('Output Results: ' +str('\n'))
    if self.WetFCP['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.WetFCP['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.WetFCP['Figures'].lower() == 'no' and self.WetFCP['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')
    file.write('\n')

    ############################################################################
    file.write( '===================================================\n')
    file.write( '              High Center Polygons                 \n')
    file.write( '===================================================\n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Wet_HCP)+str('\n'))
    file.write( 'Final Fraction Area (km2): '+str( self.Final_Wet_HCP)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Wet_HCP - self.Init_Wet_HCP)+str('\n'))
    file.write( 'Percent change: '+str( ((self.Final_Wet_HCP - self.Init_Wet_HCP)/self.Init_Wet_HCP)*100.)\
                +str('\n \n'))

    file.write( 'POI Function Used: '+str(self.WetHCP['POI_Function']) + str('\n'))
    if self.WetHCP['POI_Function'].lower() == 'sigmoid':
        file.write('POI = A2 + (A1 - A2) / (1. + exp((x - x0) / dx)) \n')
        file.write('  A1 [above | below drainage threshold]: '+str(self.WetHCP['A1_above'])+\
                   ' | '+str(self.WetHCP['A1_below'])+str('\n'))
        file.write('  A2 [above | below drainage threshold]: '+str(self.WetHCP['A2_above'])+\
                   ' | '+str(self.WetHCP['A2_below'])+str('\n'))
        file.write('  x0 [above | below drainage threshold]: '+str(self.WetHCP['x0_above'])+\
                   ' | '+str(self.WetHCP['x0_below'])+str('\n'))
        file.write('  dx [above | below drainage threshold]: '+str(self.WetHCP['dx_above'])+\
                   ' | '+str(self.WetHCP['dx_below'])+str('\n \n'))
    elif self.WetFCP['POI_Function'].lower() == 'linear':
        file.write('POI = a + (b * x) \n')
        file.write('  a [above | below drainage threshold]: '+str(self.WetHCP['a_above'])+\
                   str(' | ')+str(self.WetHCP['a_below'])+str('\n'))
        file.write('  b [above | below draingage threshold]: '+str(self.WetHCP['b_above']) +\
                   str(' | ')+str(self.WetHCP['b_below'])+str('\n \n'))

    file.write('Maximum rate of terrain transition: '+str(self.WetHCP['max_terrain_transition'])+\
               str('\n \n'))
    file.write('Soil Porosity: '+str(self.WetHCP['porosity'])+str('\n \n'))

    file.write('Rate Transitions as a function of ground ice content: \n')
    file.write('  Poor Ground Ice: '+str(self.WetHCP['ice_slope_poor'])+str('\n'))
    file.write('  Pore Ground Ice: '+str(self.WetHCP['ice_slope_pore'])+str('\n'))
    file.write('  Wedge Ground Ice: '+str(self.WetHCP['ice_slope_wedge'])+str('\n'))
    file.write('  Massive Ground Ice: '+str(self.WetHCP['ice_slope_massive'])+str('\n \n'))

    file.write('Output Results: ' +str('\n'))
    if self.WetHCP['Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.WetHCP['Movie'].lower() == 'yes':
        file.write('  Animation \n' )
    if self.WetHCP['Figures'].lower() == 'no' and self.WetHCP['Movie'].lower() == 'no':
        file.write('  No output written to disk. \n')
    file.write('\n')

    ############################################################################
    file.write( '===================================================\n')
    file.write( '                       Ponds                       \n')
    file.write( '===================================================\n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Ponds)+str('\n'))
    file.write( 'Final Fraction Area (km2): '+str( self.Final_Ponds)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Ponds - self.Init_Ponds)+str('\n'))
    file.write( 'Percent change: '+str( ((self.Final_Ponds - self.Init_Ponds)/self.Init_Ponds)*100.)\
                +str('\n \n'))
    #----------------------------------------------------------------------------------
    if self.LakePond['Pond_Distribution'].lower() == 'random':
        file.write('Pond Depth Distribution is initialized as a RANDOM function. \n')
        file.write('  Lower | Upper bounds of random function are: '+ \
                   str(self.LakePond['Lower_Pond_Depth']) + str(' | ') + \
                   str(self.LakePond['Upper_Pond_Depth'])+str(' \n \n'))
    elif self.LakePond['Pond_Distribution'].lower() == 'uniform':
        file.write('Pond Depth Distribution is initialized as UNIFORM. \n ')
        file.write(' The initial Lake Depth is: '+str(self.LakePond['Uniform_Pond_Depth'])+str(' \n \n'))
    #-------------------------------------------------------------------------------------------
    file.write('The Pond Expansion constant is set to: '+str(self.LakePond['Pond_Expansion']) +\
               str(' \n \n'))
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
    #--------------------------------------------------------------------------------------------
    file.write('Pond depth control constant: '+str(self.LakePond['pond_depth_control'])+str('\n \n'))
    #--------------------------------------------------------------------------------------------
    file.write('Output Results: ' +str('\n'))
    if self.LakePond['Pond_Depth_Figure'].lower() == 'yes':
        file.write('  Initial pond depth is output as a figure. \n')
    if self.LakePond['Pond_Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.LakePond['Pond_Movie'].lower() == 'yes':
        file.write('  Animation \n')
    file.write('\n')
                
    #--------------------------------------------------------------------------------------
                                                                         
    ############################################################################           
    file.write( '===================================================\n')
    file.write( '                      Lakes                        \n')
    file.write( '===================================================\n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Lakes)+str('\n'))
    file.write( 'Final Fraction Area (km2): '+str( self.Final_Lakes)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Lakes - self.Init_Lakes)+str('\n'))
    file.write( 'Percent change: '+str( ((self.Final_Lakes - self.Init_Lakes)/self.Init_Lakes)*100.)\
                +str('\n \n'))
    #-------------------------------------------------------------------------------------------
    file.write('The Lake Expansion constant is set to: '+str(self.LakePond['Lake_Expansion']) +\
               str('. \n \n'))
    #-------------------------------------------------------------------------------------------
    if self.LakePond['Lake_Distribution'].lower() == 'random':
        file.write('Lake Depth Distribution is initialized as a RANDOM function. \n')
        file.write('  Lower | Upper bounds of random function are: '+ \
                   str(self.LakePond['Lower_Lake_Depth']) + str(' | ') + \
                   str(self.LakePond['Upper_Lake_Depth'])+str(' \n \n'))
    elif self.LakePond['Lake_Distribution'].lower() == 'uniform':
        file.write('Lake Depth Distribution is initialized as UNIFORM. \n')
        file.write('  The initial Lake Depth is: '+str(self.LakePond['Uniform_Lake_Depth'])+str(' \n \n'))
    #---------------------------------------------------------------------------------------
    if self.LakePond['ice_thickness_distribution'].lower() == 'random':
        file.write('Ice thickness alpha value is RANDOM. \n')
        file.write('  Lower | Upper bounds of alpha values are: ' +\
                   str(self.LakePond['Lower_ice_thickness_alpha']) +str(' | ') +\
                   str(self.LakePond['Upper_ice_thickness_alpha']) +str(' \n \n'))
    elif self.LakePond['ice_thickness_distribution'].lower() == 'uniform':
        file.write('Ice thickness alpha value is UNIFORM. \n')
        file.write('  The alpha value is: '+str(self.LakePond['ice_thickness_uniform_alpha']) +\
                   str(' \n \n'))
    #-------------------------------------------------------------------------------------------
    file.write('Lake depth control constant: '+str(self.LakePond['lake_depth_control'])+str('\n \n'))
    #--------------------------------------------------------------------------------------------
    file.write('Output Results: ' +str('\n'))
    if self.LakePond['Lake_Depth_Figure'].lower() == 'yes':
        file.write('  Initial Lake depth is output as a figure. \n')
    if self.LakePond['Lake_Figures'].lower() == 'yes':
        file.write('  Yearly Figures \n')
    if self.LakePond['Lake_Movie'].lower() == 'yes':
        file.write('  Animation \n')
    file.write('\n')
    #--------------------------------------------------------------------------------------

    
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
