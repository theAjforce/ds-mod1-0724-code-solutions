from datetime import datetime
from datetime import date
def age(bd_string):
    bd = datetime.strptime(bd_string,"%m-%d-%Y").date()
    today = date.today()
    if bd.month > today.month:
        return ((today.year - bd.year)-1)
    elif bd.month==today.month:
        if today.day > bd.day:
            return (today.year - bd.year)
        else:
            return ((today.year - bd.year)-1)
    else:
        return (today.year - bd.year)
print(age("03-14-1998"))