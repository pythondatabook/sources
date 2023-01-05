# pp 61

l =  {"cars":
  [{"Year": "1997", "Make": "Ford", "Model": "E350", "Price": "3200.00"},
   {"Year": "1999", "Make": "Chevy", "Model": "Venture", "Price": "4800.00"},
   {"Year": "1996", "Make": "Jeep", "Model": "Grand Cherokee", "Price": "4900.00"}
]}

import json
jsonString = json.dumps(l)
jsonFile = open("cars.json", "w")
jsonFile.write(jsonString)
jsonFile.close() 

jsonFile = open("cars.json", "r")
pobj = json.load(jsonFile)

for car in pobj["cars"]:  
  for item in car.items():
    print(item[0],':', item[1])
  print('\n')
