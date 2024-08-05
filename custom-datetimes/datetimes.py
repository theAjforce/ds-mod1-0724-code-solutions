from datetime import datetime

def date_parser(date):
    if "/" in date:
        if date[-3] == "/":
            dt = datetime.strptime(date, "%m/%d/%y")
        elif date[-5] == "/":
            dt = datetime.strptime(date, "%d/%m/%Y")
        else:
            return "Need assistance parsing" #I included this clause because after a bit of research I was unable to find how to parse the ones with the timezones included, and I forgot what advice was given to Newton.
    elif "T" in date:
        dt = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f%z")
    else:
        date.isdigit()
        dt = datetime.fromtimestamp(int(date))
    return dt