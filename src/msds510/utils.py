from time import strptime
import datetime

def get_month(intro):
    if '88' in intro:
        return strptime(intro,'%b-%y').tm_mon
    elif '89' in intro:
        return strptime(intro,'%b-%y').tm_mon
    else:
        return strptime(intro,'%d-%b').tm_mon

def get_date_joined(year, intro):
    y = int(year)
    m = get_month(intro)
    return datetime.date(y, m, 1)

def days_since_joined(year, intro):
    d0 = get_date_joined(year, intro)
    d1 = datetime.date.today()
    delta = d1 - d0
    return delta.days
