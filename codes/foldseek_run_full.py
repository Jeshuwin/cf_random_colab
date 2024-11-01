#!/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 10:50:00 2024
 
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


##### Foldseek module is loaded for workstation or Foldseek is installed for local machine






class running_foldseek_full():
    def gen_dir(self, get_dir):
        ## getting predicted directory
        print("Getting the list of predicted models...")
        pwd = os.getcwd() + '/'

        files_list = (glob.glob(str(get_dir) + "/*_unrelaxed*pdb"))
        self.files_list = files_list



    def run_foldseek(self):
        print(self.files_list)

        pwd = os.getcwd()
        for model in self.files_list:
            print(model)
            command = '/content/foldseek/bin/foldseek easy-search ' + model + ' ' + pwd + '/pdb ' + model[:-3] + 'foldseek tmp --format-mode 0 --format-output "query,target,alntmscore,qaln,taln,alnlen,evalue,bits"'
            print(command); os.system(command)



    def __init__(self, pdb1_name):
        self.pdb1_name = pdb1_name

        ### directory name full (pdb1_name + '_predicted_models_full_rand_' + str(random_seed))
        ### directory name shallow (pdb1_name + '_predicted_models_rand_' + str(ran_seed) + '_max_*')
        ### 2oug_C_predicted_models_rand_43_max_8_ext_16/ 
        #foldseek_db = "foldseek databases PDB pdb tmp"
        #os.system(foldseek_db)


        get_dir_full  = pdb1_name + '/' + pdb1_name + '_predicted_models_full_rand_*'
  
        self.gen_dir(get_dir_full);  self.run_foldseek()




        ### for input_pdb in 0_relaxed*pdb;do foldseek easy-search ${input_pdb} $FOLDSEEK_DB/PDB ${input_pdb::-3}foldseek tmp --format-mode 0 --format-output "query,target,alntmscore,qaln,taln,alnlen,evalue,bits";done

        




