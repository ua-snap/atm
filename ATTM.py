#!/usr/bin/env python

"""
________________________________________________________________________________
Arctic Tundra Thermokarst Model (ATTM)
________________________________________________________________________________
The purpose of this script is to provide a protype source
code for testing and development of the Arctic Tundra
Thermokarst Model (ATTM) to be integrated into the Alaska
Integrated Ecosystem Model (AIEM).
________________________________________________________________________________
Created: May 2014. Bob Bolton
Modified:

________________________________________________________________________________
Module flow for debugging purposes:

class ATTM()
   __init__

   =====================
   Execution sequence
   =====================
   run_attm()                 

   ++++++++++++++++++++++++
   Initialization Sequence
   ++++++++++++++++++++++++
   read_control
   read_met_data
   calc_degree_days
   read_layers
   model_domain
   create_attm_cohort_arrays
   initial_cohort_population
   initial_cohort_check
   cohort_present
   initial_cohort_age
   read_ice_content
   read_drainage_efficiency
   read_initial_ALD
   set_ALD_constant
   set_ALD_array
   set_lake_pond_depth
   set_lake_expansion_constant
   set_lake_ice_depth_constant
   set_ice_thickness_array
   set_protective_layer
   set_initial_cumulative_probability

   +++++++++++++++++++
   Main Program Loop
   +++++++++++++++++++
   check_climate_event
   check_water_climate
   lake_pond_expansion
   active_layer_depth
   check_Wet_NPG
   check_Wet_LCP
   check_Wet_CLC
   check_Wet_FCP
   check_Wet_HCP
   ice_thickness
   check_Ponds
   check_Lakes
   cohort_check

   +++++++++++++
       Output
   +++++++++++++
   import Output_cohorts_by_year

Execute script
________________________________________________________________________________
"""

################################################################################
# Authorship
################################################################################
__author__     = "Bob Bolton"
__copyright__  = "Copyright 2014, Bob Bolton"
__credits__    = ["Bob Bolton", "Vladimir Romanovsky", "Dave McGuire", "AIEM Thermokarst Team"]
__license__    = "GPL"
__version__    = "0.1"
__maintainer__ = "Bob Bolton"
__email__      = "bbolton@iarc.uaf.edu"
__status__     = "Development"

################################################################################
# Required Modules
################################################################################
import numpy as np
import gdal, os, sys, glob, random, time, datetime
from gdalconst import *
from osgeo import *
import pylab as pl
import xlrd, xlwt
from scipy import interpolate
from scipy import integrate
import subprocess
import tarfile

# Import ATTM Modules
import clock
import read_control
import read_met_data
import read_degree_days
import calc_degree_days
import read_layers
import model_domain
import create_attm_cohort_arrays
import initial_cohort_population
import initial_cohort_check
import cohort_present
import initial_cohort_age
import read_ice_content
import read_drainage_efficiency
import read_initial_ALD
import set_ALD_constant
import set_ALD_array
import set_lake_pond_depth
import set_lake_expansion_constant
import set_lake_ice_depth_constant
import set_ice_thickness_array
import climate_expansion_arrays
import set_pond_growth_array
import set_protective_layer
import set_initial_cumulative_probability
import cohorts
import check_climate_event
import check_water_climate
import lake_pond_expansion
import active_layer_depth
import check_Wet_NPG
import check_Wet_LCP
import check_Wet_CLC
import check_Wet_FCP
import check_Wet_HCP
import ice_thickness
import check_Ponds
import check_Lakes
import cohort_check

import Output_cohorts_by_year
import results
import archive
#_______________________________________________________________________________
class ATTM(object):

    Control_file        = sys.argv[1]
 
    def __init__(self):
        # ----------------------
        # Simulation Start Time
        # ----------------------
        clock.start(self)
        
        #--------------------------------------
        # Read the Control File for Simulation
        #--------------------------------------
        self.Control_file     = sys.argv[1]
        
        ########################################################################
        # Execute the script
        ########################################################################
        self.run_attm()
#_______________________________________________________________________________
    def run_attm(self):
        
        """ Program sequence """
        #====================================================
        # Initialization Process
        #====================================================
        print '==================='
        print ' Initializing ATTM'
        print '==================='
        read_control.read_control(self)
        read_layers.read_layers(self)
        model_domain.model_domain(self)
        create_attm_cohort_arrays.create_attm_cohort_arrays(self)
        initial_cohort_population.initial_cohort_population(self, PLOT = 'FALSE', FIGURE = 'TRUE')
        initial_cohort_check.initial_cohort_check(self, PLOT = 'FALSE', FIGURE = 'TRUE')
        cohort_present.cohort_present(self)

        #_______________________________________
        # READ MET Data & Calculate Degree Days
        #_______________________________________
        read_met_data.read_met_data(self)
        if self.degree_day_method.lower() == 'read':    # 'Read' file or 'Calc' from geotiff input
            read_degree_days.read_degree_days(self, FIGURE = 'FALSE')
        else:
            calc_degree_days.calc_degree_days(self, PLOT = 'FALSE', FIGURE = 'TRUE')
        initial_cohort_age.initial_cohort_age(self, PLOT = 'FALSE', FIGURE = 'TRUE')

        
        print '====================================='
        print ' Initializing Terrestrial Properties'
        print '====================================='
        read_ice_content.read_ice_content(self, PLOT = 'FALSE', FIGURE = 'TRUE', DISTRIBUTION = 'WEDGE')
        read_drainage_efficiency.read_drainage_efficiency(self, PLOT = 'FALSE', FIGURE = 'TRUE', DISTRIBUTION = 'BELOW')
        read_initial_ALD.read_initial_ALD(self, PLOT = 'FALSE', FIGURE = 'TRUE') 
        set_ALD_constant.set_ALD_constant(self, PLOT = 'FALSE', FIGURE = 'TRUE')
        set_ALD_array.set_ALD_array(self)
        
        print '=================================== '
        print ' Initializing Lake & Pond Properties'
        print '===================================='
        set_lake_pond_depth.set_lake_pond_depth(self, PLOT = 'FALSE', FIGURE = 'TRUE')
        set_lake_expansion_constant.set_lake_expansion_constant(self)
        set_lake_ice_depth_constant.set_lake_ice_depth_constant(self)
        set_ice_thickness_array.set_ice_thickness_array(self)
        climate_expansion_arrays.set_climate_expansion_arrays(self)
        set_pond_growth_array.set_pond_growth_array(self)
        

        print '====================================================='
        print ' Initializing Combined Terrestrial / Lake Properties '
        print '====================================================='
        set_protective_layer.set_protective_layer(self, PLOT = 'FALSE', FIGURE = 'FALSE')
        set_initial_cumulative_probability.set_initial_cumulative_probability(self)

        print '=========================='
        print ' Starting the MAIN LOOP '
        print '=========================='

        # - - - - - - - - - - - - - - - - - - -
        # Shorten simulation length if testing
        # - - - - - - - - - - - - - - - - - - -
        if self.test_code.lower() == 'yes':
            stop = 5
        else:
            stop = int(self.ATTM_time_steps)
            
        #for time in range(0, int(self.ATTM_time_steps)):
        for time in range(0, stop):
            if time == 0:
                cohorts.initial(self)
            print '    at time step: ', time
            
            # ++++++++++++++++++++++++++++++++++++++
            # Check for significant climatic event
            # ++++++++++++++++++++++++++++++++++++++
            climate_blocks = 'RANDOM'          # Can be either 'RANDOM' (0,20) or a numerical value
            climate_event_probability = 0.01    # (0.013 = 1/75 chance event will happen on a given year)
            # Check sub-model domains (block by block influence)
            check_climate_event.check_climate_event(self, climate_blocks = climate_blocks,
                                                    climate_event_probability = climate_event_probability)
            
           
            # ----------------------------------------------------------
            # Looping over elements
            # ----------------------------------------------------------
            for element in range(0, self.ATTM_nrows * self.ATTM_ncols):
                
                # ----------------------------------------------------
                # Define the total fractional area of cohorts for
                # each element
                # ----------------------------------------------------
                cohort_start = cohort_check.cohort_start(self, element, time)
                
                # ----------------------------------------------------
                # Expand lake & ponds by prescribed rate
                # ----------------------------------------------------
                lake_pond_expansion.lake_pond_expansion(self, element)
                
                # ----------------------------------------------------------
                # Set active layer depth
                # ---------------------------------------------------------
                active_layer_depth.active_layer_depth(self, time, element)
                
                # ----------------------------------
                # Cycle through terrestrial cohorts
                # ----------------------------------
                check_Wet_NPG.check_Wet_NPG(self, element, time)
                check_Wet_LCP.check_Wet_LCP(self, element, time)
                check_Wet_CLC.check_Wet_CLC(self, element, time)
                check_Wet_FCP.check_Wet_FCP(self, element, time)
                check_Wet_HCP.check_Wet_HCP(self, element, time)

                # ----------------------------------
                # Set pond/lake ice thickness depth
                # ----------------------------------
                ice_thickness.ice_thickness(self, time, element)
                # ------------------------------
                # Cycle through ponds and lakes
                # ------------------------------
                check_Ponds.check_Ponds(self, element, time, growth_time_required = 3)
                check_Lakes.check_Lakes(self, element, time)
                
                
                # -------------------------------------------------
                # Cohort Fraction Check (mass balance of cohorts)
                # -------------------------------------------------
                cohort_check.cohort_check(self, element, time, cohort_start)

                if time == stop-1:
                    cohorts.final(self)
                    
            # ========================================================================
            # END MAIN LOOP 
            # ========================================================================
            
            # ========================================================================
            # OUTPUT RESULTS
            # ========================================================================

            #  - - - - - - - - -
            # Fractional Areas
            #  - - - - - - - - -
            Output_cohorts_by_year.Output_cohorts_by_year(self, time, Wet_NPG = 'TRUE', Wet_LCP = 'TRUE',
                                                          Wet_CLC = 'TRUE', Wet_FCP = 'TRUE', Wet_HCP = 'TRUE',
                                                          Gra_NPG = 'FALSE', Gra_LCP = 'FALSE', Gra_FCP = 'FALSE',
                                                          Gra_HCP = 'FALSE', Shr_NPG = 'FALSE', Shr_LCP = 'FALSE',
                                                          Shr_FCP = 'FALSE', Shr_HCP = 'FALSE', Ponds = 'TRUE',
                                                          Lakes = 'TRUE')

            #  - - - - - - - - - - - - -
            # Dominant Fractional Area
            #  - - - - - - - - - - - - - 
            Output_cohorts_by_year.dominant_cohort(self, FIGURE = 'TRUE')
            Output_cohorts_by_year.dominant_fractional_plot(self, time, FIGURE = 'TRUE')
                                                        

        # ===================
        # OUTPUT ANIMATIONS
        # ===================

        # - - - - - - - - - - - - - - -
        # Fractional Area of Cohorts
        # - - - - - - - - - - - - - - - -
        Output_cohorts_by_year.write_Fractions_avi(self, Wet_NPG = 'TRUE', Wet_LCP = 'TRUE', Wet_CLC = 'TRUE',
                                                   Wet_FCP = 'TRUE', Wet_HCP = 'TRUE', Gra_NPG = 'FALSE',
                                                   Gra_LCP = 'FALSE', Gra_FCP = 'FALSE', Gra_HCP = 'FALSE',
                                                   Shr_NPG = 'FALSE', Shr_LCP = 'FALSE', Shr_FCP = 'FALSE',
                                                   Shr_HCP = 'FALSE', Ponds = 'TRUE', Lakes = 'TRUE')

        Output_cohorts_by_year.write_Dominant_Cohort_avi(self, MOVIE = 'TRUE')

        # -------------------
        # Simulation End Time
        # -------------------
        clock.finish(self)
        
        #===========================
        # Output Simulation Results
        #===========================
        results.on_screen(self)
        if self.archive_simulation.lower() == 'yes':
            results.on_file(self)

        
        # ================
        # Archive Results
        # ================
        if self.archive_simulation.lower() == 'yes':
        #----------------------------------------------------------------------------------------------------------
        # Create the tarfile
        #----------------------------------------------------------------------------------------------------------
            self.archive_file =tarfile.open(self.control['Run_dir']+self.Output_directory+str('/Archive/')+ \
                                            self.archive_time+str('_')+self.simulation_name+".tar.gz", mode='w:gz')
        #----------------------------------------------------------------------------------------------------------
            archive.read_archive(self)
            archive.archive(self)
            

        print '\nSimulation Complete.\n'
        
        
#_______________________________________________________________________________
Variable = ATTM()
