# Json-generator-IHEC-Chip-Seq-Pipeline

This script generates a json Input file (single and paired end) to IHEC Chip-Seq Pipeline from a dataframe with IPs and INPUT samples and SRR ids information.

## You should first create a table (dataframe) with the follow informations:

|GSM | SRX | SRR | Categories|
|-----------|:-----------:|:--------:|------------|
|GSM2801176 | SRX3236723 | SRR6124070 | Trait|
|GSM2801187 | SRX3236734 | SRR6124081 | Trait|
|GSM1415874 | SRX610759 | SRR1425172 | Trait|
GSM1565791 | SRX818183 | SRR1725759,SRR1725760 | Trait|


### Command line
1. gsm_seq.py

```
python gsm_seq.py -t gsm-srr-srx-categories.csv -p srr/
```
  - "-t": dataframe as exemplified above
  - "-p": root path to SRR samples downloaded from NCBI. This directory will be read to identify if each IP/Input samples has just SRR_1 (SE) or SRR_1 and SRR_2 (PE)
  - This comand will return a dataframe with the SE/PE information per sample. 

```
usage: gsm_seq.py [-h] -t TABLE -p PATH

optional arguments:
  -h, --help            show this help message and exit
  -t TABLE, --table TABLE
                        The Category table with GSM, SRX, SRR, Category
                        columns
  -p PATH, --path PATH  Absolute path to SRR data directory
```


2. chipseq_json_generator.py 

```
python chipseq_json_generator.py -t gsm-srr-srx-categories.
csv -c config/json_config.ini -s data/seq_type.csv -p chip 
```

 - "-t": dataframe as exemplified above
 - "-c": you should pass the json_config.ini. If you want to change any information (as memory, time per step, name of chip.title or description) you should to modify this file before to run this command line
 - "-s": the seq_type.csv file generated by the first command line
 - "-p": output directory

```
usage: chipseq_json_generator.py [-h] -t TABLE -c CONFIG -s SAMPLE -p PATH

A tool to create json input files for the IHEC pipeline

optional arguments:
  -h, --help            show this help message and exit
  -t TABLE, --table TABLE
                        The Category table with GSM, SRX, SRR, Category
                        columns
  -c CONFIG, --config CONFIG
                        The json config file
  -s SAMPLE, --sample SAMPLE
                        The samples (GSM) with single or pair end information
                        after download SRR files
  -p PATH, --path PATH  The SRR path
```


### ihec_json_noinput.py

If you want to run the pipeline without Input samples, this script will get the json generated before and remove the ctl.fastqs keys and update the title and description information

```
python ihec_json_noinput.py -p json_files/ -o test_argparser_out/
```
 - "-p": path to directory with the complete json files
 - "-o": path to output directory

```
usage: ihec_json_noinput.py [-h] [-p PATH] [-o OUT]

A script to write a ihec json input file withou input samples from a complete
ihec input_json_file (IPs and INPUTs samples) The informations in chip.title
and chip.descripton will be updated as well.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  root path to directory with the complete json files
                        (IPs and INPUTs
  -o OUT, --out OUT     root path to directory to store the output files
                        (json_noinput).
```

### md5-gsm-dict.py

Script to create a dictionary where the key is the md5sum corresponding to the EpiATLAS sample, and the value is the EGAR+bigwig extension (pval, fc, raw or ctl-raw).

```
python md5-gsm-dict.py <path_to_epiatlas.json>
```


### epirr_finder.py
Script to looking for the if the 'registry_id' key (which stores the EpiRR information) exist in other keys stored in the dataset_name (missing_json created from the ihec and final_json - hg19-release 2019-11). This scripts returns a dictionary where the keys are the keys names from dataset_name and the value is the counter of registry_id matches).

```
python epirr_finder.py <path_to_missingds.json>
```

### get_dataset_md5_jsons.py

Script to find dataset names from a list of md5sum generated from a specific IHEC/Final assembly-release json files (i.e hg38-2019-11_final.json). From the dataset names list the program will check if there is an overlap with the another json file (from another assembly; i.e hg19). This list of md5sum will be returned in a txt file.
To run this program you should pass the first json file (i.e hg38_final.json), a list of md5sum filtered from this json, and the another json file to check if there is an overlap. 

```
python get_dataset_md5_jsons.py -p hg38_2019-11_final.json -l list_md5_hg38.txt -d hg19_2019-11_final.json 
```

 ```
 usage: get_dataset_md5_jsons.py [-h] [-p PATH] [-l LIST] [-d DEST]

A script to find in a first moment the dataset name related to a list of
md5sum obtained from a specific assembly/release of IHEC/final json files
(project related with EpiLap).The list of dataset names will be used to
recover the md5sum information in the json files from another assembly/release
(using the final json file)This script returns a txt file with the md5sum
information from the second assembly release

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  root path to the final json (for instance
                        hg38-2019-11_final.json) to get the dataset name from
                        a list of md5sum
  -l LIST, --list LIST  root path to a list of md5sum obtained from one
                        IHEC/final assembly-release json. For instance: list
                        of md5sum from hg38.
  -d DEST, --dest DEST  root path to the final json (for instance hg19) to
                        check if the dataset names from hg38 exist
 ```
