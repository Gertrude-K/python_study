from datetime import datetime, timedelta

def calculate_age(dob , today=None):
    dob_date = datetime.strptime(dob, "%Y-%m-%d")
    if today is None:
        today = datetime.today()
    
    days = today.day - dob_date.day
    months = today.month - dob_date.month
    years = today.year - dob_date.year
    month_start = today.replace(day=1)       # a DATE: the 1st of this month

    while days < 0:
      last_day_prev = month_start - timedelta(days=1)   # a DATE in the previous month
      days += last_day_prev.day                       # blank 1: that month's length
      months -= 1
      month_start = last_day_prev.replace(day=1)     # blank 2: move to the 1st of that month
    if months <0 :
        months += 12
        years -= 1       
        
    return years, months, days
         
print(calculate_age("2001-11-15", datetime(2026, 10, 3)))