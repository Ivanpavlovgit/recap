import pandas as pd
from Interfaces.file_processor import FileProcessor
from Interfaces.configuration import Configuration
from Functions.file_functions import read_from_csv,read_from_json,write_to_parquet

class EmployeeFileProcessor(FileProcessor):
    """Class is used to read files into panda dataframe and write panda dataframes to file"""
    def __init__(self,conf:Configuration):
        self.conf=conf

    def get_conf(self):
        return self.conf

    def file_to_df(self,file_name:str)->pd.DataFrame:
        """Function returns a panda Dataframe from a csv or json file
        specified in the properties.json input directory"""

        assert file_name[-5:]==".json" or file_name[-4:]==".csv","File is not of accepted format (json or csv)"

        if file_name[-5:]==".json":
            return read_from_json(self.conf.get_input_directory(), file_name)

        return read_from_csv(self.conf.get_input_directory(), file_name)

    def df_to_parquet(self,df:pd.DataFrame,file_name:str=None):
        """Function writes panda Dataframe to a parquet file in the output directory
        specified in the properties.json file"""
        write_to_parquet(df,self.conf.get_output_directory(),file_name)
