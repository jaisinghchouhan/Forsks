import sqlite3
from pandas import DataFrame
conn = sqlite3.connect ( 'db_university.db' )
c = conn.cursor()
c.execute ("""CREATE TABLE student(
          Student_Name TEXT, 
          Student_Age INTEGER, 
          Student_Roll_no INTEGER, 
          Student_Branch TEXT
            )""")
c.execute("INSERT INTO student VALUES ('abc',19,123,'cse')")
c.execute("INSERT INTO student VALUES ('def',19,124,'cse')")
c.execute("INSERT INTO student VALUES ('ghi',19,125,'cse')")
c.execute("INSERT INTO student VALUES ('pqr',19,126,'cse')")
c.execute("INSERT INTO student VALUES ('xyz',19,127,'cse')")

c.execute("SELECT * FROM student")

print ( c.fetchone())

c.execute("SELECT * FROM student")

df=DataFrame(c.fetchall())
df.columns=["name","age","roll no","branch"]