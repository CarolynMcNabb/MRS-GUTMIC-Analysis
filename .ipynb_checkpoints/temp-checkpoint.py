import shutil
for fname in os.listdir("/Users/Carolyn/Google Drive/My Drive/Pilot/MRS data /s001/raw_renamed"):
                #if the string defined below matches any files
                if "Stra_single_averages" in fname:
                    #create a destination for the symbolic link
                    destdir = os.path.join("/Users/Carolyn/Google Drive/My Drive/Pilot/MRS data /s001/mrs/sub-01_megapress_striatum")
                    #dest = os.path.join(destdir,fname)
                    #create a symbolic link with the same file name but in the destination folder
                    shutil.copy(fname,destdir)
                    print("symbolic link created for ",fname)
                if "plus_1H2O_Stra_ave" in fname:
                    #create a destination for the symbolic link
                    destdir = os.path.join("/Users/Carolyn/Google Drive/My Drive/Pilot/MRS data /s001/mrs/sub-01_H20-ref_striatum")
                    #dest = os.path.join(destdir,fname)
                    #create a symbolic link with the same file name but in the destination folder
                    shutil.copy(fname,destdir)
                    print("symbolic link created for ",fname)
                if "plus_1H2O_ave" in fname:
                    #create a destination for the symbolic link
                    destdir = os.path.join("/Users/Carolyn/Google Drive/My Drive/Pilot/MRS data /s001/mrs/sub-01_H20-ref_CO")
                    #dest = os.path.join(destdir,fname)
                    #create a symbolic link with the same file name but in the destination folder
                    shutil.copy(fname,destdir)
                    print("symbolic link created for ",fname)