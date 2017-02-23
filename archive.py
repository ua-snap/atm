import os

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
    print '----------------------------------- '

    if self.Simulation_area.lower() == 'barrow':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/')
    elif self.Simulation_area.lower() == 'tanana':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Tanana/')
    elif self.Simulation_area.lower() == 'yukon':
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Yukon/')
        
    self.archive = {}
    with open(self.archive_data, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                (key, val) = line.split()
                self.archive[(key)] = val

def archive(self):

    import tarfile
    import os, glob, sys
    from shutil import copy
    
    """
    The purpose of this module is to archive the simulation into a compressed
    tarball and placed into a directory for storage. Archived files will include
    all plots, binary results, simulation results and notes.

    Following the archiving process, the output (either figures or binary files)
    will be deleted in order to have clean directories for the next simulation.
    
    Modified: 21 Dec 2016, Bolton: Separating out sites instead of collating by process.
              18 Jan 2017, Bolton: Continuing to add archive files and directories. 
                                   Adding a computer code directory into the archive.

    """
     
    # =============================================================================
    # Simulation area -- Barrow
    # =============================================================================
    if self.Simulation_area.lower() == 'barrow':
        print ' ++++++++++++++++++++++++++++++++++++'
        print '  Archiving Barrow Peninsula results.'
        print ' ++++++++++++++++++++++++++++++++++++'
        os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Archive/')
        #---------------------------------------------
        # Create the archive tar file
        #---------------------------------------------
        self.archive_file =tarfile.open(self.control['Run_dir']+self.Output_directory+\
                                            '/Barrow/Archive/'+self.archive_time+str('_')+\
                                            self.simulation_name+".tar.gz", mode='w:gz')
        print '   tarfile created in Output/Barrow/Archive directory'

        #---------------------------------------------
        # Add Computer Code used for the simulation
        #---------------------------------------------
        if self.archive['Code'].lower() == 'yes':
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/Archive/')
            # Create a backup directory for the Code files (python only)
            os.system('mkdir Code')
            # Determine the python files in the Run Directory
            code_files = glob.glob(self.control['Run_dir']+'*.py')
            # Move code files into backup directory
            for f in code_files:
                copy(f, './Code/')
            # Archive the program files
            self.archive_file.add('Code')

            print '    Simulation Code (python files) added to the archive.'

            # Clean the Code directory
            if self.archive['clean_code'].lower() == 'yes':
                os.chdir('./Code')
                os.system('rm *.py')
                os.chdir('../')
                os.system('rmdir Code')
            
        #---------------------------------------------
        # Add results summary
        #---------------------------------------------
        if self.archive['Simulation_Summary'].lower() == 'yes':
            self.archive_file.add(self.archive_time+str('_')+self.simulation_name+str('.txt'))
            # Clean the results summary file
            text_files = glob.glob('*.txt')
            if len(text_files) > 0:
                os.system('rm *.txt')
            print '   Simulation summary added to the archive.'
        
        #---------------------------------------------
        # Add Control Files
        #---------------------------------------------
        os.chdir(self.control['Run_dir']+self.Input_directory+'/Barrow/')
        self.archive_file.add('Control_Files')
        os.chdir(self.control['Run_dir'])
        self.archive_file.add(sys.argv[1])
        print '   Control files added to the archive.'

        #---------------------------------------------
        # Add Initialization Files
        #---------------------------------------------
        if self.archive['Initialization'].lower() == 'yes':
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('Initialization')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('Initialization', exclude=exclude_figures)
            print '   Initialization files added to the archive.'

        """ Clean the initialization directory """
        if self.archive['clean_initialization'].lower() == 'yes':
            os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Initialization/')
            bin_files = glob.glob('*.bin')
            png_files = glob.glob('*.png')
            csv_files = glob.glob('*.csv')
            jpg_files = glob.glob('*.jpg')
            if len(png_files) > 0:
                os.system('rm *.png')
            if len(bin_files) > 0:
                os.system('rm *.bin')
            if len(csv_files) > 0:
                os.system('rm *.csv')
            if len(jpg_files) > 0:
                os.system('rm *.jpg')
            # Change to Degree Days directory
            os.chdir('./Degree_Days')
            jpg_files = glob.glob('*.jpg')
            avi_files = glob.glob('*.avi')
            if len(jpg_files) > 0:
                os.system('rm *.jpg')
            if len(avi_files) > 0:
                os.system('rm *.avi')
            
        #----------------------------------------------
        # Add All Cohorts Files
        #----------------------------------------------
        if self.archive['All_Cohorts'].lower() == 'yes':
            os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('All_Cohorts')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('All_Cohorts', exclude=exclude_figures)
            print '   All_Cohorts files added to the archive.'

        """ Clean the All_Cohorts directory """
        if self.archive['clean_all_cohorts'].lower() == 'yes':
            os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/All_Cohorts/')
            bin_files = glob.glob('*.bin')
            png_files = glob.glob('*.png')
            csv_files = glob.glob('*.csv')
            jpg_files = glob.glob('*.jpg')
            if len(png_files) > 0:
                os.system('rm *.png')
            if len(bin_files) > 0:
                os.system('rm *.bin')
            if len(csv_files) > 0:
                os.system('rm *.csv')
            if len(jpg_files) > 0:
                os.system('rm *.jpg')
            # Change to Year_Cohorts directory
            os.chdir('./Year_Cohorts')
            jpg_files = glob.glob('*.jpg')
            avi_files = glob.glob('*.avi')
            if len(jpg_files) > 0:
                os.system('rm *.jpg')
            if len(avi_files) > 0:
                os.system('rm *.avi')

        #----------------------------------------------
        # Add Lake Files
        #----------------------------------------------
        if self.archive['Lakes'].lower() == 'yes':
            print '   Adding Lakes files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('SmallLakes_WT_Y')
                self.archive_file.add('SmallLakes_WT_M')
                self.archive_file.add('SmallLakes_WT_O')
                self.archive_file.add('SmallLakes_WT_Total')
                self.archive_file.add('MediumLakes_WT_Y')
                self.archive_file.add('MediumLakes_WT_M')
                self.archive_file.add('MediumLakes_WT_O')
                self.archive_file.add('MediumLakes_WT_Total')
                self.archive_file.add('LargeLakes_WT_Y')
                self.archive_file.add('LargeLakes_WT_M')
                self.archive_file.add('LargeLakes_WT_O')
                self.archive_file.add('LargeLakes_WT_Total')
                self.archive_file.add('Lakes_WT')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('SmallLakes_WT_Y', exclude=exclude_figures)
                self.archive_file.add('SmallLakes_WT_M', exclude=exclude_figures)
                self.archive_file.add('SmallLakes_WT_O', exclude=exclude_figures)
                self.archive_file.add('SmallLakes_WT_Total', exclude=exclude_figures)
                self.archive_file.add('MediumLakes_WT_Y', exclude=exclude_figures)
                self.archive_file.add('MediumLakes_WT_M', exclude=exclude_figures)
                self.archive_file.add('MediumLakes_WT_O', exclude=exclude_figures)
                self.archive_file.add('MediumLakes_WT_Total', exclude = exclude_figures)
                self.archive_file.add('LargeLakes_WT_Y', exclude=exclude_figures)
                self.archive_file.add('LargeLakes_WT_M', exclude=exclude_figures)
                self.archive_file.add('LargeLakes_WT_O', exclude=exclude_figures)
                self.archive_file.add('LargeLakes_WT_Total', exclude=exclude_figures)
                self.archive_file.add('Lakes_WT', exclude=exclude_figures)
            print '     + Small Lakes, all ages, added to the archive.'
            print '     + Medium Lakes, all ages, added to the archive.'
            print '     + Old Lakes, all ages, added to the archive.'
            print '     + Total of Lakes, all ages, added to the archive.'

            """ Clean the Lakes directories """
            if self.archive['clean_lakes'].lower() == 'yes':
                # Small Lakes -- Wetland Tundra, Young age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_Y/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Small Lakes -- Wetland Tundra, Medium age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_M/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Small Lakes -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Small Lakes -- Wetland Tundra, All ages
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SmallLakes_WT_Total/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')

                # Medium Lakes -- Wetland Tundra, Young age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_Y/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Medium Lakes -- Wetland Tundra, Medium age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_M/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Medium Lakes -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Medium Lakes -- Wetland Tundra, All ages
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/MediumLakes_WT_Total/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')

                # Large Lakes -- Wetland Tundra, Young age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_Y/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Large Lakes -- Wetland Tundra, Medium age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_M/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Large Lakes -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Large Lakes -- Wetland Tundra, All ages
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LargeLakes_WT_Total/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # All Lakes -- Wetland Tundra, All Sizes, All ages
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Lakes_WT/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')

                    
        #----------------------------------------------
        # Add Pond Files
        #----------------------------------------------
        if self.archive['Ponds'].lower() == 'yes':
            print '   Adding Pond files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('Ponds_WT_Y')
                self.archive_file.add('Ponds_WT_M')
                self.archive_file.add('Ponds_WT_O')
                self.archive_file.add('Ponds_WT_Total')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('Ponds_WT_Y', exclude=exclude_figures)
                self.archive_file.add('Ponds_WT_M', exclude=exclude_figures)
                self.archive_file.add('Ponds_WT_O', exclude=exclude_figures)
                self.archive_file.add('Ponds_WT_Total', exclude=exclude_figures)
            print '     + Ponds, all ages, added to the archive.'
            print '     + Total of Ponds, all ages, added to the archive.'

            """ Clean the Pond directories """
            if self.archive['clean_ponds'].lower() == 'yes':
                # Ponds -- Wetland Tundra, Young age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_Y/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Ponds -- Wetland Tundra, Medium age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_M/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Ponds -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Ponds -- Wetland Tundra, All ages
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Ponds_WT_Total/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')


        #----------------------------------------------
        # Add Meadow Files
        #----------------------------------------------
        if self.archive['Meadows'].lower() == 'yes':
            print '   Adding Wetland Tundra, Meadow files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('Meadow_WT_Y')
                self.archive_file.add('Meadow_WT_M')
                self.archive_file.add('Meadow_WT_O')
                self.archive_file.add('Meadow_WT_Total')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('Meadow_WT_Y', exclude=exclude_figures)
                self.archive_file.add('Meadow_WT_M', exclude=exclude_figures)
                self.archive_file.add('Meadow_WT_O', exclude=exclude_figures)
                self.archive_file.add('Meadow_WT_Total', exclude=exclude_figures)
            print '     + Wetland Tundra Meadows, all ages, added to the archive.'
            print '     + Total of Wetland Tundra Meadows, all ages, added to the archive.'

            """ Clean the Meadow directories """
            if self.archive['clean_meadows'].lower() == 'yes':
                # Meadows -- Wetland Tundra, Young age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Meadow_WT_Y/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Meadows -- Wetland Tundra, Medium age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Meadow_WT_M/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Meadows -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Meadow_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                    
                # Meadows -- Wetland Tundra, All ages
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Meadow_WT_Total/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')

        #----------------------------------------------
        # Add Low Center Polygon Files
        #----------------------------------------------
        if self.archive['Low_Center_Polygons'].lower() == 'yes':
            print '   Adding Wetland Tundra, Low Center Polygon files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('LCP_WT_Y')
                self.archive_file.add('LCP_WT_M')
                self.archive_file.add('LCP_WT_O')
                self.archive_file.add('LCP_WT_Total')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('LCP_WT_Y', exclude=exclude_figures)
                self.archive_file.add('LCP_WT_M', exclude=exclude_figures)
                self.archive_file.add('LCP_WT_O', exclude=exclude_figures)
                self.archive_file.add('LCP_WT_Total', exclude=exclude_figures)
            print '     + Wetland Tundra Low Center Polygons, all ages, added to the archive.'
            print '     + Total of Wetland Tundra Low Center Polygons, all ages, added to the archive.'

            """ Clean the Low Center Polygons directories """
            if self.archive['clean_lcp'].lower() == 'yes':
                # Low Center Polgyons -- Wetland Tundra, Young age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LCP_WT_Y/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Low Center Polygons -- Wetland Tundra, Medium age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LCP_WT_M/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Low Center Polygons -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LCP_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                    
                # Low Center Polygons -- Wetland Tundra, All ages
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/LCP_WT_Total/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')

        #----------------------------------------------
        # Add Coalescent Low Center Polygon Files
        #----------------------------------------------
        if self.archive['Coalescent_Low_Center_Polygons'].lower() == 'yes':
            print '   Adding Wetland Tundra, Coalescent Low Center Polygon files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('CLC_WT_Y')
                self.archive_file.add('CLC_WT_M')
                self.archive_file.add('CLC_WT_O')
                self.archive_file.add('CLC_WT_Total')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('CLC_WT_Y', exclude=exclude_figures)
                self.archive_file.add('CLC_WT_M', exclude=exclude_figures)
                self.archive_file.add('CLC_WT_O', exclude=exclude_figures)
                self.archive_file.add('CLC_WT_Total', exclude=exclude_figures)
            print '     + Wetland Tundra Coalescent Low Center Polygons, all ages, added to the archive.'
            print '     + Total of Wetland Tundra Coalescent Low Center Polygons, all ages, added to the archive.'

            """ Clean the Coalescent Low Center Polygons directories """
            if self.archive['clean_clc'].lower() == 'yes':
                # Coalescent Low Center Polgyons -- Wetland Tundra, Young age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CLC_WT_Y/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Coalescent Low Center Polygons -- Wetland Tundra, Medium age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CLC_WT_M/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Coalescent Low Center Polygons -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CLC_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                    
                # Coalescent Low Center Polygons -- Wetland Tundra, All ages
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CLC_WT_Total/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
        #----------------------------------------------
        # Add Flat Center Polygon Files
        #----------------------------------------------
        if self.archive['Flat_Center_Polygons'].lower() == 'yes':
            print '   Adding Wetland Tundra, Flat Center Polygon files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('FCP_WT_Y')
                self.archive_file.add('FCP_WT_M')
                self.archive_file.add('FCP_WT_O')
                self.archive_file.add('FCP_WT_Total')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('FCP_WT_Y', exclude=exclude_figures)
                self.archive_file.add('FCP_WT_M', exclude=exclude_figures)
                self.archive_file.add('FCP_WT_O', exclude=exclude_figures)
                self.archive_file.add('FCP_WT_Total', exclude=exclude_figures)
            print '     + Wetland Tundra Flat Center Polygons, all ages, added to the archive.'
            print '     + Total of Wetland Tundra Flat Center Polygons, all ages, added to the archive.'

            """ Clean the Flat Center Polygons directories """
            if self.archive['clean_fcp'].lower() == 'yes':
                # Flat Center Polgyons -- Wetland Tundra, Young age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/FCP_WT_Y/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Flat Center Polygons -- Wetland Tundra, Medium age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/FCP_WT_M/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Flat Center Polygons -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/FCP_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                    
                # Flat Center Polygons -- Wetland Tundra, All ages
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/FCP_WT_Total/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')

        #----------------------------------------------
        # Add High Center Polygon Files
        #----------------------------------------------
        if self.archive['High_Center_Polygons'].lower() == 'yes':
            print '   Adding Wetland Tundra, High Center Polygon files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('HCP_WT_Y')
                self.archive_file.add('HCP_WT_M')
                self.archive_file.add('HCP_WT_O')
                self.archive_file.add('HCP_WT_Total')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('HCP_WT_Y', exclude=exclude_figures)
                self.archive_file.add('HCP_WT_M', exclude=exclude_figures)
                self.archive_file.add('HCP_WT_O', exclude=exclude_figures)
                self.archive_file.add('HCP_WT_Total', exclude=exclude_figures)
            print '     + Wetland Tundra High Center Polygons, all ages, added to the archive.'
            print '     + Total of Wetland Tundra High Center Polygons, all ages, added to the archive.'

            """ Clean the High Center Polygons directories """
            if self.archive['clean_hcp'].lower() == 'yes':
                # High Center Polgyons -- Wetland Tundra, Young age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/HCP_WT_Y/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # High Center Polygons -- Wetland Tundra, Medium age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/HCP_WT_M/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # High Center Polygons -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/HCP_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                    
                # High Center Polygons -- Wetland Tundra, All ages
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/HCP_WT_Total/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                    
        #----------------------------------------------
        # Add Coastal Waters Files
        #----------------------------------------------
        if self.archive['Coastal_Waters'].lower() == 'yes':
            print '   Adding Wetland Tundra, Coastal Waters files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('CoastalWaters_WT_O')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('CoastalWaters_WT_O', exclude=exclude_figures)
            print '     + Wetland Tundra Coastal Waters, Old age, added to the archive.'

            """ Clean the Coastal Water directory """
            if self.archive['clean_coastal_waters'].lower() == 'yes':
                # Coastal Waters -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/CoastalWaters_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')

        #----------------------------------------------
        # Add Drained Slopes Files
        #----------------------------------------------
        if self.archive['Drained_Slopes'].lower() == 'yes':
            print '   Adding Wetland Tundra, Drained Slope files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('DrainedSlope_WT_Y')
                self.archive_file.add('DrainedSlope_WT_M')
                self.archive_file.add('DrainedSlope_WT_O')
                self.archive_file.add('DrainedSlope_WT_Total')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('DrainedSlope_WT_Y', exclude=exclude_figures)
                self.archive_file.add('DrainedSlope_WT_M', exclude=exclude_figures)
                self.archive_file.add('DrainedSlope_WT_O', exclude=exclude_figures)
                self.archive_file.add('DrainedSlope_WT_Total', exclude=exclude_figures)
            print '     + Wetland Tundra Drained Slopes, all ages, added to the archive.'
            print '     + Total of Wetland Tundra Drained Slopes, all ages, added to the archive.'

            """ Clean the Drained Slopes directories """
            if self.archive['clean_drained_slopes'].lower() == 'yes':
                # Drained Slopes -- Wetland Tundra, Young age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/DrainedSlope_WT_Y/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Drained Slopes -- Wetland Tundra, Medium age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/DrainedSlope_WT_M/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Drained Slopes -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/DrainedSlope_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                    
                # Drained Slopes -- Wetland Tundra, All ages
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/DrainedSlope_WT_Total/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')

        #----------------------------------------------
        # Add River Files
        #----------------------------------------------
        if self.archive['Rivers'].lower() == 'yes':
            print '   Adding Wetland Tundra, River files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('Rivers_WT_Y')
                self.archive_file.add('Rivers_WT_M')
                self.archive_file.add('Rivers_WT_O')

            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('Rivers_WT_Y', exclude=exclude_figures)
                self.archive_file.add('Rivers_WT_M', exclude=exclude_figures)
                self.archive_file.add('Rivers_WT_O', exclude=exclude_figures)
            print '     + Wetland Tundra Rivers, all ages, added to the archive.'

            """ Clean the River directories """
            if self.archive['clean_rivers'].lower() == 'yes':
                # Rivers -- Wetland Tundra, Young age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Rivers_WT_Y/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Rivers -- Wetland Tundra, Medium age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Rivers_WT_M/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Rivers -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Rivers_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')

        #----------------------------------------------
        # Add Sand Dunes Files
        #----------------------------------------------
        if self.archive['Sand_Dunes'].lower() == 'yes':
            print '   Adding Wetland Tundra, Sand Dunes files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('SandDunes_WT_Y')
                self.archive_file.add('SandDunes_WT_M')
                self.archive_file.add('SandDunes_WT_O')
                self.archive_file.add('SandDunes_WT_Total')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('SandDunes_WT_Y', exclude=exclude_figures)
                self.archive_file.add('SandDunes_WT_M', exclude=exclude_figures)
                self.archive_file.add('SandDunes_WT_O', exclude=exclude_figures)
                self.archive_file.add('SandDunes_WT_Total', exclude=exclude_figures)
            print '     + Wetland Tundra Sand Dunes, all ages, added to the archive.'
            print '     + Total of Wetland Tundra Sand Dunes, all ages, added to the archive.'

            """ Clean the Sand Dunes directories """
            if self.archive['clean_sand_dunes'].lower() == 'yes':
                # Sand Dunes -- Wetland Tundra, Young age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SandDunes_WT_Y/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Sand Dunes -- Wetland Tundra, Medium age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SandDunes_WT_M/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Sand Dunes -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SandDunes_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                    
                # Sand Dunes -- Wetland Tundra, All ages
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SandDunes_WT_Total/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')

        #----------------------------------------------
        # Add Sand Dunes Files
        #----------------------------------------------
        if self.archive['Saturated_Barrens'].lower() == 'yes':
            print '   Adding Wetland Tundra, Saturated Barrens files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('SaturatedBarrens_WT_Y')
                self.archive_file.add('SaturatedBarrens_WT_M')
                self.archive_file.add('SaturatedBarrens_WT_O')
                self.archive_file.add('SaturatedBarrens_WT_Total')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('SaturatedBarrens_WT_Y', exclude=exclude_figures)
                self.archive_file.add('SaturatedBarrens_WT_M', exclude=exclude_figures)
                self.archive_file.add('SaturatedBarrens_WT_O', exclude=exclude_figures)
                self.archive_file.add('SaturatedBarrens_WT_Total', exclude=exclude_figures)
            print '     + Wetland Tundra Saturated Barrens, all ages, added to the archive.'
            print '     + Total of Wetland Tundra Saturated Barrens, all ages, added to the archive.'

            """ Clean the Sand Dunes directories """
            if self.archive['clean_saturated_barrens'].lower() == 'yes':
                # Saturated Barrens -- Wetland Tundra, Young age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SaturatedBarrens_WT_Y/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Saturated Barrens -- Wetland Tundra, Medium age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SaturatedBarrens_WT_M/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                # Saturated Barrens -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SaturatedBarrens_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                    
                # Saturated Barrens -- Wetland Tundra, All ages
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/SaturatedBarrens_WT_Total/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')


        #----------------------------------------------
        # Add Shrubs Files
        #----------------------------------------------
        if self.archive['Shrubs'].lower() == 'yes':
            print '   Adding Wetland Tundra, Shrub files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('Shrubs_WT_O')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('Shrubs_WT_O', exclude=exclude_figures)
            print '     + Wetland Tundra Shrubs, Old age, added to the archive.'

            """ Clean the Shrubs directory """
            if self.archive['clean_shrubs'].lower() == 'yes':
                # Shrubs -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Shrubs_WT_O/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')

        #----------------------------------------------
        # Add Urban Files
        #----------------------------------------------
        if self.archive['Urban'].lower() == 'yes':
            print '   Adding Wetland Tundra, Urban files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('Urban_WT')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('Urban_WT', exclude=exclude_figures)
            print '     + Wetland Tundra Urban, added to the archive.'

            """ Clean the Urban directory """
            if self.archive['clean_urban'].lower() == 'yes':
                # Urban -- Wetland Tundra, Old age
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Urban_WT/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')

        #----------------------------------------------
        # Add No Data Files
        #----------------------------------------------
        if self.archive['No_Data'].lower() == 'yes':
            print '   Adding Wetland Tundra, No Data files to the archive.'            
            os.chdir(self.control['Run_dir']+self.Output_directory+\
                     '/Barrow/')
            if self.archive['Figures'].lower() == 'yes':
                self.archive_file.add('Other_Cohorts')
            else:
                def exclude_figures(filename):
                    return filename.endswith(('jpg', 'png', 'avi'))
                self.archive_file.add('Other_Cohorts', exclude=exclude_figures)
            print '     + Wetland Tundra, No Data added to the archive.'

            """ Clean the No Data directory """
            if self.archive['clean_no_data'].lower() == 'yes':
                # No Data -- Wetland Tundra
                os.chdir(self.control['Run_dir']+self.Output_directory+'/Barrow/Other_Cohorts/')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')
                os.chdir('./Year_Cohorts')
                bin_files = glob.glob('*.bin')
                png_files = glob.glob('*.png')
                csv_files = glob.glob('*.csv')
                jpg_files = glob.glob('*.jpg')
                if len(bin_files) > 0:
                    os.system('rm *.bin')
                if len(png_files) > 0:
                    os.system('rm *.png')
                if len(csv_files) > 0:
                    os.system('rm *.csv')
                if len(jpg_files) > 0:
                    os.system('rm *.jpg')



        #-----------------------------------
        # Close the archive file
        #-----------------------------------
        self.archive_file.close()
        
        print '+++++++++++++++++++++++++++++'
        print '   Simulation archived. '
        print '+++++++++++++++++++++++++++++'
        print ' '

        
    # =============================================================================
    # Simulation area -- Yukon
    # =============================================================================
    elif self.Simulation_area.lower() == 'yukon':
        print ' ++++++++++++++++++++++++++++++++++++'
        print '  Archiving Yukon Flats results.'
        print ' ++++++++++++++++++++++++++++++++++++'

    # =============================================================================
    # Simulation area -- Tanana
    # =============================================================================
    elif self.Simulation_area.lower() == 'tanana':
        print ' ++++++++++++++++++++++++++++++++++++'        
        print '  Archiving Tanana Flats results.'
        print ' ++++++++++++++++++++++++++++++++++++'
        
    
