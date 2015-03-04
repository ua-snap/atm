import numpy as np
import gdal, os, sys, glob, random
import pylab as pl
import matplotlib.animation as animation
import subprocess

def Output_cohorts_by_year(self, time, Wet_NPG, Wet_LCP, Wet_CLC, Wet_FCP,
                           Wet_HCP, Gra_NPG, Gra_LCP, Gra_FCP, Gra_HCP,
                           Shr_NPG, Shr_LCP, Shr_FCP, Shr_HCP, Ponds,
                           Lakes):

    #=======================================
    # OUTPUT FIGURES
    #----------------------------------------
    # Wetland Non-Polygonal Ground (meadow)
    # ---------------------------------------
    if Wet_NPG == 'TRUE':
        # Change to Output Directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_NPG/Year_Cohorts')

        Wet_NPG_plot = np.reshape(self.ATTM_Wet_NPG, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Wet_NPG_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Non-Polygonal Ground Fractional Area - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Wet_NPG_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Wet_NPG_plot.tofile('Wet_NPG_Fractional_Area_'+str(year)+'.bin')
        pl.close()
    # ---------------------------------------
    # Wetland Low Center Polygons
    # ---------------------------------------
    if Wet_LCP == 'TRUE':
        # Change to Output Directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_LCP/Year_Cohorts')

        Wet_LCP_plot = np.reshape(self.ATTM_Wet_LCP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Wet_LCP_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Low Center Polygons Fractional Area - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Wet_LCP_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Wet_LCP_plot.tofile('Wet_LCP_Fractional_Area_'+str(year)+'.bin')
        pl.close()
    # ---------------------------------------
    # Wetland Coalescent Low Center Polygons
    # ---------------------------------------
    if Wet_CLC == 'TRUE':
        # Change to Output Directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_CLC/Year_Cohorts')

        Wet_CLC_plot = np.reshape(self.ATTM_Wet_CLC, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Wet_CLC_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Coalescent Low Center Polygons Fractional Area - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Wet_CLC_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Wet_CLC_plot.tofile('Wet_CLC_Fractional_Area_'+str(year)+'.bin')
        pl.close()
    # ---------------------------------------
    # Wetland Flat Center Polygons
    # ---------------------------------------
    if Wet_FCP == 'TRUE':
        # Change to Output Directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_FCP/Year_Cohorts')

        Wet_FCP_plot = np.reshape(self.ATTM_Wet_FCP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Wet_FCP_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland Flat Center Polygons Fractional Area - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Wet_FCP_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Wet_FCP_plot.tofile('Wet_FCP_Fractional_Area_'+str(year)+'.bin')
        pl.close()
    # ---------------------------------------
    # Wetland High Center Polygons
    # ---------------------------------------
    if Wet_HCP == 'TRUE':
        # Change to Output Directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_HCP/Year_Cohorts')

        Wet_HCP_plot = np.reshape(self.ATTM_Wet_HCP, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Wet_HCP_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Wetland High Center Polygons Fractional Area - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Wet_HCP_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Wet_HCP_plot.tofile('Wet_HCP_Fractional_Area_'+str(year)+'.bin')
        pl.close()
    # ---------------------------------------
    # Ponds
    # ---------------------------------------
    if Ponds == 'TRUE':
        # Change to Output Directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Ponds/Year_Cohorts')

        Ponds_plot = np.reshape(self.ATTM_Ponds, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Ponds_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Ponds Fractional Area - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Ponds_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Ponds_plot.tofile('Ponds_Fractional_Area_'+str(year)+'.bin')
        pl.close()
    # ---------------------------------------
    # Lakes
    # ---------------------------------------
    if Lakes == 'TRUE':
        # Change to Output Directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Lakes/Year_Cohorts')

        Lakes_plot = np.reshape(self.ATTM_Lakes, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()
        pl.imshow(Lakes_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0.0, vmax = 1.0)
        pl.title('Lakes Fractional Area - '+str(year))
        pl.colorbar(extend = 'neither', shrink = 0.92)
        pl.savefig('Lakes_Fractional_Area_'+str(year)+'.jpg', format = 'jpg')
        Lakes_plot.tofile('Lakes_Fractional_Area_'+str(year)+'.bin')     
        pl.close()
################################
# Animation of Fractional Area #
################################
def write_Fractions_avi(self, Wet_NPG, Wet_LCP, Wet_CLC, Wet_FCP, Wet_HCP, Gra_NPG, Gra_LCP, Gra_FCP,
                        Gra_HCP, Shr_NPG, Shr_LCP, Shr_FCP, Shr_HCP, Ponds, Lakes):
    # -----------------------------
    # Wetland Non-Polygonal Ground
    # -----------------------------
    if Wet_NPG == 'TRUE':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_NPG/Year_Cohorts')
        # Write AVI file
        subprocess.call('./avi_script_Wet_NPG_Fraction', shell = True)
        # Move to Run directory
        os.chdir(self.control['Run_dir'])
    # ---------------------------
    # Wetland Low Center Polygon
    # ---------------------------
    if Wet_LCP == 'TRUE':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_LCP/Year_Cohorts')
        # Write AVI file
        subprocess.call('./avi_script_Wet_LCP_Fraction', shell = True)
        # Move to Run directory
        os.chdir(self.control['Run_dir'])
    # --------------------------------------
    # Wetland Coalescent Low Center Polygon
    # --------------------------------------
    if Wet_CLC == 'TRUE':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_CLC/Year_Cohorts')
        # Write AVI file
        subprocess.call('./avi_script_Wet_CLC_Fraction', shell = True)
        # Move to Run directory
        os.chdir(self.control['Run_dir'])
    # -----------------------------
    # Wetland Flat Center Polygon
    # -----------------------------
    if Wet_FCP == 'TRUE':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_FCP/Year_Cohorts')
        # Write AVI file
        subprocess.call('./avi_script_Wet_FCP_Fraction', shell = True)
        # Move to Run directory
        os.chdir(self.control['Run_dir'])
    # ----------------------------
    # Wetland High Center Polygon
    # ----------------------------
    if Wet_HCP == 'TRUE':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_HCP/Year_Cohorts')
        # Write AVI file
        subprocess.call('./avi_script_Wet_HCP_Fraction', shell = True)
        # Move to Run directory
        os.chdir(self.control['Run_dir'])
    # -----------------------------
    # Ponds
    # -----------------------------
    if Ponds == 'TRUE':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Ponds/Year_Cohorts')
        # Write AVI file
        subprocess.call('./avi_script_Ponds_Fraction', shell = True)
        # Move to Run directory
        os.chdir(self.control['Run_dir'])
    # ----------------------------
    # Rivers
    # ----------------------------
    if Lakes == 'TRUE':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Lakes/Year_Cohorts')
        # Write AVI file
        subprocess.call('./avi_script_Lakes_Fraction', shell = True)
        # Move to Run directory
        os.chdir(self.control['Run_dir'])


    
#---------------------------------------------------------------------------------
def dominant_fractional_plot(self, time, FIGURE):

    if FIGURE == 'TRUE' :
        # Change to Output Directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/All_Cohorts/Year_Cohorts')

        dominant_cohort_plot = np.reshape(self.dominant_cohort, [int(self.ATTM_nrows), int(self.ATTM_ncols)])

        # --------------------------------------
        # Output figures placed into directory
        # --------------------------------------
        year = str(int(time + self.Year[0]))
        # ---------------------------------------
        # Create figures and corresponding data
        #----------------------------------------
        fig = pl.figure()

        cax = pl.imshow(dominant_cohort_plot, interpolation = 'nearest', cmap = 'spectral', vmin = 0, vmax = 9)
        pl.title('Dominant Cohort - '+str(year))

        cbar = pl.colorbar(ticks = [0,1,2,3,4,5,6,7,8,9], orientation = 'vertical')
        #cbar.set_ticklabels(['', 'Urban', 'Rivers', 'Wetland NPG', 'Wetland LCP',
        #                     'Wetland CLC','Wetland FCP', 'Wetland HCP',
        #                     'Ponds', 'Lakes'])

        cbar.set_ticklabels(['', 'Urban', 'River', 'Lake', 'Pond', 'Wetland HCP',
                             'Wetland FCP', 'Wetland CLC', 'Wetland LCP', 'Meadow'])
        
        pl.savefig('Dominant_Cohort'+str(year)+'.jpg', format = 'jpg')
        dominant_cohort_plot.tofile('Dominant_Cohort'+str(year)+'.bin')
        pl.close()
        # Return to Run Directory
        os.chdir(self.control['Run_dir'])
        
#---------------------------------------------------------------------------------
def dominant_cohort(self, FIGURE):

    if FIGURE == 'TRUE' :
        self.dominant_cohort = np.zeros([self.ATTM_nrows * self.ATTM_ncols])

        ## # Urban [0], Rivers [1], Wet_NPG [2], Wet_LCP [3], Wet_CLC [4], Wet_FCP [5], Wet_HCP [6],
        ## # Ponds [7], Lakes [8]

        # Urban [0], Rivers [1], Lakes [2], Ponds [3], Wet_HCP [4], Wet_FCP [5], Wet_CLC [6],
        # Wet_LCP [7], Wet_NPG [8]

        cohort_compare = np.zeros(9)

        for i in range(0, self.ATTM_nrows * self.ATTM_ncols):
            if np.sum(self.ATTM_Urban[i] + self.ATTM_Rivers[i] + self.ATTM_Wet_NPG[i] +
                      self.ATTM_Wet_LCP[i] + self.ATTM_Wet_CLC[i] + self.ATTM_Wet_FCP[i] +
                      self.ATTM_Wet_HCP[i] + self.ATTM_Lakes[i] + self.ATTM_Ponds[i]) > 0.0 :
                
                cohort_compare[0] = self.ATTM_Urban[i]
                cohort_compare[1] = self.ATTM_Rivers[i]
                cohort_compare[8] = self.ATTM_Wet_NPG[i]
                cohort_compare[7] = self.ATTM_Wet_LCP[i]
                cohort_compare[6] = self.ATTM_Wet_CLC[i]
                cohort_compare[5] = self.ATTM_Wet_FCP[i]
                cohort_compare[4] = self.ATTM_Wet_HCP[i]
                cohort_compare[3] = self.ATTM_Ponds[i]
                cohort_compare[2] = self.ATTM_Lakes[i]
            
                cohort_max = np.where(cohort_compare == cohort_compare.max())

                if cohort_max[0][0] == 0: self.dominant_cohort[i] = 1
                if cohort_max[0][0] == 1: self.dominant_cohort[i] = 2
                if cohort_max[0][0] == 2: self.dominant_cohort[i] = 3
                if cohort_max[0][0] == 3: self.dominant_cohort[i] = 4
                if cohort_max[0][0] == 4: self.dominant_cohort[i] = 5
                if cohort_max[0][0] == 5: self.dominant_cohort[i] = 6
                if cohort_max[0][0] == 6: self.dominant_cohort[i] = 7
                if cohort_max[0][0] == 7: self.dominant_cohort[i] = 8
                if cohort_max[0][0] == 8: self.dominant_cohort[i] = 9
            else:
                self.dominant_cohort[i] = 0

                
    
#########################################
# Animation of Dominant Fractional Area #
#########################################

def write_Dominant_Cohort_avi(self, MOVIE):
    if MOVIE == 'TRUE':
        # Move to output directory
        os.chdir(self.control['Run_dir']+self.Output_directory+'/All_Cohorts/Year_Cohorts')
        # Write AVI file
        subprocess.call('./avi_script_Dominant_Cohort', shell = True)
        # Move to Run Directory
        os.chdir(self.control['Run_dir'])
