import pandas as pd
import pandasql as ps
import data_service

employees_filepath="./Input/employees.json"
#employees=pd.read_json(employees_filepath)
#print(employees)

employees=data_service.read_from_json("file_path","file_name")

employees_salaries_filepath="./Input/employees_salaries.json"
#employees_salaries=pd.read_json(employees_salaries_filepath)
#print(employees_salaries)

employees_salaries=data_service.read_from_json("file_path","file_name")

employees_positions_filepath="./Input/employees_positions.csv"
#employees_positions=pd.read_csv(employees_positions_filepath)
#print(employees_positions_filepath)

employees_position=data_service.read_from_json("file_path","file_name")

################################################

#Set fucking index
employees_salaries.set_index("employee_id",inplace=True)
employees_positions.set_index("employee_id",inplace=True)

#Ei toq shit shte go analizirame za reportite
employees_joined=(
    employees
    .join(employees_positions,on="employee_id")
    .join(employees_salaries,on="employee_id"))
#print(employees_joined)

##############################################
#топ 3 емплой по месечна заплата
query_top3_employee="""SELECT *,salary/12 as monthly_salary
                        FROM employees_joined 
                        ORDER BY monthly_salary DESC
                        LIMIT 3"""
top3_employees=ps.sqldf(query_top3_employee)

#print(top3_employees)

query_avg_sal_dept="""SELECT department,AVG(salary) from employees_joined GROUP BY department"""

avg_sal_dept=ps.sqldf(query_avg_sal_dept)

#print(avg_sal_dept)
############################################

#менажери и техните роби

query_manager_employees="""SELECT m.employee_id AS MNGR_employee_id,
                            m.name as MNGR_name,
                            m.department as MNGR_department ,
                            m.position as MNGR_postion,
                            e.employee_id,e.name,e.department,e.position 
                            FROM employees_joined e 
                            JOIN employees_joined m 
                            WHERE e.manager_id=m.employee_id 
                            ORDER BY m.department ASC"""

manager_employees=ps.sqldf(query_manager_employees)

print(manager_employees)
##############################################
#Write the shit to files
#imenata tuka brat e hubavo da imat %_timestamp
top3_employees.to_parquet("./Output/top3_employees.parquet")
avg_sal_dept.to_parquet("./Output/avg_sal_dept.parquet")
manager_employees.to_parquet("./Output/manager_employees.parquet")

print("done")
