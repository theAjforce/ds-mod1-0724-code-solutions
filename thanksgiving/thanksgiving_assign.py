import datetime as dt

def days_until_thanksgiving():
    today = dt.date.today()
    year = today.year
    november = dt.date(year, 11, 30)
    days_to_last_thursday = (november.weekday() - 3) % 7
    thanksgiving = november - dt.timedelta(days=days_to_last_thursday)
    
    return (thanksgiving - today).days
print(days_until_thanksgiving())