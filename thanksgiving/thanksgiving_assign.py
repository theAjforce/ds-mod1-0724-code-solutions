import datetime as dt

def days_until_thanksgiving():
    today = dt.date.today()
    year = today.year
    november = dt.date(year, 11, 1)
    
    # Find the first Thursday of November
    days_to_first_thursday = (3 - november.weekday()) % 7
    first_thursday = november + dt.timedelta(days=days_to_first_thursday)
    
    # Thanksgiving is the fourth Thursday
    thanksgiving = first_thursday + dt.timedelta(weeks=3)
    
    return (thanksgiving - today).days
print(days_until_thanksgiving())