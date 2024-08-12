import sqlite3
import pandas as pd
conn = sqlite3.connect("stocks.sqlite")
cur = conn.cursor()

table_query = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = table_query.fetchall()

msft_query = cur.execute("""
        SELECT * 
        FROM STOCK_DATA
        WHERE Symbol = 'MSFT';
""")
msftdata = msft_query.fetchall()
msft = pd.DataFrame(msftdata)

cur.execute("CREATE TABLE msft (`index`, Date, Open, High, Low, Close, Volume, Adj Close, Symbol)")

cur.executemany("""
            INSERT INTO msft
            VALUES(?,?,?,?,?,?,?,?,?)
""",msft.values)

aapl_query = cur.execute("""
        SELECT * 
        FROM STOCK_DATA
        WHERE Symbol = 'AAPL';
""")
aapldata = aapl_query.fetchall()
aapl = pd.DataFrame(aapldata)

cur.execute("CREATE TABLE aapl (`index`, Date, Open, High, Low, Close, Volume, Adj Close, Symbol)")

cur.executemany("""
            INSERT INTO aapl
            VALUES(?,?,?,?,?,?,?,?,?)
""",aapl.values)

msft_date_query = cur.execute("""
        SELECT MAX(Date), MIN(Date)
        FROM msft
""")
msftdatedata = msft_date_query.fetchall()
msft_date = pd.DataFrame(msftdatedata)

aapl_date_query = cur.execute("""
        SELECT MAX(Date), MIN(Date)
        FROM aapl
""")
aapldatedata = aapl_date_query.fetchall()
aapl_date = pd.DataFrame(aapldatedata)

msft_open_query = cur.execute("""
SELECT Open
FROM msft
WHERE Open > 50
""")
msft_open_date = msft_open_query.fetchall()
msft_open = pd.DataFrame(msft_open_date)

aapl_open_query = cur.execute("""
SELECT Open
FROM aapl
WHERE Open > 50
""")
aapl_open_date = aapl_open_query.fetchall()
aapl_open = pd.DataFrame(aapl_open_date)