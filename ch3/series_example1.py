# pp 41

import pandas as pd
data = ['Jeff Russell','Jane Boorman','Tom Heints']
emps_names = pd.Series(data)
print(emps_names)
emps_names = pd.Series(data,index=[9001,9002,9003])
print(emps_names.loc[9001:9002])
