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
    ##########################################################################
    print '-----------------------------------'
    print '   Meteorologic Data Information   '
    print '-----------------------------------'
    if self.met_distribution.lower() == 'point':
        print 'Point meteorologic data is used.'
    else:
        print 'Meterologic data is distributed.'
    print 'Meteorologic Data File: ', self.met_file
    if self.degree_day_method.lower() == 'read':
        print 'Degree Days read from files: ',self.TDD_file +' and '+self.FDD_file
    else:
        print 'Degree Days calculated during simulation.'
    print ' '
        
    # Note: Might want to add climatic event probability and block size here
    ############################################################################
    ## print '------------------------------------'
    ## print '   Active Layer Depth Information   '
    ## print '------------------------------------'
    ## print 'Initial ALD [Mean, Max, Min, Std]: '+str(self.ALD_start_ave)+', '+str(self.ALD_start_max)+', '+\
    ##       str(self.ALD_start_min)+', '+str(self.ALD_start_std)
    ## print 'Final ALD [Mean, Max, Min, Std]: '+str(np.mean(self.ALD))+', '+str(np.max(self.ALD))+', ' +\
    ##       str(np.min(self.ALD))+', '+str(np.std(self.ALD))
    
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
    print '----------------------------------'
    print '        Simulation Notes '
    print '----------------------------------'
    file = open(self.control['Run_dir']+self.Input_directory+str('/Notes/')+self.notes_file, 'r')
    print file.read()
    file.close()
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
    file.write(' \n')
    ##########################################################################
    file.write( '-----------------------------------\n')
    file.write( '   Meteorologic Data Information   \n')
    file.write( '-----------------------------------\n')
    if self.met_distribution.lower() == 'point':
        file.write( 'Point meteorologic data is used. \n')
    else:
        file.write( 'Meterologic data is distributed. \n')
    file.write( 'Meteorologic Data File: '+ self.met_file +str('\n'))
    if self.degree_day_method.lower() == 'read':
        file.write('Degree Days read from files: '+ self.TDD_file +' and '+ self.FDD_file +str('\n'))
    else:
        file.write( 'Degree Days calculated during simulation. \n')
    file.write( ' \n')
        
    # Note: Might want to add climatic event probability and block size here
    ############################################################################
    file.write( '---------------------------------- \n')
    file.write( ' Non-polygonal ground - meadows \n')
    file.write( '----------------------------------\n')
    file.write( 'Initial Fractional Area (km2): '+ str(self.Init_Wet_NPG) +str('\n'))
    file.write( 'Final Fraction Area (km2): '+ str(self.Final_Wet_NPG) + str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Wet_NPG - self.Init_Wet_NPG) +str('\n'))
    file.write( 'Percent difference: '+str( ((self.Final_Wet_NPG - self.Init_Wet_NPG)/self.Init_Wet_NPG)*100.) +\
                str('\n \n'))
    ############################################################################
    file.write( '---------------------------------- \n')
    file.write( ' Low Center Polygons \n')
    file.write( '----------------------------------\n')
    file.write( 'Initial Fractional Area (km2): '+str(self.Init_Wet_LCP) + str('\n'))
    file.write( 'Final Fraction Area (km2): '+ str(self.Final_Wet_LCP) + str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Wet_LCP - self.Init_Wet_LCP)+('\n'))
    file.write( 'Percent change: '+ str(((self.Final_Wet_LCP - self.Init_Wet_LCP)/\
                                             self.Init_Wet_LCP)*100.)+str('\n \n'))
    ############################################################################
    file.write( '----------------------------------\n')
    file.write( ' Coalescent Low Center Polygons \n')
    file.write( '----------------------------------\n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Wet_CLC)+str('\n'))
    file.write('Final Fraction Area (km2): '+str( self.Final_Wet_CLC )+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Wet_CLC - self.Init_Wet_CLC)+str( '\n'))
    file.write( 'Percent change: '+str(((self.Final_Wet_CLC - self.Init_Wet_CLC)/self.Init_Wet_CLC)*100.) \
                +str('\n \n'))
    ############################################################################
    file.write( '----------------------------------\n')
    file.write( ' Flat Center Polygons \n')
    file.write( '----------------------------------\n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Wet_FCP)+str('\n'))
    file.write( 'Final Fraction Area (km2): '+str( self.Final_Wet_FCP)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Wet_FCP - self.Init_Wet_FCP)+str('\n'))
    file.write( 'Percent change: '+str( ((self.Final_Wet_FCP - self.Init_Wet_FCP)/self.Init_Wet_FCP)*100.)\
                +str('\n \n'))
    ############################################################################
    file.write( '----------------------------------\n')
    file.write( ' High Center Polygons \n')
    file.write( '----------------------------------\n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Wet_HCP)+str('\n'))
    file.write( 'Final Fraction Area (km2): '+str( self.Final_Wet_HCP)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Wet_HCP - self.Init_Wet_HCP)+str('\n'))
    file.write( 'Percent change: '+str( ((self.Final_Wet_HCP - self.Init_Wet_HCP)/self.Init_Wet_HCP)*100.)\
                +str('\n \n'))
    ############################################################################
    file.write( '----------------------------------\n')
    file.write( '          Ponds \n')
    file.write( '----------------------------------\n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Ponds)+str('\n'))
    file.write( 'Final Fraction Area (km2): '+str( self.Final_Ponds)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Ponds - self.Init_Ponds)+str('\n'))
    file.write( 'Percent change: '+str( ((self.Final_Ponds - self.Init_Ponds)/self.Init_Ponds)*100.)\
                +str('\n \n'))
    ############################################################################           
    file.write( '----------------------------------\n')
    file.write( '          Lakes \n')
    file.write( '----------------------------------\n')
    file.write( 'Initial Fractional Area (km2): '+str( self.Init_Lakes)+str('\n'))
    file.write( 'Final Fraction Area (km2): '+str( self.Final_Lakes)+str('\n'))
    file.write( 'Total Fractional Change (km2): '+str( self.Final_Lakes - self.Init_Lakes)+str('\n'))
    file.write( 'Percent change: '+str( ((self.Final_Lakes - self.Init_Lakes)/self.Init_Lakes)*100.)\
                +str('\n \n'))
    ############################################################################
    file.write( '----------------------------------\n')
    file.write( '        Simulation Notes \n')
    file.write( '----------------------------------\n')
    sim_notes = open(self.control['Run_dir']+self.Input_directory+str('/Notes/')+self.notes_file, 'r')
    file.write(sim_notes.read())
    sim_notes.close()
    ############################################################################
    file.close()
