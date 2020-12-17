import argparse
import os


def create_list_dir(root_path):

    '''Return a list of files stored in the respective directory passed by --path'''

    list_dir = os.listdir(root_path)
    return list_dir


def write_json(list_dir, root_path, out_dir):
    
    '''This function will write the json files without INPUT samples (chip.ctl_fastqs key). 
    In addition the chip.choose_ctl.always_use_pooled_ctl, chip.title, and chip.description
    will be updated (false, new_name_json and new_name_json_GEO, respectively) '''

    for input_json in list_dir:
        
        new_name_json = input_json.split('.')[0] + '_noinput' + '.json'
        
        input_data = os.path.join(root_path,input_json)
        
        output_data = os.path.join(out_dir, new_name_json)

        with open(output_data, 'w') as f:
            with open(input_data, 'r') as data_file:
                
                for line in data_file:
                    if 'chip.ctl_fastqs' in line:
                        continue
                    
                    if 'chip.choose_ctl.always_use_pooled_ctl' in line:

                        line = line.replace('true','false')
                    
                    if 'chip.title' in line:
                        line = line.replace(line, '')
                        line = '"chip.title"' + ':' + '"' + new_name_json + '"' + ',\n'

                    if 'chip.description' in line:
                        line = line.replace(line, '')
                        line = '"chip.description"' + ':' + '"' + new_name_json + '_GEO' + '"' + ',\n'
                    
                    
                    f.write(line)
                f.close()


def main():
    list_dir = create_list_dir(args.path)
    write_json(list_dir, args.path, args.out)
    print('The json files were wrote, DONE')


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description = 'A script to write a ihec json input file withou input samples from a complete ihec input_json_file (IPs and INPUTs samples) The informations in chip.title and chip.descripton will be updated as well.'
    )
    parser.add_argument('-p', '--path', action="store",
                        help='root path to directory with the complete json files (IPs and INPUTs')

    parser.add_argument('-o', '--out', action="store",
                        help='root path to directory to store the output files (json_noinput).')
    
    args = parser.parse_args()
    main()
