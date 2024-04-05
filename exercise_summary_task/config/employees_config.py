from Interfaces.configuration import Configuration
from file_funcs.file_functions import load_env_from_json
class EmployeesConfig(Configuration):
    def __init__(self, config_file:str):
        self.config_file=config_file
        self.env_var=self.setup_environment()
        self.input_directory=self.env_var["directories"]["inputDirectory"]
        self.output_directory=self.env_var["directories"]["outputDirectory"]
        self.employees_filename=self.env_var["employees"]["files"]["input"]["empDataFilename"]
        self.employees_positions_filename=self.env_var["employees"]["files"]["input"]["empPositionsFilename"]
        self.employees_salaries_filename=self.env_var["employees"]["files"]["input"]["empSalariesFilename"]
        self.top3_employees_report_filename=self.env_var["employees"]["files"]["output"]["top3_employees_report"]
        self.avg_sal_dept_report_filename=self.env_var["employees"]["files"]["output"]["avg_sal_dept_report"]
        self.mngr_employees_report_filename=self.env_var["employees"]["files"]["output"]["manager_employees_report"]

    def get_config_file(self):
        return self.config_file

    def set_config_file(self, value):
        self.config_file = value

    def get_env_var(self):
        return self.env_var

    def set_env_var(self, value):
        self.env_var = value

    def get_input_directory(self):
        return self.input_directory

    def set_input_directory(self, value):
        self.input_directory = value

    def get_output_directory(self):
        return self.output_directory

    def set_output_directory(self, value):
        self.output_directory = value

    def get_employees_filename(self):
        return self.employees_filename

    def set_employees_filename(self, value):
        self.employees_filename = value

    def get_employees_positions_filename(self):
        return self.employees_positions_filename

    def set_employees_positions_filename(self, value):
        self.employees_positions_filename = value

    def get_employees_salaries_filename(self):
        return self.employees_salaries_filename

    def set_employees_salaries_filename(self, value):
        self.employees_salaries_filename = value

    def get_query_top3_employee(self):
        return self.query_top3_employee

    def set_query_top3_employee(self, value):
        self.query_top3_employee = value

    def get_query_avg_sal_dept(self):
        return self.query_avg_sal_dept

    def set_query_avg_sal_dept(self, value):
        self.query_avg_sal_dept = value

    def get_query_manager_employees(self):
        return self.query_manager_employees

    def set_query_manager_employees(self, value):
        self.query_manager_employees = value

    def get_top3_employees_report_filename(self):
        return self.top3_employees_report_filename

    def set_top3_employees_report_filename(self, value):
        self.top3_employees_report_filename = value

    def get_avg_sal_dept_report_filename(self):
        return self.avg_sal_dept_report_filename

    def set_avg_sal_dept_report_filename(self, value):
        self.avg_sal_dept_report_filename = value

    def get_mngr_employees_report_filename(self):
        return self.mngr_employees_report_filename

    def set_mngr_employees_report_filename(self, value):
        self.mngr_employees_report_filename = value


    def setup_environment(self):
        return   load_env_from_json(self.config_file)
