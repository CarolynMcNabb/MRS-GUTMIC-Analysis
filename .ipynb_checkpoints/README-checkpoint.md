# MRS Analysis scripts for GUTMIC pilot study 
##### Carolyn McNabb, 2021

 This pipeline will reproduce output from the GUTMIC pilot study. The pipeline requires users to have access to Python 3.8, MATLAB 2020a, as well as [Osprey](https://github.com/schorschinho/osprey) 
 
 
 First, create folders to copy raw MRS data to, using:
 ```
 0.1_makedirs.py
 ```

 Next, copy raw DICOM files into these newly created folders so that each sequence has its own folder (i.e. all megapress files from the striatum go into one folder and the water reference files from the striatum go into a separate folder). 
 ```
 0.2_copyDICOMs.py
 ```