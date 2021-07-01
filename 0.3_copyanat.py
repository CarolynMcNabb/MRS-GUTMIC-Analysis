"""
Carolyn McNabb 2021
This script will copy the T1w files from the subject folders into their own inidividual folders within the MRS subfolder

"""

print("Go make yourself a cup of tea.... this could take a while.")

import os
import pathlib
import string
import shutil

#path to mrs data on shared drive
mrs_path = "/Users/Carolyn/Google Drive/My Drive/Pilot/MRS data /"
dest_path = "/Users/Carolyn/Google Drive/My Drive/MRS/GUTMIC_Pilot/"

#change directory to mrs data folder
os.chdir(path = mrs_path)

#get content of mrs data folder, if the directory starts with s0 (i.e. is a subject's file),  then do the following...
with os.scandir(".") as dir:
    for sub in dir:
        if sub.name.startswith('s0') :
            print(sub.name) 
            #create pathname for subject
            sub_path = os.path.join(mrs_path,sub.name)
            #change into the subject directory
            os.chdir(sub_path)
            #create a new name for the subject, replacing s0 with sub- (so s001 becomes sub-01)
            bids_sub = sub.name.replace("s0","sub-")
            
                       
            #the source directory contains the raw DICOM files
            sourcedir = os.path.join(sub_path, "anat")
                
            #list files in the raw_data folder
            for fname in os.listdir(sourcedir):
                #if the string defined below matches any files
                #sub-01-15 have different file names for some reason, so requires the following two if statements:
                if "sGUTMIC" and ".nii" in fname:
                    if not "c" in fname:
                        #create a destination for the file
                        destdir = os.path.join(dest_path,bids_sub,"anat")
                        if not os.path.exists(destdir):
                            os.mkdir(destdir)
                        #path to original file
                        src = os.path.join(sourcedir,fname)
                        #create a file with the same file name but in the destination folder
                        shutil.copy(src,destdir)
                        print("Copy of ",fname, "created in ",destdir)
                if "T1w.nii" in fname:
                    #create a destination for the file
                    destdir = os.path.join(dest_path,bids_sub,"anat")
                    if not os.path.exists(destdir):
                        os.mkdir(destdir)
                    #path to original file
                    src = os.path.join(sourcedir,fname)
                    #create a file with the same file name but in the destination folder
                    shutil.copy(src,destdir)
                    print("Copy of ",fname, "created in ",destdir)
               
            #move up to mrs directory and begin again
            os.chdir(path = mrs_path)

            
#return to GitHub directory
os.chdir("/Volumes/GoogleDrive/My Drive/GitHub/MRS-GUTMIC-Analysis")