import os
import unittest
from Functions.file_functions import load_env_from_json

#Unit Test function load_env_from_json
class TestLoadEnvFromJson(unittest.TestCase):
    def setUp(self):
        self.setUpTestConfigFileJson()
    def tearDown(self):
        self.tearDownAfterTtests()

    def test_load_env_from_json_happy_path(self,):
        """Tests correct reading of variables through the function"""
        out_dict=load_env_from_json("exercise_summary_task/test_file.json")

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
        
    def tearDownAfterTtests(self):
        filepath="exercise_summary_task/test_file.json"
        os.remove(filepath)
    def setUpTestConfigFileJson(self):
        filepath="exercise_summary_task/test_file.json"
        with open(filepath,"w",encoding="utf-8") as file:
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
if __name__=="__main__":

    unittest.main()
