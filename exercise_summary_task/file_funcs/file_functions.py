"""Module contains basic function to read/write DataFrame from/to file"""
import json
from datetime import datetime
import pandas as pd

def load_env_from_json(file_path:str, file_name:str=None):
    """Reads configuration JSON file and retuns dicitonary"""

    if file_name is None:
        with open(file_path, encoding="utf-8") as read_file:
            return json.load(read_file)
    else:
        with open(file_path + "/" + file_name, encoding="utf-8") as read_file:
            return json.load(read_file)

def read_from_json(file_path:str, file_name:str=None)->pd.DataFrame:
    """Function reads json file and returns it a dataframe format"""

    if file_name is None:
        return pd.read_json(file_path)
    return pd.read_json(file_path + "/" + file_name)

def read_from_csv(file_path:str, file_name:str=None)->pd.DataFrame:
    """Function reads csv file and returns it a dataframe format"""

    if file_name is None:
        return pd.read_csv(file_path)
    return pd.read_csv(file_path + "/" + file_name)

def write_to_parquet(data_frame:pd.DataFrame,file_path:str,file_name:str=None)->str:
    """Function writes dataframe to a parquet file with a timestamped name"""

    if file_name is not None:
        dt=datetime.now().strftime("%d%m%Y%H%M%S")
        time_stamped_filename=file_name.replace("timestamp", dt)
    else:
        time_stamped_filename=datetime.now().strftime("%d%m%Y%H%M%S")
    data_frame.to_parquet(f"{file_path}/{time_stamped_filename}.parquet", index=False)
    return time_stamped_filename
