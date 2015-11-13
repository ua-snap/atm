def read_archive(self):
    """
    The purpose of this module is to open and read the files &
    directories that will be archived after each simulation.

    This will allow some control over what files & the size of
    each archive that will take place. Ex. archive only the
    directory that you are looking for results/testing.
    """
    print '------------------------------------'
    print ' Archiving the simulation results'
    print ' '
    self.archive = {}
    with open(self.archive_data, 'r') as f:
        for line in f:
            (key, val) = line.split()
            self.archive[(key)] = val


def archive(self):

    import tarfile
    import os, glob, sys
    
    """
    The purpose of this module is to archive the simulation into a compressed
    tarball and placed into a directory for storage. Archived files will include
    all plots, binary results, simulation results and notes.

    Following the archiving process, the output (either figures or binary files)
    will be deleted in order to have clean directories for the next simulation.
    """

    #==========================
    # Add the results summary
    #-------------------------
    if self.archive['Simulation_Summary'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory+str('/Archive/'))
        self.archive_file.add(self.archive_time+str('_')+self.simulation_name+str('.txt'))
        # Clean the results summary
        text_files = glob.glob('*.txt')
        if len(text_files) > 0:
            os.system('rm *.txt')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #=================================
    # Add All Control Files
    #=================================
    # Model Control
    self.archive_file.add(sys.argv[1])

    #==================================
    # Add the Initialization Directory
    #----------------------------------
    if self.archive['Initialization'].lower() == 'yes':
        if self.Simulation_area.lower() == 'barrow':
            os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/')
        elif self.Simulation_area.lower() == 'tanana':
            os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/')
        self.archive_file.add(self.control['Initialize_Control'])
        os.chdir(self.control['Run_dir']+self.Output_directory)
        # Determine if Figures are to be included in the archive
        if self.archive['Figures'].lower() == 'yes':
            self.archive_file.add('Initialization')
        else:
            def exclude_figures(filename):
                return filename.endswith(('jpg','png','avi'))
            self.archive_file.add('Initialization',exclude=exclude_figures) 
        # Clean the initialization directory of files
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Initialization/')
        bin_files = glob.glob('*.bin')
        png_files = glob.glob('*.png')
        csv_files = glob.glob('*.csv')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        if len(png_files) > 0:
            os.system('rm *.png')
        #if len(csv_files) > 0:
        #    os.system('rm *.csv')
        # Change to Degree Days directory
        os.chdir('./Degree_Days')
        jpg_files = glob.glob('*.jpg')
        #if len(jpg_files) > 0:
        #    os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #==================================
    # Add the Met Control file
    #----------------------------------
    if self.archive['Met'].lower() == 'yes':
        self.archive_file.add(self.control['Met_Control'])

    #===============================
    # Add the All_Cohorts directory
    #-------------------------------
    if self.archive['All_Cohorts'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory)
        # Determine if Figures are to be included in the archive
        if self.archive['Figures'].lower() == 'yes':
            self.archive_file.add('All_Cohorts')
        else:
            def exclude_figures(filename):
                return filename.endswith(('jpg','png','avi'))
            self.archive_file.add('All_Cohorts',exclude=exclude_figures) 
        # Clean the All_Cohorts directory of files
        os.chdir(self.control['Run_dir']+self.Output_directory+'/All_Cohorts/')
        bin_files = glob.glob('*.bin')
        png_files = glob.glob('*.png')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        if len(png_files) > 0:
            os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        bin_files = glob.glob('*.bin')
        jpg_files = glob.glob('*.jpg')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(jpg_files) > 0:
        #    os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #===============================
    # Add the Lakes directory
    #-------------------------------
    if self.archive['Lakes'].lower() == 'yes':
        self.archive_file.add(self.control['Lake_Pond_Control'])
        os.chdir(self.control['Run_dir']+self.Output_directory)
        # Determine if Figures are to be included in the archive
        if self.archive['Figures'].lower() == 'yes':
            self.archive_file.add('Lakes')
        else:
            def exclude_figures(filename):
                return filename.endswith(('jpg','png','avi'))
            self.archive_file.add('Lakes',exclude=exclude_figures) 
        # Clean the Lakes directory of files
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Lakes/')
        bin_files = glob.glob('*.bin')
        png_files = glob.glob('*.png')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        if len(png_files) > 0:
            os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        bin_files = glob.glob('*.bin')
        jpg_files = glob.glob('*.jpg')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(jpg_files) > 0:
        #    os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #===============================
    # Add the Other_Cohorts directory
    #-------------------------------
    if self.archive['Other_Cohorts'].lower() == 'yes':
        os.chdir(self.control['Run_dir']+self.Output_directory)
        # Determine if Figures are to be included in the archive
        if self.archive['Figures'].lower() == 'yes':
            self.archive_file.add('Other_Cohorts')
        else:
            def exclude_figures(filename):
                return filename.endswith(('jpg','png','avi'))
            self.archive_file.add('Other_Cohorts',exclude=exclude_figures) 
        # Clean the All_Cohorts directory of files
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Other_Cohorts/')
        bin_files = glob.glob('*.bin')
        png_files = glob.glob('*.png')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(png_files) > 0:
        #    os.system('rm *.png')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #===============================
    # Add the Ponds directory
    #-------------------------------
    if self.archive['Ponds'].lower() == 'yes':
        self.archive_file.add(self.control['Lake_Pond_Control'])
        os.chdir(self.control['Run_dir']+self.Output_directory)
        # Determine if Figures are to be included in the archive
        if self.archive['Figures'].lower() == 'yes':
            self.archive_file.add('Ponds')
        else:
            def exclude_figures(filename):
                return filename.endswith(('jpg','png','avi'))
            self.archive_file.add('Ponds',exclude=exclude_figures) 
        # Clean the Lakes directory of files
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Ponds/')
        bin_files = glob.glob('*.bin')
        png_files = glob.glob('*.png')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(png_files) > 0:
        #    os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        bin_files = glob.glob('*.bin')
        jpg_files = glob.glob('*.jpg')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(jpg_files) > 0:
        #    os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #==========================================================
    # Add the Wetlands Coalescent Low Center Polygons directory
    #----------------------------------------------------------
    if self.archive['Wetlands_CLC'].lower() == 'yes':
        self.archive_file.add(self.control['Wet_CLC_Control'])
        os.chdir(self.control['Run_dir']+self.Output_directory)
        # Determine if Figures are to be included in the archive
        if self.archive['Figures'].lower() == 'yes':
            self.archive_file.add('Wet_CLC')
        else:
            def exclude_figures(filename):
                return filename.endswith(('jpg','png','avi'))
            self.archive_file.add('Wet_CLC',exclude=exclude_figures) 
        # Clean the Lakes directory of files
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_CLC/')
        bin_files = glob.glob('*.bin')
        png_files = glob.glob('*.png')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(png_files) > 0:
        #    os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        bin_files = glob.glob('*.bin')
        jpg_files = glob.glob('*.jpg')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(jpg_files) > 0:
        #    os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #=================================================
    # Add the Wetlands Low Center Polygons directory
    #-------------------------------------------------
    if self.archive['Wetlands_LCP'].lower() == 'yes':
        self.archive_file.add(self.control['Wet_LCP_Control'])
        os.chdir(self.control['Run_dir']+self.Output_directory)
        # Determine if Figures are to be included in the archive
        if self.archive['Figures'].lower() == 'yes':
            self.archive_file.add('Wet_LCP')
        else:
            def exclude_figures(filename):
                return filename.endswith(('jpg','png','avi'))
            self.archive_file.add('Wet_LCP',exclude=exclude_figures) 
        # Clean the Lakes directory of files
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_LCP/')
        bin_files = glob.glob('*.bin')
        png_files = glob.glob('*.png')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(png_files) > 0:
        #    os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        bin_files = glob.glob('*.bin')
        jpg_files = glob.glob('*.jpg')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(jpg_files) > 0:
        #    os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #=================================================
    # Add the Wetlands Flat Center Polygons directory
    #-------------------------------------------------
    if self.archive['Wetlands_FCP'].lower() == 'yes':
        self.archive_file.add(self.control['Wet_FCP_Control'])
        os.chdir(self.control['Run_dir']+self.Output_directory)
        # Determine if Figures are to be included in the archive
        if self.archive['Figures'].lower() == 'yes':
            self.archive_file.add('Wet_FCP')
        else:
            def exclude_figures(filename):
                return filename.endswith(('jpg','png','avi'))
            self.archive_file.add('Wet_FCP',exclude=exclude_figures) 
        # Clean the Lakes directory of files
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_FCP/')
        bin_files = glob.glob('*.bin')
        png_files = glob.glob('*.png')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(png_files) > 0:
        #    os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        bin_files = glob.glob('*.bin')
        jpg_files = glob.glob('*.jpg')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(jpg_files) > 0:
        #    os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #=================================================
    # Add the Wetlands High Center Polygons directory
    #-------------------------------------------------
    if self.archive['Wetlands_HCP'].lower() == 'yes':
        self.archive_file.add(self.control['Wet_HCP_Control'])
        os.chdir(self.control['Run_dir']+self.Output_directory)
        # Determine if Figures are to be included in the archive
        if self.archive['Figures'].lower() == 'yes':
            self.archive_file.add('Wet_HCP')
        else:
            def exclude_figures(filename):
                return filename.endswith(('jpg','png','avi'))
            self.archive_file.add('Wet_HCP',exclude=exclude_figures) 
        # Clean the Lakes directory of files
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_HCP/')
        bin_files = glob.glob('*.bin')
        png_files = glob.glob('*.png')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(png_files) > 0:
        #    os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        bin_files = glob.glob('*.bin')
        jpg_files = glob.glob('*.jpg')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(jpg_files) > 0:
        #    os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #=================================================
    # Add the Wetlands Non-Polygonal Ground directory
    #-------------------------------------------------
    if self.archive['Wetlands_NPG'].lower() == 'yes':
        self.archive_file.add(self.control['Wet_NPG_Control'])
        os.chdir(self.control['Run_dir']+self.Output_directory)
        # Determine if Figures are to be included in the archive
        if self.archive['Figures'].lower() == 'yes':
            self.archive_file.add('Wet_NPG')
        else:
            def exclude_figures(filename):
                return filename.endswith(('jpg','png','avi'))
            self.archive_file.add('Wet_NPG',exclude=exclude_figures) 
        # Clean the Lakes directory of files
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Wet_NPG/')
        bin_files = glob.glob('*.bin')
        png_files = glob.glob('*.png')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(png_files) > 0:
        #    os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        bin_files = glob.glob('*.bin')
        jpg_files = glob.glob('*.jpg')
        #if len(bin_files) > 0:
        #    os.system('rm *.bin')
        #if len(jpg_files) > 0:
            #os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #--------------------
    # Close the tarfile
    #--------------------
    self.archive_file.close()
