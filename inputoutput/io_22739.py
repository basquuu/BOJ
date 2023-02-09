x, y = map(int,input().split())

from datetime import datetime, date
def what_day(date):
    days =['MON','TUE','WED','THU','FRI','SAT','SUN']
    day = date.weekday()
    print(days[day])
    
what_day(date(2007,x,y))