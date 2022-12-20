# pp 117

import numpy as np
jeff_salary = [2700,3000,3000]
nick_salary = [2600,2800,2800]
tom_salary = [2300,2500,2500]
base_salary1 = np.array([jeff_salary, nick_salary, tom_salary])
maya_salary = [2200,2400,2400]
john_salary = [2500,2700,2700]
base_salary2 = np.array([maya_salary, john_salary])
base_salary = np.concatenate((base_salary1, base_salary2), axis=0)
new_month_salary = np.array([[3000],[2900],[2500],[2500],[2700]])
base_salary = np.concatenate((base_salary, new_month_salary), axis=1)
new_month_salary = np.array([[3000, 3100],[2900, 2900],[2500,2600],[2500,2600],[2700,2800]])
base_salary = np.concatenate((base_salary, new_month_salary), axis=1)
