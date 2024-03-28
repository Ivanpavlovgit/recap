import sys

from config.employees_config import EmployeesConfig
from FileProcessors.employees_file_processor import EmployeeFileProcessor
from ReportServices.employee_report_service import EmployeeReportService


def main():
    """App main logic"""
    config=EmployeesConfig("exercise_summary_task/config/properties.json")
    #conf=Config(sys.argv[1])
    processor=EmployeeFileProcessor(config)
    emp_service=EmployeeReportService(processor)
    emp_service.generate_top_10_employees_report()
    emp_service.generate_average_salary_per_department_report()
    emp_service.generate_managers_subordinates_report()

if __name__=="__main__":

    main()
