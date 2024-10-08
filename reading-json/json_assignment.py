import json
with open("json_file.txt") as f:
    data = json.load(f)
data
for i in range(len(data)):
    for k,v in data[i].items():
        print(f"{k}: {v}")
    print(17*"=")
with open("daily_covid_cases.json") as c:
    covid = json.load(c)
covid
for k,v in covid.items():
    print(k)
    for k,i in v.items():
        print(f'{k}:{i}')
    print("\n")