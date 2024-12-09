from bs4 import BeautifulSoup
import pandas as pd
import requests
url = "https://www.formula1.com/en/results/2022/drivers"
r = requests.get(url)
r.status_code
data = BeautifulSoup(r.content)
table = data.table
table_rows = table.find_all('tr')
header_row = table_rows[0]
data_rows = table_rows[1:]
headers = header_row.find_all('th')
column_names = [name.text for name in headers]

rows = []
for row in data_rows:
  tds = row.find_all('td')
  tds_data = [td.text for td in tds]
  rows.append(tds_data)

f1_df = pd.DataFrame(data=rows, columns=column_names)
pd.read_html(url)[0]