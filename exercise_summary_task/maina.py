import sys

from config.config import Config
from file_processor import Processor
from employee_report_service import EmployeeReportService
def main():
    config=Config("exercise_summary_task/config/properties.json")
#conf=Config(sys.argv[1])
    processor=Processor(config)
    empService=EmployeeReportService(processor)
    empService.generate_top_10_employees_report()
    empService.generate_average_salary_per_department_report()
    empService.generate_managers_subordinates_report()

if __name__=="__main__":

    main()
