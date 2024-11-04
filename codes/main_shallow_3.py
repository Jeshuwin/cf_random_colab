#!/upyMolsr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:51:00 2024
 
@author: Myeongsang (Samuel) Lee
"""

import re
import Bio
import os
from os import listdir
from os.path import isfile, join
import sys
from pathlib import Path
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import glob
import argparse


from pred_cal_tmscore_FS import *
from pred_cal_tmscore_blind_shallow_3 import *
from pred_cal_tmscore_AC import *
from additional_pred_FS import * 
from additional_pred_AC import *
from CF_random_blind import *
from cal_plddt_ACFS import *
from PLOT_AC import *
from PLOT_FS import *

if __name__ == "__main__":

    import warnings
    warnings.filterwarnings('ignore')

    ######################################################################################################
    ###### initiallization pdb format (removing HETATM)
    #os.system("for i in *pdb;do echo $i;sed -i '/HETATM/d' $i;done")



    ######################################################################################################
    ###### initiallization and input
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdb1", type=str, help='PDB structure for the target crystal structure (target to be predicted)')
    parser.add_argument("--pdb2", type=str, help='PDB structure for the alternative crystal structure')
    parser.add_argument("--fname", type=str, help='put folder name after colabsearch' )
    parser.add_argument("--pname", type=str, help='put tentative protein name for blind search' )    
    parser.add_argument("--option", type=str, help='select prediction mode AC and FS e.g. AC = alterantive conformation or FS = fold-switching')
    args = parser.parse_args()


    if args.pdb1 is not None:
        pdb1 = args.pdb1; pdb2 = args.pdb2
    else:
        blind_pdb_name = args.pname


    
 
    if args.pdb1 is None:
        blind_pdb_name = args.pname; pdb1_name = blind_pdb_name
    else:
        pdb1_name = pdb1.replace('.pdb','');  pdb2_name = pdb2.replace('.pdb','')
     

    if args.pdb1 is not None and args.option == "blind":
      pdb1_name = args.pdb1; pdb1_name = pdb1.replace('.pdb','')
    elif args.pdb1 is not None and args.option == "blind":
      blind_pdb_name = args.pname; pdb1_name = blind_pdb_name;


    pwd = os.getcwd() + '/'
    search_dir = ' ' + pwd + args.fname





    print("Predicting fold-swithcing proteins without crystal structures of pdbs")
    
    
    
    ###### running prediction using shallow random-MSA
    blind_pred_path = pdb1_name
    print(blind_pred_path)
    
    prediction_all_blind_shallow_3(pdb1_name, search_dir)
    print("               ")
    print("Finished running for prediction using shallow random-MSAs")
            
