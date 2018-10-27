rday, rmonth, ryear = [int(x) for x in input().split(' ')]
eday, emonth, eyear = [int(x) for x in input().split(' ')]

if ryear < eyear:
    print('0')
if ryear > eyear:
    print('10000')
if ryear == eyear:
    if rmonth < emonth:
        print('0')
    if rmonth > emonth:
        print((rmonth-emonth) * 500)
    if rmonth == emonth:
        if rday <= eday:
            print('0')
        if rday > eday:
            print((rday - eday) * 15)
