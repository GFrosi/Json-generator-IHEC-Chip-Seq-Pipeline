import argparse
import json 



def open_json(file_n):

    '''load the json file to find the dataset names associated with each md5sum'''

    with open(file_n) as f:
        hg = json.load(f) #just one key = datasets 
        return hg
        #print hg['datasets'][0].keys()

        
#list to store the dataset name information related with the md5sum from hg38 (to check in hg19 final json)
list_hg38_dstname = []

def get_dsname(md5sum, hg):
    '''This function receives a list of md5sum and a json file (loaded before). It will return a 
    list of dataset names associated with each md5sum (if exist)'''

    for i in md5sum:

        md5 = i.strip()
        #print(md5)
    
        for ele in hg['datasets']:
            
            try:
            
                if ele['md5sum'] == md5:
                    #print(ele)
                
                    list_hg38_dstname.append(ele['dataset_name'])
                    #list_hg38_dstname_md5.append((ele['dataset_name'], md5))
                
            except KeyError as e:
                continue

    return list_hg38_dstname


#list to store the md5sum information from hg19 final json related with the dataset names from hg38 (overlap)
list_hg19_md5 = []
list_no_match = []

def get_md5(list_dsname, hg2):
    
    for i in list_dsname:

        dset = i.strip()
        # print(md5)
        
        for ele in hg2['datasets']:
            try:
                if ele['dataset_name'] == dset:
                    list_hg19_md5.append(ele['md5sum'])
                
                # if 'MS001101_H3K27me3' in ele['dataset_name']:
                #     print(ele)
            except: #KeyError as e:
                list_no_match.append(ele['dataset_name'])
                # continue

    return list_hg19_md5, list_no_match

def write_file(list_md5):

    '''write a txt file with the md5sum for all matched files from hg38 in hg19'''
    
    with open('output1_md5.txt', 'w') as f:
        f.write('\n'.join(list_md5))
    



def main():
    hg = open_json(args.path)
    md5sum = open(args.list, 'r')
    list_hg38_dstname = get_dsname(md5sum, hg)
    hg2 = open_json(args.dest)
    list_hg19_md5, list_no_match = get_md5(list_hg38_dstname, hg2)
    write_file(list_hg19_md5)
    #print(len(list_hg19_md5))
    #print(list_no_match)
    



if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(
        description = 'A script to find in a first moment the dataset name related to a list of md5sum obtained from a specific assembly/release of IHEC/final json files (project related with EpiLap).' 
        'The list of dataset names will be used to recover the md5sum information in the json files from another assembly/release (using the final json file)'
        'This script returns a txt file with the md5sum information from the second assembly release'
        )
    
    parser.add_argument('-p', '--path', action="store",
                        help='root path to the final json (for instance hg38-2019-11_final.json) to get the dataset name from a list of md5sum '
        )
    
    parser.add_argument('-l', '--list', action="store",
                        help='root path to a list of md5sum obtained from one IHEC/final assembly-release json. For instance: list of md5sum from hg38.'
        )
    
    parser.add_argument('-d', '--dest', action="store",
                        help='root path to the final json (for instance hg19) to check if the dataset names from hg38 exist'
        )
    
    args = parser.parse_args()
    main()


