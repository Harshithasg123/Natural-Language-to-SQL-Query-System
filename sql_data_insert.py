import sqlite3

connection=sqlite3.connect("employee.db")

cursor=connection.cursor()

table_info="""
Create table EMPLOYEE(EMP_NAME VARCHAR(25),EMP_ID VARCHAR(25),DESIGNATION VARCHAR(25),EMP_AGE INT);
"""

try:
    cursor.execute(table_info)
except:
    pass    

cursor.execute('''Insert Into EMPLOYEE values('Satish','XY012','NLP Engineer',28)''')
cursor.execute('''Insert Into EMPLOYEE values('Aditya','XY014','Data Engineer',35)''')
cursor.execute('''Insert Into EMPLOYEE values('Amith','XY016','Data Enginner',38)''')
cursor.execute('''Insert Into EMPLOYEE values('Arun','XY018','Cloud Engineer',45)''')

print("The inserted records are:")
data=cursor.execute('''Select * from EMPLOYEE''')
for row in data:
    print(row)

#commit your changes in the db
connection.commit()
connection.close()