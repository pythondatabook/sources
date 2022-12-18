# pp 50

import json
import pandas as pd
data = [
 {"Empno":9001,"Salary":3000},
 {"Empno":9002,"Salary":2800},
 {"Empno":9003,"Salary":2500}
]
json_data = json.dumps(data)
salary = pd.read_json(json_data)
salary = salary.set_index('Empno')
print(salary) 

data = [['9001','Jeff Russell', 'sales'],
 ['9002','Jane Boorman', 'sales'],
 ['9003','Tom Heints', 'sales']]
emps = pd.DataFrame(data, columns = ['Empno', 'Name', 'Job'])
column_types = {'Empno': int, 'Name': str, 'Job': str}
emps = emps.astype(column_types)
emps = emps.set_index('Empno')
print(emps)

emps_salary = emps.join(salary)
print(emps_salary)

new_emp = pd.Series({'Name': 'John Hardy', 'Job': 'sales'}, name = 9004)
emps = emps.append(new_emp)

emps_salary = emps.join(salary, how = 'inner')
print(emps_salary)

new_salary = pd.Series({'Salary': 2400}, name = 9006)
salary = salary.append(new_salary)

emps_salary = emps.join(salary, how = 'inner')
print(emps_salary)

emps_salary = emps.join(salary, how = 'outer')
print(emps_salary)
