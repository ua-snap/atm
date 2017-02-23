import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
import random

def barrow_initial_cohort_population(self):
    #==========================================================================
    # NOTE: 3 June 2016, Bolton. Changing cohorts to reflect no
    #       landform definitions to be used for both
    #       Barrow and AK Arctic Coastal Plain projects
    # ----------------------------------------------------------------------------
    # Note -- in this Barrow example:
    # ATTM Model domain is 1000m by 1000m (self.Y_resolution, self.X_resolution)
    # Geotiff files are 25m by 25m (self.y_res, self.x_res)
    # Therefore, the # of rows/columns to to read are 40x40 (1000/25, 1000/25)
    # ----------------------------------------------------------------------------
    #def count_cohorts(a, b):
    #    b = a > 0
    #    return len(a[b])
    #-----------------------------------------------------------------------------
    # ------------------------------------------------------------------------------
    # Define the ATTM Land Surface Cohorts
    #      NOTE: Assuming the entire Barrow test site is considered Wetland Tundra
    # ------------------------------------------------------------------------------
    count = 0
    
    for i in range(0, int(self.nrows), int(float(self.Y_resolution)/(self.y_res))):
        for j in range(0, int(self.ncols), int(float(self.X_resolution)/(self.x_res))):
            # ============================================================
            # Wetland Tundra Non-Polygonal Ground, Young, Medium, Old age
            # ============================================================
            #A = self.NPG[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
            #             j:j+int(float(self.X_resolution)/(self.x_res))-1]
            A = self.Meadow_WT_Y[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                 j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            #self.ATTM_Wet_NPG[count] = len(A[b])
            self.ATTM_Meadow_WT_Y[count] = len(A[b])
            #----------------------------------------------------------------------
            A = self.Meadow_WT_M[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                 j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Meadow_WT_M[count] = len(A[b])
            #----------------------------------------------------------------------
            A = self.Meadow_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                 j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Meadow_WT_O[count] = len(A[b])
            # ==========================================================
            # Wetland Tundra Low Center Polygon, Young, Medium, Old age
            # ==========================================================
            A = self.LCP_WT_Y[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                              j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_LCP_WT_Y[count] = len(A[b])
            #----------------------------------------------------------------------
            A = self.LCP_WT_M[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                             j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_LCP_WT_M[count] = len(A[b])
            #----------------------------------------------------------------------
            A = self.LCP_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                             j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_LCP_WT_O[count] = len(A[b])
            # =====================================================================
            # Wetland Tundra Coalescent Low Center Polygon, Young, Medium, Old age
            # =====================================================================
            A = self.CLC_WT_Y[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                              j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_CLC_WT_Y[count] = len(A[b])
            #-----------------------------------------------------------------------
            A = self.CLC_WT_M[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                              j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_CLC_WT_M[count] = len(A[b])
            #-----------------------------------------------------------------------
            A = self.CLC_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                              j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_CLC_WT_O[count] = len(A[b])            
            # =======================================================================
            # Wetland Tundra Flat Center Polygon, Young, Medium, Old age
            # =======================================================================
            A = self.FCP_WT_Y[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                              j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_FCP_WT_Y[count] = len(A[b])
            #-------------------------------------------------------------------------
            A = self.FCP_WT_M[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                              j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_FCP_WT_M[count] = len(A[b])
            #-------------------------------------------------------------------------            
            A = self.FCP_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                              j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_FCP_WT_O[count] = len(A[b])
            # ==========================================================================
            # Wetland Tundra High Center Polygon, Young, Medium, Old age
            # ==========================================================================
            A = self.HCP_WT_Y[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                              j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_HCP_WT_Y[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.HCP_WT_M[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                              j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_HCP_WT_M[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.HCP_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                              j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_HCP_WT_O[count] = len(A[b])            
            # ===========================================================================
            # Rivers, Wetland Tundra, Young, Medium and Old age
            # ===========================================================================
            A = self.Rivers_WT_Y[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Rivers_WT_Y[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.Rivers_WT_M[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Rivers_WT_M[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.Rivers_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Rivers_WT_O[count] = len(A[b])
            # ===========================================================================
            # Large Lakes, Wetland Tundra, Young, Medium, Old age
            # ===========================================================================
            A = self.LargeLakes_WT_Y[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                     j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_LargeLakes_WT_Y[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.LargeLakes_WT_M[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                     j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_LargeLakes_WT_M[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.LargeLakes_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                     j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_LargeLakes_WT_O[count] = len(A[b])
            # ===========================================================================
            # Medium Lakes, Wetland Tundra, Young, Medium, Old age
            # ===========================================================================
            A = self.MediumLakes_WT_Y[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                     j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_MediumLakes_WT_Y[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.MediumLakes_WT_M[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                     j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_MediumLakes_WT_M[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.MediumLakes_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                     j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_MediumLakes_WT_O[count] = len(A[b])
            # ===========================================================================
            # Small Lakes, Wetland Tundra, Young, Medium, Old age
            # ===========================================================================
            A = self.SmallLakes_WT_Y[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                     j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_SmallLakes_WT_Y[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.SmallLakes_WT_M[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                     j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_SmallLakes_WT_M[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.SmallLakes_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                     j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_SmallLakes_WT_O[count] = len(A[b])            
            # ===========================================================================
            # Ponds, Wetland Tundra, Young, Medium, Old age
            # ===========================================================================
            A = self.Ponds_WT_Y[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Ponds_WT_Y[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.Ponds_WT_M[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Ponds_WT_M[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.Ponds_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Ponds_WT_O[count] = len(A[b])
            # ===========================================================================
            # Urban, Wetland Tundra
            # ===========================================================================
            A = self.Urban_WT[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                              j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Urban_WT[count] = len(A[b])
            # ===========================================================================
            # Coastal Waters, Wetland Tundra, Old age
            # ===========================================================================
            A = self.CoastalWaters_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                        j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_CoastalWaters_WT_O[count] = len(A[b])
            # ===========================================================================
            # Drained Slope, Wetland Tundra, Young, Medium, Old age
            # ===========================================================================
            A = self.DrainedSlope_WT_Y[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                       j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_DrainedSlope_WT_Y[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.DrainedSlope_WT_M[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                       j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_DrainedSlope_WT_M[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.DrainedSlope_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                       j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_DrainedSlope_WT_O[count] = len(A[b])
            # ===========================================================================
            # Sand Dunes, Wetland Tundra, Young, Medium, Old age
            # ===========================================================================
            A = self.SandDunes_WT_Y[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                    j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_SandDunes_WT_Y[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.SandDunes_WT_M[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                    j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_SandDunes_WT_M[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.SandDunes_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                    j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_SandDunes_WT_O[count] = len(A[b])
            # ===========================================================================
            # Saturated Barrens, Wetland Tundra, Young, Medium, Old age
            # ===========================================================================
            A = self.SaturatedBarrens_WT_Y[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                           j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_SaturatedBarrens_WT_Y[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.SaturatedBarrens_WT_M[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                           j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_SaturatedBarrens_WT_M[count] = len(A[b])
            #----------------------------------------------------------------------------
            A = self.SaturatedBarrens_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                           j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_SaturatedBarrens_WT_O[count] = len(A[b])
            # ===========================================================================
            # Shrubs, Wetland Tundra, Old age
            # ===========================================================================
            A = self.Shrubs_WT_O[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                           j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Shrubs_WT_O[count] = len(A[b])

            # ===================================
            # Total
            # ===================================
            self.ATTM_Total = self.ATTM_CLC_WT_Y + self.ATTM_CLC_WT_M + self.ATTM_CLC_WT_O + \
                              self.ATTM_CoastalWaters_WT_O + \
                              self.ATTM_DrainedSlope_WT_Y + self.ATTM_DrainedSlope_WT_M + \
                              self.ATTM_DrainedSlope_WT_O + self.ATTM_FCP_WT_Y + \
                              self.ATTM_FCP_WT_M + self.ATTM_FCP_WT_O + \
                              self.ATTM_HCP_WT_Y + self.ATTM_HCP_WT_M + self.ATTM_HCP_WT_O + \
                              self.ATTM_LargeLakes_WT_Y + self.ATTM_LargeLakes_WT_M + \
                              self.ATTM_LargeLakes_WT_O + self.ATTM_LCP_WT_Y + \
                              self.ATTM_LCP_WT_M + self.ATTM_LCP_WT_O + self.ATTM_Meadow_WT_Y + \
                              self.ATTM_Meadow_WT_M + self.ATTM_Meadow_WT_O + \
                              self.ATTM_MediumLakes_WT_Y + self.ATTM_MediumLakes_WT_M + \
                              self.ATTM_MediumLakes_WT_O + self.ATTM_NoData_WT_O + \
                              self.ATTM_Ponds_WT_Y + self.ATTM_Ponds_WT_M + \
                              self.ATTM_Ponds_WT_O + self.ATTM_Rivers_WT_Y + \
                              self.ATTM_Rivers_WT_M + self.ATTM_Rivers_WT_O + \
                              self.ATTM_SandDunes_WT_Y + self.ATTM_SandDunes_WT_M + \
                              self.ATTM_SandDunes_WT_O + self.ATTM_SaturatedBarrens_WT_Y + \
                              self.ATTM_SaturatedBarrens_WT_M + self.ATTM_SaturatedBarrens_WT_O +\
                              self.ATTM_Shrubs_WT_O + self.ATTM_SmallLakes_WT_Y + \
                              self.ATTM_SmallLakes_WT_M + self.ATTM_SmallLakes_WT_O + \
                              self.ATTM_Urban_WT
            #-------------------
            # Note to Bob: Need to add cohorts of Graminoid and Shrub Tundra to everything above (and back
            #              through the initialization files to this point.
            #------------------
            
            #self.ATTM_Total = self.ATTM_Wet_NPG + self.ATTM_Wet_LCP + \
            #                  self.ATTM_Wet_CLC + self.ATTM_Wet_FCP + \
            #                  self.ATTM_Wet_HCP + self.ATTM_Gra_NPG + \
            #                  self.ATTM_Gra_LCP + self.ATTM_Gra_FCP + \
            #                  self.ATTM_Gra_HCP + self.ATTM_Shr_NPG + \
            #                  self.ATTM_Shr_LCP + self.ATTM_Shr_FCP + \
            #                  self.ATTM_Shr_HCP + self.ATTM_Rivers  + \
            #                  self.ATTM_Lakes   + self.ATTM_Ponds   + \
            #                  self.ATTM_Urban
            # ===================================
            # Move to the next element
            # ===================================
            count = count +1

#    if PLOT == 'TRUE' or FIGURE == 'TRUE':
    if self.initialize['Initial_Cohort_Distribution_Figure'].lower() == 'yes':
    
        # Files for plotting & reference #
        #ATTM_Wet_NPG_plot =  np.reshape(self.ATTM_Wet_NPG, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Wet_LCP_plot =  np.reshape(self.ATTM_Wet_LCP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Wet_CLC_plot =  np.reshape(self.ATTM_Wet_CLC, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Wet_FCP_plot =  np.reshape(self.ATTM_Wet_FCP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Wet_HCP_plot =  np.reshape(self.ATTM_Wet_HCP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Rivers_plot  =  np.reshape(self.ATTM_Rivers,  [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Lakes_plot   =  np.reshape(self.ATTM_Lakes,   [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Ponds_plot   =  np.reshape(self.ATTM_Ponds,   [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        #ATTM_Urban_plot   =  np.reshape(self.ATTM_Urban,   [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Total_plot    = np.reshape(self.ATTM_Total,   [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_CLC_WT_Y_plot = np.reshape(self.ATTM_CLC_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_CLC_WT_M_plot = np.reshape(self.ATTM_CLC_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_CLC_WT_O_plot = np.reshape(self.ATTM_CLC_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_CoastalWaters_WT_O_plot = np.reshape(self.ATTM_CoastalWaters_WT_O, \
                                                   [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_DrainedSlope_WT_Y_plot = np.reshape(self.ATTM_DrainedSlope_WT_Y, \
                                                     [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_DrainedSlope_WT_M_plot = np.reshape(self.ATTM_DrainedSlope_WT_M, \
                                                     [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_DrainedSlope_WT_O_plot = np.reshape(self.ATTM_DrainedSlope_WT_O, \
                                                     [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_FCP_WT_Y_plot = np.reshape(self.ATTM_FCP_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_FCP_WT_M_plot = np.reshape(self.ATTM_FCP_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_FCP_WT_O_plot = np.reshape(self.ATTM_FCP_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_HCP_WT_Y_plot = np.reshape(self.ATTM_HCP_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_HCP_WT_M_plot = np.reshape(self.ATTM_HCP_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_HCP_WT_O_plot = np.reshape(self.ATTM_HCP_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_LCP_WT_Y_plot = np.reshape(self.ATTM_LCP_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_LCP_WT_M_plot = np.reshape(self.ATTM_LCP_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_LCP_WT_O_plot = np.reshape(self.ATTM_LCP_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Meadow_WT_Y_plot = np.reshape(self.ATTM_Meadow_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Meadow_WT_M_plot = np.reshape(self.ATTM_Meadow_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Meadow_WT_O_plot = np.reshape(self.ATTM_Meadow_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SandDunes_WT_Y_plot = np.reshape(self.ATTM_SandDunes_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SandDunes_WT_M_plot = np.reshape(self.ATTM_SandDunes_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SandDunes_WT_O_plot = np.reshape(self.ATTM_SandDunes_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SaturatedBarrens_WT_Y_plot = np.reshape(self.ATTM_SandDunes_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SaturatedBarrens_WT_M_plot = np.reshape(self.ATTM_SandDunes_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SaturatedBarrens_WT_O_plot = np.reshape(self.ATTM_SandDunes_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Shrubs_WT_O_plot = np.reshape(self.ATTM_Shrubs_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Urban_WT_plot = np.reshape(self.ATTM_Urban_WT, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_LargeLakes_WT_Y_plot = np.reshape(self.ATTM_LargeLakes_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_LargeLakes_WT_M_plot = np.reshape(self.ATTM_LargeLakes_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_LargeLakes_WT_O_plot = np.reshape(self.ATTM_LargeLakes_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_MediumLakes_WT_Y_plot = np.reshape(self.ATTM_MediumLakes_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_MediumLakes_WT_M_plot = np.reshape(self.ATTM_MediumLakes_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_MediumLakes_WT_O_plot = np.reshape(self.ATTM_MediumLakes_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SmallLakes_WT_Y_plot = np.reshape(self.ATTM_SmallLakes_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SmallLakes_WT_M_plot = np.reshape(self.ATTM_SmallLakes_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_SmallLakes_WT_O_plot = np.reshape(self.ATTM_SmallLakes_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Ponds_WT_Y_plot = np.reshape(self.ATTM_Ponds_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Ponds_WT_M_plot = np.reshape(self.ATTM_Ponds_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Ponds_WT_O_plot = np.reshape(self.ATTM_Ponds_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Rivers_WT_Y_plot = np.reshape(self.ATTM_Rivers_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Rivers_WT_M_plot = np.reshape(self.ATTM_Rivers_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Rivers_WT_O_plot = np.reshape(self.ATTM_Rivers_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # Move to output directory #
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/')
        
        #-----------------------------------------------------------------------
        # Create Figures, Plots, and Binary files for each cohort
        # ----------------------------------------------------------------------
        if self.initialize['WetNPG_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_NPG_plot, interpolation = 'nearest', cmap= 'spectral', vmin=0.0, vmax=1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Non-Polygonal Ground Initial Cohort Distribution')
            pl.savefig('./Wet_NPG/Initial_Wet_NPG.png', format = 'png')
            self.ATTM_Wet_NPG.tofile('./Wet_NPG/Wet_NPG_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['WetLCP_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_LCP_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Low Center Polygon Initial Cohort Distribution')
            pl.savefig('./Wet_LCP/Initial_Wet_LCP.png', format = 'png')
            self.ATTM_Wet_LCP.tofile('./Wet_LCP/Wet_LCP_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['WetCLC_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_CLC_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Coalescent Low Center Polygon Initial Cohort Distribution')
            pl.savefig('./Wet_CLC/Initial_Wet_CLC.png', format = 'png')
            self.ATTM_Wet_CLC.tofile('./Wet_CLC/Wet_CLC_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['WetFCP_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_FCP_plot, interpolation = 'nearest', cmap= 'spectral', vmin= 1.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland Flat Center Polygon Initial Cohort Distribution')
            pl.savefig('./Wet_FCP/Initial_Wet_FCP.png', format = 'png')
            self.ATTM_Wet_FCP.tofile('./Wet_FCP/Wet_FCP_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['WetHCP_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Wet_HCP_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Wetland High Center Polygon Initial Cohort Distribution')
            pl.savefig('./Wet_HCP/Initial_Wet_HCP.png', format = 'png')
            self.ATTM_Wet_HCP.tofile('./Wet_HCP/Wet_HCP_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Ponds_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Ponds_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Ponds Initial Cohort Distribution')
            pl.savefig('./Ponds/Initial_Ponds.png', format = 'png')
            self.ATTM_Ponds.tofile('./Ponds/Ponds_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Lakes_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Lakes_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Lakes Initial Cohort Distribution')
            pl.savefig('./Lakes/Initial_Lakes.png', format = 'png')
            self.ATTM_Lakes.tofile('./Lakes/Lakes_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Rivers_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Rivers_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Rivers Initial Cohort Distribution')
            pl.savefig('./Other_Cohorts/Initial_Rivers.png', format = 'png')
            self.ATTM_Rivers.tofile('./Other_Cohorts/Rivers_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Urban_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Urban_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Urban Area Initial Cohort Distribution')
            pl.savefig('./Other_Cohorts/Initial_Urban.png', format = 'png')
            self.ATTM_Urban.tofile('./Other_Cohorts/Urban_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['All_Cohorts_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Total_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('All Cohorts Combined Distribution')
            pl.savefig('./All_Cohorts/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Total.tofile('./All_Cohorts/Total_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['CLC_WT_Y_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_CLC_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Coalescent Low Center Polygon\n Wetland Tundra - Young Age\n Initial Cohort Distribution')
            pl.savefig('./CLC_WT_Y/Initial_Cohorts_CLC_WT_Y.png', format = 'png')
            self.ATTM_CLC_WT_Y.tofile('./CLC_WT_Y/CLC_WT_Y_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['CLC_WT_M_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_CLC_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Coalescent Low Center Polygon\n Wetland Tundra - Medium Age\n Initial Cohort Distribution')
            pl.savefig('./CLC_WT_M/Initial_Cohorts_CLC_WT_M.png', format = 'png')
            self.ATTM_CLC_WT_M.tofile('./CLC_WT_M/CLC_WT_M_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['CLC_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_CLC_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Coalescent Low Center Polygon\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./CLC_WT_O/Initial_Cohorts_CLC_WT_O.png', format = 'png')
            self.ATTM_CLC_WT_O.tofile('./CLC_WT_O/CLC_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['CoastalWaters_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_CoastalWaters_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Coastal Waters\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./CoastalWaters_WT_O/Initial_Cohorts_CoastalWaters_WT_O.png', format = 'png')
            self.ATTM_CoastalWaters_WT_O.tofile('./CoastalWaters_WT_O/CoastalWaters_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['DrainedSlope_WT_Y_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_DrainedSlope_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Drained Slope\n Wetland Tundra - Young Age\n Initial Cohort Distribution')
            pl.savefig('./DrainedSlope_WT_Y/Initial_Cohorts_DrainedSlope_WT_Y.png', format = 'png')
            self.ATTM_DrainedSlope_WT_Y.tofile('./DrainedSlope_WT_Y/DrainedSlope_WT_Y_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['DrainedSlope_WT_M_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_DrainedSlope_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Drained Slope\n Wetland Tundra - Medium Age\n Initial Cohort Distribution')
            pl.savefig('./DrainedSlope_WT_M/Initial_Cohorts_DrainedSlope_WT_M.png', format = 'png')
            self.ATTM_DrainedSlope_WT_M.tofile('./DrainedSlope_WT_M/DrainedSlope_WT_M_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['DrainedSlope_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_DrainedSlope_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Drained Slope\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./DrainedSlope_WT_O/Initial_Cohorts_DrainedSlope_WT_O.png', format = 'png')
            self.ATTM_DrainedSlope_WT_O.tofile('./DrainedSlope_WT_O/DrainedSlope_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['FCP_WT_Y_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_FCP_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Flat Center Polygon\n Wetland Tundra - Young Age\n Initial Cohort Distribution')
            pl.savefig('./FCP_WT_Y/Initial_Cohorts_FCP_WT_Y.png', format = 'png')
            self.ATTM_FCP_WT_Y.tofile('./FCP_WT_Y/FCP_WT_Y_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['FCP_WT_M_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_FCP_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Flat Center Polygon\n Wetland Tundra - Medium Age\n Initial Cohort Distribution')
            pl.savefig('./FCP_WT_M/Initial_Cohorts_FCP_WT_M.png', format = 'png')
            self.ATTM_FCP_WT_M.tofile('./FCP_WT_M/FCP_WT_M_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['FCP_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_FCP_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Flat Center Polygon\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./FCP_WT_O/Initial_Cohorts_FCP_WT_O.png', format = 'png')
            self.ATTM_FCP_WT_O.tofile('./FCP_WT_O/FCP_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['HCP_WT_Y_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_HCP_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('High Center Polygon\n Wetland Tundra - Young Age\n Initial Cohort Distribution')
            pl.savefig('./HCP_WT_Y/Initial_Cohorts_HCP_WT_Y.png', format = 'png')
            self.ATTM_HCP_WT_Y.tofile('./HCP_WT_Y/HCP_WT_Y_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['HCP_WT_M_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_HCP_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('High Center Polygon\n Wetland Tundra - Medium Age\n Initial Cohort Distribution')
            pl.savefig('./HCP_WT_M/Initial_Cohorts_HCP_WT_M.png', format = 'png')
            self.ATTM_HCP_WT_M.tofile('./HCP_WT_M/HCP_WT_M_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['HCP_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_HCP_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('High Center Polygon\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./HCP_WT_O/Initial_Cohorts_HCP_WT_O.png', format = 'png')
            self.ATTM_HCP_WT_O.tofile('./HCP_WT_O/HCP_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['LCP_WT_Y_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_LCP_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Low Center Polygon\n Wetland Tundra - Young Age\n Initial Cohort Distribution')
            pl.savefig('./LCP_WT_Y/Initial_Cohorts_LCP_WT_Y.png', format = 'png')
            self.ATTM_LCP_WT_Y.tofile('./LCP_WT_Y/LCP_WT_Y_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['LCP_WT_M_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_LCP_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Low Center Polygon\n Wetland Tundra - Medium Age\n Initial Cohort Distribution')
            pl.savefig('./LCP_WT_M/Initial_Cohorts_LCP_WT_M.png', format = 'png')
            self.ATTM_LCP_WT_M.tofile('./LCP_WT_M/LCP_WT_M_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['LCP_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_LCP_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Low Center Polygon\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./LCP_WT_O/Initial_Cohorts_LCP_WT_O.png', format = 'png')
            self.ATTM_LCP_WT_O.tofile('./LCP_WT_O/LCP_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Meadow_WT_Y_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Meadow_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Meadow\n Wetland Tundra - Young Age\n Initial Cohort Distribution')
            pl.savefig('./Meadow_WT_Y/Initial_Cohorts_Meadow_WT_Y.png', format = 'png')
            self.ATTM_Meadow_WT_Y.tofile('./Meadow_WT_Y/Meadow_WT_Y_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Meadow_WT_M_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Meadow_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Meadow\n Wetland Tundra - Medium Age\n Initial Cohort Distribution')
            pl.savefig('./Meadow_WT_M/Initial_Cohorts_Meadow_WT_M.png', format = 'png')
            self.ATTM_Meadow_WT_M.tofile('./Meadow_WT_M/Meadow_WT_M_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Meadow_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Meadow_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Meadow\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./Meadow_WT_O/Initial_Cohorts_Meadow_WT_O.png', format = 'png')
            self.ATTM_Meadow_WT_O.tofile('./Meadow_WT_O/Meadow_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SaturatedBarrens_WT_Y_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SaturatedBarrens_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Saturated Barrens\n Wetland Tundra - Young Age\n Initial Cohort Distribution')
            pl.savefig('./SaturatedBarrens_WT_Y/Initial_Cohorts_SaturatedBarrens_WT_Y.png', format = 'png')
            self.ATTM_SaturatedBarrens_WT_Y.tofile('./SaturatedBarrens_WT_Y/SaturatedBarrens_WT_Y_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SaturatedBarrens_WT_M_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SaturatedBarrens_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Saturated Barrens\n Wetland Tundra - Medium Age\n Initial Cohort Distribution')
            pl.savefig('./SaturatedBarrens_WT_M/Initial_Cohorts_SaturatedBarrens_WT_M.png', format = 'png')
            self.ATTM_SaturatedBarrens_WT_M.tofile('./SaturatedBarrens_WT_M/SaturatedBarrens_WT_M_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SaturatedBarrens_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SaturatedBarrens_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Saturated Barrens\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./SaturatedBarrens_WT_O/Initial_Cohorts_SaturatedBarrens_WT_O.png', format = 'png')
            self.ATTM_SaturatedBarrens_WT_O.tofile('./SaturatedBarrens_WT_O/SaturatedBarrens_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SandDunes_WT_Y_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SandDunes_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Sand Dunes\n Wetland Tundra - Young Age\n Initial Cohort Distribution')
            pl.savefig('./SandDunes_WT_Y/Initial_Cohorts_SandDunes_WT_Y.png', format = 'png')
            self.ATTM_SandDunes_WT_Y.tofile('./SandDunes_WT_Y/SandDunes_WT_Y_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SandDunes_WT_M_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SandDunes_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Sand Dunes\n Wetland Tundra - Medium Age\n Initial Cohort Distribution')
            pl.savefig('./SandDunes_WT_M/Initial_Cohorts_SandDunes_WT_M.png', format = 'png')
            self.ATTM_SandDunes_WT_M.tofile('./SandDunes_WT_M/SandDunes_WT_M_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SandDunes_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SandDunes_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Sand Dunes\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./SandDunes_WT_O/Initial_Cohorts_SandDunes_WT_O.png', format = 'png')
            self.ATTM_SandDunes_WT_O.tofile('./SandDunes_WT_O/SandDunes_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Shrubs_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Shrubs_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Shrubs\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./Shrubs_WT_O/Initial_Cohorts_Shrubs_WT_O.png', format = 'png')
            self.ATTM_Shrubs_WT_O.tofile('./Shrubs_WT_O/Shrubs_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Urban_WT_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Urban_WT_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Urban Area \n Wetland Tundra \n Initial Cohort Distribution')
            pl.savefig('./Urban_WT/Initial_Cohorts_Urban_WT.png', format = 'png')
            self.ATTM_Urban_WT.tofile('./Urban_WT/Urban_WT_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['LargeLakes_WT_Y_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_LargeLakes_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Large Lakes\n Wetland Tundra - Young Age\n Initial Cohort Distribution')
            pl.savefig('./LargeLakes_WT_Y/Initial_Cohorts_LargeLakes_WT_Y.png', format = 'png')
            self.ATTM_LargeLakes_WT_Y.tofile('./LargeLakes_WT_Y/LargeLakes_WT_Y_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['LargeLakes_WT_M_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_LargeLakes_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Large Lakes\n Wetland Tundra - Medium Age\n Initial Cohort Distribution')
            pl.savefig('./LargeLakes_WT_M/Initial_Cohorts_LargeLakes_WT_M.png', format = 'png')
            self.ATTM_LargeLakes_WT_M.tofile('./LargeLakes_WT_M/LargeLakes_WT_M_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['LargeLakes_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_LargeLakes_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('LargeLakes\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./LargeLakes_WT_O/Initial_Cohorts_LargeLakes_WT_O.png', format = 'png')
            self.ATTM_LargeLakes_WT_O.tofile('./LargeLakes_WT_O/LargeLakes_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['MediumLakes_WT_Y_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_MediumLakes_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Medium Lakes\n Wetland Tundra - Young Age\n Initial Cohort Distribution')
            pl.savefig('./MediumLakes_WT_Y/Initial_Cohorts_MediumLakes_WT_Y.png', format = 'png')
            self.ATTM_MediumLakes_WT_Y.tofile('./MediumLakes_WT_Y/MediumLakes_WT_Y_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['MediumLakes_WT_M_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_MediumLakes_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Medium Lakes\n Wetland Tundra - Medium Age\n Initial Cohort Distribution')
            pl.savefig('./MediumLakes_WT_M/Initial_Cohorts_MediumLakes_WT_M.png', format = 'png')
            self.ATTM_MediumLakes_WT_M.tofile('./MediumLakes_WT_M/MediumLakes_WT_M_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['MediumLakes_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_MediumLakes_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('MediumLakes\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./MediumLakes_WT_O/Initial_Cohorts_MediumLakes_WT_O.png', format = 'png')
            self.ATTM_MediumLakes_WT_O.tofile('./MediumLakes_WT_O/MediumLakes_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SmallLakes_WT_Y_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SmallLakes_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Small Lakes\n Wetland Tundra - Young Age\n Initial Cohort Distribution')
            pl.savefig('./SmallLakes_WT_Y/Initial_Cohorts_SmallLakes_WT_Y.png', format = 'png')
            self.ATTM_SmallLakes_WT_Y.tofile('./SmallLakes_WT_Y/SmallLakes_WT_Y_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SmallLakes_WT_M_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SmallLakes_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Small Lakes\n Wetland Tundra - Medium Age\n Initial Cohort Distribution')
            pl.savefig('./SmallLakes_WT_M/Initial_Cohorts_SmallLakes_WT_M.png', format = 'png')
            self.ATTM_SmallLakes_WT_M.tofile('./SmallLakes_WT_M/SmallLakes_WT_M_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['SmallLakes_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_SmallLakes_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('SmallLakes\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./SmallLakes_WT_O/Initial_Cohorts_SmallLakes_WT_O.png', format = 'png')
            self.ATTM_SmallLakes_WT_O.tofile('./SmallLakes_WT_O/SmallLakes_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Ponds_WT_Y_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Ponds_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Ponds\n Wetland Tundra - Young Age\n Initial Cohort Distribution')
            pl.savefig('./Ponds_WT_Y/Initial_Cohorts_Ponds_WT_Y.png', format = 'png')
            self.ATTM_Ponds_WT_Y.tofile('./Ponds_WT_Y/Ponds_WT_Y_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Ponds_WT_M_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Ponds_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Ponds\n Wetland Tundra - Medium Age\n Initial Cohort Distribution')
            pl.savefig('./Ponds_WT_M/Initial_Cohorts_Ponds_WT_M.png', format = 'png')
            self.ATTM_Ponds_WT_M.tofile('./Ponds_WT_M/Ponds_WT_M_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Ponds_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Ponds_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Ponds\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./Ponds_WT_O/Initial_Cohorts_Ponds_WT_O.png', format = 'png')
            self.ATTM_Ponds_WT_O.tofile('./Ponds_WT_O/Ponds_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Rivers_WT_Y_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Rivers_WT_Y_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Rivers\n Wetland Tundra - Young Age\n Initial Cohort Distribution')
            pl.savefig('./Rivers_WT_Y/Initial_Cohorts_Rivers_WT_Y.png', format = 'png')
            self.ATTM_Rivers_WT_Y.tofile('./Rivers_WT_Y/Rivers_WT_Y_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Rivers_WT_M_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Rivers_WT_M_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Rivers\n Wetland Tundra - Medium Age\n Initial Cohort Distribution')
            pl.savefig('./Rivers_WT_M/Initial_Cohorts_Rivers_WT_M.png', format = 'png')
            self.ATTM_Rivers_WT_M.tofile('./Rivers_WT_M/Rivers_WT_M_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Rivers_WT_O_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Rivers_WT_O_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Rivers\n Wetland Tundra - Old Age\n Initial Cohort Distribution')
            pl.savefig('./Rivers_WT_O/Initial_Cohorts_Rivers_WT_O.png', format = 'png')
            self.ATTM_Rivers_WT_O.tofile('./Rivers_WT_O/Rivers_WT_O_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        
        # Return to Run Directory
        os.chdir(self.control['Run_dir'])

def tanana_initial_cohort_population(self):
    # ----------------------------------------------------------------------------
    # Note -- in this Barrow example:
    # ATTM Model domain is 1000m by 1000m (self.Y_resolution, self.X_resolution)
    # Geotiff files are 25m by 25m (self.y_res, self.x_res)
    # Therefore, the # of rows/columns to to read are 40x40 (1000/25, 1000/25)
    # ----------------------------------------------------------------------------
    #def count_cohorts(a, b):
    #    b = a > 0
    #    return len(a[b])
    #-----------------------------------------------------------------------------

    # ------------------------------------------------------------------------------
    # Define the ATTM Land Surface Cohorts
    #      NOTE: Assuming the entire Barrow test site is considered Wetland Tundra
    # ------------------------------------------------------------------------------
    count = 0
    for i in range(0, int(self.nrows), int(float(self.Y_resolution)/(self.y_res))):
        for j in range(0, int(self.ncols), int(float(self.X_resolution)/(self.x_res))):
            # ==================================
            # Tanana Flats - Old Bog
            # ==================================
            A = self.TF_OB[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                           j:j+int(float(self.X_resolution)/(self.x_res))-1]

            b = A > 0
            self.ATTM_TF_OB[count] = len(A[b])
            # ==================================
            # Tanana Flats - Young Bog
            # ==================================
            A = self.TF_YB[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                           j:j+int(float(self.X_resolution)/(self.x_res))-1]

            b = A > 0
            self.ATTM_TF_YB[count] = len(A[b])
            # =============================================
            # Tanana Flats - Old Fen
            # =============================================
            A = self.TF_YF[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                           j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_TF_YF[count] = len(A[b])
            # ===================================
            # Tanana Flats - Young Fen
            # ===================================
            A = self.TF_YF[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                           j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_TF_YF[count] = len(A[b])
            # ===================================
            # Tanana Flats - Coniferous Permafrost Plateau
            # ===================================
            A = self.TF_Con_PP[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                               j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_TF_Con_PP[count] = len(A[b])
            # ===================================
            # Tanana Flats - Deciduous Permafrost Plateau
            # ===================================
            A = self.TF_Dec_PP[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                               j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_TF_Dec_PP[count] = len(A[b])
            # ===================================
            # Tanana Flats - Thermokarst Lakes
            # ===================================
            A = self.TF_TL[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                           j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_TF_TL[count] = len(A[b])
            # ===================================
            # Total
            # ===================================
            self.ATTM_Total = self.ATTM_TF_OB + self.ATTM_TF_YB + \
                              self.ATTM_TF_OF + self.ATTM_TF_YF + \
                              self.ATTM_TF_Con_PP + self.ATTM_TF_Dec_PP + \
                              self.ATTM_TF_TL
            # ===================================
            # Move to the next element
            # ===================================
            count = count +1

    if self.initialize['Initial_Cohort_Distribution_Figure'].lower() == 'yes':
    
        # Files for plotting & reference #
        ATTM_TF_OB_plot     =  np.reshape(self.ATTM_TF_OB, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_YB_plot     =  np.reshape(self.ATTM_TF_YB, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_OF_plot     =  np.reshape(self.ATTM_TF_OF, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_YF_plot     =  np.reshape(self.ATTM_TF_YF, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_Con_PP_plot =  np.reshape(self.ATTM_TF_Con_PP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_Dec_PP_plot =  np.reshape(self.ATTM_TF_Dec_PP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_TF_TL_plot     =  np.reshape(self.ATTM_TF_TL, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Total_plot     =  np.reshape(self.ATTM_Total,   [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # Move to output directory #
        os.chdir(self.control['Run_dir']+self.Output_directory)
        
        #-----------------------------------------------------------------------
        # Create Figures, Plots, and Binary files for each cohort
        # ----------------------------------------------------------------------
        if self.initialize['TF_OB_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_OB_plot, interpolation = 'nearest', cmap= 'spectral', vmin=0.0, vmax=1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Tanana Flats - Old Bog Initial Cohort Distribution')
            pl.savefig('./TF_OB/Initial_TF_OB.png', format = 'png')
            self.ATTM_TF_OB.tofile('./TF_OB/TF_OB_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['TF_YB_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_YB_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Tanana Flats Young Bog Initial Cohort Distribution')
            pl.savefig('./TF_YB/Initial_TF_YB.png', format = 'png')
            self.ATTM_TF_YB.tofile('./TF_YB/TF_YB_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['TF_OF_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_OF_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Tanana Flats Old Fen Initial Cohort Distribution')
            pl.savefig('./TF_OF/Initial_TF_OF.png', format = 'png')
            self.ATTM_TF_OF.tofile('./TF_OF/TF_OF_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['TF_YF_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_YF_plot, interpolation = 'nearest', cmap= 'spectral', vmin= 1.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Tanana Flats Young Fen Initial Cohort Distribution')
            pl.savefig('./TF_YF/Initial_TF_YF.png', format = 'png')
            self.ATTM_TF_YF.tofile('./TF_YF/TF_YF_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['TF_Con_PP_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_Con_PP_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Tanana Flats Coniferous Permafrost Plateau Initial Cohort Distribution')
            pl.savefig('./TF_Con_PP/Initial_TF_Con_PP.png', format = 'png')
            self.ATTM_TF_Con_PP.tofile('./TF_Con_PP/TF_Con_PP_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['TF_Dec_PP_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_Dec_PP_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Tanana Flats Deciduous Permafrost Plateau Initial Cohort Distribution')
            pl.savefig('./TF_Dec_PP/Initial_TF_Con_PP.png', format = 'png')
            self.ATTM_TF_Dec_PP.tofile('./TF_Dec_PP/TF_Dec_PP_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------       
        if self.initialize['TF_TL_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_TF_TL_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Tanana Flats Thermokarst Lake Initial Cohort Distribution')
            pl.savefig('./TF_TL/Initial_Ponds.png', format = 'png')
            self.ATTM_TF_TL.tofile('./TF_TL/TF_TL_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['TF_All_Cohorts_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Total_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 0.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('All Cohorts Combined Distribution')
            pl.savefig('./TF_All_Cohorts/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Total.tofile('./TF_All_Cohorts/Total_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        # Return to Run Directory
        os.chdir(self.control['Run_dir'])

#===========================================================================================================
def yukon_initial_cohort_population(self):
    # Implemented 16 June 2016 - Bolton
    # Modified 28 July 2016 - Bolton: Adding young bogs and fens and clustering
    
    #==============================================================================
    # Note -- in this Barrow example:
    # ATTM Model domain is 1000m by 1000m (self.Y_resolution, self.X_resolution)
    # Geotiff files are 25m by 25m (self.y_res, self.x_res)
    # Therefore, the # of rows/columns to to read are 40x40 (1000/25, 1000/25)
    # ----------------------------------------------------------------------------
    #def count_cohorts(a, b):
    #    b = a > 0
    #    return len(a[b])
    #-----------------------------------------------------------------------------
    #=============================================================================
    count = 0

    for i in range(0, int(self.nrows), int(float(self.Y_resolution)/(self.y_res))):
        for j in range(0, int(self.ncols), int(float(self.X_resolution)/(self.x_res))):
            #--------------------------------------------------------------------------
            # Barren ground, Yukon Flats
            #--------------------------------------------------------------------------
            A = self.Barren_Yukon[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                  j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Barren_Yukon[count] = len(A[b])
            #--------------------------------------------------------------------------
            # Bogs, Yukon Flats
            #--------------------------------------------------------------------------
            A = self.Bog_Yukon[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                               j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Bog_Yukon[count] = len(A[b])
            #--------------------------------------------------------------------------
            # Deciduous Forest, Yukon Flats
            #--------------------------------------------------------------------------
            A = self.DeciduousForest_Yukon[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                          j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_DeciduousForest_Yukon[count] = len(A[b])
            #--------------------------------------------------------------------------
            # Dwarf Shrubs, Yukon Flats
            #--------------------------------------------------------------------------
            A = self.DwarfShrub_Yukon[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                      j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_DwarfShrub_Yukon[count] = len(A[b])
            #--------------------------------------------------------------------------
            # Evergreen Forest, Yukon Flats
            #--------------------------------------------------------------------------
            A = self.EvergreenForest_Yukon[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                           j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_EvergreenForest_Yukon[count] = len(A[b])
            #--------------------------------------------------------------------------
            # Fens, Yukon Flats
            #--------------------------------------------------------------------------
            A = self.Fen_Yukon[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                               j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Fen_Yukon[count] = len(A[b])
            #--------------------------------------------------------------------------
            # Lakes, Yukon Flats
            #--------------------------------------------------------------------------
            A = self.Lake_Yukon[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Lake_Yukon[count] = len(A[b])
            #--------------------------------------------------------------------------
            # Ponds, Yukon Flats
            #--------------------------------------------------------------------------
            A = self.Pond_Yukon[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Pond_Yukon[count] = len(A[b])
            #--------------------------------------------------------------------------
            # Rivers, Yukon Flats
            #--------------------------------------------------------------------------
            A = self.River_Yukon[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                 j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_River_Yukon[count] = len(A[b])
            #--------------------------------------------------------------------------
            # Shrub Scrub, Yukon Flats
            #--------------------------------------------------------------------------
            A = self.ShrubScrub_Yukon[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                      j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_ShrubScrub_Yukon[count] = len(A[b])
            #--------------------------------------------------------------------------
            # Unclassfied, Yukon Flats
            #--------------------------------------------------------------------------
            A = self.Unclassified_Yukon[i:i+int(float(self.Y_resolution)/(self.y_res))-1, \
                                        j:j+int(float(self.X_resolution)/(self.x_res))-1]
            b = A > 0
            self.ATTM_Unclassified_Yukon[count] = len(A[b])

            count = count + 1


    # =============================================================================
    # If the Young_Fen/Bog_Flag is set to "yes", create artifical young fens/bogs
    # based upon a random distribution between specified boundaries in the
    # Control file
    # =============================================================================
    if self.Young_Fen_Flag.lower() == 'yes':
        for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
            # Determine the fraction of the total fen that is young
            young_fen_percentage = random.uniform(self.Lower_Fen_Percentage, self.Upper_Fen_Percentage)/100.0
            young_fen_count = self.ATTM_Fen_Yukon[i] * young_fen_percentage
            # Remove the young fen fraction from the total fen
            self.ATTM_Fen_Yukon[i] = self.ATTM_Fen_Yukon[i] - young_fen_count
            # Determine fraction of the young fen that will be uniformally distributed through time
            # at initialziation (young fen = 0-99 years age)
            young_fen_fraction = young_fen_count / 100.0
            # Populate young bog cohort data arrays
            self.ATTM_Fen_Yukon_00[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_01[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_02[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_03[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_04[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_05[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_06[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_07[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_08[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_09[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_10[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_11[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_12[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_13[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_14[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_15[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_16[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_17[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_18[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_19[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_20[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_21[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_22[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_23[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_24[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_25[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_26[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_27[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_28[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_29[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_30[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_31[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_32[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_33[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_34[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_35[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_36[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_37[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_38[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_39[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_40[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_41[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_42[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_43[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_44[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_45[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_46[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_47[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_48[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_49[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_50[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_51[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_52[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_53[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_54[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_55[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_56[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_57[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_58[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_59[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_60[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_61[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_62[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_63[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_64[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_65[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_66[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_67[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_68[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_69[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_70[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_71[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_72[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_73[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_74[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_75[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_76[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_77[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_78[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_79[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_80[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_81[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_82[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_83[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_84[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_85[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_86[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_87[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_88[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_89[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_90[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_91[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_92[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_93[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_94[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_95[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_96[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_97[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_98[i] = young_fen_fraction
            self.ATTM_Fen_Yukon_99[i] = young_fen_fraction
            # population clustered arrays (10 year clusters - for TEM)
            self.ATTM_Fen_Yukon_00_09[i] = young_fen_fraction * 10.
            self.ATTM_Fen_Yukon_10_19[i] = young_fen_fraction * 10.
            self.ATTM_Fen_Yukon_20_29[i] = young_fen_fraction * 10.
            self.ATTM_Fen_Yukon_30_39[i] = young_fen_fraction * 10.
            self.ATTM_Fen_Yukon_40_49[i] = young_fen_fraction * 10.
            self.ATTM_Fen_Yukon_50_59[i] = young_fen_fraction * 10.
            self.ATTM_Fen_Yukon_60_69[i] = young_fen_fraction * 10.
            self.ATTM_Fen_Yukon_70_79[i] = young_fen_fraction * 10.
            self.ATTM_Fen_Yukon_80_89[i] = young_fen_fraction * 10.
            self.ATTM_Fen_Yukon_90_99[i] = young_fen_fraction * 10.
            
    if self.Young_Bog_Flag.lower() == 'yes':
        for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
            # Determine the fraction of the total bog that is young
            young_bog_percentage = random.uniform(self.Lower_Bog_Percentage, self.Upper_Bog_Percentage)/100.0
            young_bog_count = self.ATTM_Bog_Yukon[i] * young_bog_percentage
            # Remove the young bog fraction from the total bog
            self.ATTM_Bog_Yukon[i] = self.ATTM_Bog_Yukon[i] - young_bog_count
            # Determine fraction of the young bog that will be uniformally distributed through time
            # at initialziation (young bog = 0-99 years age)
            young_bog_fraction = young_bog_count / 100.0
            # Populate young bog cohort data arrays
            self.ATTM_Bog_Yukon_00[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_01[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_02[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_03[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_04[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_05[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_06[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_07[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_08[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_09[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_10[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_11[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_12[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_13[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_14[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_15[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_16[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_17[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_18[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_19[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_20[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_21[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_22[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_23[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_24[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_25[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_26[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_27[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_28[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_29[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_30[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_31[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_32[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_33[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_34[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_35[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_36[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_37[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_38[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_39[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_40[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_41[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_42[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_43[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_44[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_45[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_46[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_47[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_48[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_49[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_50[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_51[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_52[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_53[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_54[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_55[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_56[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_57[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_58[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_59[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_60[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_61[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_62[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_63[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_64[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_65[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_66[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_67[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_68[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_69[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_70[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_71[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_72[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_73[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_74[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_75[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_76[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_77[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_78[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_79[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_80[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_81[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_82[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_83[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_84[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_85[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_86[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_87[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_88[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_89[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_90[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_91[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_92[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_93[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_94[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_95[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_96[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_97[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_98[i] = young_bog_fraction
            self.ATTM_Bog_Yukon_99[i] = young_bog_fraction
            # populate clustered arrays (10 year clumps - for TEM)
            self.ATTM_Bog_Yukon_00_09[i] = young_bog_fraction * 10.
            self.ATTM_Bog_Yukon_10_19[i] = young_bog_fraction * 10.
            self.ATTM_Bog_Yukon_20_29[i] = young_bog_fraction * 10.
            self.ATTM_Bog_Yukon_30_39[i] = young_bog_fraction * 10.
            self.ATTM_Bog_Yukon_40_49[i] = young_bog_fraction * 10.
            self.ATTM_Bog_Yukon_50_59[i] = young_bog_fraction * 10.
            self.ATTM_Bog_Yukon_60_69[i] = young_bog_fraction * 10.
            self.ATTM_Bog_Yukon_70_79[i] = young_bog_fraction * 10.
            self.ATTM_Bog_Yukon_80_89[i] = young_bog_fraction * 10.
            self.ATTM_Bog_Yukon_90_99[i] = young_bog_fraction * 10.
            # Test  -- works
#            test_total = self.ATTM_Bog_Yukon_01[i] + self.ATTM_Bog_Yukon_02[i] + \
#                         self.ATTM_Bog_Yukon_03[i] + self.ATTM_Bog_Yukon_04[i] + \
#                         self.ATTM_Bog_Yukon_05[i] + self.ATTM_Bog_Yukon_05[i] + \
#                         self.ATTM_Bog_Yukon_06[i] + self.ATTM_Bog_Yukon_07[i] + \
#                         self.ATTM_Bog_Yukon_08[i] + self.ATTM_Bog_Yukon_09[i]
#            print i, self.ATTM_Bog_Yukon_00_09[i], test_total

    #==========================================================================
    # Total, Yukon Flats
    #==========================================================================
    self.ATTM_Total = self.ATTM_Barren_Yukon + self.ATTM_Bog_Yukon + \
                      self.ATTM_Bog_Yukon_00_09 + self.ATTM_Bog_Yukon_10_19 + \
                      self.ATTM_Bog_Yukon_20_29 + self.ATTM_Bog_Yukon_30_39 + \
                      self.ATTM_Bog_Yukon_40_49 + self.ATTM_Bog_Yukon_50_59 + \
                      self.ATTM_Bog_Yukon_60_69 + self.ATTM_Bog_Yukon_70_79 + \
                      self.ATTM_Bog_Yukon_80_89 + self.ATTM_Bog_Yukon_90_99 + \
                      self.ATTM_DeciduousForest_Yukon + self.ATTM_DwarfShrub_Yukon + \
                      self.ATTM_EvergreenForest_Yukon  + self.ATTM_Fen_Yukon + \
                      self.ATTM_Fen_Yukon_00_09 + self.ATTM_Fen_Yukon_10_19 + \
                      self.ATTM_Fen_Yukon_20_29 + self.ATTM_Fen_Yukon_30_39 + \
                      self.ATTM_Fen_Yukon_40_49 + self.ATTM_Fen_Yukon_50_59 + \
                      self.ATTM_Fen_Yukon_60_69 + self.ATTM_Fen_Yukon_70_79 + \
                      self.ATTM_Fen_Yukon_80_89 + self.ATTM_Fen_Yukon_90_99 + \
                      self.ATTM_Lake_Yukon + self.ATTM_Pond_Yukon + \
                      self.ATTM_River_Yukon + self.ATTM_ShrubScrub_Yukon + \
                      self.ATTM_Unclassified_Yukon            
            
    # =======================================================
    # Create Initial Cohort Distribution Figures if required
    # =======================================================
    if self.initialize['Initial_Cohort_Distribution_Figure'].lower() == 'yes':
        ATTM_Total_plot   = np.reshape(self.ATTM_Total, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Barren_Yukon_plot = np.reshape(self.ATTM_Barren_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_plot    = np.reshape(self.ATTM_Bog_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_DeciduousForest_Yukon_plot = np.reshape(self.ATTM_DeciduousForest_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_DwarfShrub_Yukon_plot = np.reshape(self.ATTM_DwarfShrub_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_EvergreenForest_Yukon_plot = np.reshape(self.ATTM_EvergreenForest_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_plot = np.reshape(self.ATTM_Fen_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Lake_Yukon_plot = np.reshape(self.ATTM_Lake_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Pond_Yukon_plot = np.reshape(self.ATTM_Pond_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_River_Yukon_plot = np.reshape(self.ATTM_River_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_ShrubScrub_Yukon_plot = np.reshape(self.ATTM_ShrubScrub_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Unclassified_Yukon_plot = np.reshape(self.ATTM_Unclassified_Yukon, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_00_09_plot = np.reshape(self.ATTM_Bog_Yukon_00_09, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_10_19_plot = np.reshape(self.ATTM_Bog_Yukon_10_19, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_20_29_plot = np.reshape(self.ATTM_Bog_Yukon_20_29, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_30_39_plot = np.reshape(self.ATTM_Bog_Yukon_30_39, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_40_49_plot = np.reshape(self.ATTM_Bog_Yukon_40_49, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_50_59_plot = np.reshape(self.ATTM_Bog_Yukon_50_59, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_60_69_plot = np.reshape(self.ATTM_Bog_Yukon_60_69, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_70_79_plot = np.reshape(self.ATTM_Bog_Yukon_70_79, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_80_89_plot = np.reshape(self.ATTM_Bog_Yukon_80_89, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Bog_Yukon_90_99_plot = np.reshape(self.ATTM_Bog_Yukon_90_99, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_00_09_plot = np.reshape(self.ATTM_Fen_Yukon_00_09, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_10_19_plot = np.reshape(self.ATTM_Fen_Yukon_10_19, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_20_29_plot = np.reshape(self.ATTM_Fen_Yukon_20_29, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_30_39_plot = np.reshape(self.ATTM_Fen_Yukon_30_39, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_40_49_plot = np.reshape(self.ATTM_Fen_Yukon_40_49, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_50_59_plot = np.reshape(self.ATTM_Fen_Yukon_50_59, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_60_69_plot = np.reshape(self.ATTM_Fen_Yukon_60_69, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_70_79_plot = np.reshape(self.ATTM_Fen_Yukon_70_79, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_80_89_plot = np.reshape(self.ATTM_Fen_Yukon_80_89, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        ATTM_Fen_Yukon_90_99_plot = np.reshape(self.ATTM_Fen_Yukon_90_99, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        
        # Move to output directory #
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Yukon/')

        #---------------------------------------------------------
        # Create Figures, Plots and Binary files for each cohort
        #---------------------------------------------------------
        if self.initialize['Barren_Yukon_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Barren_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Barren\n Initial Cohort Distribution')
            pl.savefig('./Barren_Yukon/Initial_Cohorts_Barren_Yukon.png', format = 'png')
            self.ATTM_Barren_Yukon.tofile('./Barren_Yukon/Barren_Yukon_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Bog_Yukon_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs\n Initial Cohort Distribution')
            pl.savefig('./Bog_Yukon/Initial_Cohorts_Bog_Yukon.png', format = 'png')
            self.ATTM_Bog_Yukon.tofile('./Bog_Yukon/Bog_Yukon_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['DeciduousForest_Yukon_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_DeciduousForest_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Deciduous Forest\n Initial Cohort Distribution')
            pl.savefig('./DeciduousForest_Yukon/Initial_Cohorts_DeciduousForest_Yukon.png', format = 'png')
            self.ATTM_DeciduousForest_Yukon.tofile('./DeciduousForest_Yukon/DeciduousForest_Yukon_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------                                       
        if self.initialize['DwarfShrub_Yukon_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_DwarfShrub_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Dwarf Shrub\n Initial Cohort Distribution')
            pl.savefig('./DwarfShrub_Yukon/Initial_Cohorts_DwarfShrub_Yukon.png', format = 'png')
            self.ATTM_DwarfShrub_Yukon.tofile('./DwarfShrub_Yukon/DwarfShrub_Yukon_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Fen_Yukon_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens\n Initial Cohort Distribution')
            pl.savefig('./Fen_Yukon/Initial_Cohorts_Fen_Yukon.png', format = 'png')
            self.ATTM_Fen_Yukon.tofile('./Fen_Yukon/Fen_Yukon_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['EvergreenForest_Yukon_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_EvergreenForest_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - EvergreenForest\n Initial Cohort Distribution')
            pl.savefig('./EvergreenForest_Yukon/Initial_Cohorts_EvergreenForest_Yukon.png', format = 'png')
            self.ATTM_EvergreenForest_Yukon.tofile('./EvergreenForest_Yukon/EvergreenForest_Yukon_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Lake_Yukon_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Lake_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Lakes\n Initial Cohort Distribution')
            pl.savefig('./Lake_Yukon/Initial_Cohorts_Lake_Yukon.png', format = 'png')
            self.ATTM_Lake_Yukon.tofile('./Lake_Yukon/Lake_Yukon_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['Pond_Yukon_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Pond_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Ponds\n Initial Cohort Distribution')
            pl.savefig('./Pond_Yukon/Initial_Cohorts_Pond_Yukon.png', format = 'png')
            self.ATTM_Pond_Yukon.tofile('./Pond_Yukon/Pond_Yukon_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['River_Yukon_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_River_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Rivers\n Initial Cohort Distribution')
            pl.savefig('./River_Yukon/Initial_Cohorts_River_Yukon.png', format = 'png')
            self.ATTM_River_Yukon.tofile('./River_Yukon/River_Yukon_initial_cohorts.bin')
            pl.close()
        # ----------------------------------------------------------------------
        if self.initialize['ShrubScrub_Yukon_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_ShrubScrub_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Shrub-Scrub\n Initial Cohort Distribution')
            pl.savefig('./ShrubScrub_Yukon/Initial_Cohorts_ShrubScrub_Yukon.png', format = 'png')
            self.ATTM_ShrubScrub_Yukon.tofile('./ShrubScrub_Yukon/ShrubScrub_Yukon_initial_cohorts.bin')
            pl.close()
        #-------------------------------------------------------------------------
        if self.initialize['Unclassified_Yukon_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Unclassified_Yukon_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Unclassified\n Initial Cohort Distribution')
            pl.savefig('./Unclassified_Yukon/Initial_Cohorts_Unclassifeid_Yukon.png', format = 'png')
            self.ATTM_Unclassified_Yukon.tofile('./Unclassified_Yukon/Unclassified_Yukon_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['All_Cohorts_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Total_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('All Cohorts Combined Distribution')
            pl.savefig('./Yukon_All_Cohorts/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Total.tofile('./Yukon_All_Cohorts/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_00_09_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_00_09_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs age: 00_09')
            pl.savefig('./Bog_Yukon_00_09/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Bog_Yukon_00_09.tofile('./Bog_Yukon_00_09/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_10_19_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_10_19_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs age: 10_19')
            pl.savefig('./Bog_Yukon_10_19/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Bog_Yukon_10_19.tofile('./Bog_Yukon_10_19/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_20_29_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_20_29_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs age: 20_29')
            pl.savefig('./Bog_Yukon_20_29/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Bog_Yukon_20_29.tofile('./Bog_Yukon_20_29/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_30_39_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_30_39_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs age: 30_39')
            pl.savefig('./Bog_Yukon_30_39/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Bog_Yukon_30_39.tofile('./Bog_Yukon_30_39/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_40_49_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_40_49_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs age: 40_49')
            pl.savefig('./Bog_Yukon_40_49/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Bog_Yukon_40_49.tofile('./Bog_Yukon_40_49/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_50_59_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_50_59_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs age: 50_59')
            pl.savefig('./Bog_Yukon_50_59/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Bog_Yukon_50_59.tofile('./Bog_Yukon_50_59/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_60_69_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_60_69_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs age: 60_69')
            pl.savefig('./Bog_Yukon_60_69/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Bog_Yukon_60_69.tofile('./Bog_Yukon_60_69/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_70_79_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_70_79_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs age: 70_79')
            pl.savefig('./Bog_Yukon_70_79/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Bog_Yukon_70_79.tofile('./Bog_Yukon_70_79/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_80_89_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_80_89_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs age: 80_89')
            pl.savefig('./Bog_Yukon_80_89/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Bog_Yukon_80_89.tofile('./Bog_Yukon_80_89/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Bog_Yukon_90_99_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Bog_Yukon_90_99_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Bogs age: 90_99')
            pl.savefig('./Bog_Yukon_90_99/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Bog_Yukon_90_99.tofile('./Bog_Yukon_90_99/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_00_09_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_00_09_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens age: 00-09')
            pl.savefig('./Fen_Yukon_00_09/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Fen_Yukon_00_09.tofile('./Fen_Yukon_00_09/Total_initial_cohorts.bin')
            pl.close()            
        #---------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_10_19_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_10_19_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens age: 10-19')
            pl.savefig('./Fen_Yukon_10_19/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Fen_Yukon_10_19.tofile('./Fen_Yukon_10_19/Total_initial_cohorts.bin')
            pl.close()            
        #---------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_20_29_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_20_29_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens age: 20-29')
            pl.savefig('./Fen_Yukon_20_29/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Fen_Yukon_20_29.tofile('./Fen_Yukon_20_29/Total_initial_cohorts.bin')
            pl.close()            
        #---------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_30_39_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_30_39_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens age: 30-39')
            pl.savefig('./Fen_Yukon_30_39/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Fen_Yukon_30_39.tofile('./Fen_Yukon_30_39/Total_initial_cohorts.bin')
            pl.close()            
        #---------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_40_49_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_40_49_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens age: 40-49')
            pl.savefig('./Fen_Yukon_40_49/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Fen_Yukon_40_49.tofile('./Fen_Yukon_40_49/Total_initial_cohorts.bin')
            pl.close()            
        #---------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_50_59_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_50_59_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens age: 50-59')
            pl.savefig('./Fen_Yukon_50_59/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Fen_Yukon_50_59.tofile('./Fen_Yukon_50_59/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_60_69_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_60_69_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens age: 60-69')
            pl.savefig('./Fen_Yukon_60_69/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Fen_Yukon_60_69.tofile('./Fen_Yukon_60_69/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_70_79_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_70_79_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens age: 70-79')
            pl.savefig('./Fen_Yukon_70_79/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Fen_Yukon_70_79.tofile('./Fen_Yukon_70_79/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_80_89_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_80_89_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens age: 80-89')
            pl.savefig('./Fen_Yukon_80_89/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Fen_Yukon_80_89.tofile('./Fen_Yukon_80_89/Total_initial_cohorts.bin')
            pl.close()
        #---------------------------------------------------------------------------
        if self.initialize['Fen_Yukon_90_99_Figure'].lower() == 'yes':
            fig = pl.figure()
            pl.imshow(ATTM_Fen_Yukon_90_99_plot, interpolation = 'nearest', cmap= 'spectral', vmin = 0.0, vmax = 1.0)
            pl.colorbar(extend = 'max', shrink = 0.92)
            pl.title('Yukon Flats - Fens age: 90-99')
            pl.savefig('./Fen_Yukon_90_99/Initial_Total_Cohorts.png', format = 'png')
            self.ATTM_Fen_Yukon_90_99.tofile('./Fen_Yukon_90_99/Total_initial_cohorts.bin')
            pl.close()
        #=====================================================================================================
        # Return to Run Directory
        os.chdir(self.control['Run_dir'])
