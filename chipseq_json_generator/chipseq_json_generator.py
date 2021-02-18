import argparse
from util.read_category_table import read_table, read_sample
from util.read_config import read_config
import os 


def print_json(config, chip_ctl, chip_treat):

    '''Function to print an input json.file for the IHEC pipeline. Config is a base json file 
    (json_config.ini) with the basic parameters to run the pipleine. Chip_ctl and Chip treat are 
    strings that contains the replicate tag and the path to SRR files'''

    print('{')
    print(chip_ctl)
    print()
    print(chip_treat)
    
    for k,v in config.items():
        print('"'+ k + '":' + v)
    
    print('}')



def add_path(list_of_srr, srr_path, number):

    if number == 1:
        list_with_path =  [ '"' + os.path.join(srr_path,srr) + '_' + str(number) + '.fastq.gz"' for srr in list_of_srr ]
        return list_with_path
    else:
        list_with_path_R1 =  [ '"' + os.path.join(srr_path,srr) + '_' + str(number - 1) + '.fastq.gz"' for srr in list_of_srr ]
        list_with_path_R2 =  [ '"' + os.path.join(srr_path,srr) + '_' + str(number) + '.fastq.gz"' for srr in list_of_srr ]

        return list_with_path_R1, list_with_path_R2


def prepare_sample_json(ctl, treat, sample, srr_path):
    '''This function organize the information about control and IP replicates for the json input file. 
    Ctl and treat are dictionaries with the control and IP sample and their SRR (or SRRs) information, 
    respectively. Sample is a dictionary with GSM as key and sequence type (single or paired end) as its value.
    The srr_path is the absolut directory path for the SRR files. It is passed as args.path (see def_main)'''
    
    chip_ctl = ''
    chip_treat = ''

    counter_t = 0
    counter_c = 0

    for gsm, seq_type in sample.items():
        if seq_type == 'single':
            if gsm in ctl.keys():
                list_with_path = add_path(ctl[gsm],srr_path, 1)
                str_line = ",".join(list_with_path)

                chip_treat += '"chip.ctl_fastqs_rep'+ str(counter_c + 1) + '_R1" : [' +  str_line  + '],\n'
                counter_c +=1

            
            if gsm in treat.keys():

                list_with_path = add_path(treat[gsm],srr_path,1)
                str_line = ",".join(list_with_path)

                chip_treat += '"chip.fastqs_rep'+ str(counter_t + 1) + '_R1" : [' +  str_line  + '],\n'
                
                counter_t += 1
                
 #pair end

        else:
            if gsm in ctl.keys():

                list_with_path_R1, list_with_path_R2 = add_path(ctl[gsm],srr_path, 2)
                str_line_R1 = ",".join(list_with_path_R1)
                str_line_R2 = ",".join(list_with_path_R2)

                chip_ctl += '"chip.ctl_fastqs_rep'+ str(counter_c+1) + '_R1" : [' + str_line_R1 + '],\n"chip.ctl_fastqs_rep'+ str(counter_c+1) + '_R2" : [' + str_line_R2 +'],\n' 
                counter_c += 1
             
            if gsm in treat.keys():
                list_with_path_R1, list_with_path_R2 = add_path(treat[gsm],srr_path, 2)
                str_line_R1 = ",".join(list_with_path_R1)
                str_line_R2 = ",".join(list_with_path_R2)

                chip_ctl += '"chip.fastqs_rep'+ str(counter_t+1) + '_R1" : [' + str_line_R1 + '],\n"chip.fastqs_rep'+ str(counter_t+1) + '_R2" : [' + str_line_R2 +'],\n' 

                counter_t +=1

    return chip_ctl, chip_treat



def main():
    ctl, treat = read_table(args.table)
    config = read_config(args.config)
    sample = read_sample(args.sample)
    chip_ctl, chip_treat = prepare_sample_json(ctl, treat, sample, args.path)
    print_json(config, chip_ctl, chip_treat)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="A tool to create json input files for the IHEC pipeline")

    parser.add_argument('-t', '--table', action="store",
                        help='The Category table with GSM, SRX, SRR, Category columns',
                        required=True)

    parser.add_argument('-c', '--config', action='store',
                        help='The json config file',
                        required=True)

    parser.add_argument('-s', '--sample', action='store',
                        help='The samples (GSM) with single or pair end information after download SRR files',
                        required=True)

    parser.add_argument('-p', '--path', action='store',
                        help='The SRR path',
                        required=True)
    
    args = parser.parse_args()
    main()