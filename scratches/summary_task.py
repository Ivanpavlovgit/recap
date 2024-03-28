#import json
#import pandas as pd
# TODO: Research how to make this path as a parameter to the python script
#PROPERTIES_FILE=r"C:\Users\Ivan.Pavlov2\OneDrive - Adastra, s.r.o\Python course\Recap taks\exercise_summary_task\properties.json"
#
#with open(PROP,encoding="utf-8") as read_file:
#    data = json.load(read_file)
#print(data)
#print(data["mainDirectory"])
from data_service import DataService
import pandas as pd
PROPERTIES_FILE_DIR=r"C:\Users\Ivan.Pavlov2\OneDrive - Adastra, s.r.o\Python course\Recap taks\exercise_summary_task"
PROPERTIES_FILE_NAME="properties.json"
def initEnvVars():
    """Bind environment variables from configuration files"""
    ds=DataService()
    dict_env_vars=DataService.load_from_json(ds,PROPERTIES_FILE_DIR,PROPERTIES_FILE_NAME)
    print(dict_env_vars)
    #inputDirectory=dict_envVars["inputDirectory"]
    #tempDirectory=dict_envVars["tempDirectory"]
    #outputDirectory=dict_envVars["outputDirectory"]
    #empDataFilename=dict_envVars["empDataFilename"]
    #empPositionFilename=dict_envVars["empPositionFilename"]
    #empSalariesFilename=dict_envVars["empSalariesFilename"]
    return dict_env_vars,ds

if __name__=="__main__":
    env_vars,ds=initEnvVars()
    
    main_directory=env_vars["mainDirectory"]
    emp_data_filename=env_vars["empDataFilename"]
    emp_salaries_filename=env_vars["empSalariesFilename"]
    
    emp_data_json=DataService.load_from_json(ds,main_directory,emp_data_filename)
    emp_salarier_json=DataService.load_from_json(ds,main_directory,emp_salaries_filename)
    print ("I have started")
    print(emp_data_json)
    print(emp_salarier_json)
 