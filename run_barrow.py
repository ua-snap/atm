#! /usr/bin/env python

"""
The purpose of this script is to self-contain all
of the initialization processes for the Barrow
Peninsula simulations in order to keep the ATM
code clean.
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
def initialize_barrow(self):
    initial_cohort_population.barrow_initial_cohort_population(self)
    initial_cohort_check.barrow_initial_cohort_check(self)
    cohort_present.barrow_cohort_present(self)
#---------------------------------------------------------------------
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
#---------------------------------------------------------------------
def run_barrow(self, time):
    for time in range(0, self.stop):
        if time == 0:
            cohorts.initial_barrow(self)
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

            if time == self.stop -1:
                cohorts.final_barrow(self)

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
#---------------------------------------------------------------------
