# pp 43

import pandas as pd
data = ['jeff.russell','jane.boorman','tom.heints']
emps_emails = pd.Series(data,index=[9001,9002,9003], name = 'emails')
emps_names = pd.Series(data,index=[9001,9002,9003])
emps_names.name = 'names'
phones = ['+1 246 111-xxxx', '+1 246 222-xxxx','+1 246 333-xxxx',]
emps_phones = pd.Series(phones,index=[9001,9002,9003])
emps_phones.name = 'names'
df = pd.concat([emps_names,emps_emails, emps_phones], axis=1)
print(df)
