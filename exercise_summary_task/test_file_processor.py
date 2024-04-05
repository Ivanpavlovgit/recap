"""Test module for file_processor"""
import os
import unittest
import pandas as pd
from unittest.mock import patch,Mock
from config.employees_config import EmployeesConfig
from file_funcs.file_functions import read_from_csv,read_from_json,write_to_parquet
from FileProcessors.employees_file_processor import EmployeeFileProcessor

class TestEmployeeFileProcessor(unittest.TestCase):
    """Used for testitng functions of employee file processor"""
    #@patch.object(EmployeesConfig,"test_file_to_df")
    def test_EmployeeFileProcessor_file_to_df(self):

        with patch('config.employees_config.EmployeesConfig') as mock_config1:

                mock_config1.get_input_directory.return_value =(
                "../recap/exercise_summary_task/unit_tests/source/")

                test_processor=EmployeeFileProcessor(mock_config1)

                df_json_1=test_processor.file_to_df("employees.json")
                dir_json=test_processor.get_conf().get_input_directory()+"employees.json"
                df_json_2=pd.read_json(dir_json)

                pd.testing.assert_frame_equal(df_json_1,df_json_2)

                df_csv_1=test_processor.file_to_df("employees_positions.csv")
                dir_csv=test_processor.get_conf().get_input_directory()+"employees_positions.csv"
                df_csv_2=pd.read_csv(dir_csv)

                pd.testing.assert_frame_equal(df_csv_1,df_csv_2)

    def test_EmployeeFileProcessor_write_to_parquetf(self):
        with patch('config.employees_config.EmployeesConfig') as mock_config1:
            mock_config1.get_output_directory.return_value =(
                "../recap/exercise_summary_task/unit_tests/target/")
            test_processor=EmployeeFileProcessor(mock_config1)
            test_data={'col1': [1, 2], 'col2': [3, 4]}
            test_df=pd.DataFrame(data=test_data)
            test_processor.df_to_parquet(test_df,"test_write_to_parquet")
               
            imported_df=pd.read_parquet(test_processor.get_conf().get_output_directory()+"test_write_to_parquet.parquet")
            
            pd.testing.assert_frame_equal(test_df,imported_df)
 
if __name__=="__main__":
    unittest.main()
