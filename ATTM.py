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
import initialize
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
        initialize.initialize(self)
        read_layers.read_layers(self)
        model_domain.model_domain(self)
        create_attm_cohort_arrays.create_attm_cohort_arrays(self)
        if self.Simulation_area.lower() == 'barrow':
            initial_cohort_population.barrow_initial_cohort_population(self)
            initial_cohort_check.barrow_initial_cohort_check(self)
            cohort_present.barrow_cohort_present(self)
        elif self.Simulation_area.lower() == 'tanana':
            initial_cohort_population.tanana_initial_cohort_population(self)
            initial_cohort_check.tanana_initial_cohort_check(self)
            cohort_present.tanana_cohort_present(self)

         
        #=======================================
        # READ MET Data & Calculate Degree Days
        #=======================================
        initialize.Met(self)


        #++++++++++++++++++++++++++++++++++++++++++++++
        #  ========================================
        #    INITIALIZE BARROW COHORT PROPERTIES
        #  ========================================
        #++++++++++++++++++++++++++++++++++++++++++++++
        if self.Simulation_area.lower() == 'barrow':
            print '=================================== '
            print ' Initializing Lake & Pond Properties'
            print '===================================='
            initialize.LakePond(self)
            set_lake_pond_depth.set_lake_pond_depth(self)
            set_lake_ice_depth_constant.set_lake_ice_depth_constant(self)
            set_ice_thickness_array.set_ice_thickness_array(self)
            climate_expansion_arrays.set_climate_expansion_arrays(self)
            set_pond_growth_array.set_pond_growth_array(self)

            print '====================================='
            print ' Initializing Terrestrial Properties'
            print '====================================='
            initialize.Terrestrial_Barrow(self)
            read_ice_content.read_ice_content(self)
            read_drainage_efficiency.read_drainage_efficiency(self)
            read_initial_ALD.read_initial_ALD(self)
            set_ALD_constant.set_ALD_constant(self)
            set_ALD_array.set_ALD_array(self)
            set_protective_layer.set_protective_layer(self)
            set_initial_cumulative_probability.set_initial_cumulative_probability(self)
            # Initializing Terrestrial Cohort Properties 
            initialize.Wet_NPG(self)
            initialize.Wet_LCP(self)
            initialize.Wet_CLC(self)
            initialize.Wet_FCP(self)
            initialize.Wet_HCP(self)
            # Other needed information [in the future]
            initial_cohort_age.initial_cohort_age(self)

        elif self.Simulation_area.lower() == 'tanana':
            print '======================================'
            print ' Initializing Terrestrial Properties '
            print '======================================'
            initialize.Terrestrial_Tanana(self)


        print '=================================================='
        print '            Starting the MAIN LOOP '
        print '=================================================='

        initialize.run(self)
        for time in range(0, self.stop):
            if time == 0:
                if self.Simulation_area.lower() == 'barrow':
                    cohorts.initial_barrow(self)
                elif self.Simulation_area.lower() == 'tanana':
                    cohorts.initial_tanana(self)
            print '    at time step: ', time
            
            # ++++++++++++++++++++++++++++++++++++++
            # Check for significant climatic event
            # ++++++++++++++++++++++++++++++++++++++
            check_climate_event.check_climate_event(self)            
           
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
                # Expand/Infill lake & ponds by prescribed rates
                # ----------------------------------------------------
                lake_pond_expansion.lake_pond_expansion(self, element)
                lake_pond_expansion.pond_infill(self, element, time)
                
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
                check_Ponds.check_Ponds(self, element, time)
                check_Lakes.check_Lakes(self, element, time)
                 
                # -------------------------------------------------
                # Cohort Fraction Check (mass balance of cohorts)
                # -------------------------------------------------
                cohort_check.cohort_check(self, element, time, cohort_start)

                if time == self.stop-1:
                    if self.Simulation_area.lower() == 'barrow':
                        cohorts.final_barrow(self)
                    elif self.Simulation_area.lower() == 'tanana':
                        cohorts.final_tanana(self)
                    
            # ========================================================================
            # END MAIN LOOP 
            # ========================================================================
            
            # ========================================================================
            # OUTPUT RESULTS (if requested)
            # ========================================================================
            #  - - - - - - - - -
            # Fractional Areas
            #  - - - - - - - - -
            Output_cohorts_by_year.Output_cohorts_by_year(self, time)
            #  - - - - - - - - - - - - -
            # Dominant Fractional Area
            #  - - - - - - - - - - - - - 
            Output_cohorts_by_year.dominant_cohort(self)                 # Terrestrial_Control
            Output_cohorts_by_year.dominant_fractional_plot(self, time)  # Terrestrial_Control

        # =================================
        # OUTPUT ANIMATIONS (if requested)
        # =================================
        # - - - - - - - - - - - - - - -
        # Fractional Area of Cohorts
        # - - - - - - - - - - - - - - - -
        Output_cohorts_by_year.write_Fractions_avi(self)
        Output_cohorts_by_year.write_Dominant_Cohort_avi(self) # Terrestrial_Control

        # -------------------
        # Simulation End Time
        # -------------------
        clock.finish(self)
        
        #===========================
        # Output Simulation Results
        #===========================
        if self.results_onscreen.lower() == 'yes':
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
            
        print '----------------------------------------'
        print '        Simulation Complete             '
        print '----------------------------------------'        
        
#_______________________________________________________________________________
Variable = ATTM()
