"""Test module for simple functions"""
import os
import unittest
import pandas as pd
from file_funcs.file_functions import load_env_from_json, read_from_json, read_from_csv,write_to_parquet
class TestLoadEnvFromJson(unittest.TestCase):

    """Unit Test function load_env_from_json
    Test reading panda dataframe from a file
    Test writing a dataframe to a parquet file"""
    file_name_json_config="test_file.json"
    filepath_json_config="../recap/exercise_summary_task/unit_tests/target/test_file.json"
    full_file_path_json="../recap/exercise_summary_task/unit_tests/source/employees.json"
    file_path_json="../recap/exercise_summary_task/unit_tests/source/"
    file_name_json="employees.json"
    file_path_csv="../recap/exercise_summary_task/unit_tests/source/"
    employee_csv_file_name="employees_positions.csv"
    employee_csv_full_file_path="../recap/exercise_summary_task/unit_tests/source/employees_positions.csv"
    file_path_parquet_read="../recap/exercise_summary_task/unit_tests/source/top3.parquet"
    file_target_dir="../recap/exercise_summary_task/unit_tests/target/"
    file_name_parquet="timestamp_top3"

    def setUp(self):
        self.set_up_test_config_file_json()

    def tearDown(self) -> None:
        self.tear_down_after_tests()

    def test_load_env_from_json_with_file_name(self):
        """Tests correct reading of variables through the function"""
        out_dict=load_env_from_json(self.file_target_dir,self.file_name_json_config)
        main_directory=out_dict["directories"]["mainDirectory"]
        input_directory=out_dict["directories"]["inputDirectory"]
        temp_directory=out_dict["directories"]["tempDirectory"]
        output_directory=out_dict["directories"]["outputDirectory"]
        input_file_name1=out_dict["reportInformation"]["files"]["input"]["fileName1"]
        input_file_name2=out_dict["reportInformation"]["files"]["input"]["fileName2"]
        input_file_name3=out_dict["reportInformation"]["files"]["input"]["fileName3"]


        self.assertEqual(main_directory,"main","Incorrect read for mainDirectory")
        self.assertEqual(input_directory,"input","Incorrect read for inputDirectory")
        self.assertEqual(temp_directory,"temp","Incorrect read for tempDirectory")
        self.assertEqual(output_directory,"output","Incorrect read for outputDirectory")
        self.assertEqual(input_file_name1,"file1.json","Incorrect read for fileName1")
        self.assertEqual(input_file_name2,"file2.csv","Incorrect read for fileName2")
        self.assertEqual(input_file_name3,"file3.txt","Incorrect read for fileName3")

    def test_load_env_from_json_without_file_name(self):
        """Tests correct reading of variables through the function"""
        out_dict=load_env_from_json(self.filepath_json_config)
        main_directory=out_dict["directories"]["mainDirectory"]
        input_directory=out_dict["directories"]["inputDirectory"]
        temp_directory=out_dict["directories"]["tempDirectory"]
        output_directory=out_dict["directories"]["outputDirectory"]
        input_file_name1=out_dict["reportInformation"]["files"]["input"]["fileName1"]
        input_file_name2=out_dict["reportInformation"]["files"]["input"]["fileName2"]
        input_file_name3=out_dict["reportInformation"]["files"]["input"]["fileName3"]


        self.assertEqual(main_directory,"main","Incorrect read for mainDirectory")
        self.assertEqual(input_directory,"input","Incorrect read for inputDirectory")
        self.assertEqual(temp_directory,"temp","Incorrect read for tempDirectory")
        self.assertEqual(output_directory,"output","Incorrect read for outputDirectory")
        self.assertEqual(input_file_name1,"file1.json","Incorrect read for fileName1")
        self.assertEqual(input_file_name2,"file2.csv","Incorrect read for fileName2")
        self.assertEqual(input_file_name3,"file3.txt","Incorrect read for fileName3")

    def test_read_df_from_csv_with_file_name(self):
        """Tests native reading of CSV file into dataframe 
        against pandas reading dataframe from CSV"""

        native_frame=pd.read_csv(self.employee_csv_full_file_path)
        source_frame=read_from_csv(self.file_path_csv,self.employee_csv_file_name)

        pd.testing.assert_frame_equal(native_frame,source_frame)

    def test_read_df_from_csv_without_file_name(self):
        """Tests native reading of CSV file into dataframe 
        against pandas reading dataframe from CSV"""

        native_frame=pd.read_csv(self.employee_csv_full_file_path)
        source_frame=read_from_csv(self.employee_csv_full_file_path)

        pd.testing.assert_frame_equal(native_frame,source_frame)

    def test_read_df_from_json_without_file_name(self):
        """Tests native reading of JSOn file into dataframe 
        against pandas reading dataframe from JSON"""
        native_frame=pd.read_json(self.full_file_path_json)
        source_frame=read_from_json(self.full_file_path_json)

        pd.testing.assert_frame_equal(native_frame,source_frame)

    def test_read_df_from_json_with_file_name(self):
        """Tests native reading of JSOn file into dataframe 
        against pandas reading dataframe from JSON"""
        native_frame=pd.read_json(self.full_file_path_json)
        source_frame=read_from_json(self.file_path_json,self.file_name_json)

        pd.testing.assert_frame_equal(native_frame,source_frame)

    def test_write_to_parquet(self):
        """Test writing a dataframe to a parquet file"""
        df1=pd.read_parquet(self.file_path_parquet_read)
        file_name=write_to_parquet(df1,self.file_target_dir,self.file_name_parquet)+".parquet"
        df2=pd.read_parquet(self.file_target_dir+file_name)
        pd.testing.assert_frame_equal(df1,df2)

        file_name2=write_to_parquet(df1,self.file_target_dir)+".parquet"
        df3=pd.read_parquet(self.file_target_dir+file_name2)
        pd.testing.assert_frame_equal(df1,df3)

    def tear_down_after_tests(self):
        """Cleanup generated files during testing"""

        for file_name in os.listdir(self.file_target_dir):
            if file_name.endswith(".parquet") or file_name.endswith(".json"):
                os.remove(self.file_target_dir+file_name)

    def set_up_test_config_file_json(self):
        """Set up json to be used for importing and testing"""
        with open(self.filepath_json_config,"w",encoding="utf-8") as file:
            file.write("""
    {
    "directories": {
        "mainDirectory": "main",
        "inputDirectory": "input",
        "tempDirectory": "temp",
        "outputDirectory": "output"
    },
    "reportInformation": {
        "files": {
            "input": {
                "fileName1": "file1.json",
                "fileName2": "file2.csv",
                "fileName3": "file3.txt"
            },
            "output": {
                "output1": "timestamp_1"
            }
        }
    }
}""")
            file.close()

if __name__=="__main__":

    unittest.main()
