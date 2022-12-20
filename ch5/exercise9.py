# pp 92

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['sampledb']
emps_collection = db['emps']

ord_list = [
{"empno": 9026, "empname": "Bob Dores", "orders": [4608, 4617, 4620]},
{"empno": 9027, "empname": "Tony Aaron", "orders": [4708, 4717, 4720]}
]

emps_collection.insert_many(ord_list)
db.emps.find()  
