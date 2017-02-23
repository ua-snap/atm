import os
import numpy as np
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

    
    """ Read files from the input directory """
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+\
                     self.Control_directory)
    elif self.Simulation_area.lower() == 'arctic_coast':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Arctic'+\
                     self.Control_directory+'/')
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana')
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon')
    elif self.Simulation_area.lower() == 'aiem':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/AIEM')
    elif self.Simulation_area.lower() == 'ngee':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/NGEE')
    
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
    
    self.LakePond['Lower_LargeLake_WT_Y_Depth']  = float(self.LakePond['Lower_LargeLake_WT_Y_Depth'])
    self.LakePond['Upper_LargeLake_WT_Y_Depth']  = float(self.LakePond['Upper_LargeLake_WT_Y_Depth'])
    self.LakePond['Lower_MediumLake_WT_Y_Depth'] = float(self.LakePond['Lower_MediumLake_WT_Y_Depth'])
    self.LakePond['Upper_MediumLake_WT_Y_Depth'] = float(self.LakePond['Upper_MediumLake_WT_Y_Depth'])
    self.LakePond['Lower_SmallLake_WT_Y_Depth']  = float(self.LakePond['Lower_SmallLake_WT_Y_Depth'])
    self.LakePond['Upper_SmallLake_WT_Y_Depth']  = float(self.LakePond['Upper_SmallLake_WT_Y_Depth'])

    self.LakePond['Lower_LargeLake_WT_M_Depth']  = float(self.LakePond['Lower_LargeLake_WT_M_Depth'])
    self.LakePond['Upper_LargeLake_WT_M_Depth']  = float(self.LakePond['Upper_LargeLake_WT_M_Depth'])
    self.LakePond['Lower_MediumLake_WT_M_Depth'] = float(self.LakePond['Lower_MediumLake_WT_M_Depth'])
    self.LakePond['Upper_MediumLake_WT_M_Depth'] = float(self.LakePond['Upper_MediumLake_WT_M_Depth'])
    self.LakePond['Lower_SmallLake_WT_M_Depth']  = float(self.LakePond['Lower_SmallLake_WT_M_Depth'])
    self.LakePond['Upper_SmallLake_WT_M_Depth']  = float(self.LakePond['Upper_SmallLake_WT_M_Depth'])    
                                                         
    self.LakePond['Lower_LargeLake_WT_O_Depth']  = float(self.LakePond['Lower_LargeLake_WT_O_Depth'])
    self.LakePond['Upper_LargeLake_WT_O_Depth']  = float(self.LakePond['Upper_LargeLake_WT_O_Depth'])
    self.LakePond['Lower_MediumLake_WT_O_Depth'] = float(self.LakePond['Lower_MediumLake_WT_O_Depth'])
    self.LakePond['Upper_MediumLake_WT_O_Depth'] = float(self.LakePond['Upper_MediumLake_WT_O_Depth'])
    self.LakePond['Lower_SmallLake_WT_O_Depth']  = float(self.LakePond['Lower_SmallLake_WT_O_Depth'])
    self.LakePond['Upper_SmallLake_WT_O_Depth']  = float(self.LakePond['Upper_SmallLake_WT_O_Depth'])  

    self.LakePond['Lower_Lake_Depth']            = float(self.LakePond['Lower_Lake_Depth'])
    self.LakePond['Upper_Lake_Depth']            = float(self.LakePond['Upper_Lake_Depth'])

    self.LakePond['Uniform_Pond_Depth']          = float(self.LakePond['Uniform_Pond_Depth'])
    self.LakePond['Lower_Pond_Depth']            = float(self.LakePond['Lower_Pond_Depth'])
    self.LakePond['Upper_Pond_Depth']            = float(self.LakePond['Upper_Pond_Depth'])

    self.LakePond['Lower_Pond_WT_Y_Depth']       = float(self.LakePond['Lower_Pond_WT_Y_Depth'])
    self.LakePond['Upper_Pond_WT_Y_Depth']       = float(self.LakePond['Upper_Pond_WT_Y_Depth'])
    self.LakePond['Lower_Pond_WT_M_Depth']       = float(self.LakePond['Lower_Pond_WT_M_Depth'])
    self.LakePond['Upper_Pond_WT_M_Depth']       = float(self.LakePond['Upper_Pond_WT_M_Depth'])
    self.LakePond['Lower_Pond_WT_O_Depth']       = float(self.LakePond['Lower_Pond_WT_O_Depth'])
    self.LakePond['Upper_Pond_WT_O_Depth']       = float(self.LakePond['Upper_Pond_WT_O_Depth'])
    
    self.LakePond['Lake_Expansion']              = float(self.LakePond['Lake_Expansion'])
    self.LakePond['Pond_Expansion']              = float(self.LakePond['Pond_Expansion'])

    self.LakePond['LargeLake_WT_Y_Expansion']    = float(self.LakePond['LargeLake_WT_Y_Expansion'])
    self.LakePond['MediumLake_WT_Y_Expansion']   = float(self.LakePond['MediumLake_WT_Y_Expansion'])
    self.LakePond['SmallLake_WT_Y_Expansion']    = float(self.LakePond['SmallLake_WT_Y_Expansion'])
    self.LakePond['LargeLake_WT_M_Expansion']    = float(self.LakePond['LargeLake_WT_M_Expansion'])
    self.LakePond['MediumLake_WT_M_Expansion']   = float(self.LakePond['MediumLake_WT_M_Expansion'])
    self.LakePond['SmallLake_WT_M_Expansion']    = float(self.LakePond['SmallLake_WT_M_Expansion'])
    self.LakePond['LargeLake_WT_O_Expansion']    = float(self.LakePond['LargeLake_WT_O_Expansion'])
    self.LakePond['MediumLake_WT_O_Expansion']   = float(self.LakePond['MediumLake_WT_O_Expansion'])
    self.LakePond['SmallLake_WT_O_Expansion']    = float(self.LakePond['SmallLake_WT_O_Expansion'])
    self.LakePond['Pond_WT_Y_Expansion']         = float(self.LakePond['Pond_WT_Y_Expansion'])
    self.LakePond['Pond_WT_M_Expansion']         = float(self.LakePond['Pond_WT_M_Expansion'])
    self.LakePond['Pond_WT_O_Expansion']         = float(self.LakePond['Pond_WT_O_Expansion'])
    
    self.LakePond['Pond_Infill_Constant']        = float(self.LakePond['Pond_Infill_Constant'])
    self.LakePond['Pond_WT_Y_Infill_Constant']   = float(self.LakePond['Pond_WT_Y_Infill_Constant'])
    self.LakePond['Pond_WT_M_Infill_Constant']   = float(self.LakePond['Pond_WT_M_Infill_Constant'])
    self.LakePond['Pond_WT_O_Infill_Constant']   = float(self.LakePond['Pond_WT_O_Infill_Constant'])
    
    self.LakePond['ice_thickness_uniform_alpha'] = float(self.LakePond['ice_thickness_uniform_alpha'])
    self.LakePond['Lower_ice_thickness_alpha']   = float(self.LakePond['Lower_ice_thickness_alpha'])
    self.LakePond['Upper_ice_thickness_alpha']   = float(self.LakePond['Upper_ice_thickness_alpha'])
    self.LakePond['pond_growth_time_required']   = float(self.LakePond['pond_growth_time_required'])
    self.LakePond['Pond_WT_Y_growth_time_required'] = float(self.LakePond['Pond_WT_Y_growth_time_required'])
    self.LakePond['Pond_WT_M_growth_time_required'] = float(self.LakePond['Pond_WT_M_growth_time_required'])
    self.LakePond['Pond_WT_O_growth_time_required'] = float(self.LakePond['Pond_WT_O_growth_time_required'])
    
    self.LakePond['lake_depth_control']          = float(self.LakePond['lake_depth_control'])
    self.LakePond['LargeLake_WT_Y_depth_control']  = float(self.LakePond['LargeLake_WT_Y_depth_control'])
    self.LakePond['LargeLake_WT_M_depth_control']  = float(self.LakePond['LargeLake_WT_M_depth_control'])
    self.LakePond['LargeLake_WT_O_depth_control']  = float(self.LakePond['LargeLake_WT_O_depth_control'])
    self.LakePond['MediumLake_WT_Y_depth_control'] = float(self.LakePond['MediumLake_WT_Y_depth_control'])
    self.LakePond['MediumLake_WT_M_depth_control'] = float(self.LakePond['MediumLake_WT_M_depth_control'])
    self.LakePond['MediumLake_WT_O_depth_control'] = float(self.LakePond['MediumLake_WT_O_depth_control'])
    self.LakePond['SmallLake_WT_Y_depth_control']  = float(self.LakePond['SmallLake_WT_Y_depth_control'])
    self.LakePond['SmallLake_WT_M_depth_control']  = float(self.LakePond['SmallLake_WT_M_depth_control'])
    self.LakePond['SmallLake_WT_O_depth_control']  = float(self.LakePond['SmallLake_WT_O_depth_control'])
    
    self.LakePond['pond_depth_control']          = float(self.LakePond['pond_depth_control'])
    self.LakePond['Pond_WT_Y_depth_control']     = float(self.LakePond['Pond_WT_Y_depth_control'])
    self.LakePond['Pond_WT_M_depth_control']     = float(self.LakePond['Pond_WT_M_depth_control'])
    self.LakePond['Pond_WT_O_depth_control']     = float(self.LakePond['Pond_WT_O_depth_control'])

#===============================================================================
def Terrestrial_Barrow(self):
    print '..Reading General Terrestrial Parameters'

    """ Move to the control directory """

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

    #self.Terrestrial['Wet_NPG_PLF'] = float(self.Terrestrial['Wet_NPG_PLF'])
    #self.Terrestrial['Wet_LCP_PLF'] = float(self.Terrestrial['Wet_LCP_PLF'])
    #self.Terrestrial['Wet_CLC_PLF'] = float(self.Terrestrial['Wet_CLC_PLF'])
    #self.Terrestrial['Wet_FCP_PLF'] = float(self.Terrestrial['Wet_FCP_PLF'])
    #self.Terrestrial['Wet_HCP_PLF'] = float(self.Terrestrial['Wet_HCP_PLF'])
    #self.Terrestrial['Gra_NPG_PLF'] = float(self.Terrestrial['Gra_NPG_PLF'])
    #self.Terrestrial['Gra_LCP_PLF'] = float(self.Terrestrial['Gra_LCP_PLF'])
    #self.Terrestrial['Gra_FCP_PLF'] = float(self.Terrestrial['Gra_FCP_PLF'])
    #self.Terrestrial['Gra_HCP_PLF'] = float(self.Terrestrial['Gra_HCP_PLF'])
    #self.Terrestrial['Shr_NPG_PLF'] = float(self.Terrestrial['Shr_NPG_PLF'])
    #self.Terrestrial['Shr_LCP_PLF'] = float(self.Terrestrial['Shr_LCP_PLF'])
    #self.Terrestrial['Shr_FCP_PLF'] = float(self.Terrestrial['Shr_FCP_PLF'])
    #self.Terrestrial['Shr_HCP_PLF'] = float(self.Terrestrial['Shr_HCP_PLF'])
    #self.Terrestrial['Lakes_PLF']   = float(self.Terrestrial['Lakes_PLF'])
    #self.Terrestrial['Ponds_PLF']   = float(self.Terrestrial['Ponds_PLF'])
    self.Terrestrial['CLC_WT_Y_PLF'] = float(self.Terrestrial['CLC_WT_Y_PLF'])
    self.Terrestrial['CLC_WT_M_PLF'] = float(self.Terrestrial['CLC_WT_M_PLF'])
    self.Terrestrial['CLC_WT_O_PLF'] = float(self.Terrestrial['CLC_WT_O_PLF'])
    self.Terrestrial['CoastalWaters_WT_O_PLF'] = float(self.Terrestrial['CoastalWaters_WT_O_PLF'])    
    self.Terrestrial['DrainedSlope_WT_Y_PLF'] = float(self.Terrestrial['DrainedSlope_WT_Y_PLF'])
    self.Terrestrial['DrainedSlope_WT_M_PLF'] = float(self.Terrestrial['DrainedSlope_WT_M_PLF'])
    self.Terrestrial['DrainedSlope_WT_O_PLF'] = float(self.Terrestrial['DrainedSlope_WT_O_PLF'])    
    self.Terrestrial['FCP_WT_Y_PLF'] = float(self.Terrestrial['FCP_WT_Y_PLF'])
    self.Terrestrial['FCP_WT_M_PLF'] = float(self.Terrestrial['FCP_WT_M_PLF'])
    self.Terrestrial['FCP_WT_O_PLF'] = float(self.Terrestrial['FCP_WT_O_PLF'])    
    self.Terrestrial['HCP_WT_Y_PLF'] = float(self.Terrestrial['HCP_WT_Y_PLF'])
    self.Terrestrial['HCP_WT_M_PLF'] = float(self.Terrestrial['HCP_WT_M_PLF'])
    self.Terrestrial['HCP_WT_O_PLF'] = float(self.Terrestrial['HCP_WT_O_PLF'])    
    self.Terrestrial['LCP_WT_Y_PLF'] = float(self.Terrestrial['LCP_WT_Y_PLF'])
    self.Terrestrial['LCP_WT_M_PLF'] = float(self.Terrestrial['LCP_WT_M_PLF'])
    self.Terrestrial['LCP_WT_O_PLF'] = float(self.Terrestrial['LCP_WT_O_PLF'])    
    self.Terrestrial['Meadow_WT_Y_PLF'] = float(self.Terrestrial['Meadow_WT_Y_PLF'])
    self.Terrestrial['Meadow_WT_M_PLF'] = float(self.Terrestrial['Meadow_WT_M_PLF'])
    self.Terrestrial['Meadow_WT_O_PLF'] = float(self.Terrestrial['Meadow_WT_O_PLF'])    
    self.Terrestrial['NoData_WT_O_PLF'] = float(self.Terrestrial['NoData_WT_O_PLF'])    
    self.Terrestrial['SandDunes_WT_Y_PLF'] = float(self.Terrestrial['SandDunes_WT_Y_PLF'])
    self.Terrestrial['SandDunes_WT_M_PLF'] = float(self.Terrestrial['SandDunes_WT_M_PLF'])
    self.Terrestrial['SandDunes_WT_O_PLF'] = float(self.Terrestrial['SandDunes_WT_O_PLF'])
    self.Terrestrial['SaturatedBarrens_WT_Y_PLF'] = float(self.Terrestrial['SaturatedBarrens_WT_Y_PLF'])
    self.Terrestrial['SaturatedBarrens_WT_M_PLF'] = float(self.Terrestrial['SaturatedBarrens_WT_M_PLF'])
    self.Terrestrial['SaturatedBarrens_WT_O_PLF'] = float(self.Terrestrial['SaturatedBarrens_WT_O_PLF'])
    self.Terrestrial['Shrubs_WT_O_PLF'] = float(self.Terrestrial['Shrubs_WT_O_PLF'])
    self.Terrestrial['Urban_WT_PLF'] = float(self.Terrestrial['Urban_WT_PLF'])
    self.Terrestrial['LargeLakes_WT_Y_PLF'] = float(self.Terrestrial['LargeLakes_WT_Y_PLF'])
    self.Terrestrial['LargeLakes_WT_M_PLF'] = float(self.Terrestrial['LargeLakes_WT_M_PLF'])
    self.Terrestrial['LargeLakes_WT_O_PLF'] = float(self.Terrestrial['LargeLakes_WT_O_PLF'])   
    self.Terrestrial['MediumLakes_WT_Y_PLF'] = float(self.Terrestrial['MediumLakes_WT_Y_PLF'])
    self.Terrestrial['MediumLakes_WT_M_PLF'] = float(self.Terrestrial['MediumLakes_WT_M_PLF'])
    self.Terrestrial['MediumLakes_WT_O_PLF'] = float(self.Terrestrial['MediumLakes_WT_O_PLF'])   
    self.Terrestrial['SmallLakes_WT_Y_PLF'] = float(self.Terrestrial['SmallLakes_WT_Y_PLF'])
    self.Terrestrial['SmallLakes_WT_M_PLF'] = float(self.Terrestrial['SmallLakes_WT_M_PLF'])
    self.Terrestrial['SmallLakes_WT_O_PLF'] = float(self.Terrestrial['SmallLakes_WT_O_PLF'])   
    self.Terrestrial['Ponds_WT_Y_PLF'] = float(self.Terrestrial['Ponds_WT_Y_PLF'])
    self.Terrestrial['Ponds_WT_M_PLF'] = float(self.Terrestrial['Ponds_WT_M_PLF'])
    self.Terrestrial['Ponds_WT_O_PLF'] = float(self.Terrestrial['Ponds_WT_O_PLF'])   
    self.Terrestrial['Rivers_WT_Y_PLF'] = float(self.Terrestrial['Rivers_WT_Y_PLF'])
    self.Terrestrial['Rivers_WT_M_PLF'] = float(self.Terrestrial['Rivers_WT_M_PLF'])
    self.Terrestrial['Rivers_WT_O_PLF'] = float(self.Terrestrial['Rivers_WT_O_PLF'])   

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
    
    print '..Reading General Meteorologic Parameters'

    """ Read files from the input directory """
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+\
                     self.Control_directory+'/')
    elif self.Simulation_area.lower() == 'arctic_coast':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Arctic/'+\
                     self.Control_directory+'/')
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/'+\
                     self.Control_directory+'/')
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/'+\
                     self.Control_directory+'/')
    elif self.Simulation_area.lower() == 'aiem':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/AIEM/'+\
                     self.Control_directory+'/')
    elif self.Simulation_area.lower() == 'ngee':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/NGEE/'+\
                     self.Control_directory+'/')

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
    
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+\
                     self.control['Control_dir']+'/')
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/'+\
                     self.control['Control_dir'])
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/'+\
                     self.control['Control_dir'])

    self.initialize = {}
    with open(self.Initialize_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.initialize[(key)] = val
#====================================================================================
def CLC_WT(self):
    
    print '    ..Reading Wetland Tundra Coalescent Low Center Polygon Parameters'

    """ Read files from the input directory """
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+\
                     self.Control_directory)
    elif self.Simulation_area.lower() == 'arctic_coast':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Arctic/'+\
                     self.Control_directory)
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/'+\
                     self.Control_directory)
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/'+\
                     self.Control_directory)
    elif self.Simulation_area.lower() == 'aiem':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/AIEM/'+\
                     self.Control_directory)
    elif self.Simulation_area.lower() == 'ngee':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/NGEE/'+\
                     self.Control_directory)

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Young Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Young age parameters'

    self.CLC_WT_Y = {}
    with open(self.CLC_WT_Y_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.CLC_WT_Y[(key)] = val

    # Convert strings to floats as necessary
    self.CLC_WT_Y['A1_above']    = float(self.CLC_WT_Y['A1_above'])
    self.CLC_WT_Y['A2_above']    = float(self.CLC_WT_Y['A2_above'])
    self.CLC_WT_Y['x0_above']    = float(self.CLC_WT_Y['x0_above'])
    self.CLC_WT_Y['dx_above']    = float(self.CLC_WT_Y['dx_above'])
    self.CLC_WT_Y['A1_below']    = float(self.CLC_WT_Y['A1_below'])
    self.CLC_WT_Y['A2_below']    = float(self.CLC_WT_Y['A2_below'])
    self.CLC_WT_Y['x0_below']    = float(self.CLC_WT_Y['x0_below'])
    self.CLC_WT_Y['dx_below']    = float(self.CLC_WT_Y['dx_below'])
    self.CLC_WT_Y['a_above']     = float(self.CLC_WT_Y['a_above'])
    self.CLC_WT_Y['b_above']     = float(self.CLC_WT_Y['b_above'])
    self.CLC_WT_Y['a_below']     = float(self.CLC_WT_Y['a_below'])
    self.CLC_WT_Y['b_below']     = float(self.CLC_WT_Y['b_below'])
    self.CLC_WT_Y['K_above']     = float(self.CLC_WT_Y['K_above'])
    self.CLC_WT_Y['C_above']     = float(self.CLC_WT_Y['C_above'])
    self.CLC_WT_Y['A_above']     = float(self.CLC_WT_Y['A_above'])
    self.CLC_WT_Y['B_above']     = float(self.CLC_WT_Y['B_above'])
    self.CLC_WT_Y['K_below']     = float(self.CLC_WT_Y['K_below'])
    self.CLC_WT_Y['C_below']     = float(self.CLC_WT_Y['C_below'])
    self.CLC_WT_Y['A_below']     = float(self.CLC_WT_Y['A_below'])
    self.CLC_WT_Y['B_below']     = float(self.CLC_WT_Y['B_below'])
    self.CLC_WT_Y['HillB_above'] = float(self.CLC_WT_Y['HillB_above'])
    self.CLC_WT_Y['HillN_above'] = float(self.CLC_WT_Y['HillN_above'])
    self.CLC_WT_Y['HillB_below'] = float(self.CLC_WT_Y['HillB_below'])
    self.CLC_WT_Y['HillN_below'] = float(self.CLC_WT_Y['HillN_below'])
    self.CLC_WT_Y['max_terrain_transition'] = \
      float(self.CLC_WT_Y['max_terrain_transition'])
    self.CLC_WT_Y['ice_slope_poor']    = float(self.CLC_WT_Y['ice_slope_poor'])
    self.CLC_WT_Y['ice_slope_pore']    = float(self.CLC_WT_Y['ice_slope_pore'])
    self.CLC_WT_Y['ice_slope_wedge']   = float(self.CLC_WT_Y['ice_slope_wedge'])
    self.CLC_WT_Y['ice_slope_massive'] = float(self.CLC_WT_Y['ice_slope_massive'])
    self.CLC_WT_Y['porosity'] = float(self.CLC_WT_Y['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Medium Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Medium age parameters'
    
    self.CLC_WT_M = {}
    with open(self.CLC_WT_M_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.CLC_WT_M[(key)] = val

    # Convert strings to floats as necessary
    self.CLC_WT_M['A1_above']    = float(self.CLC_WT_M['A1_above'])
    self.CLC_WT_M['A2_above']    = float(self.CLC_WT_M['A2_above'])
    self.CLC_WT_M['x0_above']    = float(self.CLC_WT_M['x0_above'])
    self.CLC_WT_M['dx_above']    = float(self.CLC_WT_M['dx_above'])
    self.CLC_WT_M['A1_below']    = float(self.CLC_WT_M['A1_below'])
    self.CLC_WT_M['A2_below']    = float(self.CLC_WT_M['A2_below'])
    self.CLC_WT_M['x0_below']    = float(self.CLC_WT_M['x0_below'])
    self.CLC_WT_M['dx_below']    = float(self.CLC_WT_M['dx_below'])
    self.CLC_WT_M['a_above']     = float(self.CLC_WT_M['a_above'])
    self.CLC_WT_M['b_above']     = float(self.CLC_WT_M['b_above'])
    self.CLC_WT_M['a_below']     = float(self.CLC_WT_M['a_below'])
    self.CLC_WT_M['b_below']     = float(self.CLC_WT_M['b_below'])
    self.CLC_WT_M['K_above']     = float(self.CLC_WT_M['K_above'])
    self.CLC_WT_M['C_above']     = float(self.CLC_WT_M['C_above'])
    self.CLC_WT_M['A_above']     = float(self.CLC_WT_M['A_above'])
    self.CLC_WT_M['B_above']     = float(self.CLC_WT_M['B_above'])
    self.CLC_WT_M['K_below']     = float(self.CLC_WT_M['K_below'])
    self.CLC_WT_M['C_below']     = float(self.CLC_WT_M['C_below'])
    self.CLC_WT_M['A_below']     = float(self.CLC_WT_M['A_below'])
    self.CLC_WT_M['B_below']     = float(self.CLC_WT_M['B_below'])
    self.CLC_WT_M['HillB_above'] = float(self.CLC_WT_M['HillB_above'])
    self.CLC_WT_M['HillN_above'] = float(self.CLC_WT_M['HillN_above'])
    self.CLC_WT_M['HillB_below'] = float(self.CLC_WT_M['HillB_below'])
    self.CLC_WT_M['HillN_below'] = float(self.CLC_WT_M['HillN_below'])
    self.CLC_WT_M['max_terrain_transition'] = \
      float(self.CLC_WT_M['max_terrain_transition'])
    self.CLC_WT_M['ice_slope_poor']    = float(self.CLC_WT_M['ice_slope_poor'])
    self.CLC_WT_M['ice_slope_pore']    = float(self.CLC_WT_M['ice_slope_pore'])
    self.CLC_WT_M['ice_slope_wedge']   = float(self.CLC_WT_M['ice_slope_wedge'])
    self.CLC_WT_M['ice_slope_massive'] = float(self.CLC_WT_M['ice_slope_massive'])
    self.CLC_WT_M['porosity'] = float(self.CLC_WT_M['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Old Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Old age parameters'
    
    self.CLC_WT_O = {}
    with open(self.CLC_WT_O_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.CLC_WT_O[(key)] = val

    # Convert strings to floats as necessary
    self.CLC_WT_O['A1_above']    = float(self.CLC_WT_O['A1_above'])
    self.CLC_WT_O['A2_above']    = float(self.CLC_WT_O['A2_above'])
    self.CLC_WT_O['x0_above']    = float(self.CLC_WT_O['x0_above'])
    self.CLC_WT_O['dx_above']    = float(self.CLC_WT_O['dx_above'])
    self.CLC_WT_O['A1_below']    = float(self.CLC_WT_O['A1_below'])
    self.CLC_WT_O['A2_below']    = float(self.CLC_WT_O['A2_below'])
    self.CLC_WT_O['x0_below']    = float(self.CLC_WT_O['x0_below'])
    self.CLC_WT_O['dx_below']    = float(self.CLC_WT_O['dx_below'])
    self.CLC_WT_O['a_above']     = float(self.CLC_WT_O['a_above'])
    self.CLC_WT_O['b_above']     = float(self.CLC_WT_O['b_above'])
    self.CLC_WT_O['a_below']     = float(self.CLC_WT_O['a_below'])
    self.CLC_WT_O['b_below']     = float(self.CLC_WT_O['b_below'])
    self.CLC_WT_O['K_above']     = float(self.CLC_WT_O['K_above'])
    self.CLC_WT_O['C_above']     = float(self.CLC_WT_O['C_above'])
    self.CLC_WT_O['A_above']     = float(self.CLC_WT_O['A_above'])
    self.CLC_WT_O['B_above']     = float(self.CLC_WT_O['B_above'])
    self.CLC_WT_O['K_below']     = float(self.CLC_WT_O['K_below'])
    self.CLC_WT_O['C_below']     = float(self.CLC_WT_O['C_below'])
    self.CLC_WT_O['A_below']     = float(self.CLC_WT_O['A_below'])
    self.CLC_WT_O['B_below']     = float(self.CLC_WT_O['B_below'])
    self.CLC_WT_O['HillB_above'] = float(self.CLC_WT_O['HillB_above'])
    self.CLC_WT_O['HillN_above'] = float(self.CLC_WT_O['HillN_above'])
    self.CLC_WT_O['HillB_below'] = float(self.CLC_WT_O['HillB_below'])
    self.CLC_WT_O['HillN_below'] = float(self.CLC_WT_O['HillN_below'])
    self.CLC_WT_O['max_terrain_transition'] = \
      float(self.CLC_WT_O['max_terrain_transition'])
    self.CLC_WT_O['ice_slope_poor']    = float(self.CLC_WT_O['ice_slope_poor'])
    self.CLC_WT_O['ice_slope_pore']    = float(self.CLC_WT_O['ice_slope_pore'])
    self.CLC_WT_O['ice_slope_wedge']   = float(self.CLC_WT_O['ice_slope_wedge'])
    self.CLC_WT_O['ice_slope_massive'] = float(self.CLC_WT_O['ice_slope_massive'])
    self.CLC_WT_O['porosity'] = float(self.CLC_WT_O['porosity'])    

#====================================================================================
def CoastalWaters_WT(self):
    
    print '    ..Reading Wetland Tundra Coastal Waters Parameters'

    """ Read files from the input directory """
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'arctic_coast':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Arctic/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'aiem':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/AIEM/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'ngee':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/NGEE/'+\
                 self.Control_directory)

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Old Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    self.CoastalWaters_WT_O = {}
    with open(self.CoastalWaters_WT_O_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.CoastalWaters_WT_O[(key)] = val

    # Convert strings to floats as necessary
    self.CoastalWaters_WT_O['A1_above']    = float(self.CoastalWaters_WT_O['A1_above'])
    self.CoastalWaters_WT_O['A2_above']    = float(self.CoastalWaters_WT_O['A2_above'])
    self.CoastalWaters_WT_O['x0_above']    = float(self.CoastalWaters_WT_O['x0_above'])
    self.CoastalWaters_WT_O['dx_above']    = float(self.CoastalWaters_WT_O['dx_above'])
    self.CoastalWaters_WT_O['A1_below']    = float(self.CoastalWaters_WT_O['A1_below'])
    self.CoastalWaters_WT_O['A2_below']    = float(self.CoastalWaters_WT_O['A2_below'])
    self.CoastalWaters_WT_O['x0_below']    = float(self.CoastalWaters_WT_O['x0_below'])
    self.CoastalWaters_WT_O['dx_below']    = float(self.CoastalWaters_WT_O['dx_below'])
    self.CoastalWaters_WT_O['a_above']     = float(self.CoastalWaters_WT_O['a_above'])
    self.CoastalWaters_WT_O['b_above']     = float(self.CoastalWaters_WT_O['b_above'])
    self.CoastalWaters_WT_O['a_below']     = float(self.CoastalWaters_WT_O['a_below'])
    self.CoastalWaters_WT_O['b_below']     = float(self.CoastalWaters_WT_O['b_below'])
    self.CoastalWaters_WT_O['K_above']     = float(self.CoastalWaters_WT_O['K_above'])
    self.CoastalWaters_WT_O['C_above']     = float(self.CoastalWaters_WT_O['C_above'])
    self.CoastalWaters_WT_O['A_above']     = float(self.CoastalWaters_WT_O['A_above'])
    self.CoastalWaters_WT_O['B_above']     = float(self.CoastalWaters_WT_O['B_above'])
    self.CoastalWaters_WT_O['K_below']     = float(self.CoastalWaters_WT_O['K_below'])
    self.CoastalWaters_WT_O['C_below']     = float(self.CoastalWaters_WT_O['C_below'])
    self.CoastalWaters_WT_O['A_below']     = float(self.CoastalWaters_WT_O['A_below'])
    self.CoastalWaters_WT_O['B_below']     = float(self.CoastalWaters_WT_O['B_below'])
    self.CoastalWaters_WT_O['HillB_above'] = float(self.CoastalWaters_WT_O['HillB_above'])
    self.CoastalWaters_WT_O['HillN_above'] = float(self.CoastalWaters_WT_O['HillN_above'])
    self.CoastalWaters_WT_O['HillB_below'] = float(self.CoastalWaters_WT_O['HillB_below'])
    self.CoastalWaters_WT_O['HillN_below'] = float(self.CoastalWaters_WT_O['HillN_below'])
    self.CoastalWaters_WT_O['max_terrain_transition'] = \
      float(self.CoastalWaters_WT_O['max_terrain_transition'])
    self.CoastalWaters_WT_O['ice_slope_poor']    = float(self.CoastalWaters_WT_O['ice_slope_poor'])
    self.CoastalWaters_WT_O['ice_slope_pore']    = float(self.CoastalWaters_WT_O['ice_slope_pore'])
    self.CoastalWaters_WT_O['ice_slope_wedge']   = float(self.CoastalWaters_WT_O['ice_slope_wedge'])
    self.CoastalWaters_WT_O['ice_slope_massive'] = float(self.CoastalWaters_WT_O['ice_slope_massive'])
    self.CoastalWaters_WT_O['porosity'] = float(self.CoastalWaters_WT_O['porosity'])    

#====================================================================================
def DrainedSlope_WT(self):
    
    print '    ..Reading Wetland Tundra Drained Slope Parameters'

    """ Read files from the input directory """
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'arctic_coast':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Arctic/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'aiem':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/AIEM/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'ngee':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/NGEE/'+\
                 self.Control_directory)

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Young Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Young age parameters'
    
    self.DrainedSlope_WT_Y = {}
    with open(self.DrainedSlope_WT_Y_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.DrainedSlope_WT_Y[(key)] = val

    # Convert strings to floats as necessary
    self.DrainedSlope_WT_Y['A1_above']    = float(self.DrainedSlope_WT_Y['A1_above'])
    self.DrainedSlope_WT_Y['A2_above']    = float(self.DrainedSlope_WT_Y['A2_above'])
    self.DrainedSlope_WT_Y['x0_above']    = float(self.DrainedSlope_WT_Y['x0_above'])
    self.DrainedSlope_WT_Y['dx_above']    = float(self.DrainedSlope_WT_Y['dx_above'])
    self.DrainedSlope_WT_Y['A1_below']    = float(self.DrainedSlope_WT_Y['A1_below'])
    self.DrainedSlope_WT_Y['A2_below']    = float(self.DrainedSlope_WT_Y['A2_below'])
    self.DrainedSlope_WT_Y['x0_below']    = float(self.DrainedSlope_WT_Y['x0_below'])
    self.DrainedSlope_WT_Y['dx_below']    = float(self.DrainedSlope_WT_Y['dx_below'])
    self.DrainedSlope_WT_Y['a_above']     = float(self.DrainedSlope_WT_Y['a_above'])
    self.DrainedSlope_WT_Y['b_above']     = float(self.DrainedSlope_WT_Y['b_above'])
    self.DrainedSlope_WT_Y['a_below']     = float(self.DrainedSlope_WT_Y['a_below'])
    self.DrainedSlope_WT_Y['b_below']     = float(self.DrainedSlope_WT_Y['b_below'])
    self.DrainedSlope_WT_Y['K_above']     = float(self.DrainedSlope_WT_Y['K_above'])
    self.DrainedSlope_WT_Y['C_above']     = float(self.DrainedSlope_WT_Y['C_above'])
    self.DrainedSlope_WT_Y['A_above']     = float(self.DrainedSlope_WT_Y['A_above'])
    self.DrainedSlope_WT_Y['B_above']     = float(self.DrainedSlope_WT_Y['B_above'])
    self.DrainedSlope_WT_Y['K_below']     = float(self.DrainedSlope_WT_Y['K_below'])
    self.DrainedSlope_WT_Y['C_below']     = float(self.DrainedSlope_WT_Y['C_below'])
    self.DrainedSlope_WT_Y['A_below']     = float(self.DrainedSlope_WT_Y['A_below'])
    self.DrainedSlope_WT_Y['B_below']     = float(self.DrainedSlope_WT_Y['B_below'])
    self.DrainedSlope_WT_Y['HillB_above'] = float(self.DrainedSlope_WT_Y['HillB_above'])
    self.DrainedSlope_WT_Y['HillN_above'] = float(self.DrainedSlope_WT_Y['HillN_above'])
    self.DrainedSlope_WT_Y['HillB_below'] = float(self.DrainedSlope_WT_Y['HillB_below'])
    self.DrainedSlope_WT_Y['HillN_below'] = float(self.DrainedSlope_WT_Y['HillN_below'])
    self.DrainedSlope_WT_Y['max_terrain_transition'] = \
      float(self.DrainedSlope_WT_Y['max_terrain_transition'])
    self.DrainedSlope_WT_Y['ice_slope_poor']    = float(self.DrainedSlope_WT_Y['ice_slope_poor'])
    self.DrainedSlope_WT_Y['ice_slope_pore']    = float(self.DrainedSlope_WT_Y['ice_slope_pore'])
    self.DrainedSlope_WT_Y['ice_slope_wedge']   = float(self.DrainedSlope_WT_Y['ice_slope_wedge'])
    self.DrainedSlope_WT_Y['ice_slope_massive'] = float(self.DrainedSlope_WT_Y['ice_slope_massive'])
    self.DrainedSlope_WT_Y['porosity'] = float(self.DrainedSlope_WT_Y['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Medium Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Medium age parameters'
    
    self.DrainedSlope_WT_M = {}
    with open(self.DrainedSlope_WT_M_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.DrainedSlope_WT_M[(key)] = val

    # Convert strings to floats as necessary
    self.DrainedSlope_WT_M['A1_above']    = float(self.DrainedSlope_WT_M['A1_above'])
    self.DrainedSlope_WT_M['A2_above']    = float(self.DrainedSlope_WT_M['A2_above'])
    self.DrainedSlope_WT_M['x0_above']    = float(self.DrainedSlope_WT_M['x0_above'])
    self.DrainedSlope_WT_M['dx_above']    = float(self.DrainedSlope_WT_M['dx_above'])
    self.DrainedSlope_WT_M['A1_below']    = float(self.DrainedSlope_WT_M['A1_below'])
    self.DrainedSlope_WT_M['A2_below']    = float(self.DrainedSlope_WT_M['A2_below'])
    self.DrainedSlope_WT_M['x0_below']    = float(self.DrainedSlope_WT_M['x0_below'])
    self.DrainedSlope_WT_M['dx_below']    = float(self.DrainedSlope_WT_M['dx_below'])
    self.DrainedSlope_WT_M['a_above']     = float(self.DrainedSlope_WT_M['a_above'])
    self.DrainedSlope_WT_M['b_above']     = float(self.DrainedSlope_WT_M['b_above'])
    self.DrainedSlope_WT_M['a_below']     = float(self.DrainedSlope_WT_M['a_below'])
    self.DrainedSlope_WT_M['b_below']     = float(self.DrainedSlope_WT_M['b_below'])
    self.DrainedSlope_WT_M['K_above']     = float(self.DrainedSlope_WT_M['K_above'])
    self.DrainedSlope_WT_M['C_above']     = float(self.DrainedSlope_WT_M['C_above'])
    self.DrainedSlope_WT_M['A_above']     = float(self.DrainedSlope_WT_M['A_above'])
    self.DrainedSlope_WT_M['B_above']     = float(self.DrainedSlope_WT_M['B_above'])
    self.DrainedSlope_WT_M['K_below']     = float(self.DrainedSlope_WT_M['K_below'])
    self.DrainedSlope_WT_M['C_below']     = float(self.DrainedSlope_WT_M['C_below'])
    self.DrainedSlope_WT_M['A_below']     = float(self.DrainedSlope_WT_M['A_below'])
    self.DrainedSlope_WT_M['B_below']     = float(self.DrainedSlope_WT_M['B_below'])
    self.DrainedSlope_WT_M['HillB_above'] = float(self.DrainedSlope_WT_M['HillB_above'])
    self.DrainedSlope_WT_M['HillN_above'] = float(self.DrainedSlope_WT_M['HillN_above'])
    self.DrainedSlope_WT_M['HillB_below'] = float(self.DrainedSlope_WT_M['HillB_below'])
    self.DrainedSlope_WT_M['HillN_below'] = float(self.DrainedSlope_WT_M['HillN_below'])
    self.DrainedSlope_WT_M['max_terrain_transition'] = \
      float(self.DrainedSlope_WT_M['max_terrain_transition'])
    self.DrainedSlope_WT_M['ice_slope_poor']    = float(self.DrainedSlope_WT_M['ice_slope_poor'])
    self.DrainedSlope_WT_M['ice_slope_pore']    = float(self.DrainedSlope_WT_M['ice_slope_pore'])
    self.DrainedSlope_WT_M['ice_slope_wedge']   = float(self.DrainedSlope_WT_M['ice_slope_wedge'])
    self.DrainedSlope_WT_M['ice_slope_massive'] = float(self.DrainedSlope_WT_M['ice_slope_massive'])
    self.DrainedSlope_WT_M['porosity'] = float(self.DrainedSlope_WT_M['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Old Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Old age parameters'
    
    self.DrainedSlope_WT_O = {}
    with open(self.DrainedSlope_WT_O_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.DrainedSlope_WT_O[(key)] = val

    # Convert strings to floats as necessary
    self.DrainedSlope_WT_O['A1_above']    = float(self.DrainedSlope_WT_O['A1_above'])
    self.DrainedSlope_WT_O['A2_above']    = float(self.DrainedSlope_WT_O['A2_above'])
    self.DrainedSlope_WT_O['x0_above']    = float(self.DrainedSlope_WT_O['x0_above'])
    self.DrainedSlope_WT_O['dx_above']    = float(self.DrainedSlope_WT_O['dx_above'])
    self.DrainedSlope_WT_O['A1_below']    = float(self.DrainedSlope_WT_O['A1_below'])
    self.DrainedSlope_WT_O['A2_below']    = float(self.DrainedSlope_WT_O['A2_below'])
    self.DrainedSlope_WT_O['x0_below']    = float(self.DrainedSlope_WT_O['x0_below'])
    self.DrainedSlope_WT_O['dx_below']    = float(self.DrainedSlope_WT_O['dx_below'])
    self.DrainedSlope_WT_O['a_above']     = float(self.DrainedSlope_WT_O['a_above'])
    self.DrainedSlope_WT_O['b_above']     = float(self.DrainedSlope_WT_O['b_above'])
    self.DrainedSlope_WT_O['a_below']     = float(self.DrainedSlope_WT_O['a_below'])
    self.DrainedSlope_WT_O['b_below']     = float(self.DrainedSlope_WT_O['b_below'])
    self.DrainedSlope_WT_O['K_above']     = float(self.DrainedSlope_WT_O['K_above'])
    self.DrainedSlope_WT_O['C_above']     = float(self.DrainedSlope_WT_O['C_above'])
    self.DrainedSlope_WT_O['A_above']     = float(self.DrainedSlope_WT_O['A_above'])
    self.DrainedSlope_WT_O['B_above']     = float(self.DrainedSlope_WT_O['B_above'])
    self.DrainedSlope_WT_O['K_below']     = float(self.DrainedSlope_WT_O['K_below'])
    self.DrainedSlope_WT_O['C_below']     = float(self.DrainedSlope_WT_O['C_below'])
    self.DrainedSlope_WT_O['A_below']     = float(self.DrainedSlope_WT_O['A_below'])
    self.DrainedSlope_WT_O['B_below']     = float(self.DrainedSlope_WT_O['B_below'])
    self.DrainedSlope_WT_O['HillB_above'] = float(self.DrainedSlope_WT_O['HillB_above'])
    self.DrainedSlope_WT_O['HillN_above'] = float(self.DrainedSlope_WT_O['HillN_above'])
    self.DrainedSlope_WT_O['HillB_below'] = float(self.DrainedSlope_WT_O['HillB_below'])
    self.DrainedSlope_WT_O['HillN_below'] = float(self.DrainedSlope_WT_O['HillN_below'])
    self.DrainedSlope_WT_O['max_terrain_transition'] = \
      float(self.DrainedSlope_WT_O['max_terrain_transition'])
    self.DrainedSlope_WT_O['ice_slope_poor']    = float(self.DrainedSlope_WT_O['ice_slope_poor'])
    self.DrainedSlope_WT_O['ice_slope_pore']    = float(self.DrainedSlope_WT_O['ice_slope_pore'])
    self.DrainedSlope_WT_O['ice_slope_wedge']   = float(self.DrainedSlope_WT_O['ice_slope_wedge'])
    self.DrainedSlope_WT_O['ice_slope_massive'] = float(self.DrainedSlope_WT_O['ice_slope_massive'])
    self.DrainedSlope_WT_O['porosity'] = float(self.DrainedSlope_WT_O['porosity'])    

#====================================================================================
def FCP_WT(self):
    
    print '    ..Reading Wetland Tundra Flat Center Polygon Parameters'

    """ Read files from the input directory """
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'arctic_coast':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Arctic/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'aiem':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/AIEM/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'ngee':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/NGEE/'+\
                 self.Control_directory)

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Young Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Young age parameters'
    
    self.FCP_WT_Y = {}
    with open(self.FCP_WT_Y_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.FCP_WT_Y[(key)] = val

    # Convert strings to floats as necessary
    self.FCP_WT_Y['A1_above']    = float(self.FCP_WT_Y['A1_above'])
    self.FCP_WT_Y['A2_above']    = float(self.FCP_WT_Y['A2_above'])
    self.FCP_WT_Y['x0_above']    = float(self.FCP_WT_Y['x0_above'])
    self.FCP_WT_Y['dx_above']    = float(self.FCP_WT_Y['dx_above'])
    self.FCP_WT_Y['A1_below']    = float(self.FCP_WT_Y['A1_below'])
    self.FCP_WT_Y['A2_below']    = float(self.FCP_WT_Y['A2_below'])
    self.FCP_WT_Y['x0_below']    = float(self.FCP_WT_Y['x0_below'])
    self.FCP_WT_Y['dx_below']    = float(self.FCP_WT_Y['dx_below'])
    self.FCP_WT_Y['a_above']     = float(self.FCP_WT_Y['a_above'])
    self.FCP_WT_Y['b_above']     = float(self.FCP_WT_Y['b_above'])
    self.FCP_WT_Y['a_below']     = float(self.FCP_WT_Y['a_below'])
    self.FCP_WT_Y['b_below']     = float(self.FCP_WT_Y['b_below'])
    self.FCP_WT_Y['K_above']     = float(self.FCP_WT_Y['K_above'])
    self.FCP_WT_Y['C_above']     = float(self.FCP_WT_Y['C_above'])
    self.FCP_WT_Y['A_above']     = float(self.FCP_WT_Y['A_above'])
    self.FCP_WT_Y['B_above']     = float(self.FCP_WT_Y['B_above'])
    self.FCP_WT_Y['K_below']     = float(self.FCP_WT_Y['K_below'])
    self.FCP_WT_Y['C_below']     = float(self.FCP_WT_Y['C_below'])
    self.FCP_WT_Y['A_below']     = float(self.FCP_WT_Y['A_below'])
    self.FCP_WT_Y['B_below']     = float(self.FCP_WT_Y['B_below'])
    self.FCP_WT_Y['HillB_above'] = float(self.FCP_WT_Y['HillB_above'])
    self.FCP_WT_Y['HillN_above'] = float(self.FCP_WT_Y['HillN_above'])
    self.FCP_WT_Y['HillB_below'] = float(self.FCP_WT_Y['HillB_below'])
    self.FCP_WT_Y['HillN_below'] = float(self.FCP_WT_Y['HillN_below'])
    self.FCP_WT_Y['max_terrain_transition'] = \
      float(self.FCP_WT_Y['max_terrain_transition'])
    self.FCP_WT_Y['ice_slope_poor']    = float(self.FCP_WT_Y['ice_slope_poor'])
    self.FCP_WT_Y['ice_slope_pore']    = float(self.FCP_WT_Y['ice_slope_pore'])
    self.FCP_WT_Y['ice_slope_wedge']   = float(self.FCP_WT_Y['ice_slope_wedge'])
    self.FCP_WT_Y['ice_slope_massive'] = float(self.FCP_WT_Y['ice_slope_massive'])
    self.FCP_WT_Y['porosity'] = float(self.FCP_WT_Y['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Medium Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Medium age parameters'
    
    self.FCP_WT_M = {}
    with open(self.FCP_WT_M_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.FCP_WT_M[(key)] = val

    # Convert strings to floats as necessary
    self.FCP_WT_M['A1_above']    = float(self.FCP_WT_M['A1_above'])
    self.FCP_WT_M['A2_above']    = float(self.FCP_WT_M['A2_above'])
    self.FCP_WT_M['x0_above']    = float(self.FCP_WT_M['x0_above'])
    self.FCP_WT_M['dx_above']    = float(self.FCP_WT_M['dx_above'])
    self.FCP_WT_M['A1_below']    = float(self.FCP_WT_M['A1_below'])
    self.FCP_WT_M['A2_below']    = float(self.FCP_WT_M['A2_below'])
    self.FCP_WT_M['x0_below']    = float(self.FCP_WT_M['x0_below'])
    self.FCP_WT_M['dx_below']    = float(self.FCP_WT_M['dx_below'])
    self.FCP_WT_M['a_above']     = float(self.FCP_WT_M['a_above'])
    self.FCP_WT_M['b_above']     = float(self.FCP_WT_M['b_above'])
    self.FCP_WT_M['a_below']     = float(self.FCP_WT_M['a_below'])
    self.FCP_WT_M['b_below']     = float(self.FCP_WT_M['b_below'])
    self.FCP_WT_M['K_above']     = float(self.FCP_WT_M['K_above'])
    self.FCP_WT_M['C_above']     = float(self.FCP_WT_M['C_above'])
    self.FCP_WT_M['A_above']     = float(self.FCP_WT_M['A_above'])
    self.FCP_WT_M['B_above']     = float(self.FCP_WT_M['B_above'])
    self.FCP_WT_M['K_below']     = float(self.FCP_WT_M['K_below'])
    self.FCP_WT_M['C_below']     = float(self.FCP_WT_M['C_below'])
    self.FCP_WT_M['A_below']     = float(self.FCP_WT_M['A_below'])
    self.FCP_WT_M['B_below']     = float(self.FCP_WT_M['B_below'])
    self.FCP_WT_M['HillB_above'] = float(self.FCP_WT_M['HillB_above'])
    self.FCP_WT_M['HillN_above'] = float(self.FCP_WT_M['HillN_above'])
    self.FCP_WT_M['HillB_below'] = float(self.FCP_WT_M['HillB_below'])
    self.FCP_WT_M['HillN_below'] = float(self.FCP_WT_M['HillN_below'])
    self.FCP_WT_M['max_terrain_transition'] = \
      float(self.FCP_WT_M['max_terrain_transition'])
    self.FCP_WT_M['ice_slope_poor']    = float(self.FCP_WT_M['ice_slope_poor'])
    self.FCP_WT_M['ice_slope_pore']    = float(self.FCP_WT_M['ice_slope_pore'])
    self.FCP_WT_M['ice_slope_wedge']   = float(self.FCP_WT_M['ice_slope_wedge'])
    self.FCP_WT_M['ice_slope_massive'] = float(self.FCP_WT_M['ice_slope_massive'])
    self.FCP_WT_M['porosity'] = float(self.FCP_WT_M['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Old Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Old age parameters'
    
    self.FCP_WT_O = {}
    with open(self.FCP_WT_O_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.FCP_WT_O[(key)] = val

    # Convert strings to floats as necessary
    self.FCP_WT_O['A1_above']    = float(self.FCP_WT_O['A1_above'])
    self.FCP_WT_O['A2_above']    = float(self.FCP_WT_O['A2_above'])
    self.FCP_WT_O['x0_above']    = float(self.FCP_WT_O['x0_above'])
    self.FCP_WT_O['dx_above']    = float(self.FCP_WT_O['dx_above'])
    self.FCP_WT_O['A1_below']    = float(self.FCP_WT_O['A1_below'])
    self.FCP_WT_O['A2_below']    = float(self.FCP_WT_O['A2_below'])
    self.FCP_WT_O['x0_below']    = float(self.FCP_WT_O['x0_below'])
    self.FCP_WT_O['dx_below']    = float(self.FCP_WT_O['dx_below'])
    self.FCP_WT_O['a_above']     = float(self.FCP_WT_O['a_above'])
    self.FCP_WT_O['b_above']     = float(self.FCP_WT_O['b_above'])
    self.FCP_WT_O['a_below']     = float(self.FCP_WT_O['a_below'])
    self.FCP_WT_O['b_below']     = float(self.FCP_WT_O['b_below'])
    self.FCP_WT_O['K_above']     = float(self.FCP_WT_O['K_above'])
    self.FCP_WT_O['C_above']     = float(self.FCP_WT_O['C_above'])
    self.FCP_WT_O['A_above']     = float(self.FCP_WT_O['A_above'])
    self.FCP_WT_O['B_above']     = float(self.FCP_WT_O['B_above'])
    self.FCP_WT_O['K_below']     = float(self.FCP_WT_O['K_below'])
    self.FCP_WT_O['C_below']     = float(self.FCP_WT_O['C_below'])
    self.FCP_WT_O['A_below']     = float(self.FCP_WT_O['A_below'])
    self.FCP_WT_O['B_below']     = float(self.FCP_WT_O['B_below'])
    self.FCP_WT_O['HillB_above'] = float(self.FCP_WT_O['HillB_above'])
    self.FCP_WT_O['HillN_above'] = float(self.FCP_WT_O['HillN_above'])
    self.FCP_WT_O['HillB_below'] = float(self.FCP_WT_O['HillB_below'])
    self.FCP_WT_O['HillN_below'] = float(self.FCP_WT_O['HillN_below'])
    self.FCP_WT_O['max_terrain_transition'] = \
      float(self.FCP_WT_O['max_terrain_transition'])
    self.FCP_WT_O['ice_slope_poor']    = float(self.FCP_WT_O['ice_slope_poor'])
    self.FCP_WT_O['ice_slope_pore']    = float(self.FCP_WT_O['ice_slope_pore'])
    self.FCP_WT_O['ice_slope_wedge']   = float(self.FCP_WT_O['ice_slope_wedge'])
    self.FCP_WT_O['ice_slope_massive'] = float(self.FCP_WT_O['ice_slope_massive'])
    self.FCP_WT_O['porosity'] = float(self.FCP_WT_O['porosity'])    

#====================================================================================
def HCP_WT(self):
    
    print '    ..Reading Wetland Tundra High Center Polygon Parameters'

    """ Read files from the input directory """
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'arctic_coast':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Arctic/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'aiem':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/AIEM/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'ngee':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/NGEE/'+\
                 self.Control_directory)

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Young Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Young age parameters'
    
    self.HCP_WT_Y = {}
    with open(self.HCP_WT_Y_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.HCP_WT_Y[(key)] = val

    # Convert strings to floats as necessary
    self.HCP_WT_Y['A1_above']    = float(self.HCP_WT_Y['A1_above'])
    self.HCP_WT_Y['A2_above']    = float(self.HCP_WT_Y['A2_above'])
    self.HCP_WT_Y['x0_above']    = float(self.HCP_WT_Y['x0_above'])
    self.HCP_WT_Y['dx_above']    = float(self.HCP_WT_Y['dx_above'])
    self.HCP_WT_Y['A1_below']    = float(self.HCP_WT_Y['A1_below'])
    self.HCP_WT_Y['A2_below']    = float(self.HCP_WT_Y['A2_below'])
    self.HCP_WT_Y['x0_below']    = float(self.HCP_WT_Y['x0_below'])
    self.HCP_WT_Y['dx_below']    = float(self.HCP_WT_Y['dx_below'])
    self.HCP_WT_Y['a_above']     = float(self.HCP_WT_Y['a_above'])
    self.HCP_WT_Y['b_above']     = float(self.HCP_WT_Y['b_above'])
    self.HCP_WT_Y['a_below']     = float(self.HCP_WT_Y['a_below'])
    self.HCP_WT_Y['b_below']     = float(self.HCP_WT_Y['b_below'])
    self.HCP_WT_Y['K_above']     = float(self.HCP_WT_Y['K_above'])
    self.HCP_WT_Y['C_above']     = float(self.HCP_WT_Y['C_above'])
    self.HCP_WT_Y['A_above']     = float(self.HCP_WT_Y['A_above'])
    self.HCP_WT_Y['B_above']     = float(self.HCP_WT_Y['B_above'])
    self.HCP_WT_Y['K_below']     = float(self.HCP_WT_Y['K_below'])
    self.HCP_WT_Y['C_below']     = float(self.HCP_WT_Y['C_below'])
    self.HCP_WT_Y['A_below']     = float(self.HCP_WT_Y['A_below'])
    self.HCP_WT_Y['B_below']     = float(self.HCP_WT_Y['B_below'])
    self.HCP_WT_Y['HillB_above'] = float(self.HCP_WT_Y['HillB_above'])
    self.HCP_WT_Y['HillN_above'] = float(self.HCP_WT_Y['HillN_above'])
    self.HCP_WT_Y['HillB_below'] = float(self.HCP_WT_Y['HillB_below'])
    self.HCP_WT_Y['HillN_below'] = float(self.HCP_WT_Y['HillN_below'])
    self.HCP_WT_Y['max_terrain_transition'] = \
      float(self.HCP_WT_Y['max_terrain_transition'])
    self.HCP_WT_Y['ice_slope_poor']    = float(self.HCP_WT_Y['ice_slope_poor'])
    self.HCP_WT_Y['ice_slope_pore']    = float(self.HCP_WT_Y['ice_slope_pore'])
    self.HCP_WT_Y['ice_slope_wedge']   = float(self.HCP_WT_Y['ice_slope_wedge'])
    self.HCP_WT_Y['ice_slope_massive'] = float(self.HCP_WT_Y['ice_slope_massive'])
    self.HCP_WT_Y['porosity'] = float(self.HCP_WT_Y['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Medium Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Medium age parameters'
    
    self.HCP_WT_M = {}
    with open(self.HCP_WT_M_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.HCP_WT_M[(key)] = val

    # Convert strings to floats as necessary
    self.HCP_WT_M['A1_above']    = float(self.HCP_WT_M['A1_above'])
    self.HCP_WT_M['A2_above']    = float(self.HCP_WT_M['A2_above'])
    self.HCP_WT_M['x0_above']    = float(self.HCP_WT_M['x0_above'])
    self.HCP_WT_M['dx_above']    = float(self.HCP_WT_M['dx_above'])
    self.HCP_WT_M['A1_below']    = float(self.HCP_WT_M['A1_below'])
    self.HCP_WT_M['A2_below']    = float(self.HCP_WT_M['A2_below'])
    self.HCP_WT_M['x0_below']    = float(self.HCP_WT_M['x0_below'])
    self.HCP_WT_M['dx_below']    = float(self.HCP_WT_M['dx_below'])
    self.HCP_WT_M['a_above']     = float(self.HCP_WT_M['a_above'])
    self.HCP_WT_M['b_above']     = float(self.HCP_WT_M['b_above'])
    self.HCP_WT_M['a_below']     = float(self.HCP_WT_M['a_below'])
    self.HCP_WT_M['b_below']     = float(self.HCP_WT_M['b_below'])
    self.HCP_WT_M['K_above']     = float(self.HCP_WT_M['K_above'])
    self.HCP_WT_M['C_above']     = float(self.HCP_WT_M['C_above'])
    self.HCP_WT_M['A_above']     = float(self.HCP_WT_M['A_above'])
    self.HCP_WT_M['B_above']     = float(self.HCP_WT_M['B_above'])
    self.HCP_WT_M['K_below']     = float(self.HCP_WT_M['K_below'])
    self.HCP_WT_M['C_below']     = float(self.HCP_WT_M['C_below'])
    self.HCP_WT_M['A_below']     = float(self.HCP_WT_M['A_below'])
    self.HCP_WT_M['B_below']     = float(self.HCP_WT_M['B_below'])
    self.HCP_WT_M['HillB_above'] = float(self.HCP_WT_M['HillB_above'])
    self.HCP_WT_M['HillN_above'] = float(self.HCP_WT_M['HillN_above'])
    self.HCP_WT_M['HillB_below'] = float(self.HCP_WT_M['HillB_below'])
    self.HCP_WT_M['HillN_below'] = float(self.HCP_WT_M['HillN_below'])
    self.HCP_WT_M['max_terrain_transition'] = \
      float(self.HCP_WT_M['max_terrain_transition'])
    self.HCP_WT_M['ice_slope_poor']    = float(self.HCP_WT_M['ice_slope_poor'])
    self.HCP_WT_M['ice_slope_pore']    = float(self.HCP_WT_M['ice_slope_pore'])
    self.HCP_WT_M['ice_slope_wedge']   = float(self.HCP_WT_M['ice_slope_wedge'])
    self.HCP_WT_M['ice_slope_massive'] = float(self.HCP_WT_M['ice_slope_massive'])
    self.HCP_WT_M['porosity'] = float(self.HCP_WT_M['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Old Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Old age parameters'
    
    self.HCP_WT_O = {}
    with open(self.HCP_WT_O_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.HCP_WT_O[(key)] = val

    # Convert strings to floats as necessary
    self.HCP_WT_O['A1_above']    = float(self.HCP_WT_O['A1_above'])
    self.HCP_WT_O['A2_above']    = float(self.HCP_WT_O['A2_above'])
    self.HCP_WT_O['x0_above']    = float(self.HCP_WT_O['x0_above'])
    self.HCP_WT_O['dx_above']    = float(self.HCP_WT_O['dx_above'])
    self.HCP_WT_O['A1_below']    = float(self.HCP_WT_O['A1_below'])
    self.HCP_WT_O['A2_below']    = float(self.HCP_WT_O['A2_below'])
    self.HCP_WT_O['x0_below']    = float(self.HCP_WT_O['x0_below'])
    self.HCP_WT_O['dx_below']    = float(self.HCP_WT_O['dx_below'])
    self.HCP_WT_O['a_above']     = float(self.HCP_WT_O['a_above'])
    self.HCP_WT_O['b_above']     = float(self.HCP_WT_O['b_above'])
    self.HCP_WT_O['a_below']     = float(self.HCP_WT_O['a_below'])
    self.HCP_WT_O['b_below']     = float(self.HCP_WT_O['b_below'])
    self.HCP_WT_O['K_above']     = float(self.HCP_WT_O['K_above'])
    self.HCP_WT_O['C_above']     = float(self.HCP_WT_O['C_above'])
    self.HCP_WT_O['A_above']     = float(self.HCP_WT_O['A_above'])
    self.HCP_WT_O['B_above']     = float(self.HCP_WT_O['B_above'])
    self.HCP_WT_O['K_below']     = float(self.HCP_WT_O['K_below'])
    self.HCP_WT_O['C_below']     = float(self.HCP_WT_O['C_below'])
    self.HCP_WT_O['A_below']     = float(self.HCP_WT_O['A_below'])
    self.HCP_WT_O['B_below']     = float(self.HCP_WT_O['B_below'])
    self.HCP_WT_O['HillB_above'] = float(self.HCP_WT_O['HillB_above'])
    self.HCP_WT_O['HillN_above'] = float(self.HCP_WT_O['HillN_above'])
    self.HCP_WT_O['HillB_below'] = float(self.HCP_WT_O['HillB_below'])
    self.HCP_WT_O['HillN_below'] = float(self.HCP_WT_O['HillN_below'])
    self.HCP_WT_O['max_terrain_transition'] = \
      float(self.HCP_WT_O['max_terrain_transition'])
    self.HCP_WT_O['ice_slope_poor']    = float(self.HCP_WT_O['ice_slope_poor'])
    self.HCP_WT_O['ice_slope_pore']    = float(self.HCP_WT_O['ice_slope_pore'])
    self.HCP_WT_O['ice_slope_wedge']   = float(self.HCP_WT_O['ice_slope_wedge'])
    self.HCP_WT_O['ice_slope_massive'] = float(self.HCP_WT_O['ice_slope_massive'])
    self.HCP_WT_O['porosity'] = float(self.HCP_WT_O['porosity'])    

#====================================================================================
def LCP_WT(self):
    
    print '    ..Reading Wetland Tundra Low Center Polygon Parameters'

    """ Read files from the input directory """
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'arctic_coast':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Arctic/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'aiem':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/AIEM/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'ngee':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/NGEE/'+\
                 self.Control_directory)

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Young Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Young age parameters'
    
    self.LCP_WT_Y = {}
    with open(self.LCP_WT_Y_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.LCP_WT_Y[(key)] = val

    # Convert strings to floats as necessary
    self.LCP_WT_Y['A1_above']    = float(self.LCP_WT_Y['A1_above'])
    self.LCP_WT_Y['A2_above']    = float(self.LCP_WT_Y['A2_above'])
    self.LCP_WT_Y['x0_above']    = float(self.LCP_WT_Y['x0_above'])
    self.LCP_WT_Y['dx_above']    = float(self.LCP_WT_Y['dx_above'])
    self.LCP_WT_Y['A1_below']    = float(self.LCP_WT_Y['A1_below'])
    self.LCP_WT_Y['A2_below']    = float(self.LCP_WT_Y['A2_below'])
    self.LCP_WT_Y['x0_below']    = float(self.LCP_WT_Y['x0_below'])
    self.LCP_WT_Y['dx_below']    = float(self.LCP_WT_Y['dx_below'])
    self.LCP_WT_Y['a_above']     = float(self.LCP_WT_Y['a_above'])
    self.LCP_WT_Y['b_above']     = float(self.LCP_WT_Y['b_above'])
    self.LCP_WT_Y['a_below']     = float(self.LCP_WT_Y['a_below'])
    self.LCP_WT_Y['b_below']     = float(self.LCP_WT_Y['b_below'])
    self.LCP_WT_Y['K_above']     = float(self.LCP_WT_Y['K_above'])
    self.LCP_WT_Y['C_above']     = float(self.LCP_WT_Y['C_above'])
    self.LCP_WT_Y['A_above']     = float(self.LCP_WT_Y['A_above'])
    self.LCP_WT_Y['B_above']     = float(self.LCP_WT_Y['B_above'])
    self.LCP_WT_Y['K_below']     = float(self.LCP_WT_Y['K_below'])
    self.LCP_WT_Y['C_below']     = float(self.LCP_WT_Y['C_below'])
    self.LCP_WT_Y['A_below']     = float(self.LCP_WT_Y['A_below'])
    self.LCP_WT_Y['B_below']     = float(self.LCP_WT_Y['B_below'])
    self.LCP_WT_Y['HillB_above'] = float(self.LCP_WT_Y['HillB_above'])
    self.LCP_WT_Y['HillN_above'] = float(self.LCP_WT_Y['HillN_above'])
    self.LCP_WT_Y['HillB_below'] = float(self.LCP_WT_Y['HillB_below'])
    self.LCP_WT_Y['HillN_below'] = float(self.LCP_WT_Y['HillN_below'])
    self.LCP_WT_Y['max_terrain_transition'] = \
      float(self.LCP_WT_Y['max_terrain_transition'])
    self.LCP_WT_Y['ice_slope_poor']    = float(self.LCP_WT_Y['ice_slope_poor'])
    self.LCP_WT_Y['ice_slope_pore']    = float(self.LCP_WT_Y['ice_slope_pore'])
    self.LCP_WT_Y['ice_slope_wedge']   = float(self.LCP_WT_Y['ice_slope_wedge'])
    self.LCP_WT_Y['ice_slope_massive'] = float(self.LCP_WT_Y['ice_slope_massive'])
    self.LCP_WT_Y['porosity'] = float(self.LCP_WT_Y['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Medium Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Medium age parameters'
    
    self.LCP_WT_M = {}
    with open(self.LCP_WT_M_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.LCP_WT_M[(key)] = val

    # Convert strings to floats as necessary
    self.LCP_WT_M['A1_above']    = float(self.LCP_WT_M['A1_above'])
    self.LCP_WT_M['A2_above']    = float(self.LCP_WT_M['A2_above'])
    self.LCP_WT_M['x0_above']    = float(self.LCP_WT_M['x0_above'])
    self.LCP_WT_M['dx_above']    = float(self.LCP_WT_M['dx_above'])
    self.LCP_WT_M['A1_below']    = float(self.LCP_WT_M['A1_below'])
    self.LCP_WT_M['A2_below']    = float(self.LCP_WT_M['A2_below'])
    self.LCP_WT_M['x0_below']    = float(self.LCP_WT_M['x0_below'])
    self.LCP_WT_M['dx_below']    = float(self.LCP_WT_M['dx_below'])
    self.LCP_WT_M['a_above']     = float(self.LCP_WT_M['a_above'])
    self.LCP_WT_M['b_above']     = float(self.LCP_WT_M['b_above'])
    self.LCP_WT_M['a_below']     = float(self.LCP_WT_M['a_below'])
    self.LCP_WT_M['b_below']     = float(self.LCP_WT_M['b_below'])
    self.LCP_WT_M['K_above']     = float(self.LCP_WT_M['K_above'])
    self.LCP_WT_M['C_above']     = float(self.LCP_WT_M['C_above'])
    self.LCP_WT_M['A_above']     = float(self.LCP_WT_M['A_above'])
    self.LCP_WT_M['B_above']     = float(self.LCP_WT_M['B_above'])
    self.LCP_WT_M['K_below']     = float(self.LCP_WT_M['K_below'])
    self.LCP_WT_M['C_below']     = float(self.LCP_WT_M['C_below'])
    self.LCP_WT_M['A_below']     = float(self.LCP_WT_M['A_below'])
    self.LCP_WT_M['B_below']     = float(self.LCP_WT_M['B_below'])
    self.LCP_WT_M['HillB_above'] = float(self.LCP_WT_M['HillB_above'])
    self.LCP_WT_M['HillN_above'] = float(self.LCP_WT_M['HillN_above'])
    self.LCP_WT_M['HillB_below'] = float(self.LCP_WT_M['HillB_below'])
    self.LCP_WT_M['HillN_below'] = float(self.LCP_WT_M['HillN_below'])
    self.LCP_WT_M['max_terrain_transition'] = \
      float(self.LCP_WT_M['max_terrain_transition'])
    self.LCP_WT_M['ice_slope_poor']    = float(self.LCP_WT_M['ice_slope_poor'])
    self.LCP_WT_M['ice_slope_pore']    = float(self.LCP_WT_M['ice_slope_pore'])
    self.LCP_WT_M['ice_slope_wedge']   = float(self.LCP_WT_M['ice_slope_wedge'])
    self.LCP_WT_M['ice_slope_massive'] = float(self.LCP_WT_M['ice_slope_massive'])
    self.LCP_WT_M['porosity'] = float(self.LCP_WT_M['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Old Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Old age parameters'
    
    self.LCP_WT_O = {}
    with open(self.LCP_WT_O_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.LCP_WT_O[(key)] = val

    # Convert strings to floats as necessary
    self.LCP_WT_O['A1_above']    = float(self.LCP_WT_O['A1_above'])
    self.LCP_WT_O['A2_above']    = float(self.LCP_WT_O['A2_above'])
    self.LCP_WT_O['x0_above']    = float(self.LCP_WT_O['x0_above'])
    self.LCP_WT_O['dx_above']    = float(self.LCP_WT_O['dx_above'])
    self.LCP_WT_O['A1_below']    = float(self.LCP_WT_O['A1_below'])
    self.LCP_WT_O['A2_below']    = float(self.LCP_WT_O['A2_below'])
    self.LCP_WT_O['x0_below']    = float(self.LCP_WT_O['x0_below'])
    self.LCP_WT_O['dx_below']    = float(self.LCP_WT_O['dx_below'])
    self.LCP_WT_O['a_above']     = float(self.LCP_WT_O['a_above'])
    self.LCP_WT_O['b_above']     = float(self.LCP_WT_O['b_above'])
    self.LCP_WT_O['a_below']     = float(self.LCP_WT_O['a_below'])
    self.LCP_WT_O['b_below']     = float(self.LCP_WT_O['b_below'])
    self.LCP_WT_O['K_above']     = float(self.LCP_WT_O['K_above'])
    self.LCP_WT_O['C_above']     = float(self.LCP_WT_O['C_above'])
    self.LCP_WT_O['A_above']     = float(self.LCP_WT_O['A_above'])
    self.LCP_WT_O['B_above']     = float(self.LCP_WT_O['B_above'])
    self.LCP_WT_O['K_below']     = float(self.LCP_WT_O['K_below'])
    self.LCP_WT_O['C_below']     = float(self.LCP_WT_O['C_below'])
    self.LCP_WT_O['A_below']     = float(self.LCP_WT_O['A_below'])
    self.LCP_WT_O['B_below']     = float(self.LCP_WT_O['B_below'])
    self.LCP_WT_O['HillB_above'] = float(self.LCP_WT_O['HillB_above'])
    self.LCP_WT_O['HillN_above'] = float(self.LCP_WT_O['HillN_above'])
    self.LCP_WT_O['HillB_below'] = float(self.LCP_WT_O['HillB_below'])
    self.LCP_WT_O['HillN_below'] = float(self.LCP_WT_O['HillN_below'])
    self.LCP_WT_O['max_terrain_transition'] = \
      float(self.LCP_WT_O['max_terrain_transition'])
    self.LCP_WT_O['ice_slope_poor']    = float(self.LCP_WT_O['ice_slope_poor'])
    self.LCP_WT_O['ice_slope_pore']    = float(self.LCP_WT_O['ice_slope_pore'])
    self.LCP_WT_O['ice_slope_wedge']   = float(self.LCP_WT_O['ice_slope_wedge'])
    self.LCP_WT_O['ice_slope_massive'] = float(self.LCP_WT_O['ice_slope_massive'])
    self.LCP_WT_O['porosity'] = float(self.LCP_WT_O['porosity'])    

#====================================================================================
def Meadow_WT(self):
    
    print '    ..Reading Wetland Tundra Meadow Parameters'

    """ Read files from the input directory """
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'arctic_coast':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Arctic/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'aiem':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/AIEM/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'ngee':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/NGEE/'+\
                 self.Control_directory)

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Young Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Young age parameters'
    
    self.Meadow_WT_Y = {}
    with open(self.Meadow_WT_Y_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.Meadow_WT_Y[(key)] = val

    # Convert strings to floats as necessary
    self.Meadow_WT_Y['A1_above']    = float(self.Meadow_WT_Y['A1_above'])
    self.Meadow_WT_Y['A2_above']    = float(self.Meadow_WT_Y['A2_above'])
    self.Meadow_WT_Y['x0_above']    = float(self.Meadow_WT_Y['x0_above'])
    self.Meadow_WT_Y['dx_above']    = float(self.Meadow_WT_Y['dx_above'])
    self.Meadow_WT_Y['A1_below']    = float(self.Meadow_WT_Y['A1_below'])
    self.Meadow_WT_Y['A2_below']    = float(self.Meadow_WT_Y['A2_below'])
    self.Meadow_WT_Y['x0_below']    = float(self.Meadow_WT_Y['x0_below'])
    self.Meadow_WT_Y['dx_below']    = float(self.Meadow_WT_Y['dx_below'])
    self.Meadow_WT_Y['a_above']     = float(self.Meadow_WT_Y['a_above'])
    self.Meadow_WT_Y['b_above']     = float(self.Meadow_WT_Y['b_above'])
    self.Meadow_WT_Y['a_below']     = float(self.Meadow_WT_Y['a_below'])
    self.Meadow_WT_Y['b_below']     = float(self.Meadow_WT_Y['b_below'])
    self.Meadow_WT_Y['K_above']     = float(self.Meadow_WT_Y['K_above'])
    self.Meadow_WT_Y['C_above']     = float(self.Meadow_WT_Y['C_above'])
    self.Meadow_WT_Y['A_above']     = float(self.Meadow_WT_Y['A_above'])
    self.Meadow_WT_Y['B_above']     = float(self.Meadow_WT_Y['B_above'])
    self.Meadow_WT_Y['K_below']     = float(self.Meadow_WT_Y['K_below'])
    self.Meadow_WT_Y['C_below']     = float(self.Meadow_WT_Y['C_below'])
    self.Meadow_WT_Y['A_below']     = float(self.Meadow_WT_Y['A_below'])
    self.Meadow_WT_Y['B_below']     = float(self.Meadow_WT_Y['B_below'])
    self.Meadow_WT_Y['HillB_above'] = float(self.Meadow_WT_Y['HillB_above'])
    self.Meadow_WT_Y['HillN_above'] = float(self.Meadow_WT_Y['HillN_above'])
    self.Meadow_WT_Y['HillB_below'] = float(self.Meadow_WT_Y['HillB_below'])
    self.Meadow_WT_Y['HillN_below'] = float(self.Meadow_WT_Y['HillN_below'])
    self.Meadow_WT_Y['max_terrain_transition'] = \
      float(self.Meadow_WT_Y['max_terrain_transition'])
    self.Meadow_WT_Y['ice_slope_poor']    = float(self.Meadow_WT_Y['ice_slope_poor'])
    self.Meadow_WT_Y['ice_slope_pore']    = float(self.Meadow_WT_Y['ice_slope_pore'])
    self.Meadow_WT_Y['ice_slope_wedge']   = float(self.Meadow_WT_Y['ice_slope_wedge'])
    self.Meadow_WT_Y['ice_slope_massive'] = float(self.Meadow_WT_Y['ice_slope_massive'])
    self.Meadow_WT_Y['porosity'] = float(self.Meadow_WT_Y['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Medium Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Medium age parameters'
    
    self.Meadow_WT_M = {}
    with open(self.Meadow_WT_M_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.Meadow_WT_M[(key)] = val

    # Convert strings to floats as necessary
    self.Meadow_WT_M['A1_above']    = float(self.Meadow_WT_M['A1_above'])
    self.Meadow_WT_M['A2_above']    = float(self.Meadow_WT_M['A2_above'])
    self.Meadow_WT_M['x0_above']    = float(self.Meadow_WT_M['x0_above'])
    self.Meadow_WT_M['dx_above']    = float(self.Meadow_WT_M['dx_above'])
    self.Meadow_WT_M['A1_below']    = float(self.Meadow_WT_M['A1_below'])
    self.Meadow_WT_M['A2_below']    = float(self.Meadow_WT_M['A2_below'])
    self.Meadow_WT_M['x0_below']    = float(self.Meadow_WT_M['x0_below'])
    self.Meadow_WT_M['dx_below']    = float(self.Meadow_WT_M['dx_below'])
    self.Meadow_WT_M['a_above']     = float(self.Meadow_WT_M['a_above'])
    self.Meadow_WT_M['b_above']     = float(self.Meadow_WT_M['b_above'])
    self.Meadow_WT_M['a_below']     = float(self.Meadow_WT_M['a_below'])
    self.Meadow_WT_M['b_below']     = float(self.Meadow_WT_M['b_below'])
    self.Meadow_WT_M['K_above']     = float(self.Meadow_WT_M['K_above'])
    self.Meadow_WT_M['C_above']     = float(self.Meadow_WT_M['C_above'])
    self.Meadow_WT_M['A_above']     = float(self.Meadow_WT_M['A_above'])
    self.Meadow_WT_M['B_above']     = float(self.Meadow_WT_M['B_above'])
    self.Meadow_WT_M['K_below']     = float(self.Meadow_WT_M['K_below'])
    self.Meadow_WT_M['C_below']     = float(self.Meadow_WT_M['C_below'])
    self.Meadow_WT_M['A_below']     = float(self.Meadow_WT_M['A_below'])
    self.Meadow_WT_M['B_below']     = float(self.Meadow_WT_M['B_below'])
    self.Meadow_WT_M['HillB_above'] = float(self.Meadow_WT_M['HillB_above'])
    self.Meadow_WT_M['HillN_above'] = float(self.Meadow_WT_M['HillN_above'])
    self.Meadow_WT_M['HillB_below'] = float(self.Meadow_WT_M['HillB_below'])
    self.Meadow_WT_M['HillN_below'] = float(self.Meadow_WT_M['HillN_below'])
    self.Meadow_WT_M['max_terrain_transition'] = \
      float(self.Meadow_WT_M['max_terrain_transition'])
    self.Meadow_WT_M['ice_slope_poor']    = float(self.Meadow_WT_M['ice_slope_poor'])
    self.Meadow_WT_M['ice_slope_pore']    = float(self.Meadow_WT_M['ice_slope_pore'])
    self.Meadow_WT_M['ice_slope_wedge']   = float(self.Meadow_WT_M['ice_slope_wedge'])
    self.Meadow_WT_M['ice_slope_massive'] = float(self.Meadow_WT_M['ice_slope_massive'])
    self.Meadow_WT_M['porosity'] = float(self.Meadow_WT_M['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Old Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Old age parameters'
    
    self.Meadow_WT_O = {}
    with open(self.Meadow_WT_O_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.Meadow_WT_O[(key)] = val

    # Convert strings to floats as necessary
    self.Meadow_WT_O['A1_above']    = float(self.Meadow_WT_O['A1_above'])
    self.Meadow_WT_O['A2_above']    = float(self.Meadow_WT_O['A2_above'])
    self.Meadow_WT_O['x0_above']    = float(self.Meadow_WT_O['x0_above'])
    self.Meadow_WT_O['dx_above']    = float(self.Meadow_WT_O['dx_above'])
    self.Meadow_WT_O['A1_below']    = float(self.Meadow_WT_O['A1_below'])
    self.Meadow_WT_O['A2_below']    = float(self.Meadow_WT_O['A2_below'])
    self.Meadow_WT_O['x0_below']    = float(self.Meadow_WT_O['x0_below'])
    self.Meadow_WT_O['dx_below']    = float(self.Meadow_WT_O['dx_below'])
    self.Meadow_WT_O['a_above']     = float(self.Meadow_WT_O['a_above'])
    self.Meadow_WT_O['b_above']     = float(self.Meadow_WT_O['b_above'])
    self.Meadow_WT_O['a_below']     = float(self.Meadow_WT_O['a_below'])
    self.Meadow_WT_O['b_below']     = float(self.Meadow_WT_O['b_below'])
    self.Meadow_WT_O['K_above']     = float(self.Meadow_WT_O['K_above'])
    self.Meadow_WT_O['C_above']     = float(self.Meadow_WT_O['C_above'])
    self.Meadow_WT_O['A_above']     = float(self.Meadow_WT_O['A_above'])
    self.Meadow_WT_O['B_above']     = float(self.Meadow_WT_O['B_above'])
    self.Meadow_WT_O['K_below']     = float(self.Meadow_WT_O['K_below'])
    self.Meadow_WT_O['C_below']     = float(self.Meadow_WT_O['C_below'])
    self.Meadow_WT_O['A_below']     = float(self.Meadow_WT_O['A_below'])
    self.Meadow_WT_O['B_below']     = float(self.Meadow_WT_O['B_below'])
    self.Meadow_WT_O['HillB_above'] = float(self.Meadow_WT_O['HillB_above'])
    self.Meadow_WT_O['HillN_above'] = float(self.Meadow_WT_O['HillN_above'])
    self.Meadow_WT_O['HillB_below'] = float(self.Meadow_WT_O['HillB_below'])
    self.Meadow_WT_O['HillN_below'] = float(self.Meadow_WT_O['HillN_below'])
    self.Meadow_WT_O['max_terrain_transition'] = \
      float(self.Meadow_WT_O['max_terrain_transition'])
    self.Meadow_WT_O['ice_slope_poor']    = float(self.Meadow_WT_O['ice_slope_poor'])
    self.Meadow_WT_O['ice_slope_pore']    = float(self.Meadow_WT_O['ice_slope_pore'])
    self.Meadow_WT_O['ice_slope_wedge']   = float(self.Meadow_WT_O['ice_slope_wedge'])
    self.Meadow_WT_O['ice_slope_massive'] = float(self.Meadow_WT_O['ice_slope_massive'])
    self.Meadow_WT_O['porosity'] = float(self.Meadow_WT_O['porosity'])    

#====================================================================================
def NoData_WT(self):
    
    print '    ..Reading Wetland Tundra No Data Parameters'

    """ Read files from the input directory """
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'arctic_coast':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Arctic/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'aiem':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/AIEM/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'ngee':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/NGEE/'+\
                 self.Control_directory)

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Old Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    self.NoData_WT_O = {}
    with open(self.NoData_WT_O_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.NoData_WT_O[(key)] = val

    # Convert strings to floats as necessary
    self.NoData_WT_O['A1_above']    = float(self.NoData_WT_O['A1_above'])
    self.NoData_WT_O['A2_above']    = float(self.NoData_WT_O['A2_above'])
    self.NoData_WT_O['x0_above']    = float(self.NoData_WT_O['x0_above'])
    self.NoData_WT_O['dx_above']    = float(self.NoData_WT_O['dx_above'])
    self.NoData_WT_O['A1_below']    = float(self.NoData_WT_O['A1_below'])
    self.NoData_WT_O['A2_below']    = float(self.NoData_WT_O['A2_below'])
    self.NoData_WT_O['x0_below']    = float(self.NoData_WT_O['x0_below'])
    self.NoData_WT_O['dx_below']    = float(self.NoData_WT_O['dx_below'])
    self.NoData_WT_O['a_above']     = float(self.NoData_WT_O['a_above'])
    self.NoData_WT_O['b_above']     = float(self.NoData_WT_O['b_above'])
    self.NoData_WT_O['a_below']     = float(self.NoData_WT_O['a_below'])
    self.NoData_WT_O['b_below']     = float(self.NoData_WT_O['b_below'])
    self.NoData_WT_O['K_above']     = float(self.NoData_WT_O['K_above'])
    self.NoData_WT_O['C_above']     = float(self.NoData_WT_O['C_above'])
    self.NoData_WT_O['A_above']     = float(self.NoData_WT_O['A_above'])
    self.NoData_WT_O['B_above']     = float(self.NoData_WT_O['B_above'])
    self.NoData_WT_O['K_below']     = float(self.NoData_WT_O['K_below'])
    self.NoData_WT_O['C_below']     = float(self.NoData_WT_O['C_below'])
    self.NoData_WT_O['A_below']     = float(self.NoData_WT_O['A_below'])
    self.NoData_WT_O['B_below']     = float(self.NoData_WT_O['B_below'])
    self.NoData_WT_O['HillB_above'] = float(self.NoData_WT_O['HillB_above'])
    self.NoData_WT_O['HillN_above'] = float(self.NoData_WT_O['HillN_above'])
    self.NoData_WT_O['HillB_below'] = float(self.NoData_WT_O['HillB_below'])
    self.NoData_WT_O['HillN_below'] = float(self.NoData_WT_O['HillN_below'])
    self.NoData_WT_O['max_terrain_transition'] = \
      float(self.NoData_WT_O['max_terrain_transition'])
    self.NoData_WT_O['ice_slope_poor']    = float(self.NoData_WT_O['ice_slope_poor'])
    self.NoData_WT_O['ice_slope_pore']    = float(self.NoData_WT_O['ice_slope_pore'])
    self.NoData_WT_O['ice_slope_wedge']   = float(self.NoData_WT_O['ice_slope_wedge'])
    self.NoData_WT_O['ice_slope_massive'] = float(self.NoData_WT_O['ice_slope_massive'])
    self.NoData_WT_O['porosity'] = float(self.NoData_WT_O['porosity'])

#====================================================================================
def SandDunes_WT(self):
    
    print '    ..Reading Wetland Tundra Sand Dune Parameters'

    """ Read files from the input directory """
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'arctic_coast':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Arctic/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'aiem':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/AIEM/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'ngee':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/NGEE/'+\
                 self.Control_directory)

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Young Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Young age parameters'
    
    self.SandDunes_WT_Y = {}
    with open(self.SandDunes_WT_Y_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.SandDunes_WT_Y[(key)] = val

    # Convert strings to floats as necessary
    self.SandDunes_WT_Y['A1_above']    = float(self.SandDunes_WT_Y['A1_above'])
    self.SandDunes_WT_Y['A2_above']    = float(self.SandDunes_WT_Y['A2_above'])
    self.SandDunes_WT_Y['x0_above']    = float(self.SandDunes_WT_Y['x0_above'])
    self.SandDunes_WT_Y['dx_above']    = float(self.SandDunes_WT_Y['dx_above'])
    self.SandDunes_WT_Y['A1_below']    = float(self.SandDunes_WT_Y['A1_below'])
    self.SandDunes_WT_Y['A2_below']    = float(self.SandDunes_WT_Y['A2_below'])
    self.SandDunes_WT_Y['x0_below']    = float(self.SandDunes_WT_Y['x0_below'])
    self.SandDunes_WT_Y['dx_below']    = float(self.SandDunes_WT_Y['dx_below'])
    self.SandDunes_WT_Y['a_above']     = float(self.SandDunes_WT_Y['a_above'])
    self.SandDunes_WT_Y['b_above']     = float(self.SandDunes_WT_Y['b_above'])
    self.SandDunes_WT_Y['a_below']     = float(self.SandDunes_WT_Y['a_below'])
    self.SandDunes_WT_Y['b_below']     = float(self.SandDunes_WT_Y['b_below'])
    self.SandDunes_WT_Y['K_above']     = float(self.SandDunes_WT_Y['K_above'])
    self.SandDunes_WT_Y['C_above']     = float(self.SandDunes_WT_Y['C_above'])
    self.SandDunes_WT_Y['A_above']     = float(self.SandDunes_WT_Y['A_above'])
    self.SandDunes_WT_Y['B_above']     = float(self.SandDunes_WT_Y['B_above'])
    self.SandDunes_WT_Y['K_below']     = float(self.SandDunes_WT_Y['K_below'])
    self.SandDunes_WT_Y['C_below']     = float(self.SandDunes_WT_Y['C_below'])
    self.SandDunes_WT_Y['A_below']     = float(self.SandDunes_WT_Y['A_below'])
    self.SandDunes_WT_Y['B_below']     = float(self.SandDunes_WT_Y['B_below'])
    self.SandDunes_WT_Y['HillB_above'] = float(self.SandDunes_WT_Y['HillB_above'])
    self.SandDunes_WT_Y['HillN_above'] = float(self.SandDunes_WT_Y['HillN_above'])
    self.SandDunes_WT_Y['HillB_below'] = float(self.SandDunes_WT_Y['HillB_below'])
    self.SandDunes_WT_Y['HillN_below'] = float(self.SandDunes_WT_Y['HillN_below'])
    self.SandDunes_WT_Y['max_terrain_transition'] = \
      float(self.SandDunes_WT_Y['max_terrain_transition'])
    self.SandDunes_WT_Y['ice_slope_poor']    = float(self.SandDunes_WT_Y['ice_slope_poor'])
    self.SandDunes_WT_Y['ice_slope_pore']    = float(self.SandDunes_WT_Y['ice_slope_pore'])
    self.SandDunes_WT_Y['ice_slope_wedge']   = float(self.SandDunes_WT_Y['ice_slope_wedge'])
    self.SandDunes_WT_Y['ice_slope_massive'] = float(self.SandDunes_WT_Y['ice_slope_massive'])
    self.SandDunes_WT_Y['porosity'] = float(self.SandDunes_WT_Y['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Medium Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Medium age parameters'
    
    self.SandDunes_WT_M = {}
    with open(self.SandDunes_WT_M_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.SandDunes_WT_M[(key)] = val

    # Convert strings to floats as necessary
    self.SandDunes_WT_M['A1_above']    = float(self.SandDunes_WT_M['A1_above'])
    self.SandDunes_WT_M['A2_above']    = float(self.SandDunes_WT_M['A2_above'])
    self.SandDunes_WT_M['x0_above']    = float(self.SandDunes_WT_M['x0_above'])
    self.SandDunes_WT_M['dx_above']    = float(self.SandDunes_WT_M['dx_above'])
    self.SandDunes_WT_M['A1_below']    = float(self.SandDunes_WT_M['A1_below'])
    self.SandDunes_WT_M['A2_below']    = float(self.SandDunes_WT_M['A2_below'])
    self.SandDunes_WT_M['x0_below']    = float(self.SandDunes_WT_M['x0_below'])
    self.SandDunes_WT_M['dx_below']    = float(self.SandDunes_WT_M['dx_below'])
    self.SandDunes_WT_M['a_above']     = float(self.SandDunes_WT_M['a_above'])
    self.SandDunes_WT_M['b_above']     = float(self.SandDunes_WT_M['b_above'])
    self.SandDunes_WT_M['a_below']     = float(self.SandDunes_WT_M['a_below'])
    self.SandDunes_WT_M['b_below']     = float(self.SandDunes_WT_M['b_below'])
    self.SandDunes_WT_M['K_above']     = float(self.SandDunes_WT_M['K_above'])
    self.SandDunes_WT_M['C_above']     = float(self.SandDunes_WT_M['C_above'])
    self.SandDunes_WT_M['A_above']     = float(self.SandDunes_WT_M['A_above'])
    self.SandDunes_WT_M['B_above']     = float(self.SandDunes_WT_M['B_above'])
    self.SandDunes_WT_M['K_below']     = float(self.SandDunes_WT_M['K_below'])
    self.SandDunes_WT_M['C_below']     = float(self.SandDunes_WT_M['C_below'])
    self.SandDunes_WT_M['A_below']     = float(self.SandDunes_WT_M['A_below'])
    self.SandDunes_WT_M['B_below']     = float(self.SandDunes_WT_M['B_below'])
    self.SandDunes_WT_M['HillB_above'] = float(self.SandDunes_WT_M['HillB_above'])
    self.SandDunes_WT_M['HillN_above'] = float(self.SandDunes_WT_M['HillN_above'])
    self.SandDunes_WT_M['HillB_below'] = float(self.SandDunes_WT_M['HillB_below'])
    self.SandDunes_WT_M['HillN_below'] = float(self.SandDunes_WT_M['HillN_below'])
    self.SandDunes_WT_M['max_terrain_transition'] = \
      float(self.SandDunes_WT_M['max_terrain_transition'])
    self.SandDunes_WT_M['ice_slope_poor']    = float(self.SandDunes_WT_M['ice_slope_poor'])
    self.SandDunes_WT_M['ice_slope_pore']    = float(self.SandDunes_WT_M['ice_slope_pore'])
    self.SandDunes_WT_M['ice_slope_wedge']   = float(self.SandDunes_WT_M['ice_slope_wedge'])
    self.SandDunes_WT_M['ice_slope_massive'] = float(self.SandDunes_WT_M['ice_slope_massive'])
    self.SandDunes_WT_M['porosity'] = float(self.SandDunes_WT_M['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Old Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Old age parameters'
    
    self.SandDunes_WT_O = {}
    with open(self.SandDunes_WT_O_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.SandDunes_WT_O[(key)] = val

    # Convert strings to floats as necessary
    self.SandDunes_WT_O['A1_above']    = float(self.SandDunes_WT_O['A1_above'])
    self.SandDunes_WT_O['A2_above']    = float(self.SandDunes_WT_O['A2_above'])
    self.SandDunes_WT_O['x0_above']    = float(self.SandDunes_WT_O['x0_above'])
    self.SandDunes_WT_O['dx_above']    = float(self.SandDunes_WT_O['dx_above'])
    self.SandDunes_WT_O['A1_below']    = float(self.SandDunes_WT_O['A1_below'])
    self.SandDunes_WT_O['A2_below']    = float(self.SandDunes_WT_O['A2_below'])
    self.SandDunes_WT_O['x0_below']    = float(self.SandDunes_WT_O['x0_below'])
    self.SandDunes_WT_O['dx_below']    = float(self.SandDunes_WT_O['dx_below'])
    self.SandDunes_WT_O['a_above']     = float(self.SandDunes_WT_O['a_above'])
    self.SandDunes_WT_O['b_above']     = float(self.SandDunes_WT_O['b_above'])
    self.SandDunes_WT_O['a_below']     = float(self.SandDunes_WT_O['a_below'])
    self.SandDunes_WT_O['b_below']     = float(self.SandDunes_WT_O['b_below'])
    self.SandDunes_WT_O['K_above']     = float(self.SandDunes_WT_O['K_above'])
    self.SandDunes_WT_O['C_above']     = float(self.SandDunes_WT_O['C_above'])
    self.SandDunes_WT_O['A_above']     = float(self.SandDunes_WT_O['A_above'])
    self.SandDunes_WT_O['B_above']     = float(self.SandDunes_WT_O['B_above'])
    self.SandDunes_WT_O['K_below']     = float(self.SandDunes_WT_O['K_below'])
    self.SandDunes_WT_O['C_below']     = float(self.SandDunes_WT_O['C_below'])
    self.SandDunes_WT_O['A_below']     = float(self.SandDunes_WT_O['A_below'])
    self.SandDunes_WT_O['B_below']     = float(self.SandDunes_WT_O['B_below'])
    self.SandDunes_WT_O['HillB_above'] = float(self.SandDunes_WT_O['HillB_above'])
    self.SandDunes_WT_O['HillN_above'] = float(self.SandDunes_WT_O['HillN_above'])
    self.SandDunes_WT_O['HillB_below'] = float(self.SandDunes_WT_O['HillB_below'])
    self.SandDunes_WT_O['HillN_below'] = float(self.SandDunes_WT_O['HillN_below'])
    self.SandDunes_WT_O['max_terrain_transition'] = \
      float(self.SandDunes_WT_O['max_terrain_transition'])
    self.SandDunes_WT_O['ice_slope_poor']    = float(self.SandDunes_WT_O['ice_slope_poor'])
    self.SandDunes_WT_O['ice_slope_pore']    = float(self.SandDunes_WT_O['ice_slope_pore'])
    self.SandDunes_WT_O['ice_slope_wedge']   = float(self.SandDunes_WT_O['ice_slope_wedge'])
    self.SandDunes_WT_O['ice_slope_massive'] = float(self.SandDunes_WT_O['ice_slope_massive'])
    self.SandDunes_WT_O['porosity'] = float(self.SandDunes_WT_O['porosity'])    
    
#====================================================================================
def SaturatedBarrens_WT(self):
    
    print '    ..Reading Wetland Tundra Saturated Barren Parameters'

    """ Read files from the input directory """
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'arctic_coast':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Arctic/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'aiem':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/AIEM/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'ngee':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/NGEE/'+\
                 self.Control_directory)

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Young Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Young age parameters'
    
    self.SaturatedBarrens_WT_Y = {}
    with open(self.SaturatedBarrens_WT_Y_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.SaturatedBarrens_WT_Y[(key)] = val

    # Convert strings to floats as necessary
    self.SaturatedBarrens_WT_Y['A1_above']    = float(self.SaturatedBarrens_WT_Y['A1_above'])
    self.SaturatedBarrens_WT_Y['A2_above']    = float(self.SaturatedBarrens_WT_Y['A2_above'])
    self.SaturatedBarrens_WT_Y['x0_above']    = float(self.SaturatedBarrens_WT_Y['x0_above'])
    self.SaturatedBarrens_WT_Y['dx_above']    = float(self.SaturatedBarrens_WT_Y['dx_above'])
    self.SaturatedBarrens_WT_Y['A1_below']    = float(self.SaturatedBarrens_WT_Y['A1_below'])
    self.SaturatedBarrens_WT_Y['A2_below']    = float(self.SaturatedBarrens_WT_Y['A2_below'])
    self.SaturatedBarrens_WT_Y['x0_below']    = float(self.SaturatedBarrens_WT_Y['x0_below'])
    self.SaturatedBarrens_WT_Y['dx_below']    = float(self.SaturatedBarrens_WT_Y['dx_below'])
    self.SaturatedBarrens_WT_Y['a_above']     = float(self.SaturatedBarrens_WT_Y['a_above'])
    self.SaturatedBarrens_WT_Y['b_above']     = float(self.SaturatedBarrens_WT_Y['b_above'])
    self.SaturatedBarrens_WT_Y['a_below']     = float(self.SaturatedBarrens_WT_Y['a_below'])
    self.SaturatedBarrens_WT_Y['b_below']     = float(self.SaturatedBarrens_WT_Y['b_below'])
    self.SaturatedBarrens_WT_Y['K_above']     = float(self.SaturatedBarrens_WT_Y['K_above'])
    self.SaturatedBarrens_WT_Y['C_above']     = float(self.SaturatedBarrens_WT_Y['C_above'])
    self.SaturatedBarrens_WT_Y['A_above']     = float(self.SaturatedBarrens_WT_Y['A_above'])
    self.SaturatedBarrens_WT_Y['B_above']     = float(self.SaturatedBarrens_WT_Y['B_above'])
    self.SaturatedBarrens_WT_Y['K_below']     = float(self.SaturatedBarrens_WT_Y['K_below'])
    self.SaturatedBarrens_WT_Y['C_below']     = float(self.SaturatedBarrens_WT_Y['C_below'])
    self.SaturatedBarrens_WT_Y['A_below']     = float(self.SaturatedBarrens_WT_Y['A_below'])
    self.SaturatedBarrens_WT_Y['B_below']     = float(self.SaturatedBarrens_WT_Y['B_below'])
    self.SaturatedBarrens_WT_Y['HillB_above'] = float(self.SaturatedBarrens_WT_Y['HillB_above'])
    self.SaturatedBarrens_WT_Y['HillN_above'] = float(self.SaturatedBarrens_WT_Y['HillN_above'])
    self.SaturatedBarrens_WT_Y['HillB_below'] = float(self.SaturatedBarrens_WT_Y['HillB_below'])
    self.SaturatedBarrens_WT_Y['HillN_below'] = float(self.SaturatedBarrens_WT_Y['HillN_below'])
    self.SaturatedBarrens_WT_Y['max_terrain_transition'] = \
      float(self.SaturatedBarrens_WT_Y['max_terrain_transition'])
    self.SaturatedBarrens_WT_Y['ice_slope_poor']    = float(self.SaturatedBarrens_WT_Y['ice_slope_poor'])
    self.SaturatedBarrens_WT_Y['ice_slope_pore']    = float(self.SaturatedBarrens_WT_Y['ice_slope_pore'])
    self.SaturatedBarrens_WT_Y['ice_slope_wedge']   = float(self.SaturatedBarrens_WT_Y['ice_slope_wedge'])
    self.SaturatedBarrens_WT_Y['ice_slope_massive'] = float(self.SaturatedBarrens_WT_Y['ice_slope_massive'])
    self.SaturatedBarrens_WT_Y['porosity'] = float(self.SaturatedBarrens_WT_Y['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Medium Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Medium age parameters'
    
    self.SaturatedBarrens_WT_M = {}
    with open(self.SaturatedBarrens_WT_M_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.SaturatedBarrens_WT_M[(key)] = val

    # Convert strings to floats as necessary
    self.SaturatedBarrens_WT_M['A1_above']    = float(self.SaturatedBarrens_WT_M['A1_above'])
    self.SaturatedBarrens_WT_M['A2_above']    = float(self.SaturatedBarrens_WT_M['A2_above'])
    self.SaturatedBarrens_WT_M['x0_above']    = float(self.SaturatedBarrens_WT_M['x0_above'])
    self.SaturatedBarrens_WT_M['dx_above']    = float(self.SaturatedBarrens_WT_M['dx_above'])
    self.SaturatedBarrens_WT_M['A1_below']    = float(self.SaturatedBarrens_WT_M['A1_below'])
    self.SaturatedBarrens_WT_M['A2_below']    = float(self.SaturatedBarrens_WT_M['A2_below'])
    self.SaturatedBarrens_WT_M['x0_below']    = float(self.SaturatedBarrens_WT_M['x0_below'])
    self.SaturatedBarrens_WT_M['dx_below']    = float(self.SaturatedBarrens_WT_M['dx_below'])
    self.SaturatedBarrens_WT_M['a_above']     = float(self.SaturatedBarrens_WT_M['a_above'])
    self.SaturatedBarrens_WT_M['b_above']     = float(self.SaturatedBarrens_WT_M['b_above'])
    self.SaturatedBarrens_WT_M['a_below']     = float(self.SaturatedBarrens_WT_M['a_below'])
    self.SaturatedBarrens_WT_M['b_below']     = float(self.SaturatedBarrens_WT_M['b_below'])
    self.SaturatedBarrens_WT_M['K_above']     = float(self.SaturatedBarrens_WT_M['K_above'])
    self.SaturatedBarrens_WT_M['C_above']     = float(self.SaturatedBarrens_WT_M['C_above'])
    self.SaturatedBarrens_WT_M['A_above']     = float(self.SaturatedBarrens_WT_M['A_above'])
    self.SaturatedBarrens_WT_M['B_above']     = float(self.SaturatedBarrens_WT_M['B_above'])
    self.SaturatedBarrens_WT_M['K_below']     = float(self.SaturatedBarrens_WT_M['K_below'])
    self.SaturatedBarrens_WT_M['C_below']     = float(self.SaturatedBarrens_WT_M['C_below'])
    self.SaturatedBarrens_WT_M['A_below']     = float(self.SaturatedBarrens_WT_M['A_below'])
    self.SaturatedBarrens_WT_M['B_below']     = float(self.SaturatedBarrens_WT_M['B_below'])
    self.SaturatedBarrens_WT_M['HillB_above'] = float(self.SaturatedBarrens_WT_M['HillB_above'])
    self.SaturatedBarrens_WT_M['HillN_above'] = float(self.SaturatedBarrens_WT_M['HillN_above'])
    self.SaturatedBarrens_WT_M['HillB_below'] = float(self.SaturatedBarrens_WT_M['HillB_below'])
    self.SaturatedBarrens_WT_M['HillN_below'] = float(self.SaturatedBarrens_WT_M['HillN_below'])
    self.SaturatedBarrens_WT_M['max_terrain_transition'] = \
      float(self.SaturatedBarrens_WT_M['max_terrain_transition'])
    self.SaturatedBarrens_WT_M['ice_slope_poor']    = float(self.SaturatedBarrens_WT_M['ice_slope_poor'])
    self.SaturatedBarrens_WT_M['ice_slope_pore']    = float(self.SaturatedBarrens_WT_M['ice_slope_pore'])
    self.SaturatedBarrens_WT_M['ice_slope_wedge']   = float(self.SaturatedBarrens_WT_M['ice_slope_wedge'])
    self.SaturatedBarrens_WT_M['ice_slope_massive'] = float(self.SaturatedBarrens_WT_M['ice_slope_massive'])
    self.SaturatedBarrens_WT_M['porosity'] = float(self.SaturatedBarrens_WT_M['porosity'])    

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Old Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    print '      .. Old age parameters'
    
    self.SaturatedBarrens_WT_O = {}
    with open(self.SaturatedBarrens_WT_O_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.SaturatedBarrens_WT_O[(key)] = val

    # Convert strings to floats as necessary
    self.SaturatedBarrens_WT_O['A1_above']    = float(self.SaturatedBarrens_WT_O['A1_above'])
    self.SaturatedBarrens_WT_O['A2_above']    = float(self.SaturatedBarrens_WT_O['A2_above'])
    self.SaturatedBarrens_WT_O['x0_above']    = float(self.SaturatedBarrens_WT_O['x0_above'])
    self.SaturatedBarrens_WT_O['dx_above']    = float(self.SaturatedBarrens_WT_O['dx_above'])
    self.SaturatedBarrens_WT_O['A1_below']    = float(self.SaturatedBarrens_WT_O['A1_below'])
    self.SaturatedBarrens_WT_O['A2_below']    = float(self.SaturatedBarrens_WT_O['A2_below'])
    self.SaturatedBarrens_WT_O['x0_below']    = float(self.SaturatedBarrens_WT_O['x0_below'])
    self.SaturatedBarrens_WT_O['dx_below']    = float(self.SaturatedBarrens_WT_O['dx_below'])
    self.SaturatedBarrens_WT_O['a_above']     = float(self.SaturatedBarrens_WT_O['a_above'])
    self.SaturatedBarrens_WT_O['b_above']     = float(self.SaturatedBarrens_WT_O['b_above'])
    self.SaturatedBarrens_WT_O['a_below']     = float(self.SaturatedBarrens_WT_O['a_below'])
    self.SaturatedBarrens_WT_O['b_below']     = float(self.SaturatedBarrens_WT_O['b_below'])
    self.SaturatedBarrens_WT_O['K_above']     = float(self.SaturatedBarrens_WT_O['K_above'])
    self.SaturatedBarrens_WT_O['C_above']     = float(self.SaturatedBarrens_WT_O['C_above'])
    self.SaturatedBarrens_WT_O['A_above']     = float(self.SaturatedBarrens_WT_O['A_above'])
    self.SaturatedBarrens_WT_O['B_above']     = float(self.SaturatedBarrens_WT_O['B_above'])
    self.SaturatedBarrens_WT_O['K_below']     = float(self.SaturatedBarrens_WT_O['K_below'])
    self.SaturatedBarrens_WT_O['C_below']     = float(self.SaturatedBarrens_WT_O['C_below'])
    self.SaturatedBarrens_WT_O['A_below']     = float(self.SaturatedBarrens_WT_O['A_below'])
    self.SaturatedBarrens_WT_O['B_below']     = float(self.SaturatedBarrens_WT_O['B_below'])
    self.SaturatedBarrens_WT_O['HillB_above'] = float(self.SaturatedBarrens_WT_O['HillB_above'])
    self.SaturatedBarrens_WT_O['HillN_above'] = float(self.SaturatedBarrens_WT_O['HillN_above'])
    self.SaturatedBarrens_WT_O['HillB_below'] = float(self.SaturatedBarrens_WT_O['HillB_below'])
    self.SaturatedBarrens_WT_O['HillN_below'] = float(self.SaturatedBarrens_WT_O['HillN_below'])
    self.SaturatedBarrens_WT_O['max_terrain_transition'] = \
      float(self.SaturatedBarrens_WT_O['max_terrain_transition'])
    self.SaturatedBarrens_WT_O['ice_slope_poor']    = float(self.SaturatedBarrens_WT_O['ice_slope_poor'])
    self.SaturatedBarrens_WT_O['ice_slope_pore']    = float(self.SaturatedBarrens_WT_O['ice_slope_pore'])
    self.SaturatedBarrens_WT_O['ice_slope_wedge']   = float(self.SaturatedBarrens_WT_O['ice_slope_wedge'])
    self.SaturatedBarrens_WT_O['ice_slope_massive'] = float(self.SaturatedBarrens_WT_O['ice_slope_massive'])
    self.SaturatedBarrens_WT_O['porosity'] = float(self.SaturatedBarrens_WT_O['porosity'])    
    
#====================================================================================
def Shrubs_WT(self):
    
    print '    ..Reading Wetland Tundra Shrub Parameters'

    """ Read files from the input directory """
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'arctic_coast':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Arctic/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'aiem':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/AIEM/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'ngee':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/NGEE/'+\
                 self.Control_directory)

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Old Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    self.Shrubs_WT_O = {}
    with open(self.Shrubs_WT_O_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.Shrubs_WT_O[(key)] = val

    # Convert strings to floats as necessary
    self.Shrubs_WT_O['A1_above']    = float(self.Shrubs_WT_O['A1_above'])
    self.Shrubs_WT_O['A2_above']    = float(self.Shrubs_WT_O['A2_above'])
    self.Shrubs_WT_O['x0_above']    = float(self.Shrubs_WT_O['x0_above'])
    self.Shrubs_WT_O['dx_above']    = float(self.Shrubs_WT_O['dx_above'])
    self.Shrubs_WT_O['A1_below']    = float(self.Shrubs_WT_O['A1_below'])
    self.Shrubs_WT_O['A2_below']    = float(self.Shrubs_WT_O['A2_below'])
    self.Shrubs_WT_O['x0_below']    = float(self.Shrubs_WT_O['x0_below'])
    self.Shrubs_WT_O['dx_below']    = float(self.Shrubs_WT_O['dx_below'])
    self.Shrubs_WT_O['a_above']     = float(self.Shrubs_WT_O['a_above'])
    self.Shrubs_WT_O['b_above']     = float(self.Shrubs_WT_O['b_above'])
    self.Shrubs_WT_O['a_below']     = float(self.Shrubs_WT_O['a_below'])
    self.Shrubs_WT_O['b_below']     = float(self.Shrubs_WT_O['b_below'])
    self.Shrubs_WT_O['K_above']     = float(self.Shrubs_WT_O['K_above'])
    self.Shrubs_WT_O['C_above']     = float(self.Shrubs_WT_O['C_above'])
    self.Shrubs_WT_O['A_above']     = float(self.Shrubs_WT_O['A_above'])
    self.Shrubs_WT_O['B_above']     = float(self.Shrubs_WT_O['B_above'])
    self.Shrubs_WT_O['K_below']     = float(self.Shrubs_WT_O['K_below'])
    self.Shrubs_WT_O['C_below']     = float(self.Shrubs_WT_O['C_below'])
    self.Shrubs_WT_O['A_below']     = float(self.Shrubs_WT_O['A_below'])
    self.Shrubs_WT_O['B_below']     = float(self.Shrubs_WT_O['B_below'])
    self.Shrubs_WT_O['HillB_above'] = float(self.Shrubs_WT_O['HillB_above'])
    self.Shrubs_WT_O['HillN_above'] = float(self.Shrubs_WT_O['HillN_above'])
    self.Shrubs_WT_O['HillB_below'] = float(self.Shrubs_WT_O['HillB_below'])
    self.Shrubs_WT_O['HillN_below'] = float(self.Shrubs_WT_O['HillN_below'])
    self.Shrubs_WT_O['max_terrain_transition'] = \
      float(self.Shrubs_WT_O['max_terrain_transition'])
    self.Shrubs_WT_O['ice_slope_poor']    = float(self.Shrubs_WT_O['ice_slope_poor'])
    self.Shrubs_WT_O['ice_slope_pore']    = float(self.Shrubs_WT_O['ice_slope_pore'])
    self.Shrubs_WT_O['ice_slope_wedge']   = float(self.Shrubs_WT_O['ice_slope_wedge'])
    self.Shrubs_WT_O['ice_slope_massive'] = float(self.Shrubs_WT_O['ice_slope_massive'])
    self.Shrubs_WT_O['porosity'] = float(self.Shrubs_WT_O['porosity'])

#====================================================================================
def Urban_WT(self):
    
    print '    ..Reading Wetland Tundra Urban Parameters'

    """ Read files from the input directory """
    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'arctic_coast':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Arctic/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'aiem':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/AIEM/'+\
                 self.Control_directory)
    elif self.Simulation_area.lower() == 'ngee':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/NGEE/'+\
                 self.Control_directory)

    # - - - - - - - - - - - - - - - - - - - - - - - - -
    # Reading Old Age Parameters from Control file
    # - - - - - - - - - - - - - - - - - - - - - - - - -
    self.Urban_WT = {}
    with open(self.Urban_WT_Control, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.Urban_WT[(key)] = val

    # Convert strings to floats as necessary
    self.Urban_WT['A1_above']    = float(self.Urban_WT['A1_above'])
    self.Urban_WT['A2_above']    = float(self.Urban_WT['A2_above'])
    self.Urban_WT['x0_above']    = float(self.Urban_WT['x0_above'])
    self.Urban_WT['dx_above']    = float(self.Urban_WT['dx_above'])
    self.Urban_WT['A1_below']    = float(self.Urban_WT['A1_below'])
    self.Urban_WT['A2_below']    = float(self.Urban_WT['A2_below'])
    self.Urban_WT['x0_below']    = float(self.Urban_WT['x0_below'])
    self.Urban_WT['dx_below']    = float(self.Urban_WT['dx_below'])
    self.Urban_WT['a_above']     = float(self.Urban_WT['a_above'])
    self.Urban_WT['b_above']     = float(self.Urban_WT['b_above'])
    self.Urban_WT['a_below']     = float(self.Urban_WT['a_below'])
    self.Urban_WT['b_below']     = float(self.Urban_WT['b_below'])
    self.Urban_WT['K_above']     = float(self.Urban_WT['K_above'])
    self.Urban_WT['C_above']     = float(self.Urban_WT['C_above'])
    self.Urban_WT['A_above']     = float(self.Urban_WT['A_above'])
    self.Urban_WT['B_above']     = float(self.Urban_WT['B_above'])
    self.Urban_WT['K_below']     = float(self.Urban_WT['K_below'])
    self.Urban_WT['C_below']     = float(self.Urban_WT['C_below'])
    self.Urban_WT['A_below']     = float(self.Urban_WT['A_below'])
    self.Urban_WT['B_below']     = float(self.Urban_WT['B_below'])
    self.Urban_WT['HillB_above'] = float(self.Urban_WT['HillB_above'])
    self.Urban_WT['HillN_above'] = float(self.Urban_WT['HillN_above'])
    self.Urban_WT['HillB_below'] = float(self.Urban_WT['HillB_below'])
    self.Urban_WT['HillN_below'] = float(self.Urban_WT['HillN_below'])
    self.Urban_WT['max_terrain_transition'] = \
      float(self.Urban_WT['max_terrain_transition'])
    self.Urban_WT['ice_slope_poor']    = float(self.Urban_WT['ice_slope_poor'])
    self.Urban_WT['ice_slope_pore']    = float(self.Urban_WT['ice_slope_pore'])
    self.Urban_WT['ice_slope_wedge']   = float(self.Urban_WT['ice_slope_wedge'])
    self.Urban_WT['ice_slope_massive'] = float(self.Urban_WT['ice_slope_massive'])
    self.Urban_WT['porosity'] = float(self.Urban_WT['porosity'])
