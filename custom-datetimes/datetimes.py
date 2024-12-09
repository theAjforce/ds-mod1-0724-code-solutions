from datetime import datetime
import pytz

def date_parser(date):
    if "/" in date:
        if date[-3] == "/":
            dt = datetime.strptime(date, "%m/%d/%y")
        elif date[-5] == "/":
            dt = datetime.strptime(date, "%d/%m/%Y")
        else:
            date_split = date.split()
            timezone = date_split.pop()
            timezone_value = pytz.timezone(timezone)
            joined_date = date_split.join()
            

            
    elif "T" in date:
        dt = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f%z")
    else:
        date.isdigit()
        dt = datetime.fromtimestamp(int(date))
    return dt
print(date_parser("March 23rd, 2021 13:01 US/Pacific"))