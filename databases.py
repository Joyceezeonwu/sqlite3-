import sqlite3
print('Success')

#connect to a database
Conn = sqlite3.connect('student.db')

#create a cursor object
C = Conn.cursor()

#sequel commands go in here

#commit to database
Conn.commit()

#close your connection
Conn.close()
