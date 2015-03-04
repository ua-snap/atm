def read_archive(self):
    """
    The purpose of this module is to open and read the files &
    directories that will be archived after each simulation.

    This will allow some control over what files & the size of
    each archive that will take place. Ex. archive only the
    directory that you are looking for results/testing.
    """
    print '    Reading the archive control file: ', self.archive_data
    self.archive = {}
    with open(self.archive_data, 'r') as f:
        for line in f:
            (key, val) = line.split()
            self.archive[(key)] = val


def archive(self):

    import tarfile
    import os
    
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
        os.system('rm *.txt')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #==================================
    # Add the Initialization Directory
    #----------------------------------
    if self.archive['Initialization'].lower() == 'yes':
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
        os.system('rm *.bin')
        os.system('rm *.png')
        os.system('rm *.csv')
        os.chdir('./Degree_Days')
        os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

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
        os.system('rm *.bin')
        os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        os.system('rm *.bin')
        os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #===============================
    # Add the Lakes directory
    #-------------------------------
    if self.archive['Lakes'].lower() == 'yes':
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
        os.system('rm *.bin')
        os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        os.system('rm *.bin')
        os.system('rm *.jpg')
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
        os.system('rm *.bin')
        os.system('rm *.png')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

         
    #===============================
    # Add the Ponds directory
    #-------------------------------
    if self.archive['Ponds'].lower() == 'yes':
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
        os.system('rm *.bin')
        os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        os.system('rm *.bin')
        os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #==========================================================
    # Add the Wetlands Coalescent Low Center Polygons directory
    #----------------------------------------------------------
    if self.archive['Wetlands_CLC'].lower() == 'yes':
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
        os.system('rm *.bin')
        os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        os.system('rm *.bin')
        os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #=================================================
    # Add the Wetlands Low Center Polygons directory
    #-------------------------------------------------
    if self.archive['Wetlands_LCP'].lower() == 'yes':
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
        os.system('rm *.bin')
        os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        os.system('rm *.bin')
        os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #=================================================
    # Add the Wetlands Flat Center Polygons directory
    #-------------------------------------------------
    if self.archive['Wetlands_FCP'].lower() == 'yes':
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
        os.system('rm *.bin')
        os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        os.system('rm *.bin')
        os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #=================================================
    # Add the Wetlands High Center Polygons directory
    #-------------------------------------------------
    if self.archive['Wetlands_HCP'].lower() == 'yes':
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
        os.system('rm *.bin')
        os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        os.system('rm *.bin')
        os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #=================================================
    # Add the Wetlands Non-Polygonal Ground directory
    #-------------------------------------------------
    if self.archive['Wetlands_NPG'].lower() == 'yes':
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
        os.system('rm *.bin')
        os.system('rm *.png')
        os.chdir('./Year_Cohorts/')
        #os.system('rm *.avi')
        os.system('rm *.bin')
        os.system('rm *.jpg')
        # Return to the run directory
        os.chdir(self.control['Run_dir'])

    #--------------------
    # Close the tarfile
    #--------------------
    self.archive_file.close()
