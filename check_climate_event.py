import numpy as np
import gdal, os, sys, glob, random
import pylab as pl

def check_climate_event(self):#, climate_blocks, climate_event_probability):
    """
    The purpose of this module is to check if a major/significant
    climatic event took place over the year. If a climatic event
    occurs and a lake/pond (or both) cohort exists - a portion
    of the water body will expand or drain.  The mechanism for
    determining whether or not the water body will expand or
    drain is yet to be determined.

    At this point, a random function will be used to determine
    if a climate event happens. I will set this at 1.3% chance of
    happening (~ 1/75 years).

    ################################################################3
    Update: 20 Ocotober 2014:
    After talking with Vladimir last week (Friday), we decided to
    create 'blocks' of influece for the climate event to happen.
    Before, if a climate event happened, the entire model domain
    was influenced.

    Each block (block = X) is the one side of a square consisting
    of 2 * X model elements. For example, block = 10 indicates that
    the storm influence will be 10 km^2.
    #################################################################

    If a water exists in the element, the elements will undergo
    expansion and drainage.  Expansion will continue at the
    assigned rate (set by lake-pond expansion rate - currently
    this is 0.005 (15 Oct).

    Drainage will occur at different rates depending upon the
    fractional area of the water bodies.  Loosely based upon
    Ben Jones et al paper.

    If Lakes + Ponds is between 0.001 to .01, the drainage
    rate is 8.5%.

    If Lakes + Ponds is between 0.01 and 0.1, the draingage
    rate is 5.75

    If Lakes + Ponds is between 0.1 and 0.4, the drainage
    rate is 20%

    If Lakes + Ponds is between 0.1 and less than 1.0, the
    drainage rate is 20.0%.

    If Lakes + Ponds = 1.0, no drainage or expansion will occur.

    Partial drainage will occur in the element at a randomly
    defined rate between 0 and the drain rate assigned.
    
    """

    # Step 0: Set the size of the climate blocks
    if self.Met['climate_blocks'].lower() == 'random':
        climate_blocks = \
          random.randint(self.Met['climate_block_lower_bound'], self.Met['climate_block_upper_bound'])           
    else:
        climate_blocks = int(self.Met['climate_blocks'])
        
    # Step 1: Reshape Lakes and Ponds to 'regular model domain'
    self.ATTM_Lakes = np.reshape(self.ATTM_Lakes, [self.ATTM_nrows, self.ATTM_ncols])
    self.ATTM_Ponds = np.reshape(self.ATTM_Ponds, [self.ATTM_nrows, self.ATTM_ncols])

    # Step 2: Reshape Wetland NPG to 'regular model domain'
    self.ATTM_Wet_NPG = np.reshape(self.ATTM_Wet_NPG, [self.ATTM_nrows, self.ATTM_ncols])

    # Step 3: Reshape Expansion Arrays
    self.climate_expansion_lakes = np.reshape(self.climate_expansion_lakes,([self.ATTM_nrows, self.ATTM_ncols]))
    self.climate_expansion_ponds = np.reshape(self.climate_expansion_ponds,([self.ATTM_nrows, self.ATTM_ncols]))

    # Step 4: Loop over blocks and check for extreme events
    climate_count = 0
    for j in range(0, self.ATTM_ncols, climate_blocks):
        for k in range(0, self.ATTM_nrows, climate_blocks):
            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # Set the climate event probability of occuring in each block
            # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            climate_event = random.uniform(0.0, 1.0)
            
            if climate_event <= self.Met['climate_event_probability']:  # A climate event happens
                print 'Climate Event in Block: ', climate_count
                print '... Checking for Lakes and Ponds...'

                # Define sub-domain (the block) for all water and terrestrial cohorts
                Lakes   = self.ATTM_Lakes[k:k+climate_blocks, j:j+climate_blocks]
                Ponds   = self.ATTM_Ponds[k:k+climate_blocks, j:j+climate_blocks]
                #-------------------------------------------------------------------------------------
                Wet_NPG = self.ATTM_Wet_NPG[k:k+climate_blocks, j:j+climate_blocks]
                #----------------------------------------------------------------------------------------------
                climate_expansion_lakes = self.climate_expansion_lakes[k:k+climate_blocks, j:j+climate_blocks]
                climate_expansion_ponds = self.climate_expansion_ponds[k:k+climate_blocks, j:j+climate_blocks]
                #----------------------------------------------------------------------------------------------
                row_dim = np.shape(Lakes)[0]
                col_dim = np.shape(Lakes)[1]
                # ====================================================================================================
                # Step X : Flatten all arrays
                # - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                Lakes = np.reshape(Lakes, [np.shape(Lakes)[0] * np.shape(Lakes)[1]])
                Ponds = np.reshape(Ponds, [np.shape(Ponds)[0] * np.shape(Ponds)[1]])
                Wet_NPG = np.reshape(Wet_NPG, [np.shape(Wet_NPG)[0] * np.shape(Wet_NPG)[1]])
                climate_expansion_lakes = np.reshape(climate_expansion_lakes, np.shape(climate_expansion_lakes)[0] *\
                                                     np.shape(climate_expansion_lakes)[1])
                climate_expansion_ponds = np.reshape(climate_expansion_ponds, np.shape(climate_expansion_ponds)[0] *\
                                                     np.shape(climate_expansion_ponds)[1])
                # ====================================================================================================
                
                # -----------------------------------
                # Step 4 : Drain the Lakes and Ponds
                # -----------------------------------
                for i in range(0, np.size(Lakes)):
                    ####################
                    # Pond Drain Rates #
                    ####################
                    if Ponds[i] == 0.0 :
                        pond_drain_rate = 0.0
                        pond_partial_rate = 0.0
                    if Ponds[i] > 0.0 and Ponds[i] <= 0.01:
                        pond_drain_rate = self.Met['pond_drain_rate_<0.01']
                        pond_partial_rate = random.uniform(0., pond_drain_rate)
                    if Ponds[i] > 0.01 and Ponds[i] <= 0.1 :
                        pond_drain_rate = self.Met['pond_drain_rate_0.01<0.1']
                        pond_partial_rate = random.uniform(0., pond_drain_rate)
                    if Ponds[i] > 0.1 and Ponds[i] <= 0.4 :
                        pond_drain_rate = self.Met['pond_drain_rate_0.1<0.4']
                        pond_partial_rate = random.uniform(0., pond_drain_rate)
                    if Ponds[i] > 0.4 and Ponds[i] < 1.0 :
                        pond_drain_rate = self.Met['pond_drain_rate_0.4<1.0']
                        pond_partial_rate = random.uniform(0., pond_drain_rate)
                    if Ponds[i] == 1.0:
                        pond_drain_rate = 0.0
                        pond_partial_rate = 0.0
                    ####################
                    # Lake Drain Rates #
                    ####################
                    if Lakes[i] == 0.0 :
                        lake_drain_rate = 0.0
                        lake_partial_rate = 0.0
                    if Lakes[i] > 0.0 and Lakes[i] <= 0.01:
                        lake_drain_rate = self.Met['lake_drain_rate_<0.01']
                        lake_partial_rate = random.uniform(0., lake_drain_rate)
                    if Lakes[i] > 0.01 and Lakes[i] <= 0.1 :
                        lake_drain_rate = self.Met['lake_drain_rate_0.01<0.1']
                        lake_partial_rate = random.uniform(0., lake_drain_rate)
                    if Lakes[i] > 0.1 and Lakes[i] <= 0.4 :
                        lake_drain_rate = self.Met['lake_drain_rate_0.1<0.4']
                        lake_partial_rate = random.uniform(0., lake_drain_rate)
                    if Lakes[i] > 0.4 and Lakes[i] < 1.0 :
                        lake_drain_rate = self.Met['lake_drain_rate_0.4<1.0']
                        lake_partial_rate = random.uniform(0., lake_drain_rate)
                    if Lakes[i] == 1.0:
                        lake_drain_rate = 0.0
                        lake_partial_rate = 0.0


                    # -----------------------------------------------------------
                    # Step 5: Complete Drainage of Ponds/Lakes @ prescribed Rate
                    # -----------------------------------------------------------
                    if Ponds[i] > 0.0 and Ponds[i] < 1.0:
                        full_pond_change = Ponds[i] * pond_drain_rate
                        partial_pond_change = Ponds[i] * pond_partial_rate
                        Ponds[i] = Ponds[i] - full_pond_change - partial_pond_change
                        Wet_NPG[i] = Wet_NPG[i] + full_pond_change + partial_pond_change

                        # Set expansion flag
                        climate_expansion_ponds[i] = 1.0

                    if Lakes[i] > 0.0 and Lakes[i] < 1.0:
                        full_lake_change = Lakes[i] * lake_drain_rate
                        partial_lake_change = Lakes[i] * lake_partial_rate
                        Lakes[i] = Lakes[i] - full_lake_change - partial_lake_change
                        Wet_NPG[i] = Wet_NPG[i] + full_lake_change + partial_lake_change

                        # Set expansion flag
                        climate_expansion_lakes[i] = 1.0

                #---------------------------------------------------- 
                # Reshape sub-arrays to fit back into model domain
                #----------------------------------------------------
                Lakes = np.reshape(Lakes, [row_dim, col_dim])
                Ponds = np.reshape(Ponds, [row_dim, col_dim])
                Wet_NPG = np.reshape(Wet_NPG, [row_dim, col_dim])
                climate_expansion_lakes = np.reshape(climate_expansion_lakes,[row_dim, col_dim])
                climate_expansion_ponds = np.reshape(climate_expansion_ponds,[row_dim, col_dim])

                # -------------------------------------------------------------------
                # Step 8: Replace block changes back into the model domain
                # -------------------------------------------------------------------
                self.ATTM_Lakes[k:k+climate_blocks, j:j+climate_blocks] = Lakes
                self.ATTM_Ponds[k:k+climate_blocks, j:j+climate_blocks] = Ponds
                self.ATTM_Wet_NPG[k:k+climate_blocks, j:j+climate_blocks] = Wet_NPG

                self.climate_expansion_lakes[k:k+climate_blocks, j:j+climate_blocks] = \
                                                                 climate_expansion_lakes
                self.climate_expansion_ponds[k:k+climate_blocks, j:j+climate_blocks] = \
                                                                 climate_expansion_ponds

            else:
                self.climate_expansion_lakes[k:k+climate_blocks, j:j+climate_blocks] = 0.0
                self.climate_expansion_ponds[k:k+climate_blocks, j:j+climate_blocks] = 0.0
            # --------------------------------------------------------------
            # Step 9 : Increase the climate count to move to the next block
            # --------------------------------------------------------------
            climate_count = climate_count + 1
                
                
    # -----------------------------------------------------------------
    # Reshape Lakes, Ponds, Wet_NPG and expansion arrays into 1D array
    # -----------------------------------------------------------------
    self.ATTM_Lakes = np.reshape(self.ATTM_Lakes, [self.ATTM_nrows * self.ATTM_ncols])
    self.ATTM_Ponds = np.reshape(self.ATTM_Ponds, [self.ATTM_nrows * self.ATTM_ncols])
    self.ATTM_Wet_NPG = np.reshape(self.ATTM_Wet_NPG, [self.ATTM_nrows * self.ATTM_ncols])
    self.climate_expansion_lakes = np.reshape(self.climate_expansion_lakes, [self.ATTM_nrows * self.ATTM_ncols])
    self.climate_expansion_ponds = np.reshape(self.climate_expansion_lakes, [self.ATTM_nrows * self.ATTM_ncols])


           
    
    
