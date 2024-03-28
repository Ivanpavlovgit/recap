import pandasql as ps
import pandas as pd
class Employee:
    def __init__(self,
                 df1:pd.DataFrame,
                 df2:pd.DataFrame,
                 df3:pd.DataFrame):
        self.df1=df1
        self.df2=df2
        self.df3=df3
        self.joined_frames=self.join_dfs_emp_id()##move this

    def join_dfs_emp_id(self)->pd.DataFrame:
        """Functions joins the thee employees dataframes on employee_id column"""
        self.df2.set_index("employee_id",inplace=True)
        self.df3.set_index("employee_id",inplace=True)
        joined_frames=self.df1.join(self.df2,on="employee_id").join(self.df3,on="employee_id")
        return joined_frames
    def top10(self)->pd.DataFrame:
        """IM LAZY"""
        df=self.joined_frames
        query_top3_employee="SELECT *,salary/12 as monthly_salary FROM df ORDER BY monthly_salary DESC LIMIT 3"#replace DF API
        return ps.sqldf(query_top3_employee)
    def avg_sal_dept(self)->pd.DataFrame:
        """IM LAZY"""
        df=self.joined_frames
        query_avg_sal_dept= "SELECT department,AVG(salary) from df GROUP BY department"
        avg_sal=ps.sqldf(query_avg_sal_dept)
        return avg_sal
    def manager_employees(self)->pd.DataFrame:
        """IM LAZY"""
        df=self.joined_frames
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
        mngr_employees=ps.sqldf(query_manager_employees)
        return mngr_employees