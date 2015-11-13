#==================================================================================
def Wet_NPG(self):

    print '..Reading Wetland Tundra Non-Polygonal Ground Parameters'

    self.WetNPG = {}
    with open(self.Wet_NPG_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.WetNPG[(key)] = val

    # Convert strings to floats as necessary
    self.WetNPG['A1_above']    = float(self.WetNPG['A1_above'])
    self.WetNPG['A2_above']    = float(self.WetNPG['A2_above'])
    self.WetNPG['x0_above']    = float(self.WetNPG['x0_above'])
    self.WetNPG['dx_above']    = float(self.WetNPG['dx_above'])
    self.WetNPG['A1_below']    = float(self.WetNPG['A1_below'])
    self.WetNPG['A2_below']    = float(self.WetNPG['A2_below'])
    self.WetNPG['x0_below']    = float(self.WetNPG['x0_below'])
    self.WetNPG['dx_below']    = float(self.WetNPG['dx_below'])
    self.WetNPG['a_above']     = float(self.WetNPG['a_above'])
    self.WetNPG['b_above']     = float(self.WetNPG['b_above'])
    self.WetNPG['a_below']     = float(self.WetNPG['a_below'])
    self.WetNPG['b_below']     = float(self.WetNPG['b_below'])
    self.WetNPG['K_above']     = float(self.WetNPG['K_above'])
    self.WetNPG['C_above']     = float(self.WetNPG['C_above'])
    self.WetNPG['A_above']     = float(self.WetNPG['A_above'])
    self.WetNPG['B_above']     = float(self.WetNPG['B_above'])
    self.WetNPG['K_below']     = float(self.WetNPG['K_below'])
    self.WetNPG['C_below']     = float(self.WetNPG['C_below'])
    self.WetNPG['A_below']     = float(self.WetNPG['A_below'])
    self.WetNPG['B_below']     = float(self.WetNPG['B_below'])
    self.WetNPG['HillB_above'] = float(self.WetNPG['HillB_above'])
    self.WetNPG['HillN_above'] = float(self.WetNPG['HillN_above'])
    self.WetNPG['HillB_below'] = float(self.WetNPG['HillB_below'])
    self.WetNPG['HillN_below'] = float(self.WetNPG['HillN_below'])
    self.WetNPG['max_terrain_transition'] = \
      float(self.WetNPG['max_terrain_transition'])
    self.WetNPG['ice_slope_poor']    = float(self.WetNPG['ice_slope_poor'])
    self.WetNPG['ice_slope_pore']    = float(self.WetNPG['ice_slope_pore'])
    self.WetNPG['ice_slope_wedge']   = float(self.WetNPG['ice_slope_wedge'])
    self.WetNPG['ice_slope_massive'] = float(self.WetNPG['ice_slope_massive'])
    self.WetNPG['porosity'] = float(self.WetNPG['porosity'])
#================================================================================
def Wet_LCP(self):

    print '..Reading Wetland Low Center Polygon Cohort Parameters'

    self.WetLCP = {}
    with open(self.Wet_LCP_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.WetLCP[(key)] = val

    # Convert strings to floats as necessary
    self.WetLCP['A1_above']    = float(self.WetLCP['A1_above'])
    self.WetLCP['A2_above']    = float(self.WetLCP['A2_above'])
    self.WetLCP['x0_above']    = float(self.WetLCP['x0_above'])
    self.WetLCP['dx_above']    = float(self.WetLCP['dx_above'])
    self.WetLCP['A1_below']    = float(self.WetLCP['A1_below'])
    self.WetLCP['A2_below']    = float(self.WetLCP['A2_below'])
    self.WetLCP['x0_below']    = float(self.WetLCP['x0_below'])
    self.WetLCP['dx_below']    = float(self.WetLCP['dx_below'])
    self.WetLCP['a_above']     = float(self.WetLCP['a_above'])
    self.WetLCP['b_above']     = float(self.WetLCP['b_above'])
    self.WetLCP['a_below']     = float(self.WetLCP['a_below'])
    self.WetLCP['b_below']     = float(self.WetLCP['b_below'])
    self.WetLCP['K_above']     = float(self.WetLCP['K_above'])
    self.WetLCP['C_above']     = float(self.WetLCP['C_above'])
    self.WetLCP['A_above']     = float(self.WetLCP['A_above'])
    self.WetLCP['B_above']     = float(self.WetLCP['B_above'])
    self.WetLCP['K_below']     = float(self.WetLCP['K_below'])
    self.WetLCP['C_below']     = float(self.WetLCP['C_below'])
    self.WetLCP['A_below']     = float(self.WetLCP['A_below'])
    self.WetLCP['B_below']     = float(self.WetLCP['B_below'])
    self.WetLCP['HillB_above'] = float(self.WetLCP['HillB_above'])
    self.WetLCP['HillN_above'] = float(self.WetLCP['HillN_above'])
    self.WetLCP['HillB_below'] = float(self.WetLCP['HillB_below'])
    self.WetLCP['HillN_below'] = float(self.WetLCP['HillN_below'])
    self.WetLCP['max_terrain_transition'] = \
      float(self.WetNPG['max_terrain_transition'])
    self.WetLCP['ice_slope_poor']    = float(self.WetLCP['ice_slope_poor'])
    self.WetLCP['ice_slope_pore']    = float(self.WetLCP['ice_slope_pore'])
    self.WetLCP['ice_slope_wedge']   = float(self.WetLCP['ice_slope_wedge'])
    self.WetLCP['ice_slope_massive'] = float(self.WetLCP['ice_slope_massive'])
    self.WetLCP['porosity'] = float(self.WetLCP['porosity'])
#===============================================================================
def Wet_CLC(self):

    print '..Reading Wetland Coalescent Low Center Polygon Cohort Parameters'

    self.WetCLC = {}
    with open(self.Wet_CLC_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.WetCLC[(key)] = val

    # Convert strings to floats as necessary
    self.WetCLC['A1_above']    = float(self.WetCLC['A1_above'])
    self.WetCLC['A2_above']    = float(self.WetCLC['A2_above'])
    self.WetCLC['x0_above']    = float(self.WetCLC['x0_above'])
    self.WetCLC['dx_above']    = float(self.WetCLC['dx_above'])
    self.WetCLC['A1_below']    = float(self.WetCLC['A1_below'])
    self.WetCLC['A2_below']    = float(self.WetCLC['A2_below'])
    self.WetCLC['x0_below']    = float(self.WetCLC['x0_below'])
    self.WetCLC['dx_below']    = float(self.WetCLC['dx_below'])
    self.WetCLC['a_above']     = float(self.WetCLC['a_above'])
    self.WetCLC['b_above']     = float(self.WetCLC['b_above'])
    self.WetCLC['a_below']     = float(self.WetCLC['a_below'])
    self.WetCLC['b_below']     = float(self.WetCLC['b_below'])
    self.WetCLC['K_above']     = float(self.WetCLC['K_above'])
    self.WetCLC['C_above']     = float(self.WetCLC['C_above'])
    self.WetCLC['A_above']     = float(self.WetCLC['A_above'])
    self.WetCLC['B_above']     = float(self.WetCLC['B_above'])
    self.WetCLC['K_below']     = float(self.WetCLC['K_below'])
    self.WetCLC['C_below']     = float(self.WetCLC['C_below'])
    self.WetCLC['A_below']     = float(self.WetCLC['A_below'])
    self.WetCLC['B_below']     = float(self.WetCLC['B_below'])
    self.WetCLC['HillB_above'] = float(self.WetCLC['HillB_above'])
    self.WetCLC['HillN_above'] = float(self.WetCLC['HillN_above'])
    self.WetCLC['HillB_below'] = float(self.WetCLC['HillB_below'])
    self.WetCLC['HillN_below'] = float(self.WetCLC['HillN_below'])
    self.WetCLC['max_terrain_transition'] = \
      float(self.WetCLC['max_terrain_transition'])
    self.WetCLC['ice_slope_poor']    = float(self.WetCLC['ice_slope_poor'])
    self.WetCLC['ice_slope_pore']    = float(self.WetCLC['ice_slope_pore'])
    self.WetCLC['ice_slope_wedge']   = float(self.WetCLC['ice_slope_wedge'])
    self.WetCLC['ice_slope_massive'] = float(self.WetCLC['ice_slope_massive'])
    self.WetCLC['porosity'] = float(self.WetCLC['porosity'])
#=================================================================================
def Wet_FCP(self):

    print '..Reading Wetland Flat Center Polygon Cohort Parameters'

    self.WetFCP = {}
    with open(self.Wet_FCP_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.WetFCP[(key)] = val

    # Convert strings to floats as necessary
    self.WetFCP['A1_above']    = float(self.WetFCP['A1_above'])
    self.WetFCP['A2_above']    = float(self.WetFCP['A2_above'])
    self.WetFCP['x0_above']    = float(self.WetFCP['x0_above'])
    self.WetFCP['dx_above']    = float(self.WetFCP['dx_above'])
    self.WetFCP['A1_below']    = float(self.WetFCP['A1_below'])
    self.WetFCP['A2_below']    = float(self.WetFCP['A2_below'])
    self.WetFCP['x0_below']    = float(self.WetFCP['x0_below'])
    self.WetFCP['dx_below']    = float(self.WetFCP['dx_below'])
    self.WetFCP['a_above']     = float(self.WetFCP['a_above'])
    self.WetFCP['b_above']     = float(self.WetFCP['b_above'])
    self.WetFCP['a_below']     = float(self.WetFCP['a_below'])
    self.WetFCP['b_below']     = float(self.WetFCP['b_below'])
    self.WetFCP['K_above']     = float(self.WetFCP['K_above'])
    self.WetFCP['C_above']     = float(self.WetFCP['C_above'])
    self.WetFCP['A_above']     = float(self.WetFCP['A_above'])
    self.WetFCP['B_above']     = float(self.WetFCP['B_above'])
    self.WetFCP['K_below']     = float(self.WetFCP['K_below'])
    self.WetFCP['C_below']     = float(self.WetFCP['C_below'])
    self.WetFCP['A_below']     = float(self.WetFCP['A_below'])
    self.WetFCP['B_below']     = float(self.WetFCP['B_below'])
    self.WetFCP['HillB_above'] = float(self.WetFCP['HillB_above'])
    self.WetFCP['HillN_above'] = float(self.WetFCP['HillN_above'])
    self.WetFCP['HillB_below'] = float(self.WetFCP['HillB_below'])
    self.WetFCP['HillN_below'] = float(self.WetFCP['HillN_below'])
    self.WetFCP['max_terrain_transition'] = \
      float(self.WetFCP['max_terrain_transition'])
    self.WetFCP['ice_slope_poor']    = float(self.WetFCP['ice_slope_poor'])
    self.WetFCP['ice_slope_pore']    = float(self.WetFCP['ice_slope_pore'])
    self.WetFCP['ice_slope_wedge']   = float(self.WetFCP['ice_slope_wedge'])
    self.WetFCP['ice_slope_massive'] = float(self.WetFCP['ice_slope_massive'])
    self.WetFCP['porosity'] = float(self.WetFCP['porosity'])
#===============================================================================
def Wet_HCP(self):

    print '..Reading Wetland Flat Center Polygon Cohort Parameters'

    self.WetHCP = {}
    with open(self.Wet_HCP_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.WetHCP[(key)] = val

    # Convert strings to floats as necessary
    self.WetHCP['A1_above']    = float(self.WetHCP['A1_above'])
    self.WetHCP['A2_above']    = float(self.WetHCP['A2_above'])
    self.WetHCP['x0_above']    = float(self.WetHCP['x0_above'])
    self.WetHCP['dx_above']    = float(self.WetHCP['dx_above'])
    self.WetHCP['A1_below']    = float(self.WetHCP['A1_below'])
    self.WetHCP['A2_below']    = float(self.WetHCP['A2_below'])
    self.WetHCP['x0_below']    = float(self.WetHCP['x0_below'])
    self.WetHCP['dx_below']    = float(self.WetHCP['dx_below'])
    self.WetHCP['a_above']     = float(self.WetHCP['a_above'])
    self.WetHCP['b_above']     = float(self.WetHCP['b_above'])
    self.WetHCP['a_below']     = float(self.WetHCP['a_below'])
    self.WetHCP['b_below']     = float(self.WetHCP['b_below'])
    self.WetHCP['K_above']     = float(self.WetHCP['K_above'])
    self.WetHCP['C_above']     = float(self.WetHCP['C_above'])
    self.WetHCP['A_above']     = float(self.WetHCP['A_above'])
    self.WetHCP['B_above']     = float(self.WetHCP['B_above'])
    self.WetHCP['K_below']     = float(self.WetHCP['K_below'])
    self.WetHCP['C_below']     = float(self.WetHCP['C_below'])
    self.WetHCP['A_below']     = float(self.WetHCP['A_below'])
    self.WetHCP['B_below']     = float(self.WetHCP['B_below'])
    self.WetHCP['HillB_above'] = float(self.WetHCP['HillB_above'])
    self.WetHCP['HillN_above'] = float(self.WetHCP['HillN_above'])
    self.WetHCP['HillB_below'] = float(self.WetHCP['HillB_below'])
    self.WetHCP['max_terrain_transition'] = \
      float(self.WetHCP['max_terrain_transition'])
    self.WetHCP['ice_slope_poor']    = float(self.WetHCP['ice_slope_poor'])
    self.WetHCP['ice_slope_pore']    = float(self.WetHCP['ice_slope_pore'])
    self.WetHCP['ice_slope_wedge']   = float(self.WetHCP['ice_slope_wedge'])
    self.WetHCP['ice_slope_massive'] = float(self.WetHCP['ice_slope_massive'])
    self.WetHCP['porosity']          = float(self.WetHCP['porosity'])
#===============================================================================
def LakePond(self):
    print '..Reading Land and Pond Cohort Parameters'

    self.LakePond = {}
    with open(self.Lake_Pond_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.LakePond[(key)] = val

    # Convert strings to floats as necessary
    self.LakePond['Uniform_Lake_Depth']          = float(self.LakePond['Uniform_Lake_Depth'])
    self.LakePond['Lower_Lake_Depth']            = float(self.LakePond['Lower_Lake_Depth'])
    self.LakePond['Upper_Lake_Depth']            = float(self.LakePond['Upper_Lake_Depth'])
    self.LakePond['Uniform_Pond_Depth']          = float(self.LakePond['Uniform_Pond_Depth'])
    self.LakePond['Lower_Pond_Depth']            = float(self.LakePond['Lower_Pond_Depth'])
    self.LakePond['Upper_Pond_Depth']            = float(self.LakePond['Upper_Pond_Depth'])
    self.LakePond['Lake_Expansion']              = float(self.LakePond['Lake_Expansion'])
    self.LakePond['Pond_Expansion']              = float(self.LakePond['Pond_Expansion'])
    self.LakePond['Pond_Infill_Constant']        = float(self.LakePond['Pond_Infill_Constant'])
    self.LakePond['ice_thickness_uniform_alpha'] = float(self.LakePond['ice_thickness_uniform_alpha'])
    self.LakePond['Lower_ice_thickness_alpha']   = float(self.LakePond['Lower_ice_thickness_alpha'])
    self.LakePond['Upper_ice_thickness_alpha']   = float(self.LakePond['Upper_ice_thickness_alpha'])
    self.LakePond['growth_time_required']        = float(self.LakePond['growth_time_required'])
    self.LakePond['lake_depth_control']          = float(self.LakePond['lake_depth_control'])
    self.LakePond['pond_depth_control']          = float(self.LakePond['pond_depth_control'])
#===============================================================================
def Terrestrial_Barrow(self):
    print '..Reading General Terrestrial Parameters'

    self.Terrestrial = {}
    print self.Terrestrial_Control
    with open(self.Terrestrial_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.Terrestrial[(key)] = val

    # Convert to strings if necessary
    self.Terrestrial['Drainage_Efficiency_Random_Value'] = \
      float(self.Terrestrial['Drainage_Efficiency_Random_Value'])
    self.Terrestrial['ALD_Distribution_Lower_Bound'] = \
      float(self.Terrestrial['ALD_Distribution_Lower_Bound'])
    self.Terrestrial['ALD_Distribution_Upper_Bound'] = \
      float(self.Terrestrial['ALD_Distribution_Upper_Bound'])

    self.Terrestrial['Wet_NPG_PLF'] = float(self.Terrestrial['Wet_NPG_PLF'])
    self.Terrestrial['Wet_LCP_PLF'] = float(self.Terrestrial['Wet_LCP_PLF'])
    self.Terrestrial['Wet_CLC_PLF'] = float(self.Terrestrial['Wet_CLC_PLF'])
    self.Terrestrial['Wet_FCP_PLF'] = float(self.Terrestrial['Wet_FCP_PLF'])
    self.Terrestrial['Wet_HCP_PLF'] = float(self.Terrestrial['Wet_HCP_PLF'])
    self.Terrestrial['Gra_NPG_PLF'] = float(self.Terrestrial['Gra_NPG_PLF'])
    self.Terrestrial['Gra_LCP_PLF'] = float(self.Terrestrial['Gra_LCP_PLF'])
    self.Terrestrial['Gra_FCP_PLF'] = float(self.Terrestrial['Gra_FCP_PLF'])
    self.Terrestrial['Gra_HCP_PLF'] = float(self.Terrestrial['Gra_HCP_PLF'])
    self.Terrestrial['Shr_NPG_PLF'] = float(self.Terrestrial['Shr_NPG_PLF'])
    self.Terrestrial['Shr_LCP_PLF'] = float(self.Terrestrial['Shr_LCP_PLF'])
    self.Terrestrial['Shr_FCP_PLF'] = float(self.Terrestrial['Shr_FCP_PLF'])
    self.Terrestrial['Shr_HCP_PLF'] = float(self.Terrestrial['Shr_HCP_PLF'])
    self.Terrestrial['Lakes_PLF']   = float(self.Terrestrial['Lakes_PLF'])
    self.Terrestrial['Ponds_PLF']   = float(self.Terrestrial['Ponds_PLF'])


#===============================================================================
def Terrestrial_Tanana(self):
    print '..Reading General Terrestrial Parameters'

    self.Terrestrial = {}
    with open(self.Terrestrial_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.Terrestrial[(key)] = val

    # Convert to strings if necessary
    self.Terrestrial['Drainage_Efficiency_Random_Value'] = \
      float(self.Terrestrial['Drainage_Efficiency_Random_Value'])
    self.Terrestrial['ALD_Distribution_Lower_Bound'] = \
      float(self.Terrestrial['ALD_Distribution_Lower_Bound'])
    self.Terrestrial['ALD_Distribution_Upper_Bound'] = \
      float(self.Terrestrial['ALD_Distribution_Upper_Bound'])

    self.Terrestrial['TF_OB_PLF'] = float(self.Terrestrial['TF_OB_PLF'])
    self.Terrestrial['TF_YB_PLF'] = float(self.Terrestrial['TF_YB_PLF'])
    self.Terrestrial['TF_OF_PLF'] = float(self.Terrestrial['TF_OF_PLF'])
    self.Terrestrial['TF_YF_PLF'] = float(self.Terrestrial['TF_YF_PLF'])
    self.Terrestrial['TF_Dec_PP_PLF'] = float(self.Terrestrial['TF_Dec_PP_PLF'])
    self.Terrestrial['TF_Con_PP_PLF'] = float(self.Terrestrial['TF_Con_PP_PLF'])
    self.Terrestrial['TF_TL_PLF'] = float(self.Terrestrial['TF_TL_PLF'])

#==================================================================================
def Met(self):
    import read_degree_days
    import calc_degree_days
    import read_met_data
    
    print '..Reading General Terrestrial Parameters'

    self.Met = {}
    with open(self.Met_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.Met[(key)] = val

    # Convert string variables if necessary

    self.Met['climate_block_lower_bound'] = int(self.Met['climate_block_lower_bound'])
    self.Met['climate_block_upper_bound'] = int(self.Met['climate_block_upper_bound'])
    self.Met['climate_event_probability'] = float(self.Met['climate_event_probability'])
    self.Met['pond_drain_rate_<0.01']     = float(self.Met['pond_drain_rate_<0.01'])
    self.Met['pond_drain_rate_0.01<0.1']  = float(self.Met['pond_drain_rate_0.01<0.1'])
    self.Met['pond_drain_rate_0.1<0.4']   = float(self.Met['pond_drain_rate_0.1<0.4'])
    self.Met['pond_drain_rate_0.1<1.0']   = float(self.Met['pond_drain_rate_0.4<1.0'])
    self.Met['lake_drain_rate_<0.01']     = float(self.Met['lake_drain_rate_<0.01'])
    self.Met['lake_drain_rate_0.01<0.1']  = float(self.Met['lake_drain_rate_0.01<0.1'])
    self.Met['lake_drain_rate_0.1<0.4']   = float(self.Met['lake_drain_rate_0.1<0.4'])
    self.Met['lake_drain_rate_0.4<1.0']   = float(self.Met['lake_drain_rate_0.4<1.0'])

    #-----------------------------------------------------
    # Read the Met Data
    #-----------------------------------------------------
    if self.Met['met_distribution'].lower() == 'point':
        self.met_file = self.Met['met_file_point']
    elif self.Met['met_distribution'].lower() == 'spatial':
        self.met_file = self.Met['met_file_distributed']

    print '       The meteorologic file to be used is :', self.met_file

    read_met_data.read_met_data(self)
    #_______________________________________
    # READ MET Data & Calculate Degree Days
    #_______________________________________
    if self.Met['degree_day_method'].lower() == 'read':    # 'Read' file or 'Calc' from geotiff input
        read_degree_days.read_degree_days(self)
    else:
        calc_degree_days.calc_degree_days(self)

#====================================================================================
def run(self):
    if self.test_code.lower() == 'yes':
        self.stop = self.test_code_duration
    else:
        self.stop = int(self.ATTM_time_steps)
    
#====================================================================================
def initialize(self):

    print '    Initializing the model'

    self.initialize = {}
    with open(self.Initialize_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.initialize[(key)] = val
