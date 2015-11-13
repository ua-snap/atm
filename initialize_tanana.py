#! /usr/bin/env python

"""
The purpose of this script is to self-contain all
of the initialization processes for the Tanana
Flats simulations in order to keep the ATM
code clean.
"""

import initial_cohort_population
import initial_cohort_check
import cohort_present

def initialize_tanana(self):
    initial_cohort_population.tanana_initial_cohort_population(self)
    initial_cohort_check.tanana_initial_cohort_check(self)
    cohort_present.tanana_cohort_present(self)


