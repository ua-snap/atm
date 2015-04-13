import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
from math import exp as exp

"""
The purpose of this module is to check the status of the ponds.
Ponds are defined as shallow lakes, or lakes that are shallower
than the ice thickness.  Once the pond becomes deeper than
the ice thickness (either through climate change (thinner ice)
or thermokarst (deepening of the pond)), then the Pond becomes
a lake (or a deep lake).

In this module, I am assuming that Ponds can only deepen if
the Total Degree Days is the current (up to that time) maximum.
If the TDDs are less than the maximum, the pond depth remains
the same.
"""

def check_Ponds(self, element, time):#, growth_time_required):

    # --------------------------------------
    # Check to see if the Total Degree Days
    # are at the current maximum.
    #
    # If yes, set new TDD max and increase
    # the pond count.
    # --------------------------------------
#    if element == 0:
    if self.Met['met_distribution'].lower() == 'point':
        if time == 0:
            self.TDD_max = self.degree_days[0,1]
        else:
            if self.degree_days[time,1] > self.TDD_max:
                # Set new TDD_max
                self.TDD_max = self.degree_days[time,1]
                # Increase the pond count
                self.pond_count = self.pond_count + 1
    else:
        if time == 0:
            self.TDD_max = self.TDD[0,:]
        else:
            for i in range(0,self.ATTM_nrows * self.ATTM_ncols):
                if self.TDD[time, i] > self.TDD_max[i]:
                    # Set new TDD_max
                    self.TDD_max[i] = self.TDD[time,i]
                    # Increase the pond count
                    self.pond_count = self.pond_count + 1
                        
    # ----------------------------------
    # Check to see if ponds are present
    # ----------------------------------
    if self.ATTM_Ponds[element] > 0.0:
        # --------------------------------------
        # Check to see if the Total Degree Days
        # are at the current maximum.
        # --------------------------------------
        if self.Met['met_distribution'].lower() == 'point':
            if self.degree_days[time,1] == self.TDD_max:
                # Increase the depth of the pond by sqrt[pond_count]
                self.Pond_Depth[element] = self.Pond_Depth[element] + np.sqrt(self.pond_count)/ \
                  self.LakePond['pond_depth_control']
                # Check if pond depth >= ice thickness
                if self.Pond_Depth[element] >= self.ice_thickness[element]:
                    # Check if Pond Growth has been sustained over time
                    if self.pond_growth[element] >= self.LakePond['growth_time_required']:
                        # Transition Ponds -> Lakes
                        self.ATTM_Lakes[element] = self.ATTM_Lakes[element] + self.ATTM_Ponds[element]
                        # Transition Ponds -> 0.0
                        self.ATTM_Ponds[element] = 0.0
                        # Transition Pond Depth -> 0.0
                        self.Pond_Depth[element] = 0.0
                        # Update pond growth array
                        self.pond_growth[element] = self.pond_growth[element] + 1.
            else:
                # Pond depth remains the same.
                # Check if pond depth >= ice thickness
                if self.Pond_Depth[element] >= self.ice_thickness[element]:
                    if self.pond_growth[element] >= self.LakePond['growth_time_required']:
                        # Transition Ponds -> Lakes
                        self.ATTM_Lakes[element] = self.ATTM_Lakes[element] + self.ATTM_Ponds[element]
                        # Transition Ponds -> 0.0
                        self.ATTM_Ponds[element] = 0.0
                        # Transition Pond Depth -> 0.0
                        self.Pond_Depth[element] = 0.0
                        # Update pond growth array
                        self.pond_growth[element] = self.pond_growth[element] + 1.
                    else:
                        self.ATTM_Ponds[element] = self.ATTM_Ponds[element]
                        self.pond_growth[element] = 0.0
        else:
            if self.TDD[time, element] == self.TDD_max[element]:
                # Increase the depth of the pond by sqrt[pond_count]
                self.Pond_Depth[element] = self.Pond_Depth[element] + np.sqrt(self.pond_count)/ \
                  self.LakePond['pond_depth_control']
                # Check if pond depth >= ice thickness
                if self.Pond_Depth[element] >= self.ice_thickness[element]:
                    # Check if Pond Growth has been sustained over time
                    if self.pond_growth[element] >= self.LakePond['growth_time_required']:
                        # Transition Ponds -> Lakes
                        self.ATTM_Lakes[element] = self.ATTM_Lakes[element] + self.ATTM_Ponds[element]
                        # Transition Ponds -> 0.0
                        self.ATTM_Ponds[element] = 0.0
                        # Transition Pond Depth -> 0.0
                        self.Pond_Depth[element] = 0.0
                        # Update pond growth array
                        self.pond_growth[element] = self.pond_growth[element] + 1.
            else:
                # Pond depth remains the same.
                # Check if pond depth >= ice thickness
                if self.Pond_Depth[element] >= self.ice_thickness[element]:
                    if self.pond_growth[element] >= self.LakePond['growth_time_required']:
                        # Transition Ponds -> Lakes
                        self.ATTM_Lakes[element] = self.ATTM_Lakes[element] + self.ATTM_Ponds[element]
                        # Transition Ponds -> 0.0
                        self.ATTM_Ponds[element] = 0.0
                        # Transition Pond Depth -> 0.0
                        self.Pond_Depth[element] = 0.0
                        # Update pond growth array
                        self.pond_growth[element] = self.pond_growth[element] + 1.
                    else:
                        self.ATTM_Ponds[element] = self.ATTM_Ponds[element]
                        self.pond_growth[element] = 0.0



            
