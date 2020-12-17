
import sys
import json
import csv


'''Script to rename the EpiAtlas files (named with the md5sum). This script receives a json metadata file
with the information of md5sum (file_name key), target (key), GSM (key), typeBW (key). It will return a
file csv file with the md5sum and the new name (md5sum + pval (or fc or raw or ctl-raw))'''


file_n = sys.argv[1] #json file with the information described above (this json was generated from the total json used by epigeec annotate)


with open(file_n) as f:
    big_dict = json.load(f) #just one key = datasets (json epigeec) 
   

#print big_dict['datasets']
#print big_dict['datasets'][0].keys() #here you can access the keys of each dict inserted into the list 
#print big_dict['datasets'][0].values() #here you can access the values for each keys for each dict into the list 

map_dict = {}
for ele in big_dict['datasets']:
    
    if 'INPUT' in ele['target']:

        
        suffix = ele['GSM'] + '.' + 'ctl-raw'
        map_dict[ele['file_name']] = suffix

    elif 'raw' in ele['typeBW'] and ele['target'] != 'INPUT':

       
        suffix_IP_raw = ele['GSM'] + '.' + 'raw'
        map_dict[ele['file_name']] = suffix_IP_raw
        
    else:

        suffix_IP = ele['GSM'] + '.' + ele['typeBW'].split('-')[1] + '-cctrl'
        map_dict[ele['file_name']] = suffix_IP
        
#print(len(map_dict)) # checking the length - correct 


output = csv.writer(open("output-epiatlas-mapped-name.csv", "w"))

for key, val in map_dict.items():
    
    output.writerow([key, val])

print('File saved with sucess')
      
