"""Test module for EmployeeReportService"""
import os
import unittest
from unittest.mock import Mock
import pandas as pd
from config.employees_config import EmployeesConfig
from FileProcessors.employees_file_processor import EmployeeFileProcessor
from ReportServices.employee_report_service import EmployeeReportService
#@patch.object(EmployeesConfig,"get_input_directory","../recap/exercise_summary_task/unit_tests/source/")
class TestEmployeeReportService(unittest.TestCase):
    """Test class for employee report service"""

    def setUp(self):
        self.set_up_test_employee_report_serive()

    def set_up_test_employee_report_serive(self):
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
        self.test_rep_service=EmployeeReportService(self.mock_processor)

    def tearDown(self):
        self.tear_down_after_tests()

    def tear_down_after_tests(self):
        """Cleanup generated files during testing"""

        for file_name in os.listdir(self.mock_conf.get_output_directory()):
            if file_name.endswith(".parquet") or file_name.endswith(".json"):
                os.remove(self.mock_conf.get_output_directory() + file_name)

    def test_join_dataframes(self):
        """Test creation of joined dataframes
         1. employees dataframe
         2. employees positions
         3. employees salaries"""

        test_joined_df=self.test_rep_service.join_dataframes()
        orig_joined_df=pd.read_parquet(self.mock_conf.get_input_directory() + "joined.parquet")

        pd.testing.assert_frame_equal(test_joined_df, orig_joined_df)

    def test_employees_df(self):
        """Test creation of employees dataframe"""

        test_emps=self.test_rep_service.employees_df()
        orig_emps=pd.read_json(self.mock_conf.get_input_directory() + self.mock_conf.get_employees_filename())

        pd.testing.assert_frame_equal(test_emps, orig_emps)

    def test_employees_salary_df(self):
        """Test creation of employees positions salary"""

        test_emps=self.test_rep_service.employees_salary_df()

        orig_emps=pd.read_json(self.mock_conf.get_input_directory() + self.mock_conf.get_employees_salaries_filename())
        orig_emps["monthly_salary"] = orig_emps["salary"]/12

        pd.testing.assert_frame_equal(test_emps, orig_emps)

    def test_employees_positons_df(self):
        """Test creation of employees positions dataframe"""

        test_positions=self.test_rep_service.employees_positons_df()

        orig_positions=pd.read_csv(self.mock_conf.get_input_directory() + self.mock_conf.get_employees_positions_filename())
        pd.testing.assert_frame_equal(test_positions, orig_positions)

    def test_generate_top_10_employees_report(self):
        """Tests generated report agains a local file"""

        test_top10_df=self.test_rep_service.generate_top_10_employees_report()
        orig_top10_df=pd.read_parquet(self.mock_conf.get_input_directory() + "top3.parquet")

        pd.testing.assert_frame_equal(test_top10_df, orig_top10_df)

    def test_generate_average_salary_per_department_report(self):
        """Tests generated report agains a local file"""

        test_avg_sal_dept_df=self.test_rep_service.generate_average_salary_per_department_report()
        orig_avg_sal_dept_df=pd.read_parquet(self.mock_conf.get_input_directory() + "avg_sal_dept.parquet")

        pd.testing.assert_frame_equal(test_avg_sal_dept_df, orig_avg_sal_dept_df)

    def test_generate_managers_subordinates_report(self):
        """Tests generated report agains a local file"""

        test_mngr_subs_df=self.test_rep_service.generate_managers_subordinates_report()
        orig_mngr_subs_dept_df=pd.read_parquet(self.mock_conf.get_input_directory() + "manager_employees.parquet")

        pd.testing.assert_frame_equal(test_mngr_subs_df, orig_mngr_subs_dept_df)

if __name__=="__main__":
    unittest.main()
