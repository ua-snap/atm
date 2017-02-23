import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
import matplotlib.animation as animation
import subprocess

def Output_cohorts_by_year(self, time):#, Gra_NPG, Gra_LCP, Gra_FCP, Gra_HCP,
                           #Shr_NPG, Shr_LCP, Shr_FCP, Shr_HCP):#, Ponds,
                          # Lakes):

    #=======================================
    # OUTPUT FIGURES
    #----------------------------------------
    # Wetland Non-Polygonal Ground (meadow)
    # ---------------------------------------
    if self.Meadow_WT_Y['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Meadow_WT_Y/Year_Cohorts')
        Meadow_WT_Y_plot = np.reshape(self.ATTM_Meadow_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Meadow_WT_Y_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Meadow\n Young Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Meadow_WT_Y_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Meadow_WT_Y_plot.tofile('Meadow_WT_Y_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.Meadow_WT_M['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Meadow_WT_M/Year_Cohorts')
        Meadow_WT_M_plot = np.reshape(self.ATTM_Meadow_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Meadow_WT_M_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Meadow\n Medium Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Meadow_WT_M_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Meadow_WT_M_plot.tofile('Meadow_WT_M_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.Meadow_WT_O['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Meadow_WT_O/Year_Cohorts')
        Meadow_WT_O_plot = np.reshape(self.ATTM_Meadow_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Meadow_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Meadow\n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Meadow_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Meadow_WT_O_plot.tofile('Meadow_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.Meadow_WT_Y['Figures'].lower() == 'yes' and \
        self.Meadow_WT_M['Figures'].lower() == 'yes' and \
        self.Meadow_WT_O['Figures'].lower() == 'yes':

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Meadow_WT_Total/Year_Cohorts')
        ATTM_Meadow_WT_Total = self.ATTM_Meadow_WT_Y + self.ATTM_Meadow_WT_M + self.ATTM_Meadow_WT_O
        Meadow_WT_Total_plot = np.reshape(ATTM_Meadow_WT_Total, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Meadow_WT_Total_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Meadows\n Young, Medium, Old age\n'+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Meadow_WT_Total_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Meadow_WT_Total_plot.tofile('Meadow_WT_Total_Fractional_Area_'+str(year)+'.bin')
        pl.close()

    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra Low Center Polygons
    #------------------------------------------------------------------------------------------------------
    if self.LCP_WT_Y['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LCP_WT_Y/Year_Cohorts')
        LCP_WT_Y_plot = np.reshape(self.ATTM_LCP_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(LCP_WT_Y_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Low Center Polygons\n Young Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('LCP_WT_Y_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        LCP_WT_Y_plot.tofile('LCP_WT_Y_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LCP_WT_M['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LCP_WT_M/Year_Cohorts')
        LCP_WT_M_plot = np.reshape(self.ATTM_LCP_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(LCP_WT_M_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Low Center Polygons\n Medium Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('LCP_WT_M_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        LCP_WT_M_plot.tofile('LCP_WT_M_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LCP_WT_O['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LCP_WT_O/Year_Cohorts')
        LCP_WT_O_plot = np.reshape(self.ATTM_LCP_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(LCP_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Low Center Polygons\n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('LCP_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        LCP_WT_O_plot.tofile('LCP_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LCP_WT_Y['Figures'].lower() == 'yes' and \
        self.LCP_WT_M['Figures'].lower() == 'yes' and \
        self.LCP_WT_O['Figures'].lower() == 'yes':

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LCP_WT_Total/Year_Cohorts')
        ATTM_LCP_WT_Total = self.ATTM_LCP_WT_Y + self.ATTM_LCP_WT_M + self.ATTM_LCP_WT_O
        LCP_WT_Total_plot = np.reshape(ATTM_LCP_WT_Total, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(LCP_WT_Total_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Low Center Polygons \n Young, Medium, Old age \n'+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('LCP_WT_Total_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        LCP_WT_Total_plot.tofile('LCP_WT_Total_Fractional_Area_'+str(year)+'.bin')
        pl.close()

    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra Coalescent Low Center Polygons
    #------------------------------------------------------------------------------------------------------
    if self.CLC_WT_Y['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CLC_WT_Y/Year_Cohorts')
        CLC_WT_Y_plot = np.reshape(self.ATTM_CLC_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(CLC_WT_Y_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Coalescent Low Center Polygons \n Young Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('CLC_WT_Y_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        CLC_WT_Y_plot.tofile('CLC_WT_Y_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.CLC_WT_M['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CLC_WT_M/Year_Cohorts')
        CLC_WT_M_plot = np.reshape(self.ATTM_CLC_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(CLC_WT_M_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Coalescent Low Center Polygons\n Medium Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('CLC_WT_M_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        CLC_WT_M_plot.tofile('CLC_WT_M_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.CLC_WT_O['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CLC_WT_O/Year_Cohorts')
        CLC_WT_O_plot = np.reshape(self.ATTM_CLC_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(CLC_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Coalescent Low Center Polygons\n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('CLC_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        CLC_WT_O_plot.tofile('CLC_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.CLC_WT_Y['Figures'].lower() == 'yes' and \
        self.CLC_WT_M['Figures'].lower() == 'yes' and \
        self.CLC_WT_O['Figures'].lower() == 'yes':

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CLC_WT_Total/Year_Cohorts')
        ATTM_CLC_WT_Total = self.ATTM_CLC_WT_Y + self.ATTM_CLC_WT_M + self.ATTM_CLC_WT_O
        CLC_WT_Total_plot = np.reshape(ATTM_CLC_WT_Total, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(CLC_WT_Total_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Coalescent Low Center Polygons \n Young, Medium, Old age \n'+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('CLC_WT_Total_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        CLC_WT_Total_plot.tofile('CLC_WT_Total_Fractional_Area_'+str(year)+'.bin')
        pl.close()

    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra Flat Center Polygons
    #------------------------------------------------------------------------------------------------------
    if self.FCP_WT_Y['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/FCP_WT_Y/Year_Cohorts')
        FCP_WT_Y_plot = np.reshape(self.ATTM_FCP_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(FCP_WT_Y_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Flat Center Center Polygons \n Young Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('FCP_WT_Y_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        FCP_WT_Y_plot.tofile('FCP_WT_Y_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.FCP_WT_M['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/FCP_WT_M/Year_Cohorts')
        FCP_WT_M_plot = np.reshape(self.ATTM_FCP_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(FCP_WT_M_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Flat Center Center Polygons\n Medium Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('FCP_WT_M_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        FCP_WT_M_plot.tofile('FCP_WT_M_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.FCP_WT_O['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/FCP_WT_O/Year_Cohorts')
        FCP_WT_O_plot = np.reshape(self.ATTM_FCP_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(FCP_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Flat Center Center Polygons\n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('FCP_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        FCP_WT_O_plot.tofile('FCP_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.FCP_WT_Y['Figures'].lower() == 'yes' and \
        self.FCP_WT_M['Figures'].lower() == 'yes' and \
        self.FCP_WT_O['Figures'].lower() == 'yes':

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/FCP_WT_Total/Year_Cohorts')
        ATTM_FCP_WT_Total = self.ATTM_FCP_WT_Y + self.ATTM_FCP_WT_M + self.ATTM_FCP_WT_O
        FCP_WT_Total_plot = np.reshape(ATTM_FCP_WT_Total, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(FCP_WT_Total_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Flat Center Center Polygons \n Young, Medium, Old age \n'+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('FCP_WT_Total_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        FCP_WT_Total_plot.tofile('FCP_WT_Total_Fractional_Area_'+str(year)+'.bin')
        pl.close()

    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra High Center Polygons
    #------------------------------------------------------------------------------------------------------
    if self.HCP_WT_Y['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/HCP_WT_Y/Year_Cohorts')
        HCP_WT_Y_plot = np.reshape(self.ATTM_HCP_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(HCP_WT_Y_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra High Center Polygons \n Young Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('HCP_WT_Y_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        HCP_WT_Y_plot.tofile('HCP_WT_Y_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.HCP_WT_M['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/HCP_WT_M/Year_Cohorts')
        HCP_WT_M_plot = np.reshape(self.ATTM_HCP_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(HCP_WT_M_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - High Center Polygons\n Medium Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('HCP_WT_M_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        HCP_WT_M_plot.tofile('HCP_WT_M_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.HCP_WT_O['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/HCP_WT_O/Year_Cohorts')
        HCP_WT_O_plot = np.reshape(self.ATTM_HCP_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(HCP_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - High Center Polygons\n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('HCP_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        HCP_WT_O_plot.tofile('HCP_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.HCP_WT_Y['Figures'].lower() == 'yes' and \
        self.HCP_WT_M['Figures'].lower() == 'yes' and \
        self.HCP_WT_O['Figures'].lower() == 'yes':

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/HCP_WT_Total/Year_Cohorts')
        ATTM_HCP_WT_Total = self.ATTM_HCP_WT_Y + self.ATTM_HCP_WT_M + self.ATTM_HCP_WT_O
        HCP_WT_Total_plot = np.reshape(ATTM_HCP_WT_Total, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(HCP_WT_Total_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra High Center Polygons \n Young, Medium, Old age \n'+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('HCP_WT_Total_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        HCP_WT_Total_plot.tofile('HCP_WT_Total_Fractional_Area_'+str(year)+'.bin')
        pl.close()

    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra Large Lakes
    #------------------------------------------------------------------------------------------------------
    if self.LakePond['LargeLake_WT_Y_Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_Y/Year_Cohorts')
        LargeLake_WT_Y_plot = np.reshape(self.ATTM_LargeLakes_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(LargeLake_WT_Y_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Large Lakes \n Young Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('LargeLake_WT_Y_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        LargeLake_WT_Y_plot.tofile('LargeLake_WT_Y_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LakePond['LargeLake_WT_M_Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_M/Year_Cohorts')
        LargeLake_WT_M_plot = np.reshape(self.ATTM_LargeLakes_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(LargeLake_WT_M_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Large Lakes\n Medium Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('LargeLake_WT_M_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        LargeLake_WT_M_plot.tofile('LargeLake_WT_M_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LakePond['LargeLake_WT_O_Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_O/Year_Cohorts')
        LargeLake_WT_O_plot = np.reshape(self.ATTM_LargeLakes_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(LargeLake_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Large Lakes\n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('LargeLakes_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        LargeLake_WT_O_plot.tofile('LargeLake_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LakePond['LargeLake_WT_Y_Figures'].lower() == 'yes' and \
        self.LakePond['LargeLake_WT_M_Figures'].lower() == 'yes' and \
        self.LakePond['LargeLake_WT_O_Figures'].lower() == 'yes':

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_Total/Year_Cohorts')
        ATTM_LargeLake_WT_Total = self.ATTM_LargeLakes_WT_Y + self.ATTM_LargeLakes_WT_M + \
          self.ATTM_LargeLakes_WT_O
        LargeLake_WT_Total_plot = \
          np.reshape(ATTM_LargeLake_WT_Total, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
          
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(LargeLake_WT_Total_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Large Lakes \n Young, Medium, Old age \n'+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('LargeLake_WT_Total_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        LargeLake_WT_Total_plot.tofile('LargeLake_WT_Total_Fractional_Area_'+str(year)+'.bin')
        pl.close()

    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra Medium Lakes
    #------------------------------------------------------------------------------------------------------
    if self.LakePond['MediumLake_WT_Y_Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_Y/Year_Cohorts')
        MediumLake_WT_Y_plot = np.reshape(self.ATTM_MediumLakes_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(MediumLake_WT_Y_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Medium Lakes \n Young Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('MediumLake_WT_Y_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        MediumLake_WT_Y_plot.tofile('MediumLake_WT_Y_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LakePond['MediumLake_WT_M_Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_M/Year_Cohorts')
        MediumLake_WT_M_plot = np.reshape(self.ATTM_MediumLakes_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(MediumLake_WT_M_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Medium Lakes\n Medium Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('MediumLake_WT_M_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        MediumLake_WT_M_plot.tofile('MediumLake_WT_M_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LakePond['MediumLake_WT_O_Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_O/Year_Cohorts')
        MediumLake_WT_O_plot = np.reshape(self.ATTM_MediumLakes_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(MediumLake_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Medium Lakes\n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('MediumLakes_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        MediumLake_WT_O_plot.tofile('MediumLake_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LakePond['MediumLake_WT_Y_Figures'].lower() == 'yes' and \
        self.LakePond['MediumLake_WT_M_Figures'].lower() == 'yes' and \
        self.LakePond['MediumLake_WT_O_Figures'].lower() == 'yes':

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_Total/Year_Cohorts')
        ATTM_MediumLake_WT_Total = self.ATTM_MediumLakes_WT_Y + self.ATTM_MediumLakes_WT_M + \
          self.ATTM_MediumLakes_WT_O
        MediumLake_WT_Total_plot = \
          np.reshape(ATTM_MediumLake_WT_Total, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
          
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(MediumLake_WT_Total_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Medium Lakes \n Young, Medium, Old age \n'+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('MediumLake_WT_Total_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        MediumLake_WT_Total_plot.tofile('MediumLake_WT_Total_Fractional_Area_'+str(year)+'.bin')
        pl.close()

    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra Small Lakes
    #------------------------------------------------------------------------------------------------------
    if self.LakePond['SmallLake_WT_Y_Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_Y/Year_Cohorts')
        SmallLake_WT_Y_plot = np.reshape(self.ATTM_SmallLakes_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(SmallLake_WT_Y_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Small Lakes \n Young Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('SmallLake_WT_Y_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        SmallLake_WT_Y_plot.tofile('SmallLake_WT_Y_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LakePond['SmallLake_WT_M_Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_M/Year_Cohorts')
        SmallLake_WT_M_plot = np.reshape(self.ATTM_SmallLakes_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(SmallLake_WT_M_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Small Lakes\n Medium Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('SmallLake_WT_M_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        SmallLake_WT_M_plot.tofile('SmallLake_WT_M_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LakePond['SmallLake_WT_O_Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_O/Year_Cohorts')
        SmallLake_WT_O_plot = np.reshape(self.ATTM_SmallLakes_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(SmallLake_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Small Lakes\n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('SmallLakes_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        SmallLake_WT_O_plot.tofile('SmallLake_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LakePond['SmallLake_WT_Y_Figures'].lower() == 'yes' and \
        self.LakePond['SmallLake_WT_M_Figures'].lower() == 'yes' and \
        self.LakePond['SmallLake_WT_O_Figures'].lower() == 'yes':

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_Total/Year_Cohorts')
        ATTM_SmallLake_WT_Total = self.ATTM_SmallLakes_WT_Y + self.ATTM_SmallLakes_WT_M + \
          self.ATTM_SmallLakes_WT_O
        SmallLake_WT_Total_plot = \
          np.reshape(ATTM_SmallLake_WT_Total, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
          
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(SmallLake_WT_Total_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Small Lakes \n Young, Small, Old age \n'+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('SmallLake_WT_Total_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        SmallLake_WT_Total_plot.tofile('SmallLake_WT_Total_Fractional_Area_'+str(year)+'.bin')
        pl.close()

    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra Small, Medium, and Large Lakes Combined
    #------------------------------------------------------------------------------------------------------    
    if self.LakePond['SmallLake_WT_Y_Figures'].lower() == 'yes' and \
        self.LakePond['SmallLake_WT_M_Figures'].lower() == 'yes' and \
        self.LakePond['SmallLake_WT_O_Figures'].lower() == 'yes' and \
        self.LakePond['MediumLake_WT_Y_Figures'].lower() == 'yes' and \
        self.LakePond['MediumLake_WT_M_Figures'].lower() == 'yes' and \
        self.LakePond['MediumLake_WT_O_Figures'].lower() == 'yes' and \
        self.LakePond['LargeLake_WT_Y_Figures'].lower() == 'yes' and \
        self.LakePond['LargeLake_WT_M_Figures'].lower() == 'yes' and \
        self.LakePond['LargeLake_WT_O_Figures'].lower() == 'yes' :

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Lakes_WT/Year_Cohorts')

        ATTM_Lakes_Total = self.ATTM_SmallLakes_WT_Y + self.ATTM_SmallLakes_WT_M + self.ATTM_SmallLakes_WT_O + \
          self.ATTM_MediumLakes_WT_Y + self.ATTM_MediumLakes_WT_M + self.ATTM_MediumLakes_WT_O + \
          self.ATTM_LargeLakes_WT_Y + self.ATTM_LargeLakes_WT_M + self.ATTM_LargeLakes_WT_O

        Lakes_WT_Total_plot = \
          np.reshape(ATTM_Lakes_Total, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Lakes_WT_Total_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Lakes Total \n'+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Lakes_WT_Total_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Lakes_WT_Total_plot.tofile('Lakes_WT_Total_Fractional_Area_'+str(year)+'.bin')
        pl.close()        
        

    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra Ponds
    #------------------------------------------------------------------------------------------------------
    if self.LakePond['Pond_WT_Y_Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_Y/Year_Cohorts')
        Ponds_WT_Y_plot = np.reshape(self.ATTM_Ponds_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Ponds_WT_Y_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Ponds \n Young Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Ponds_WT_Y_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Ponds_WT_Y_plot.tofile('Ponds_WT_Y_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LakePond['Pond_WT_M_Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_M/Year_Cohorts')
        Ponds_WT_M_plot = np.reshape(self.ATTM_Ponds_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Ponds_WT_M_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Ponds \n Medium Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Ponds_WT_M_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Ponds_WT_M_plot.tofile('Ponds_WT_M_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LakePond['Pond_WT_O_Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_O/Year_Cohorts')
        Ponds_WT_O_plot = np.reshape(self.ATTM_Ponds_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Ponds_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Ponds\n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Ponds_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Ponds_WT_O_plot.tofile('Ponds_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.LakePond['Pond_WT_Y_Figures'].lower() == 'yes' and \
        self.LakePond['Pond_WT_M_Figures'].lower() == 'yes' and \
        self.LakePond['Pond_WT_O_Figures'].lower() == 'yes':

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_Total/Year_Cohorts')
        ATTM_Ponds_WT_Total = self.ATTM_Ponds_WT_Y + self.ATTM_Ponds_WT_M + \
          self.ATTM_Ponds_WT_O
        Ponds_WT_Total_plot = \
          np.reshape(ATTM_Ponds_WT_Total, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
          
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Ponds_WT_Total_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Ponds \n Young, Small, Old age \n'+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Ponds_WT_Total_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Ponds_WT_Total_plot.tofile('Ponds_WT_Total_Fractional_Area_'+str(year)+'.bin')
        pl.close()


    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra Drained Slopes
    #------------------------------------------------------------------------------------------------------
    if self.DrainedSlope_WT_Y['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/DrainedSlope_WT_Y/Year_Cohorts')
        DrainedSlope_WT_Y_plot = np.reshape(self.ATTM_DrainedSlope_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(DrainedSlope_WT_Y_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Drained Slopes \n Young Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('DrainedSlope_WT_Y_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        DrainedSlope_WT_Y_plot.tofile('DrainedSlope_WT_Y_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.DrainedSlope_WT_M['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/DrainedSlope_WT_M/Year_Cohorts')
        DrainedSlope_WT_M_plot = np.reshape(self.ATTM_DrainedSlope_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(DrainedSlope_WT_M_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Drained Slopes\n Medium Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('DrainedSlope_WT_M_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        DrainedSlope_WT_M_plot.tofile('DrainedSlope_WT_M_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.DrainedSlope_WT_O['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/DrainedSlope_WT_O/Year_Cohorts')
        DrainedSlope_WT_O_plot = np.reshape(self.ATTM_DrainedSlope_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(DrainedSlope_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Drained Slopes\n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('DrainedSlope_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        DrainedSlope_WT_O_plot.tofile('DrainedSlope_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.DrainedSlope_WT_Y['Figures'].lower() == 'yes' and \
        self.DrainedSlope_WT_M['Figures'].lower() == 'yes' and \
        self.DrainedSlope_WT_O['Figures'].lower() == 'yes':

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/DrainedSlope_WT_Total/Year_Cohorts')
        ATTM_DrainedSlope_WT_Total = self.ATTM_DrainedSlope_WT_Y + self.ATTM_DrainedSlope_WT_M + self.ATTM_DrainedSlope_WT_O
        DrainedSlope_WT_Total_plot = np.reshape(ATTM_DrainedSlope_WT_Total, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(DrainedSlope_WT_Total_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Drained Slopes \n Young, Medium, Old age \n'+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('DrainedSlope_WT_Total_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        DrainedSlope_WT_Total_plot.tofile('DrainedSlope_WT_Total_Fractional_Area_'+str(year)+'.bin')
        pl.close()


    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra Coastal Waters
    #------------------------------------------------------------------------------------------------------
    if self.CoastalWaters_WT_O['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CoastalWaters_WT_O/Year_Cohorts')
        CoastalWaters_WT_O_plot = np.reshape(self.ATTM_CoastalWaters_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(CoastalWaters_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Coastal Waters\n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('CoastalWaters_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        CoastalWaters_WT_O_plot.tofile('CoastalWaters_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close() 

    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra No Data
    #------------------------------------------------------------------------------------------------------
    if self.NoData_WT_O['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Other_Cohorts/Year_Cohorts')
        NoData_WT_O_plot = np.reshape(self.ATTM_NoData_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(NoData_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - No Data\n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('NoData_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        NoData_WT_O_plot.tofile('NoData_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close()


    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra Sand Dunes
    #------------------------------------------------------------------------------------------------------
    if self.SandDunes_WT_Y['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SandDunes_WT_Y/Year_Cohorts')
        SandDunes_WT_Y_plot = np.reshape(self.ATTM_SandDunes_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(SandDunes_WT_Y_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Sand Dunes \n Young Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('SandDunes_WT_Y_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        SandDunes_WT_Y_plot.tofile('SandDunes_WT_Y_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.SandDunes_WT_M['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SandDunes_WT_M/Year_Cohorts')
        SandDunes_WT_M_plot = np.reshape(self.ATTM_SandDunes_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(SandDunes_WT_M_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Sand Dunes\n Medium Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('SandDunes_WT_M_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        SandDunes_WT_M_plot.tofile('SandDunes_WT_M_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.SandDunes_WT_O['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SandDunes_WT_O/Year_Cohorts')
        SandDunes_WT_O_plot = np.reshape(self.ATTM_SandDunes_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(SandDunes_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Sand Dunes\n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('SandDunes_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        SandDunes_WT_O_plot.tofile('SandDunes_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.SandDunes_WT_Y['Figures'].lower() == 'yes' and \
        self.SandDunes_WT_M['Figures'].lower() == 'yes' and \
        self.SandDunes_WT_O['Figures'].lower() == 'yes':

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SandDunes_WT_Total/Year_Cohorts')
        ATTM_SandDunes_WT_Total = self.ATTM_SandDunes_WT_Y + self.ATTM_SandDunes_WT_M + self.ATTM_SandDunes_WT_O
        SandDunes_WT_Total_plot = np.reshape(ATTM_SandDunes_WT_Total, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(SandDunes_WT_Total_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Sand Dunes \n Young, Medium, Old age \n'+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('SandDunes_WT_Total_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        SandDunes_WT_Total_plot.tofile('SandDunes_WT_Total_Fractional_Area_'+str(year)+'.bin')
        pl.close()


    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra Saturated Barrens
    #------------------------------------------------------------------------------------------------------
    if self.SaturatedBarrens_WT_Y['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SaturatedBarrens_WT_Y/Year_Cohorts')
        SaturatedBarrens_WT_Y_plot = np.reshape(self.ATTM_SaturatedBarrens_WT_Y, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(SaturatedBarrens_WT_Y_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Saturated Barrens \n Young Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('SaturatedBarrens_WT_Y_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        SaturatedBarrens_WT_Y_plot.tofile('SaturatedBarrens_WT_Y_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.SaturatedBarrens_WT_M['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SaturatedBarrens_WT_M/Year_Cohorts')
        SaturatedBarrens_WT_M_plot = np.reshape(self.ATTM_SaturatedBarrens_WT_M, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(SaturatedBarrens_WT_M_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Saturated Barrens\n Medium Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('SaturatedBarrens_WT_M_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        SaturatedBarrens_WT_M_plot.tofile('SaturatedBarrens_WT_M_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.SaturatedBarrens_WT_O['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SaturatedBarrens_WT_O/Year_Cohorts')
        SaturatedBarrens_WT_O_plot = np.reshape(self.ATTM_SaturatedBarrens_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(SaturatedBarrens_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra - Saturated Barrens\n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('SaturatedBarrens_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        SaturatedBarrens_WT_O_plot.tofile('SaturatedBarrens_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close()        

    if self.SaturatedBarrens_WT_Y['Figures'].lower() == 'yes' and \
        self.SaturatedBarrens_WT_M['Figures'].lower() == 'yes' and \
        self.SaturatedBarrens_WT_O['Figures'].lower() == 'yes':

        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SaturatedBarrens_WT_Total/Year_Cohorts')
        ATTM_SaturatedBarrens_WT_Total = self.ATTM_SaturatedBarrens_WT_Y + self.ATTM_SaturatedBarrens_WT_M + self.ATTM_SaturatedBarrens_WT_O
        SaturatedBarrens_WT_Total_plot = np.reshape(ATTM_SaturatedBarrens_WT_Total, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(SaturatedBarrens_WT_Total_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Saturated Barrens \n Young, Medium, Old age \n'+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('SaturatedBarrens_WT_Total_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        SaturatedBarrens_WT_Total_plot.tofile('SaturatedBarrens_WT_Total_Fractional_Area_'+str(year)+'.bin')
        pl.close()

    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra Shrubs
    #------------------------------------------------------------------------------------------------------
    if self.Shrubs_WT_O['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Shrubs_WT_O/Year_Cohorts')
        Shrubs_WT_O_plot = np.reshape(self.ATTM_Shrubs_WT_O, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Shrubs_WT_O_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Shrubs \n Old Age - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Shrubs_WT_O_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Shrubs_WT_O_plot.tofile('Shrubs_WT_O_Fractional_Area_'+str(year)+'.bin')
        pl.close()         

    # -----------------------------------------------------------------------------------------------------
    # Wetland Tundra Urban
    #------------------------------------------------------------------------------------------------------
    if self.Urban_WT['Figures'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Urban_WT/Year_Cohorts')
        Urban_WT_plot = np.reshape(self.ATTM_Urban_WT, [int(self.ATTM_nrows), int(self.ATTM_ncols)])
        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Urban_WT_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Tundra Urban area\n '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Urban_WT_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Urban_WT_plot.tofile('Urban_WT_Fractional_Area_'+str(year)+'.bin')
        pl.close()    

        
####
####
####

    # if self.WetNPG['Figures'].lower() == 'yes':
    #     # Change to Output Directory
    #     os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_NPG/Year_Cohorts')

    #     Wet_NPG_plot = np.reshape(self.ATTM_Wet_NPG, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

    #     # --------------------------------------
    #     # Output figures placed into directory
    #     # --------------------------------------
    #     year = str(int(time + self.Year[0]))
    #     # ---------------------------------------
    #     # Create figures and corresponding data
    #     #----------------------------------------
    #     fig = pl.figure()
    #     pl.imshow(Wet_NPG_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
    #     pl.title('Wetland Non-Polygonal Ground Fractional Area - '+str(year))
    #     pl.colorbar(extend = 'neither', shrink = 0.92)
    #     pl.savefig('Wet_NPG_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
    #     Wet_NPG_plot.tofile('Wet_NPG_Fractional_Area_'+str(year)+'.bin')
    #     pl.close()
    # # ---------------------------------------
    # # Wetland Low Center Polygons
    # # ---------------------------------------
    # if self.WetLCP['Figures'].lower() == 'yes':
    #     # Change to Output Directory
    #     os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_LCP/Year_Cohorts')

    #     Wet_LCP_plot = np.reshape(self.ATTM_Wet_LCP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

    #     # --------------------------------------
    #     # Output figures placed into directory
    #     # --------------------------------------
    #     year = str(int(time + self.Year[0]))
    #     # ---------------------------------------
    #     # Create figures and corresponding data
    #     #----------------------------------------
    #     fig = pl.figure()
    #     pl.imshow(Wet_LCP_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
    #     pl.title('Wetland Low Center Polygons Fractional Area - '+str(year))
    #     pl.colorbar(extend = 'neither', shrink = 0.92)
    #     pl.savefig('Wet_LCP_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
    #     Wet_LCP_plot.tofile('Wet_LCP_Fractional_Area_'+str(year)+'.bin')
    #     pl.close()
    # # ---------------------------------------
    # # Wetland Coalescent Low Center Polygons
    # # ---------------------------------------
    # if self.WetCLC['Figures'].lower() == 'yes' :
    #     # Change to Output Directory
    #     os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_CLC/Year_Cohorts')

    #     Wet_CLC_plot = np.reshape(self.ATTM_Wet_CLC, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

    #     # --------------------------------------
    #     # Output figures placed into directory
    #     # --------------------------------------
    #     year = str(int(time + self.Year[0]))
    #     # ---------------------------------------
    #     # Create figures and corresponding data
    #     #----------------------------------------
    #     fig = pl.figure()
    #     pl.imshow(Wet_CLC_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
    #     pl.title('Wetland Coalescent Low Center Polygons Fractional Area - '+str(year))
    #     pl.colorbar(extend = 'neither', shrink = 0.92)
    #     pl.savefig('Wet_CLC_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
    #     Wet_CLC_plot.tofile('Wet_CLC_Fractional_Area_'+str(year)+'.bin')
    #     pl.close()
    # # ---------------------------------------
    # # Wetland Flat Center Polygons
    # # ---------------------------------------
    # if self.WetFCP['Figures'].lower() == 'yes' :
    #     # Change to Output Directory
    #     os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_FCP/Year_Cohorts')

    #     Wet_FCP_plot = np.reshape(self.ATTM_Wet_FCP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

    #     # --------------------------------------
    #     # Output figures placed into directory
    #     # --------------------------------------
    #     year = str(int(time + self.Year[0]))
    #     # ---------------------------------------
    #     # Create figures and corresponding data
    #     #----------------------------------------
    #     fig = pl.figure()
    #     pl.imshow(Wet_FCP_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
    #     pl.title('Wetland Flat Center Polygons Fractional Area - '+str(year))
    #     pl.colorbar(extend = 'neither', shrink = 0.92)
    #     pl.savefig('Wet_FCP_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
    #     Wet_FCP_plot.tofile('Wet_FCP_Fractional_Area_'+str(year)+'.bin')
    #     pl.close()
    # # ---------------------------------------
    # # Wetland High Center Polygons
    # # ---------------------------------------
    # if self.WetHCP['Figures'].lower() == 'yes':
    #     # Change to Output Directory
    #     os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_HCP/Year_Cohorts')

    #     Wet_HCP_plot = np.reshape(self.ATTM_Wet_HCP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

    #     # --------------------------------------
    #     # Output figures placed into directory
    #     # --------------------------------------
    #     year = str(int(time + self.Year[0]))
    #     # ---------------------------------------
    #     # Create figures and corresponding data
    #     #----------------------------------------
    #     fig = pl.figure()
    #     pl.imshow(Wet_HCP_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
    #     pl.title('Wetland High Center Polygons Fractional Area - '+str(year))
    #     pl.colorbar(extend = 'neither', shrink = 0.92)
    #     pl.savefig('Wet_HCP_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
    #     Wet_HCP_plot.tofile('Wet_HCP_Fractional_Area_'+str(year)+'.bin')
    #     pl.close()
    # # ---------------------------------------
    # # Ponds
    # # ---------------------------------------
    # if self.LakePond['Pond_Figures'].lower() == 'yes':
    #     # Change to Output Directory
    #     os.chdir(self.control['Run_dir']+self.Output_directory+'/Ponds/Year_Cohorts')

    #     Ponds_plot = np.reshape(self.ATTM_Ponds, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

    #     # --------------------------------------
    #     # Output figures placed into directory
    #     # --------------------------------------
    #     year = str(int(time + self.Year[0]))
    #     # ---------------------------------------
    #     # Create figures and corresponding data
    #     #----------------------------------------
    #     fig = pl.figure()
    #     pl.imshow(Ponds_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
    #     pl.title('Ponds Fractional Area - '+str(year))
    #     pl.colorbar(extend = 'neither', shrink = 0.92)
    #     pl.savefig('Ponds_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
    #     Ponds_plot.tofile('Ponds_Fractional_Area_'+str(year)+'.bin')
    #     pl.close()
    # # ---------------------------------------
    # # Lakes
    # # ---------------------------------------
    # if self.LakePond['Lake_Figures'].lower() == 'yes':
    #     # Change to Output Directory
    #     os.chdir(self.control['Run_dir']+self.Output_directory+'/Lakes/Year_Cohorts')

    #     Lakes_plot = np.reshape(self.ATTM_Lakes, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

    #     # --------------------------------------
    #     # Output figures placed into directory
    #     # --------------------------------------
    #     year = str(int(time + self.Year[0]))
    #     # ---------------------------------------
    #     # Create figures and corresponding data
    #     #----------------------------------------
    #     fig = pl.figure()
    #     pl.imshow(Lakes_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
    #     pl.title('Lakes Fractional Area - '+str(year))
    #     pl.colorbar(extend = 'neither', shrink = 0.92)
    #     pl.savefig('Lakes_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
    #     Lakes_plot.tofile('Lakes_Fractional_Area_'+str(year)+'.bin')     
    #     pl.close()
################################
# Animation of Fractional Area #
################################
def write_Fractions_avi(self):#, Gra_NPG, Gra_LCP, Gra_FCP, Gra_HCP, Shr_NPG, Shr_LCP,
                        #Shr_FCP, Shr_HCP, Ponds, Lakes):
    # ---------------------------------------
    # Wetland Non-Polygonal Ground (Meadows)
    # ---------------------------------------
    if self.Meadow_WT_Y['Movie'].lower() == 'yes' and self.Meadow_WT_Y['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Meadow_WT_Y/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_Meadow_WT_Y_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.Meadow_WT_M['Movie'].lower() == 'yes' and self.Meadow_WT_M['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Meadow_WT_M/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_Meadow_WT_M_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])        
    if self.Meadow_WT_O['Movie'].lower() == 'yes' and self.Meadow_WT_O['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Meadow_WT_O/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_Meadow_WT_O_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.Meadow_WT_Y['Movie'].lower() == 'yes' and self.Meadow_WT_Y['Figures'].lower() == 'yes' and \
      self.Meadow_WT_M['Movie'].lower() == 'yes' and self.Meadow_WT_M['Figures'].lower() == 'yes' and \
      self.Meadow_WT_O['Movie'].lower() == 'yes' and self.Meadow_WT_O['Figures'].lower() == 'yes' :
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Meadow_WT_Total/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_Meadow_WT_Total_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])      
    # ---------------------------
    # Wetland Low Center Polygon
    # ---------------------------
    if self.LCP_WT_Y['Movie'].lower() == 'yes' and self.LCP_WT_Y['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LCP_WT_Y/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_LCP_WT_Y_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.LCP_WT_M['Movie'].lower() == 'yes' and self.LCP_WT_M['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LCP_WT_M/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_LCP_WT_M_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])        
    if self.LCP_WT_O['Movie'].lower() == 'yes' and self.LCP_WT_O['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LCP_WT_O/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_LCP_WT_O_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.LCP_WT_Y['Movie'].lower() == 'yes' and self.LCP_WT_Y['Figures'].lower() == 'yes' and \
      self.LCP_WT_M['Movie'].lower() == 'yes' and self.LCP_WT_M['Figures'].lower() == 'yes' and \
      self.LCP_WT_O['Movie'].lower() == 'yes' and self.LCP_WT_O['Figures'].lower() == 'yes' :
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LCP_WT_Total/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_LCP_WT_Total_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])    
    # --------------------------------------
    # Wetland Coalescent Low Center Polygon
    # --------------------------------------
    if self.CLC_WT_Y['Movie'].lower() == 'yes' and self.CLC_WT_Y['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CLC_WT_Y/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_CLC_WT_Y_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.CLC_WT_M['Movie'].lower() == 'yes' and self.CLC_WT_M['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CLC_WT_M/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_CLC_WT_M_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])        
    if self.CLC_WT_O['Movie'].lower() == 'yes' and self.CLC_WT_O['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CLC_WT_O/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_CLC_WT_O_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.CLC_WT_Y['Movie'].lower() == 'yes' and self.CLC_WT_Y['Figures'].lower() == 'yes' and \
      self.CLC_WT_M['Movie'].lower() == 'yes' and self.CLC_WT_M['Figures'].lower() == 'yes' and \
      self.CLC_WT_O['Movie'].lower() == 'yes' and self.CLC_WT_O['Figures'].lower() == 'yes' :
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CLC_WT_Total/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_CLC_WT_Total_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])    
    # -----------------------------
    # Wetland Flat Center Polygon
    # -----------------------------
    if self.FCP_WT_Y['Movie'].lower() == 'yes' and self.FCP_WT_Y['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/FCP_WT_Y/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_FCP_WT_Y_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.FCP_WT_M['Movie'].lower() == 'yes' and self.FCP_WT_M['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/FCP_WT_M/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_FCP_WT_M_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])        
    if self.FCP_WT_O['Movie'].lower() == 'yes' and self.FCP_WT_O['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/FCP_WT_O/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_FCP_WT_O_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.FCP_WT_Y['Movie'].lower() == 'yes' and self.FCP_WT_Y['Figures'].lower() == 'yes' and \
      self.FCP_WT_M['Movie'].lower() == 'yes' and self.FCP_WT_M['Figures'].lower() == 'yes' and \
      self.FCP_WT_O['Movie'].lower() == 'yes' and self.FCP_WT_O['Figures'].lower() == 'yes' :
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/FCP_WT_Total/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_FCP_WT_Total_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])    
    # ----------------------------
    # Wetland High Center Polygon
    # ----------------------------
    if self.HCP_WT_Y['Movie'].lower() == 'yes' and self.HCP_WT_Y['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/HCP_WT_Y/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_HCP_WT_Y_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.HCP_WT_M['Movie'].lower() == 'yes' and self.HCP_WT_M['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/HCP_WT_M/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_HCP_WT_M_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])        
    if self.HCP_WT_O['Movie'].lower() == 'yes' and self.HCP_WT_O['Figures'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/HCP_WT_O/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_HCP_WT_O_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.HCP_WT_Y['Movie'].lower() == 'yes' and self.HCP_WT_Y['Figures'].lower() == 'yes' and \
      self.HCP_WT_M['Movie'].lower() == 'yes' and self.HCP_WT_M['Figures'].lower() == 'yes' and \
      self.HCP_WT_O['Movie'].lower() == 'yes' and self.HCP_WT_O['Figures'].lower() == 'yes' :
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/HCP_WT_Total/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_HCP_WT_Total_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])    
    # -----------------------------
    # Ponds
    # -----------------------------
    if self.LakePond['Pond_WT_Y_Figures'].lower() == 'yes' and self.LakePond['Pond_WT_Y_Movie'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_Y/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_Ponds_WT_Y_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.LakePond['Pond_WT_M_Figures'].lower() == 'yes' and self.LakePond['Pond_WT_M_Movie'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_M/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_Ponds_WT_M_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.LakePond['Pond_WT_O_Figures'].lower() == 'yes' and self.LakePond['Pond_WT_O_Movie'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_O/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_Ponds_WT_O_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.LakePond['Pond_WT_Y_Figures'].lower() == 'yes' and self.LakePond['Pond_WT_Y_Movie'].lower() == 'yes' and \
      self.LakePond['Pond_WT_M_Figures'].lower() == 'yes' and self.LakePond['Pond_WT_M_Movie'].lower() == 'yes' and \
      self.LakePond['Pond_WT_O_Figures'].lower() == 'yes' and self.LakePond['Pond_WT_O_Movie'].lower() == 'yes':
      # Move to output directory
      os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_Total/Year_Cohorts')
      # Write AVI File
      subprocess.call('./avi_script_Ponds_WT_Total_Fraction', shell = True)
      # Move to Run Directory
      os.chdir(self.control['Run_dir'])      

    # ----------------------------
    # Large Lakes
    # ----------------------------
    if self.LakePond['LargeLake_WT_Y_Figures'].lower() == 'yes' and self.LakePond['LargeLake_WT_Y_Movie'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_Y/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_LargeLakes_WT_Y_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.LakePond['LargeLake_WT_M_Figures'].lower() == 'yes' and self.LakePond['LargeLake_WT_M_Movie'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_M/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_LargeLakes_WT_M_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.LakePond['LargeLake_WT_O_Figures'].lower() == 'yes' and self.LakePond['LargeLake_WT_O_Movie'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_O/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_LargeLakes_WT_O_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.LakePond['LargeLake_WT_Y_Figures'].lower() == 'yes' and self.LakePond['LargeLake_WT_Y_Movie'].lower() == 'yes' and \
      self.LakePond['LargeLake_WT_M_Figures'].lower() == 'yes' and self.LakePond['LargeLake_WT_M_Movie'].lower() == 'yes' and \
      self.LakePond['LargeLake_WT_O_Figures'].lower() == 'yes' and self.LakePond['LargeLake_WT_O_Movie'].lower() == 'yes':
      # Move to output directory
      os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_Total/Year_Cohorts')
      # Write AVI File
      subprocess.call('./avi_script_LargeLakes_WT_Total_Fraction', shell = True)
      # Move to Run Directory
      os.chdir(self.control['Run_dir'])    

    # ----------------------------
    # Small Lakes
    # ----------------------------
    if self.LakePond['SmallLake_WT_Y_Figures'].lower() == 'yes' and self.LakePond['SmallLake_WT_Y_Movie'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_Y/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_SmallLakes_WT_Y_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.LakePond['SmallLake_WT_M_Figures'].lower() == 'yes' and self.LakePond['SmallLake_WT_M_Movie'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_M/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_SmallLakes_WT_M_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.LakePond['SmallLake_WT_O_Figures'].lower() == 'yes' and self.LakePond['SmallLake_WT_O_Movie'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_O/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_SmallLakes_WT_O_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.LakePond['SmallLake_WT_Y_Figures'].lower() == 'yes' and self.LakePond['SmallLake_WT_Y_Movie'].lower() == 'yes' and \
      self.LakePond['SmallLake_WT_M_Figures'].lower() == 'yes' and self.LakePond['SmallLake_WT_M_Movie'].lower() == 'yes' and \
      self.LakePond['SmallLake_WT_O_Figures'].lower() == 'yes' and self.LakePond['SmallLake_WT_O_Movie'].lower() == 'yes':
      # Move to output directory
      os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_Total/Year_Cohorts')
      # Write AVI File
      subprocess.call('./avi_script_SmallLakes_WT_Total_Fraction', shell = True)
      # Move to Run Directory
      os.chdir(self.control['Run_dir'])

    # ----------------------------
    # Medium Lakes
    # ----------------------------
    if self.LakePond['MediumLake_WT_Y_Figures'].lower() == 'yes' and self.LakePond['MediumLake_WT_Y_Movie'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_Y/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_MediumLakes_WT_Y_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.LakePond['MediumLake_WT_M_Figures'].lower() == 'yes' and self.LakePond['MediumLake_WT_M_Movie'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_M/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_MediumLakes_WT_M_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.LakePond['MediumLake_WT_O_Figures'].lower() == 'yes' and self.LakePond['MediumLake_WT_O_Movie'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_O/Year_Cohorts')
        # Write AVI File
        subprocess.call('./avi_script_MediumLakes_WT_O_Fraction', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
    if self.LakePond['MediumLake_WT_Y_Figures'].lower() == 'yes' and self.LakePond['MediumLake_WT_Y_Movie'].lower() == 'yes' and \
      self.LakePond['MediumLake_WT_M_Figures'].lower() == 'yes' and self.LakePond['MediumLake_WT_M_Movie'].lower() == 'yes' and \
      self.LakePond['MediumLake_WT_O_Figures'].lower() == 'yes' and self.LakePond['MediumLake_WT_O_Movie'].lower() == 'yes':
      # Move to output directory
      os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_Total/Year_Cohorts')
      # Write AVI File
      subprocess.call('./avi_script_MediumLakes_WT_Total_Fraction', shell = True)
      # Move to Run Directory
      os.chdir(self.control['Run_dir'])

    # -------------------------------------------------
    # All Lakes (Small, Medium, Large) Lakes Combined
    # -------------------------------------------------
    if self.LakePond['MediumLake_WT_Y_Figures'].lower() == 'yes' and self.LakePond['MediumLake_WT_Y_Movie'].lower() == 'yes' and \
      self.LakePond['MediumLake_WT_M_Figures'].lower() == 'yes' and self.LakePond['MediumLake_WT_M_Movie'].lower() == 'yes' and \
      self.LakePond['MediumLake_WT_O_Figures'].lower() == 'yes' and self.LakePond['MediumLake_WT_O_Movie'].lower() == 'yes' and \
      self.LakePond['SmallLake_WT_Y_Figures'].lower() == 'yes' and self.LakePond['SmallLake_WT_Y_Movie'].lower() == 'yes' and \
      self.LakePond['SmallLake_WT_M_Figures'].lower() == 'yes' and self.LakePond['SmallLake_WT_M_Movie'].lower() == 'yes' and \
      self.LakePond['SmallLake_WT_O_Figures'].lower() == 'yes' and self.LakePond['SmallLake_WT_O_Movie'].lower() == 'yes' and \
      self.LakePond['LargeLake_WT_Y_Figures'].lower() == 'yes' and self.LakePond['LargeLake_WT_Y_Movie'].lower() == 'yes' and \
      self.LakePond['LargeLake_WT_M_Figures'].lower() == 'yes' and self.LakePond['LargeLake_WT_M_Movie'].lower() == 'yes' and \
      self.LakePond['LargeLake_WT_O_Figures'].lower() == 'yes' and self.LakePond['LargeLake_WT_O_Movie'].lower() == 'yes' :
      # Move to output directory
      os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Lakes_WT/Year_Cohorts')
      # Write AVI File
      subprocess.call('./avi_script_Lakes_WT_Fraction', shell = True)
      # Move to Run Directory
      os.chdir(self.control['Run_dir'])

#    # -------------------------------------------------
#    # Coastal Waters, Wetland Tundra
#    # -------------------------------------------------
#    if self.CoastalWaters_WT_O['CoastalWaters_WT_O_Figures'].lower() == 'yes' and \
#      self.CoastalWaters_WT_O['SmallLake_WT_O_Movie'].lower() == 'yes':
#      # Move to output directory
#      os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CoastalWaters_WT_O/Year_Cohorts')
#      # Write AVI File
#      subprocess.call('./avi_script_CoastalWaters_WT_O_Fraction', shell = True)
#      # Move to Run Directory
#      os.chdir(self.control['Run_dir'])

#    # -------------------------------------------------
#    # Drained Slopes, Wetland Tundra
#    # -------------------------------------------------
#    if self.DrainedSlope_WT_Y['Movie'].lower() == 'yes' and self.DrainedSlope_WT_Y['Figures'].lower() == 'yes':
#        # Move to output directory
#        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/DrainedSlope_WT_Y/Year_Cohorts')
#        # Write AVI File
#        subprocess.call('./avi_script_DrainedSlope_WT_Y_Fraction', shell = True)
#        # Move to Run Directory
#        os.chdir(self.control['Run_dir'])
#    if self.DrainedSlope_WT_M['Movie'].lower() == 'yes' and self.DrainedSlope_WT_M['Figures'].lower() == 'yes':
#        # Move to output directory
#        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/DrainedSlope_WT_M/Year_Cohorts')
#        # Write AVI File
#        subprocess.call('./avi_script_DrainedSlope_WT_M_Fraction', shell = True)
#        # Move to Run Directory
#        os.chdir(self.control['Run_dir'])        
#    if self.DrainedSlope_WT_O['Movie'].lower() == 'yes' and self.DrainedSlope_WT_O['Figures'].lower() == 'yes':
#        # Move to output directory
#        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/DrainedSlope_WT_O/Year_Cohorts')
#        # Write AVI File
#        subprocess.call('./avi_script_DrainedSlope_WT_O_Fraction', shell = True)
#        # Move to Run Directory
#        os.chdir(self.control['Run_dir'])
#    if self.DrainedSlope_WT_Y['Movie'].lower() == 'yes' and self.DrainedSlope_WT_Y['Figures'].lower() == 'yes' and \
#      self.DrainedSlope_WT_M['Movie'].lower() == 'yes' and self.DrainedSlope_WT_M['Figures'].lower() == 'yes' and \
#      self.DrainedSlope_WT_O['Movie'].lower() == 'yes' and self.DrainedSlope_WT_O['Figures'].lower() == 'yes' :
#        # Move to output directory
#        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/DrainedSlope_WT_Total/Year_Cohorts')
#        # Write AVI File
#        subprocess.call('./avi_script_DrainedSlope_WT_Total_Fraction', shell = True)
#        # Move to Run Directory
#        os.chdir(self.control['Run_dir'])    
    
#---------------------------------------------------------------------------------
def dominant_fractional_plot(self, time):
    if self.Terrestrial['Figure'].lower() == 'yes':

        # Change to Output Directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/All_Cohorts/Year_Cohorts')

        dominant_cohort_plot = np.reshape(self.dominant_cohort, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()

        cax = pl.imshow(dominant_cohort_plot, interpolation = 'nearest', cmap = 'seismic', vmin = 0, vmax = 15)
        
        pl.title('Dominant Cohort - '+str(year))

        cbar = pl.colorbar(ticks = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], orientation = 'vertical')
        #cbar.set_ticklabels(['', 'Urban', 'Rivers', 'Wetland NPG', 'Wetland CLC',
        #                     'Wetland CLC','Wetland FCP', 'Wetland HCP',
        #                     'Ponds', 'Lakes'])

        #cbar.set_ticklabels(['', 'Urban', 'River', 'Lake', 'Pond', 'Wetland HCP',
        #                     'Wetland FCP', 'Wetland CLC', 'Wetland LCP', 'Meadow'])
        
        cbar.set_ticklabels(['', 'Urban', 'Coastal Waters', 'Sand Dunes', 'Sat. Barrens', 'Shrubs',
        	                 'Drained Slopes' , 'Rivers', 'Ponds', 'Lakes', 'HC Polygons', 
        	                 'FC Polygons', 'CLC Polygons', 'LC Polygons',
        	                 'Meadows'])

        pl.savefig('Dominant_Cohort'+str(year)+'.jpg', format = 'jpg')
        dominant_cohort_plot.tofile('Dominant_Cohort'+str(year)+'.bin')
        pl.close()
        # Return to Run Directory
        os.chdir(self.control['Run_dir'])
        
#---------------------------------------------------------------------------------
def dominant_cohort(self):

    if self.Terrestrial['Figure'].lower() == 'yes':
        self.dominant_cohort = np.zeros([self.ATTM_nrows * self.ATTM_ncols])

        ## # Urban [0], Rivers [1], Wet_NPG [2], Wet_LCP [3], Wet_CLC [4], Wet_FCP [5], Wet_HCP [6],
        ## # Ponds [7], Lakes [8]

        # Urban [0], Rivers [1], Lakes [2], Ponds [3], Wet_HCP [4], Wet_FCP [5], Wet_CLC [6],
        # Wet_LCP [7], Wet_NPG [8]


        # Urban [0], Coastal Waters [1], Sand Dunes [2], Saturated Barrens [3], Shrubs [4],
        # Drained Slopes [5], Rivers [6], Ponds [7], Lakes [8], HCP [9], FCP [10], CLC [11],
        # LCP [12], Meadows [13]

        cohort_compare = np.zeros(14)

        Urban = self.ATTM_Urban_WT
        Coastal = self.ATTM_CoastalWaters_WT_O
        Sand = self.ATTM_SandDunes_WT_Y + self.ATTM_SandDunes_WT_M + self.ATTM_SandDunes_WT_O
        Barrens = self.ATTM_SaturatedBarrens_WT_Y + self.ATTM_SaturatedBarrens_WT_M + self.ATTM_SaturatedBarrens_WT_O
        Shrubs = self.ATTM_Shrubs_WT_O
        Slopes = self.ATTM_DrainedSlope_WT_Y + self.ATTM_DrainedSlope_WT_M + self.ATTM_DrainedSlope_WT_O
        Rivers = self.ATTM_Rivers_WT_Y + self.ATTM_Rivers_WT_M + self.ATTM_Rivers_WT_O
        Ponds = self.ATTM_Ponds_WT_Y + self.ATTM_Ponds_WT_M + self.ATTM_Rivers_WT_O
        Lakes = self.ATTM_LargeLakes_WT_Y + self.ATTM_LargeLakes_WT_M + self.ATTM_LargeLakes_WT_O + \
        		self.ATTM_MediumLakes_WT_Y + self.ATTM_MediumLakes_WT_M + self.ATTM_MediumLakes_WT_O + \
        		self.ATTM_SmallLakes_WT_Y + self.ATTM_SmallLakes_WT_M + self.ATTM_SmallLakes_WT_O
        HCP = self.ATTM_HCP_WT_Y + self.ATTM_HCP_WT_M + self.ATTM_HCP_WT_O
        FCP = self.ATTM_FCP_WT_Y + self.ATTM_FCP_WT_M + self.ATTM_FCP_WT_O
        CLC = self.ATTM_CLC_WT_Y + self.ATTM_CLC_WT_M + self.ATTM_CLC_WT_O
        LCP = self.ATTM_LargeLakes_WT_Y + self.ATTM_LargeLakes_WT_M + self.ATTM_LCP_WT_O
        NPG = self.ATTM_Meadow_WT_Y + self.ATTM_Meadow_WT_M + self.ATTM_Meadow_WT_O


        for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
            if np.sum(Urban[i] + Coastal[i] + Sand[i] + Barrens[i] + Shrubs[i] +
                          Slopes[i] + Rivers[i] + Ponds[i] + Lakes[i] + HCP[i] +
                          FCP[i] + CLC[i] + LCP[i] + NPG[i]) > 0.0:
                cohort_compare[0] = Urban[i]
                cohort_compare[1] = Coastal[i]
                cohort_compare[2] = Sand[i]
                cohort_compare[3] = Barrens[i]
                cohort_compare[4] = Shrubs[i]
                cohort_compare[5] = Slopes[i]
                cohort_compare[6] = Rivers[i]
                cohort_compare[7] = Ponds[i]
                cohort_compare[8] = Lakes[i]
                cohort_compare[9] = HCP[i]
                cohort_compare[10] = FCP[i]
                cohort_compare[11] = CLC[i]
                cohort_compare[12] = LCP[i]
                cohort_compare[13] = NPG[i]

                cohort_max = np.where(cohort_compare == cohort_compare.max())

                if cohort_max[0][0] == 0: self.dominant_cohort[i] = 1.
                if cohort_max[0][0] == 1: self.dominant_cohort[i] = 2.
                if cohort_max[0][0] == 2: self.dominant_cohort[i] = 3.
                if cohort_max[0][0] == 3: self.dominant_cohort[i] = 4.
                if cohort_max[0][0] == 4: self.dominant_cohort[i] = 5.
                if cohort_max[0][0] == 5: self.dominant_cohort[i] = 6.
                if cohort_max[0][0] == 6: self.dominant_cohort[i] = 7.
                if cohort_max[0][0] == 7: self.dominant_cohort[i] = 8.
                if cohort_max[0][0] == 8: self.dominant_cohort[i] = 9.
                if cohort_max[0][0] == 9: self.dominant_cohort[i] = 10.
                if cohort_max[0][0] == 10: self.dominant_cohort[i] = 11.
                if cohort_max[0][0] == 11: self.dominant_cohort[i] = 12.
                if cohort_max[0][0] == 12: self.dominant_cohort[i] = 13.
                if cohort_max[0][0] == 13: self.dominant_cohort[i] = 14.
                
                
#            if np.sum(self.ATTM_Urban[i] + self.ATTM_Rivers[i] + self.ATTM_Wet_NPG[i] +
#                      self.ATTM_Wet_LCP[i] + self.ATTM_Wet_CLC[i] + self.ATTM_Wet_FCP[i] +
#                      self.ATTM_Wet_HCP[i] + self.ATTM_Lakes[i] + self.ATTM_Ponds[i]) > 0.0 :

    
#########################################
# Animation of Dominant Fractional Area #
#########################################

def write_Dominant_Cohort_avi(self):

    if self.Terrestrial['Movie'].lower() == 'yes' and self.Terrestrial['Figure'].lower() == 'yes':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/All_Cohorts/Year_Cohorts')
        # Write AVI file
        subprocess.call('./avi_script_Dominant_Cohort', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
