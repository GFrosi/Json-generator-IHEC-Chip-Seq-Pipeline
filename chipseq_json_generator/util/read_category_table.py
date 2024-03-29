
import pandas as pd
from os import listdir


def read_table(file_name):
    """Receives a df containing at least
    GSM and SRR columns. The df should be
    separated by pipe. Returns two dicts
    (control and treatment: gsm as key and 
    srr as value)"""
  
    ctl = {}
    treat = {}

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


def read_sample(file_name):
    """Receives a csv file
    generated by gsm_seq.py.
    Returns a dictionary (keys 
    as gsm and values as type of
    sequencing - single or paired)"""
    
    sample = {}

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            gsm, seq = line.split(',')

            sample[gsm] = seq

    return sample


def read_srr_dir(srr_path):
    """Receives a path to SRR 
    files and returns a dict (keys 
    as srr and values as type of
    sequencing - single or paired)
    """

    srr_dict = {}
    srr_list = listdir(srr_path)
    
    for i in srr_list:
        srr, _ = i.split('_')

        if srr + '_2.fastq.gz' in srr_list:
            srr_dict[srr] = 'paired'
        
        else:
            srr_dict[srr] = 'single'

    return srr_dict        



def read_df(file_name):
    """Receives a file separated
    by pipe"""
  
    df = pd.read_csv(file_name, sep='|')
        
    return df


                 

