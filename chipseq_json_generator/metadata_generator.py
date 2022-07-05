import pandas as pd
import numpy as np
import sys


def create_metadata_pipe(df, path_out):

    df['Category'] = np.where(df['Target-GEO'].str.lower() == 'input', 'Control', 'Target')
    df_final = df[['GSM', 'SRX', 'SRR', 'Category']]
    df_final.to_csv(path_out, index=False, sep='|')
    


def main():
    
    df_geo = pd.read_csv(sys.argv[1])
    path_out = sys.argv[2]
    create_metadata_pipe(df_geo, path_out)




if __name__ == "__main__":

    main()