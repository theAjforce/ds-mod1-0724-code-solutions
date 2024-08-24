import sqlite3
import pandas as pd
conn = sqlite3.connect("/Users/anthonyvillegas/Documents/ds-mod1-0724-code-solutions/telecom-db/telecom.db")
cur = conn.cursor()

table_query = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = table_query.fetchall()
print(tables)


joined = cur.execute("""
            
            SELECT t.*, et.event_type, lf.log_feature, lf.volume, st.severity_type, rt.resource_type 
            FROM train t
                LEFT JOIN event_type AS et ON t.id = et.id
                LEFT JOIN log_feature AS lf ON t.id = lf.id
                LEFT JOIN severity_type AS st ON t.id = st.id
                LEFT JOIN resource_type AS rt ON t.id = rt.id;

""")
joined_data = joined.fetchall()
joineddb = pd.DataFrame(joined_data)

cur.execute("""
          CREATE TABLE joined ('index', 'id', 'location','fault_severity', 'event_type', 'log_feature', 'volume', 'severity_type', 'resource_type')
""")

cur.executemany("""
INSERT INTO joined
VALUES (?,?,?,?,?,?,?,?,?)

""",joineddb.values)

unique_occ = cur.execute("""
            SELECT DISTINCT(event_type), severity_type
            FROM joined

""")
uniquedata = unique_occ.fetchall()
uniquedf = pd.DataFrame(uniquedata)

fault_occ = cur.execute("""
            SELECT (fault_severity), COUNT(*) AS count
            FROM joined
            GROUP BY fault_severity;

""")
faultdata = fault_occ.fetchall()
faultdf = pd.DataFrame(faultdata)