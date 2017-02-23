#! /usr/bin/env python

"""
The purpose of this script is to self-contain all
of the initialization processes for the Yukon Flats
simulations in order to keep the ATM code clean.
"""
#---------------------------------------------------------------------
import active_layer_depth
import check_climate_event
import check_Lakes
import check_Ponds
import check_Wet_CLC
import check_Wet_FCP
import check_Wet_HCP
import check_Wet_LCP
import check_Wet_NPG
import climate_expansion_arrays
import cohorts
import cohort_check
import cohort_present
import ice_thickness
import initial_cohort_age
import initial_cohort_check
import initial_cohort_population
import initialize
import lake_pond_expansion
import Output_cohorts_by_year
import read_drainage_efficiency
import read_ice_content
import read_initial_ALD
import set_ALD_array
import set_ALD_constant
import set_ice_thickness_array
import set_initial_cumulative_probability
import set_lake_ice_depth_constant
import set_lake_pond_depth
import set_pond_growth_array
import set_protective_layer

#=====================================================================
def initialize_yukon(self):
    initial_cohort_population.yukon_initial_cohort_population(self)
    initial_cohort_check.yukon_initial_cohort_check(self)
    cohort_present.yukon_cohort_present(self)
