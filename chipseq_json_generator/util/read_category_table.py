

import pandas as pd
from os import listdir

'''This function creates two dictionares (control and treatment). You need to give a file (table)
with at least gsm and srr per gsm. The csv separator in this case is a pipe. If other separator,
change the line.split(','). Each dict have gsm as key and srr as value'''

def read_table(file_name):

    ctl = dict()
    treat = dict()


    with open(file_name, 'r') as file:

        for line in file:
            line = line.strip()
            gsm, srx, srr, category = line.split('|')

            srr_list = srr.split(',')

            if category == 'Control':  
                ctl[gsm] = srr_list

            else:
                treat[gsm] = srr_list

    return ctl, treat


'''Return a dict from a file that contains the gsm and sequence type (single or pair end). This file
is generated by gsm_seq.py'''

def read_sample(file_name):

    sample = {}

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            gsm, seq = line.split(',')

            sample[gsm] = seq

    return sample


'''Open a file as dataframe'''
def read_df(file_name):

    df = pd.read_csv(file_name, sep='|')
        
    return df

'''Function to return a dictionary with srr id and sequence type (single or pair end)'''

def read_srr_dir(srr_path):

    srr_dict = {}
    srr_list = listdir(srr_path)
    
    for i in srr_list:
        srr, _ = i.split('_')

        if srr + '_2.fastq.gz' in srr_list:
            srr_dict[srr] = 'paired'
        
        else:
            srr_dict[srr] = 'single'

    return srr_dict        





                 
