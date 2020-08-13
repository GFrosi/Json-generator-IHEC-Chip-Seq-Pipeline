
'''Function to create a config dictionary with the basic information for INPUT json.file
You shold to use the json_config.ini and adjust the parameter values, as well as the absolute path 
to genome table, title name, description, chip_control_pooled'''

def read_config(file_name):
    config = {}

    with open(file_name,'r') as file:
        for line in file:
            
            k,v = line.strip().split('=')
            config[k] = v
    
    return config
