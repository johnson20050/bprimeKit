# The bprimeKit

The bprimeKit aims to strip the miniAOD format used by CMSSW into a standalone ROOT Ntuple for offline analysis needs. 

## Setup and running
Below is the standard setup for the brpimeKit running under CMSSW_7_4_2 
```
cmsrel CMSSW_7_4_2
cd CMSSW_7_4_2/src
cmsenv 

git cms-merge-topic ikrav:egm_id_74X_v0
git clone https://github.com/cmsb2g/B2GAnaFW Analysis/B2GAnaFW 
git clone https://github.com/ETHZ/sixie-Muon-MuonAnalysisTools.git UserCode/sixie/Muon/MuonAnalysisTools
git clone https://github.com/amarini/QuarkGluonTagger.git
git clone -b CMSSW_7_4_2 https://github.com/enochnotsocool/bprimeKit MyAna/bprimeKit

scram b -j 10
```
To run the bprimeKit and generate ntuples, under the CMS environment:
```
cd MyAna/bprimeKit/test
cmsRun bprimeKit_miniAOD_74X.py  
```
please manually change the input and output settings in the python file for you needs.

## Adding your own object information

The data that are extracted into the bprimekit ntuple is defined in the file `interface/format.h`, while the CMSSW methods for extractign the data are implemented in the various `plugins/bprimeKit_*.cc` files. If you need to add additional data for you ntuple needs:

1. Add the data defintion in the public section of the ntuple branch.
2. Use the MACROS functions defined to properly link the data with the TTree object. 
3. Add the corresponding code required for extracting the data in the corresponding `plugins/bprimeKit_*.cc` file. 

Here are a few sidenote for additional rule to help with code clarity.
- Try to keep the data grouped by type for functionality. Add sepeartor comments if need be.
- If helper variables are required for a certain data extraction:
  - If the helper variables are required by multiple Ntuple branches, declare them as private data members of the bprimeKit class.
  - If the helper variables are only required by a signle Ntuple branch, please declare them as ``static`` global variables in the independent files.
- Before committing, please remove all commented out c++ codes. Reserve comments for code description.

