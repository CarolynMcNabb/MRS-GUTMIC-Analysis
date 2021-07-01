"""
Carolyn McNabb 2021
This script will copy the raw DICOM files from the subject folders into their own inidividual folders (arranged by sequence and brain region) within the mrs subfolder

"""

print("This might take a while...")

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
            
            #directory names are:
            striatum_dir = bids_sub + "_megapress_striatum"
            striatum_h20 = bids_sub + "_H20-ref_striatum"
            MC_dir = bids_sub + "_megapress_MC"
            MC_h20 = bids_sub + "_H20-ref_MC"
            CO_dir = bids_sub + "_megapress_CO"
            CO_h20 = bids_sub + "_H20-ref_CO"
            
            #the source directory contains the raw DICOM files
            sourcedir = os.path.join(sub_path,"raw_renamed")
                
            #list files in the raw_data folder
            for fname in os.listdir(sourcedir):
                #if the string defined below matches any files
                #sub-01 has different file names for some reason, so requires the following two if statements:
                if "Stra_single_averages" in fname:
                    #create a destination for the file
                    destdir = os.path.join(dest_path,bids_sub,striatum_dir)
                    #path to original file
                    src = os.path.join(sourcedir,fname)
                    #create a file with the same file name but in the destination folder
                    shutil.copy(src,destdir)
                    print("Copy of ",fname, "created in ",destdir)
                if "plus_1H2O_Stra_ave" in fname:
                    #create a destination for the file
                    destdir = os.path.join(dest_path,bids_sub,striatum_h20)
                    #path to original file
                    src = os.path.join(sourcedir,fname)
                    #create a file with the same file name but in the destination folder
                    shutil.copy(src,destdir)
                    print("Copy of ",fname, "created in ",destdir)
                #all the rest of the subjects have the same naming convention
                if "STR_single_averages" in fname:
                    #create a destination for the file
                    destdir = os.path.join(dest_path,bids_sub,striatum_dir)
                    #path to original file
                    src = os.path.join(sourcedir,fname)
                    #create a file with the same file name but in the destination folder
                    shutil.copy(src,destdir)
                    print("Copy of ",fname, "created in ",destdir)
                if "plus_1H2O_STR_ave" in fname:
                    #create a destination for the file
                    destdir = os.path.join(dest_path,bids_sub,striatum_h20)
                    #path to original file
                    src = os.path.join(sourcedir,fname)
                    #create a file with the same file name but in the destination folder
                    shutil.copy(src,destdir)
                    print("Copy of ",fname, "created in ",destdir)
                if "MC_single_averages" in fname:
                    #create a destination for the file
                    destdir = os.path.join(dest_path,bids_sub,MC_dir)
                    src = os.path.join(sourcedir,fname)
                    #create a file with the same file name but in the destination folder
                    shutil.copy(src,destdir)
                    print("Copy of ",fname, "created in ",destdir)
                if "plus_1H2O_MC_ave" in fname:
                    #create a destination for the file
                    destdir = os.path.join(dest_path,bids_sub,MC_h20)
                    #path to original file
                    src = os.path.join(sourcedir,fname)
                    #create a file with the same file name but in the destination folder
                    shutil.copy(src,destdir)
                    print("Copy of ",fname, "created in ",destdir)
                if "CO_single_averages" in fname:
                    #create a destination for the file
                    destdir = os.path.join(dest_path,bids_sub,CO_dir)
                    #path to original file
                    src = os.path.join(sourcedir,fname)
                    #create a file with the same file name but in the destination folder
                    shutil.copy(src,destdir)
                    print("Copy of ",fname, "created in ",destdir)
                if "plus_1H2O_CO_ave" in fname:
                    #create a destination for the file
                    destdir = os.path.join(dest_path,bids_sub,CO_h20)
                    #path to original file
                    src = os.path.join(sourcedir,fname)
                    #create a file with the same file name but in the destination folder
                    shutil.copy(src,destdir)
                    print("Copy of ",fname, "created in ",destdir)
               
            #move up to mrs directory and begin again
            os.chdir(path = mrs_path)

            
#return to GitHub directory
os.chdir("/Volumes/GoogleDrive/My Drive/GitHub/MRS-GUTMIC-Analysis")





