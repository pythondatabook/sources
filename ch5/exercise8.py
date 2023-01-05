# pp 82

import mysql.connector
from mysql.connector import errorcode
try:
  cnx = mysql.connector.connect(user='root', password='your_pswd',
                              host='127.0.0.1',
                              database='sampledb')
  cursor = cnx.cursor()
  query = ("""SELECT o.pono, e.empname, o.total 
           FROM emps e, orders o WHERE e.empno = o.empno AND e.empno > %s""")
  empno = 9000
  cursor.execute(query, (empno,))
  for (pono, empname, total) in cursor:
    print("{}, {}, {}".format(
      pono, empname, total))
except mysql.connector.Error as err:
  print("Error-Code:", err.errno)
  print("Error-Message: {}".format(err.msg))
finally:
  cursor.close()
  cnx.close() 
