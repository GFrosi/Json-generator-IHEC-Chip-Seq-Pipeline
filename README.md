# Json-generator-IHEC-Chip-Seq-Pipeline

This script generate a json Input file (single and pairend) to IHEC Chip-Seq Pipeline from a dataframe with IPs and INPUT samples and SRR ids information.

##You should first create a table (dataframe) with the follow informations:

|GSM | SRX | SRR | Categories|
|-----------|:-----------:|:--------:|------------|
|GSM2801176 | SRX3236723 | SRR6124070 | Trait|
|GSM2801187 | SRX3236734 | SRR6124081 | Trait|
|GSM1415874 | SRX610759 | SRR1425172 | Trait|
GSM1565791 | SRX818183 | SRR1725759,SRR1725760 | Trait|


###Command line
1.python gsm_seq.py -t ../gsm-srr-srx-categories.csv -p srr/
  - "-t": dataframe as exemplified above
  - "-p": root path to SRR samples download from NCBI, for instance. This directory will be read to identify if each IP/Input samples has just SRR_1 (SE) or SRR_1 and SRR_2 (PE)
  - This comand will return a dataframe with the SE/PE information per sample. 

2.python chipseq_json_generator.py -t ../gsm-srr-srx-categories.csv -c config/json_config.ini -s data/seq_type.csv -p chip "-t": dataframe as exemplified above
 
