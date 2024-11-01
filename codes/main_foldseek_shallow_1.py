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
from pred_cal_tmscore_blind_max import *
from pred_cal_tmscore_AC import *
from additional_pred_FS import * 
from additional_pred_AC import *
from foldseek_run__shallow_1 import *
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

    blind = 'blind_prediction'
    success = 'successed_prediction'
    fail = 'failed_prediction'








    if args.option == "blind":
        print("Predicting fold-swithcing proteins without crystal structures of pdbs")
        ######################################################################################################
        ###### check previous predictions were performed or not
        if not os.path.exists(pdb1_name):
            os.mkdir(pdb1_name)
            blind_dir_count = 0
        elif os.path.exists(pdb1_name):
            blind_dir_count = 0
            for root_dir, cur_dir, files in os.walk(pdb1_name + '/'):
                blind_dir_count += len(cur_dir)
            
            if os.path.exists(pdb1_name):
              if blind_dir_count >= 8:
                print("Prediction was already done")
            else:
                print("Folder is already created and cleaning existed subfolders")
                rm_pre_folders = 'rm -rf ' + pdb1_name + '/'
                os.system(rm_pre_folders)
        else:
            pass



        ###### running prediction using full- and shallow random-MSA
        blind_pred_path = pdb1_name
        print(blind_pred_path)

        if os.path.exists(pdb1_name) and blind_dir_count >= 8:
            print("Predictions including full- and random-MSA were already done")
            pass

            fseek_file_count = 0
            for root_dir, cur_dir, files in os.walk(pdb1_name + '/'):
                fseek_file_count += len(files)

            print(fseek_file_count)
            ##if fseek_file_count == 856: ##(107 * 8) 107 includes foldseek file and 8 means the numbers of prediction folders
            if fseek_file_count >= 640: ##672
                print("    "); print("Foldseek search was done")
                pass
            #    #### performing the PCA calculation with RMSD
            #    #PCA_rmsd(pdb1_name, blind_pred_path)
                blind_screening(pdb1_name, blind_pred_path)
            else:
                running_foldseek_shallow_1(pdb1_name)

            #    #### performing the PCA calculation with RMSD
            #    #PCA_rmsd(pdb1_name, blind_pred_path)
            #    blind_screening(pdb1_name, blind_pred_path)



        else:
            print("Finished running for prediction using full- and shallow random-MSAs")
            
            print("               ")
            print("Running Foldseek to find the relatedcrystal structures")
            running_foldseek_shallow_1(pdb1_name)
            





    else:
        print("Please type correct option")

