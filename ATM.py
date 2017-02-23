 #!/usr/bin/env python

"""
________________________________________________________________________________
Alaska Thermokarst Model (ATM)
________________________________________________________________________________
The purpose of this script is to provide a protype source
code for testing and development of the Alaska Thermokarst
Model (ATM) to be integrated into the Alaska Integrated
Ecosystem Model (AIEM).
________________________________________________________________________________
Created: May 2014. Bob Bolton
Modified: October 2015. Bob Bolton.
          Incorporating Tanana Flats Frames & Logic

________________________________________________________________________________

The ATM code is python based and is executed with the following command:
$ python ATM.py <control file name>

The control file is used to set up the simulation input/output locations,
defines the model domain, etc.
________________________________________________________________________________

"""

################################################################################
# Authorship
################################################################################
__author__     = "Bob Bolton"
__copyright__  = "Copyright 2014, 2015, 2016, 2017, Bob Bolton"
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
import faulthandler


# Import ATM Modules
import clock
import read_control
import read_met_data
import read_degree_days
import calc_degree_days
import read_layers
import model_domain
import create_attm_cohort_arrays
import run_barrow
import run_tanana
import run_yukon
import initialize

import Output_cohorts_by_year
import results
import archive
#_______________________________________________________________________________
class ATM(object):

    Control_file        = sys.argv[1]
 
    def __init__(self):
        # ----------------------
        # Simulation Start Time
        # ----------------------
        faulthandler.enable()
        clock.start(self)
        
        #--------------------------------------
        # Read the Control File for Simulation
        #--------------------------------------
        self.Control_file     = sys.argv[1]
        
        ########################################################################
        # Execute the script
        ########################################################################
        self.run_atm()
#_______________________________________________________________________________
    def run_atm(self):
        
        """ Program sequence """
        #====================================================
        # Initialization Process
        #====================================================
        print '==================='
        print ' Initializing ATM'
        print '==================='
        read_control.read_control(self)
        initialize.initialize(self)
        read_layers.read_layers(self)
        model_domain.model_domain(self)
        create_attm_cohort_arrays.create_attm_cohort_arrays(self)


        #=========================================
        # Initializing Site Specific Information
        #=========================================
        if self.Simulation_area.lower() == 'barrow':
            run_barrow.initialize_barrow(self)
        elif self.Simulation_area.lower() == 'tanana':
            run_tanana.initialize_tanana(self)
        elif self.Simulation_area.lower() == 'yukon':
            run_yukon.initialize_yukon(self)
         
        #=======================================
        # READ MET Data, Calculate Degree Days,
        # and Calculate Climatic Data needed
        # for ecotype changes.
        #=======================================
        initialize.Met(self)

        #++++++++++++++++++++++++++++++++++++++++++++++
        #  ========================================
        #    INITIALIZE COHORT PROPERTIES
        #  ========================================
        #++++++++++++++++++++++++++++++++++++++++++++++
    	print '======================================'
        print ' Initializing Terrestrial Properties '
        print '======================================'
        if self.Simulation_area.lower() == 'barrow':
            run_barrow.initialize_barrow_cohorts(self)
        elif self.Simulation_area.lower() == 'tanana':
            run_tanana.Terrestrial_Tanana(self)

        print '=================================================='
        print '            Starting the MAIN LOOP '
        print '=================================================='

        initialize.run(self)
        if self.Simulation_area.lower() == 'barrow':
            run_barrow.run_barrow(self, time)
        elif self.Simulation_area.lower() == 'tanana':
            run_tanana.run_tanana(self, time)

        print '=================================================='
        print '            Finished the MAIN LOOP '
        print '=================================================='


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
            archive.read_archive(self)
            archive.archive(self)
        #----------------------------------------------------------------------------------------------------------
        # Create the tarfile
        #----------------------------------------------------------------------------------------------------------
            self.archive_file =tarfile.open(self.control['Run_dir']+self.Output_directory+str('/Archive/')+ \
                                            self.archive_time+str('_')+self.simulation_name+".tar.gz", mode='w:gz')
        #----------------------------------------------------------------------------------------------------------
            if self.Simulation_area.lower() == 'barrow':
                os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/')
                

            
        print '----------------------------------------'
        print '        Simulation Complete             '
        print '----------------------------------------'        
        
#_______________________________________________________________________________
Variable = ATM()
