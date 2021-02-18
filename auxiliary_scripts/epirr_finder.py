import sys
import json 

'''Script to find an specific information using the missing_dsname.json (created from IHEC_hg19_2019-11.json form epigeec_ihec project dir)
The specific information (["dataset_name"]]["experiment_attributes"]["reference_registry_id"]) should be inserted in the experiment_attributes key (which is a value associated 
with the dataset_name. This script will check if the ["reference_registry_id"] is inserted in the other keys from dataset_name and print a counter
(number of matchs).'''

file_n = sys.argv[1] #missing json (dataset_names as value of datasets; and dataset_name has other keys)


keys_dict ={
    'sample_id': 0,
    'ihec_data_portal' : 0, 
    'analysis_attributes': 0, 
    'other_attributes' : 0, 
    'browser' : 0
}

with open(file_n) as f:
    hg = json.load(f) #just one key = datasets 


    for i in hg['datasets'].keys():  #each key is a sample
        # print(hg['datasets'][i]['ihec_data_portal']['releasing_group'])
       
        for elem in hg['datasets'][i].keys(): #each key associated with each samples (i.e ihec_data_portal, sample_id, analysis_attributes)

            for k in keys_dict.keys():
                if elem == k:
                    if 'reference_registry_id' in hg['datasets'][i][elem]:
                        keys_dict[k] += 1
                    
                
print(keys_dict)        
             


