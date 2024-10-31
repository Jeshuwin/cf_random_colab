#!/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:51:00 2024
 
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
import random
import argparse



class CF_MSA_max():
    def __init__(self, search_dir, output_dir, pdb_name, rseed):

        #command = 'colabfold_batch --num-seeds 5 --random-seed ' + str(rseed) + search_dir + output_dir
        command = 'colabfold_batch --num-seeds 5 --random-seed ' + str(rseed) + search_dir + output_dir
        print(command)
        os.system(command)
        
                




class prediction_all_blind_max():
    def __init__(self, pdb1_name, search_dir):
        
        pre_random_seed = np.random.randint(0, 16, 1)
        random_seed = ''.join(map(str, pre_random_seed))
        print(random_seed)
        output_dir = ' ' + pdb1_name + '_predicted_models_full_rand_' + str(random_seed)
        print(output_dir)


        ##### Perform predction with full-length MSA
        MSA_full = CF_MSA_max(search_dir, output_dir, pdb1_name, random_seed)
        pwd = os.getcwd() + '/'


        # Directory section
        gen_dir = pdb1_name

        if not os.path.exists(gen_dir):
            os.mkdir(gen_dir)


        pred_dir = pdb1_name + '_predicted_models_full_rand_' + str(random_seed) + '/'
        mv_folder_cmd = 'mv ' + pred_dir + ' ' + pdb1_name
        print(mv_folder_cmd); os.system(mv_folder_cmd)





