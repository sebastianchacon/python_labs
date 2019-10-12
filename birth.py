import datetime

d, m, y = 0, 0, 0
td = datetime.date.today()
person = 'Your'
b = input('Enter your birth date (DD/MM/YYYY): ')
# let's establish a SoloLearn-friendly format

try:
    d, m, y = b.split('/') #if that fails, we'll execute the 'except' part
    d = int(d)
    m = int(m)
    y = int(y)
    bd = datetime.date(y, m, d) # birth date in a datetime format
    nbd = datetime.date(td.year, m, d) # next birthday
    if (nbd - td).days < 0: # if the ate already passed for this year
        nbd = datetime.date(td.year + 1, m, d)
except:
    bd = datetime.date(1979, 11, 15) # in case of wrong input, take mine :)
    nbd = datetime.date(td.year, 11, 15)
    if (nbd - td).days < 0:
        nbd = datetime.date(td.year + 1, 11, 15)
    print("Something went wrong...\nUsing the Creator's birthday instead ;)")
    person = "The Creator's" # yep, that's me ;)

print()
print(person, 'birthday is on', nbd)
if (nbd-td).days > 0:
    print('That\'s in', (nbd - td).days, 'days already...')
else:
    print('That\'s today! Happy birthday!!!')