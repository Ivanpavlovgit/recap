"""Module contains fuctions generating reports based on the employees dataframe"""
import pandas as pd
import pandasql as ps
from datetime import datetime
import exercise_summary_task.Functions.file_functions as file_functions

#file_path="./"
#file_name="properties.json"
env_var=file_functions.load_env_from_json("./exercise_summary_task/","properties.json")
input_directory=env_var["directories"]["inputDirectory"]
ouput_directory=env_var["directories"]["outputDirectory"]

employees_filename=env_var["employees"]["files"]["input"]["empDataFilename"]
employees_positions_filename=env_var["employees"]["files"]["input"]["empPositionsFilename"]
employees_salaries_filename=env_var["employees"]["files"]["input"]["empSalariesFilename"]

query_top3_employee=env_var["employees"]["queries"]["top3_employees"]
query_avg_sal_dept=env_var["employees"]["queries"]["avg_sal_dept"]
query_manager_employees=env_var["employees"]["queries"]["manager_employees"]

dt=datetime.now().strftime("%d%m%Y%H%M%S")

top3_employees_report_filename=env_var["employees"]["files"]["output"]["top3_employees_report"].replace("timestamp",dt)
avg_sal_dept_report_filename=env_var["employees"]["files"]["output"]["avg_sal_dept_report"].replace("timestamp",dt)
mngr_employees_report_filename=env_var["employees"]["files"]["output"]["manager_employees_report"].replace("timestamp",dt)

def join_employees_dataframes(
        employees:pd.DataFrame,
        employees_salaries:pd.DataFrame
        ,employees_positions:pd.DataFrame)->pd.DataFrame:
    "Functions joins the thee employees dataframes on employee_id column"
    employees_salaries.set_index("employee_id",inplace=True)
    employees_positions.set_index("employee_id",inplace=True)

#Ei toq prekrasen DF shte go analizirame za reportite
    return (
        employees
        .join(employees_positions,on="employee_id")
        .join(employees_salaries,on="employee_id"))



def top3_employees()->pd.DataFrame:
    employees_df=join_employees_dataframes(
    file_functions.read_from_json(input_directory,employees_filename),
    file_functions.read_from_csv(input_directory,employees_positions_filename),
    file_functions.read_from_json(input_directory,employees_salaries_filename)
    )
    output=ps.sqldf(query_top3_employee)
    file_functions.write_to_parquet(output,ouput_directory,top3_employees_report_filename)
    return output

def avg_sal_dept()->pd.DataFrame:
    employees_df=join_employees_dataframes(
    file_functions.read_from_json(input_directory,employees_filename),
    file_functions.read_from_csv(input_directory,employees_positions_filename),
    file_functions.read_from_json(input_directory,employees_salaries_filename)
    )
    avg_sal=ps.sqldf(query_avg_sal_dept)
    file_functions.write_to_parquet(avg_sal,ouput_directory,avg_sal_dept_report_filename)
    return avg_sal

def manager_employees()->pd.DataFrame:
    employees_df=join_employees_dataframes(
    file_functions.read_from_json(input_directory,employees_filename),
    file_functions.read_from_csv(input_directory,employees_positions_filename),
    file_functions.read_from_json(input_directory,employees_salaries_filename)
    )
    mngr_employees=ps.sqldf(query_manager_employees)
    file_functions.write_to_parquet(mngr_employees,ouput_directory,mngr_employees_report_filename)
    return mngr_employees
