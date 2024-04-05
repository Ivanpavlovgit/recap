import pandas as pd
from FileProcessors.employees_file_processor import EmployeeFileProcessor

class EmployeeReportService:
    """Class generates reports based on the employee data
        contained in the files in the input files"""
    def __init__(self,
                processor:EmployeeFileProcessor):
        self.processor=processor

    def join_dataframes(self)->pd.DataFrame:
        """Functions joins the three employees dataframes
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
          'employee_id', 'salary', 'monthly_salary'
          from file with columns 'employee_id', 'salary'"""
        emp_sal_df=self.processor.file_to_df(self.processor.get_conf().get_employees_salaries_filename())
        emp_sal_df["monthly_salary"]=emp_sal_df["salary"]/12
        return  emp_sal_df

    def employees_positons_df(self)->pd.DataFrame:
        """Returns employees_positions Dataframe with columns :
          'employee_id', 'position'"""
        return self.processor.file_to_df(self.processor.get_conf().get_employees_positions_filename())

    def generate_top_10_employees_report(self)->pd.DataFrame:
        """Function writes the top 10 employees in a parquet file in the output directory"""
        output=self.join_dataframes().nlargest(n=3,columns="salary",keep="all")
        self.processor.df_to_parquet(output,self.processor.get_conf().get_top3_employees_report_filename())
        return output.reset_index(drop=True)

    def generate_average_salary_per_department_report(self)->pd.DataFrame:
        """Function wirtes a report for the average salary per department in a parquet file
          in the output directory"""
        output=(self.join_dataframes()
            .drop(columns=["employee_id","name","manager_id","position"],inplace=False)
            .groupby("department").mean("salary"))
        self.processor.df_to_parquet(output,self.processor.get_conf().get_avg_sal_dept_report_filename())
        return output.reset_index(drop=True)

    def generate_managers_subordinates_report(self)->pd.DataFrame:
        """Function writes a list of the managers and their subordinate employees in the following steps:
        a) merge base joined dataframe with itsel on emplpoyee_id = manager_id
        b)sort by the managers name
        c)drop unneeded columns
        d)replace NaN values with 00000
        e)reformat employee_id collumns to int
        f)remove rows where there is no manager eg-> employee_id_x=00000
        g)rename columns for final report"""
        self_merged_right_employees_df=(
        self.join_dataframes()
        .merge(self.join_dataframes(), left_on=["employee_id"], right_on=["manager_id"], how="right")
        .sort_values("name_x")
        .drop(columns=["manager_id_x","salary_x","monthly_salary_x","salary_y","manager_id_y","monthly_salary_y"])
        .fillna(00000,inplace=False)
        .astype({"employee_id_x": 'int', "employee_id_y": 'int'}))

        self_merged_right_employees_df=self_merged_right_employees_df[self_merged_right_employees_df.employee_id_x != 00000]

        self_merged_right_employees_df=(
        self_merged_right_employees_df.rename(columns={"employee_id_x":"manager_id",
                           "name_x":"manager_name",
                           "department_x":"manager_department",
                           "position_x":"manager_position",
                           "employee_id_y":"employee_id",
                           "name_y":"employee_name",
                           "department_y":"employee_department",
                           "position_y":"employee_position"}
                           ))

        self.processor.df_to_parquet(
            (self_merged_right_employees_df),
            self.processor.get_conf().get_mngr_employees_report_filename())
        return self_merged_right_employees_df.reset_index(drop=True)
