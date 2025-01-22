import pandas as pd
import os
import glob
import pyarrow
from loguru import logger
from log_utils import log_decorator



"""
    ETL PROCESS
"""


# Extrating Data
@log_decorator
def extract_data(path_json_files:str) -> pd.DataFrame:
    json_files = glob.glob(os.path.join(path_json_files,'*.json'))
    
    # Reading each json file found; create a list of df
    df_list = [pd.read_json(arquivo) for arquivo in json_files]

    # Create a DF with the list content
    df_total = pd.concat(df_list,ignore_index=True)

    return df_total
 
# Transforming data
@log_decorator
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df["total"] = df["Quantidade"] * df["Venda"]
    return df


# Loading data
@log_decorator
def load_data(df: pd.DataFrame, load_format: str):
    if load_format == "csv":
        df.to_csv("data/exported/extracted_data.csv")
    
    if load_format == "parquet":
        df.to_parquet("data/exported/extracted_data.parquet")
    
    else:
        print("Please verify if the df exist and you choose csv or parquet formats")



"""
    EXECUTING ETL
"""
if __name__ == '__main__':
    df_transfomed = transform_data(extract_data("data/import"))    
    load_data(df_transfomed, 'parquet')
    print(df_transfomed)
