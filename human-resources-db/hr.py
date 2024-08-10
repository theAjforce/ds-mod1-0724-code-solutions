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
""")
salesdata = query2.fetchall()
sales = pd.DataFrame(salesdata)

query3 = cur.execute("""
            SELECT EmployeeNumber, EducationField, Age, Gender, Attrition
            FROM employee
            WHERE EducationField IS 'Life Sciences'
""")
fielddata = query3.fetchall()
field = pd.DataFrame(fielddata)

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