#import data_service
##file_path="./"
##file_name="properties.json"
##env_var=data_service.load_env_from_json(file_path=file_path,file_name=file_name)
##input_directory=env_var["directories"]["inputDirectory"]
##ouput_directory=env_var["directories"]["outputDirectory"]
##
##employees_filename=env_var["employees"]["files"]["empDataFilename"]
##employees_positions_filename=env_var["employees"]["files"]["empPositionsFilename"]
##employees_salaries_filename=env_var["employees"]["files"]["empSalariesFilename"]
##
##
#
#env_var=data_service.load_env_from_json("./","properties.json")
#input_directory=env_var["directories"]["inputDirectory"]
#ouput_directory=env_var["directories"]["outputDirectory"]
#
#employees_filename=env_var["employees"]["files"]["input"]["empDataFilename"]
#employees_positions_filename=env_var["employees"]["files"]["input"]["empPositionsFilename"]
#employees_salaries_filename=env_var["employees"]["files"]["input"]["empSalariesFilename"]
#print(employees_filename)
#print(employees_positions_filename)
#print(employees_salaries_filename)
#print()
#query_top3_employee=env_var["employees"]["queries"]["top3_employees"]
#query_avg_sal_dept=env_var["employees"]["queries"]["avg_sal_dept"]
#query_manager_employees=env_var["employees"]["queries"]["manager_employees"]

import pandas as pd

df1=pd.read_json("employees.json")
df2=pd.read_csv("employees_positions.csv").set_index("employee_id",inplace=False)
df3=pd.read_json("employees_salaries.json").set_index("employee_id",inplace=False)
joined_df=df1.join(df2,on="employee_id",).join(df3,on="employee_id")
#print(joined_df)
#
#print(joined_df.sort_values("salary",ascending=False))
#print(joined_df.nlargest(n=3,columns="salary",keep="all"))
#print(joined_df)
#avg_dept=joined_df.drop(columns=["employee_id","name","manager_id","position"],inplace=False).groupby("department").mean("salary")
#print(avg_dept)

#print (avg_dept.groupby("department").mean("salary"))
print(joined_df)
#merged_df=joined_df.merge(right=joined_df,on="employee_id",suffixes=("_left","_right"))
#merged_df_left=joined_df.merge(joined_df, left_on=["employee_id"], right_on=["manager_id"],how="left")
#print (merged_df_left)
#merged_df_right=(
#    joined_df.merge(joined_df, left_on=["employee_id"], right_on=["manager_id"], how="right")
#    .sort_values("name_x")
#    .drop(columns=["manager_id_x","salary_x","salary_y","manager_id_y"]))
##merged_df_right = merged_df_right.astype({"employee_id_x": 'int', "manager_id_y": 'int'})
#merged_df_right.fillna(00000,inplace=True)
#merged_df_right = merged_df_right[merged_df_right.employee_id_x != 00000].astype({"employee_id_x": 'int', "employee_id_y": 'int'})
##merged_df_right = merged_df_right.astype({"employee_id_x": 'int', "manager_id_y": 'int'})
#print (merged_df_right)
#merged_df_right=(
#    merged_df_right.rename(columns={"employee_id_x":"manager_id",
#                           "name_x":"manager_name",
#                           "department_x":"manager_department",
#                           "position_x":"manager_position",
#                           "employee_id_y":"employee_id",
#                           "name_y":"employee_name",
#                           "department_y":"employee_department",
#                           "position_y":"employee_position"}
#                           ))
#print (merged_df_right)
#
#merged_df_right=(
#    joined_df.merge(joined_df, left_on=["employee_id"], right_on=["manager_id"], how="right")
#    .sort_values("name_x")
#    .drop(columns=["manager_id_x","salary_x","salary_y","manager_id_y"])
#    .fillna(00000,inplace=False).astype({"employee_id_x": 'int', "employee_id_y": 'int'})
#)
#
#
##merged_df_right = merged_df_right[merged_df_right.employee_id_x != 00000].astype({"employee_id_x": 'int', "employee_id_y": 'int'})
#merged_df_right=merged_df_right[merged_df_right.employee_id_x != 00000]
#
#merged_df_right=(
#    merged_df_right.rename(columns={"employee_id_x":"manager_id",
#                           "name_x":"manager_name",
#                           "department_x":"manager_department",
#                           "position_x":"manager_position",
#                           "employee_id_y":"employee_id",
#                           "name_y":"employee_name",
#                           "department_y":"employee_department",
#                           "position_y":"employee_position"}
#                           ))
#print (merged_df_right)