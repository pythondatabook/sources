pp 43

import pandas as pd
data = ['jeff.russell','jane.boorman','tom.heints']
emps_names = pd.Series(data,index=[9001,9002,9003])
emps_emails = pd.Series(data,index=[9001,9002,9003], name = 'emails')
emps_names.name = 'names'
df = pd.concat([emps_names,emps_emails], axis=1)
print(df)
