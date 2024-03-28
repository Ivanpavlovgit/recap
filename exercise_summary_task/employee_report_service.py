import pandas as pd
import pandasql as ps
from file_processor import Processor

class EmployeeReportService:
    """Class generates reports based on the employee data
        contained in the files in the input files"""
    def __init__(self,
                processor:Processor):
        self.processor=processor

    def join_dataframes(self)->pd.DataFrame:
        """Functions joins the thee employees
           employees_df, employees_salary_df, employees_positons_df
           dataframes on employee_id column"""

        employees_df=self.employees_df()
        employees_salary_df=self.employees_salary_df().set_index("employee_id",inplace=False)
        employees_positons_df=self.employees_positons_df().set_index("employee_id",inplace=False)

        return (
            employees_df
            .join(employees_salary_df,on="employee_id")
            .join(employees_positons_df,on="employee_id"))

    def employees_df(self)->pd.DataFrame:
        """Returns employees Dataframe with columns :
          'employee_id', 'name', 'department', 'manager_id'"""
        return self.processor.file_to_df(self.processor.get_conf().get_employees_filename())

    def employees_salary_df(self)->pd.DataFrame:
        """Returns employees_salaries Dataframe with columns :
          'employee_id', 'salary'"""
        return  self.processor.file_to_df(self.processor.get_conf().get_employees_salaries_filename())

    def employees_positons_df(self)->pd.DataFrame:
        """Returns employees_positions Dataframe with columns :
          'employee_id', 'position'"""
        return self.processor.file_to_df(self.processor.get_conf().get_employees_positions_filename())

    def generate_top_10_employees_report(self):
        """Function writes the top 10 employees in a parquet file in the output directory"""
        self.processor.df_to_parquet(
            self.join_dataframes().nlargest(n=3,columns="salary",keep="all"),
              self.processor.get_conf().get_top3_employees_report_filename())

    def generate_average_salary_per_department_report(self):
        """Function wirtes a report for the average salary per department in a parquet file
          in the output directory"""
        self.processor.df_to_parquet(
            self.join_dataframes().drop(columns=["employee_id","name","manager_id","position"],inplace=False)
            .groupby("department").mean("salary"),
            self.processor.get_conf().get_avg_sal_dept_report_filename())

    def generate_managers_subordinates_report(self):
        """Function writes a list of the managers and their subordinate employees"""
        df=self.join_dataframes()
        query_manager_employees="""SELECT m.employee_id AS MNGR_employee_id,
                                    m.name as MNGR_name,
                                    m.department as df ,
                                    m.position as MNGR_postion,
                                    e.employee_id,e.name,
                                    e.department,
                                    e.position
                                    FROM df e
                                    JOIN df m 
                                    WHERE e.manager_id=m.employee_id
                                    ORDER BY m.department ASC"""
        self.processor.df_to_parquet(ps.sqldf(query_manager_employees),self.processor.get_conf().get_mngr_employees_report_filename())
