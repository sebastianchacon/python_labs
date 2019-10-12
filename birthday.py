from datetime import datetime

def get_user_birthday():
    year = int(input('When is your birthday? [YY] '))
    month = int(input('When is your birthday? [MM] '))
    day = int(input('When is your birthday? [DD] '))

    birthday = datetime(2000+year,month,day)
    return birthday

def calculate_dates(original_date, now):
    delta1 = datetime(now.year, original_date.month, original_date.day)
    delta2 = datetime(now.year+1, original_date.month, original_date.day)
    days = (max(delta1, delta2) - now).days



    return days

bd = get_user_birthday()
now = datetime.now()
c = calculate_dates(bd, now)
c = c - 365
print(c)
