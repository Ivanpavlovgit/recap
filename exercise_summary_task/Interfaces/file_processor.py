from abc import ABC,abstractmethod

class FileProcessor(ABC):
    """Interface for fileprocessor classes to handle reading dataframes from files
    and writing dataframe to files"""
    @abstractmethod
    def file_to_df(self,file_name):
        """Function to read a file into panda dataframe"""

    def df_to_parquet(self,df,file_name):
        """Function to write a panda dataframe to a parquet file"""
