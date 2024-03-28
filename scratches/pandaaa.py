import pandas as pd
import pandasql as ps
#init vars
#main_directory="C:\\Users\\Ivan.Pavlov2\\OneDrive - Adastra, s.r.o\\Python course\\Recap taks\\exercise_summary_task"
main_directory="."
emp_data_filename= "employees.json"
emp_positions_filename= "employees_positions.csv"
emp_salaries_filename= "employees_salaries.json"
#read data from files
emp_data=pd.read_json(main_directory+"\\"+emp_data_filename)
emp_sal=pd.read_json(main_directory+"\\"+emp_salaries_filename)
emp_positions=pd.read_csv(main_directory+"\\"+emp_positions_filename)
print (emp_sal)
emp_join=emp_data.join(emp_sal,how="left",on="employee_id",rsuffix="_r").join(emp_positions,how="outer",on="employee_id",rsuffix="_rr")
#.drop(columns="employee_id_r",inplace=False)
#emp_join.drop(columns="employee_id_r",inplace=True)
print(emp_join)
#print (emp_data)
#print (emp_positions)
#emp_sal["monthly_salary"]=emp_sal["salary"]/12
#emp_sal_final=emp_sal.drop(columns="salary",inplace=False)
##print(emp_sal_final)
#
#emp_joined_data=(emp_data
#        .set_index("employee_id")
#        .join(emp_positions.set_index("employee_id"))
#        .join(emp_sal_final.set_index("employee_id")))
#
#print(emp_joined_data)
#
##top_10_employees=emp_joined_data.sort_values(by='monthly_salary').iloc[:10].
#top_3_employees=emp_joined_data.sort_values(by='monthly_salary',ascending=False).iloc[:3]
##print(top_3_employees)
##avarage salary per department
##avg_sal_per_dept=emp_joined_data.drop(columns="name")
##make a new frame... dont need posisions here
#avg_sal_per_dept=emp_joined_data.reset_index(drop=True).drop(columns=["name","manager_id","position"]).groupby("department").mean("monthly_salary")
#print(avg_sal_per_dept)
##avg_sal_per_dept=emp_joined_data.drop(columns=[emp_joined_data.columns[0]],inplace=False)
#
##print(avg_sal_per_dept)
##list of managers and employees under their supervision
#people = emp_data.to_records()
#person = people[0]
#
#
#sql_m="SELECT e.employee_id,e.name,e.manager_id,m.name as MANAGER from emp_data e JOIN emp_data m where e.manager_id=m.employee_id"
#print (sql_m)
#print(ps.sqldf(sql_m))
##print (people)
##print (person.name)
#