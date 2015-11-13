#! /usr/bin/env python

"""
The purpose of this script is to self-contain all
of the initialization processes for the Barrow
Peninsula simulations in order to keep the ATM
code clean.
"""

import initial_cohort_population
import initial_cohort_check
import cohort_present
import set_lake_pond_depth
import set_lake_ice_depth_constant
import set_ice_thickness_array
import climate_expansion_arrays
import set_pond_growth_array
import initialize
import read_ice_content
import read_drainage_efficiency
import read_initial_ALD
import set_ALD_constant
import set_ALD_array
import set_protective_layer
import set_initial_cumulative_probability
import initial_cohort_age

def initialize_barrow(self):
    initial_cohort_population.barrow_initial_cohort_population(self)
    initial_cohort_check.barrow_initial_cohort_check(self)
    cohort_present.barrow_cohort_present(self)


def initialize_barrow_cohorts(self):
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
