import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
import lake_pond_expansion

def check_water_climate(self, check_climate, i):
    """
    The purpose of this module is to determine whether or not
    a water body (lake or pond) exists in an element during
    a major climatic event.

    If a water exists in the element, the elements will undergo
    expansion and drainage.  Expansion will continue at the
    assigned rate (set by lake-pond expansion rate - currently
    this is 0.005 (15 Oct).

    Drainage will occur at different rates depending upon the
    fractional area of the water bodies.  Loosely based upon
    Ben Jones et al paper.

    If Lakes + Ponds is between 0.001 to .01, 25.5% area will be
    drained and 8.5% will be partially drained.

    If Lakes + Ponds is between 0.01 and 0.1, 17.1% area will be
    completely drained and 5.7% will be partially drained.

    If Lakes + Ponds is between 0.1 and 0.4, 60% of area will be
    completely drained and 20% will be partialy drained.

    If Lakes + Ponds is between 0.1 and less than 1.0, 100%.

    If Lakes + Ponds = 1.0, no drainage or expansion will occur.

    Partial drainage will occur in the element at a randomly
    defined rate between 0 and the drain rate assigned.
    """

    # ---------------------------------------------
    # Check element for water and expand and drain 
    # ---------------------------------------------
    if self.ATTM_Ponds[i] + self.ATTM_Lakes[i] > 0.0:
        # ------------------------
        # Set the Drainage Rates
        # ------------------------
        if self.ATTM_Ponds[i] + self.ATTM_Lakes[i] <= 0.01:
            drain_rate = 0.085
            partial_rate = random.uniform(0, drain_rate)
        if self.ATTM_Ponds[i] + self.ATTM_Lakes[i] > 0.01 and \
           self.ATTM_Ponds[i] + self.ATTM_Lakes[i] <= 0.1 :
            drain_rate = 0.057
            partial_rate = random.uniform(0, drain_rate)
        if self.ATTM_Ponds[i] + self.ATTM_Lakes[i] > 0.1 and \
           self.ATTM_Ponds[i] + self.ATTM_Lakes[i] <= 0.4 :
            drain_rate = 0.2
            partial_rate = random.uniform(0, drain_rate)
        if self.ATTM_Ponds[i] + self.ATTM_Lakes[i] > 0.4 and \
           self.ATTM_Ponds[i] + self.ATTM_Lakes[i] < 1.0 :
            drain_rate = 0.2
            partial_rate = random.uniform(0, drain_rate) 
        if self.ATTM_Ponds[i] + self.ATTM_Lakes[i] == 1.0 :
            drain_rate = 0.0
            partial_rate = 0.0
        
        # Expansion of lakes and ponds by expansion rate
        lake_pond_expansion.lake_pond_expansion(self, i)

        # Complete Drainage of Pond/Lake & Increase Meadows at prescribed rate 
        if self.ATTM_Ponds[i] > 0.0 and self.ATTM_Ponds[i] < 1.0:
            self.ATTM_Ponds[i] = self.ATTM_Ponds[i] - self.ATTM_Ponds[i]*drain_rate
            self.ATTM_Wet_NPG[i] = self.ATTM_Wet_NPG[i] + self.ATTM_Ponds[i]*drain_rate
        if self.ATTM_Lakes[i] > 0.0 and self.ATTM_Lakes[i] < 1.0:    
            self.ATTM_Lakes[i] = self.ATTM_Lakes[i] - self.ATTM_Lakes[i]*drain_rate
            self.ATTM_Wet_NPG[i] = self.ATTM_Wet_NPG[i] + self.ATTM_Lakes[i]*drain_rate

        # Complete Partial Drainage of Pond/Lake & Increase Meadows at prescribed rate 
        if self.ATTM_Ponds[i] > 0.0 and self.ATTM_Ponds[i] < 1.0:
            self.ATTM_Ponds[i] = self.ATTM_Ponds[i] - self.ATTM_Ponds[i]*partial_rate
            self.ATTM_Wet_NPG[i] = self.ATTM_Wet_NPG[i] + self.ATTM_Ponds[i]*partial_rate
        if self.ATTM_Lakes[i] > 0.0 and self.ATTM_Lakes[i] < 1.0:    
            self.ATTM_Lakes[i] = self.ATTM_Lakes[i] - self.ATTM_Lakes[i]*partial_rate
            self.ATTM_Wet_NPG[i] = self.ATTM_Wet_NPG[i] + self.ATTM_Lakes[i]*partial_rate
        

