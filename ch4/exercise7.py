# pp 70

import pandas as pd

data = [{"Emp":"Jeff Russell",
"Emp_email":"jeff.russell",
"POs":[{"Pono":2608,"Total":35},
{"Pono":2617,"Total":35},
{"Pono":2620,"Total":139}
]},
{"Emp":"Jane Boorman",
"Emp_email":"jane.boorman",
"POs":[{"Pono":2621,"Total":95},
{"Pono":2626,"Total":218}
]
}]  

df = pd.json_normalize(data, "POs", ["Emp","Emp_email"]).set_index(["Emp","Emp_email","Pono"])
df = df.reset_index()
json_doc = (df.groupby(['Emp',"Emp_email"], as_index=True)
.apply(lambda x: x[['Pono','Total']].to_dict('records'))
.reset_index()
.rename(columns={0:'POs'})
.to_json(orient='records'))
print(json_doc)
