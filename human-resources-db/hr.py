import sqlite3
import pandas as pd

conn = sqlite3.connect("hr.db")
cur = conn.cursor()
table_query = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = table_query.fetchall()

data_query = cur.execute("SELECT * FROM employee;")
data = data_query.fetchall()

query2 = cur.execute("""
                SELECT EmployeeNumber, Department, Age, Gender, Attrition
                FROM employee
                WHERE Department IS 'Sales'
""")
column_name = [description[0] for description in cur.description]
salesdata = query2.fetchall()
sales = pd.DataFrame(salesdata, columns=column_name)

query3 = cur.execute("""
            SELECT EmployeeNumber, EducationField, Age, Gender, Attrition
            FROM employee
            WHERE EducationField IS 'Life Sciences'
""")
column_name = [description[0] for description in cur.description]
fielddata = query3.fetchall()
field = pd.DataFrame(fielddata, columns=column_name)

cur.execute("CREATE TABLE sales (EmployeeNumber, Department, Age, Gender, Attrition)")
cur.executemany("""
            INSERT INTO sales
            VALUES(?,?,?,?,?)
""",sales.values)
cur.execute("CREATE TABLE field (EmployeeNumber, EducationField, Age, Gender, Attrition)")
cur.executemany("""
            INSERT INTO field
            VALUES(?,?,?,?,?)
""", field.values)
joined = cur.execute("""
        SELECT *
        FROM field as f
        INNER JOIN sales as s
        ON f.EmployeeNumber = s.EmployeeNumber;   
""")