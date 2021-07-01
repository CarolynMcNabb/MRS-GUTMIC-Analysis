"""
Carolyn McNabb 2021
This script will make the directories for the pilot MRS data so they can be accessed by Osprey for analysis

"""

import os
import pathlib
import string

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
            #list all the folder names in the subject directory
            print(os.listdir(sub_path))
            #change into the subject directory
            os.chdir(sub_path)
            #create a new name for the subject, replacing s0 with sub- (so s001 becomes sub-01)
            bids_sub = sub.name.replace("s0","sub-")
            
            #create new directory names
            striatum_dir = bids_sub + "_megapress_striatum"
            striatum_h20 = bids_sub + "_H20-ref_striatum"
            MC_dir = bids_sub + "_megapress_MC"
            MC_h20 = bids_sub + "_H20-ref_MC"
            CO_dir = bids_sub + "_megapress_CO"
            CO_h20 = bids_sub + "_H20-ref_CO"
            
            #put all these new directory names in an array
            dirs = {striatum_dir, striatum_h20, MC_dir, MC_h20, CO_dir, CO_h20}
            #within the new array (dirs), make each of the above folders under parent folder mrs
            for d in dirs:
                #make directories if they do not already exist
                newdir = pathlib.Path(os.path.join(dest_path,bids_sub,d))
                #create the new folders only if they don't already exist. Do not overwrite any files already contained within folders
                newdir.mkdir(parents=True, exist_ok=True)
                print(newdir)
               
            #move up to mrs directory and begin again
            os.chdir(path = mrs_path)

            

os.chdir("/Volumes/GoogleDrive/My Drive/GitHub/MRS-GUTMIC-Analysis")
