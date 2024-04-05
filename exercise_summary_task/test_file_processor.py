"""Test module for file_processor"""
import os
import unittest
from unittest.mock import Mock
import pandas as pd
from config.employees_config import EmployeesConfig
from FileProcessors.employees_file_processor import EmployeeFileProcessor

class TestEmployeeFileProcessor(unittest.TestCase):
    """Used for testitng functions of employee file processor"""

    #@patch.object(EmployeesConfig,"test_file_to_df")
    def setUp(self):
        self.set_up_test_employee_file_processor()

    def set_up_test_employee_file_processor(self):
        """Setup with mocking config for the unittest case"""
        
        self.mock_conf=Mock(EmployeesConfig)
        self.mock_conf.get_input_directory.return_value = (
                    "../recap/exercise_summary_task/unit_tests/source/")
        self.mock_conf.get_output_directory.return_value = (
            "../recap/exercise_summary_task/unit_tests/target/")
        self.mock_conf.get_employees_filename.return_value = "employees.json"
        self.mock_conf.get_employees_positions_filename.return_value = "employees_positions.csv"
        self.mock_conf.get_employees_salaries_filename.return_value = "employees_salaries.json"
        self.mock_conf.get_top3_employees_report_filename.return_value = "timestamp_top3"
        self.mock_conf.get_avg_sal_dept_report_filename.return_value = "timestamp_avg_sal_dept"
        self.mock_conf.get_mngr_employees_report_filename.return_value = "timestamp_manager_employees"

        #test_processor=Mock(EmployeeFileProcessor)
        #self.test_processor=test_processor(self.mock_conf)
        self.mock_processor=EmployeeFileProcessor(self.mock_conf)
        #self.test_rep_service=EmployeeReportService(self.mock_processor)

    def tearDown(self):
        self.tear_down_after_tests()

    def tear_down_after_tests(self):
        """Cleanup generated files during testing"""

        for file_name in os.listdir(self.mock_conf.get_output_directory()):
            if file_name.endswith(".parquet") or file_name.endswith(".json"):
                os.remove(self.mock_conf.get_output_directory() + file_name)

    def test_employees_file_processor_file_to_df(self):
        """Testing file to dataframe method with json and csv files"""

        df_json_1=self.mock_processor.file_to_df(self.mock_conf.get_employees_filename())
        dir_json=self.mock_processor.get_conf().get_input_directory() + self.mock_conf.get_employees_filename()
        df_json_2=pd.read_json(dir_json)

        pd.testing.assert_frame_equal(df_json_1, df_json_2)

        df_csv_1=self.mock_processor.file_to_df(self.mock_conf.get_employees_positions_filename())
        dir_csv=self.mock_processor.get_conf().get_input_directory() + self.mock_conf.get_employees_positions_filename()
        df_csv_2=pd.read_csv(dir_csv)

        pd.testing.assert_frame_equal(df_csv_1, df_csv_2)

    def test_employee_file_processor_write_to_parquetf(self):
        """Testing writi a dataframe to a parquet file"""

        #test_processor=EmployeeFileProcessor(mock_config1)
        test_data={'col1': [1, 2], 'col2': [3, 4]}
        test_df=pd.DataFrame(data=test_data)
        self.mock_processor.df_to_parquet(test_df, "test_write_to_parquet")

        imported_df=pd.read_parquet(self.mock_processor.get_conf().get_output_directory() + "test_write_to_parquet.parquet")

        pd.testing.assert_frame_equal(test_df, imported_df)

if __name__=="__main__":
    unittest.main()
