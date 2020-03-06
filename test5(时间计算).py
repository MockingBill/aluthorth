def isMoist(year):
    return (year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0)
def mondate2days(year,mon,date,days):
    if mon==1:
        days=days+date
    elif mon==2:
        days = days + date+31
    elif mon==3 and isMoist(year):
        days = days + date+31+29
    elif mon==3 and not isMoist(year):
        days = days + date+31+28
    elif mon==4:
        days = days + date+31+28+31
    elif mon==5:
        days = days + date+31+28+31+30
    elif mon==6:
        days = days + date+31+28+31+30+31
    elif mon==7:
        days = days + date+31+28+31+30+31+30
    elif mon==8:
        days = days + date+31+28+31+30+31+30+31
    elif mon==9:
        days = days + date+31+28+31+30+31+30+31+31
    elif mon==10:
        days = days + date+31+28+31+30+31+30+31+31+30
    elif mon==11:
        days = days + date+31+28+31+30+31+30+31+31+30+31
    elif mon==12:
        days = days + date+31+28+31+30+31+30+31+31+30+31+30
    return year,1,1,days-1

textArray = []
while True:
    text = input()
    if text != 'end':
        textArray.append([int(i.strip()) for i in text.split() if i.strip() != 0])
    else:
        break
if len(textArray) != 0:
    for text in textArray:
        year, mon, date, days = mondate2days(text[0], text[1], text[2], text[3])

        if isMoist(year + 1):
            while days >= 366:
                if isMoist(year + 1):
                    days = days - 366
                else:
                    days = days - 365
                year = year + 1
        else:
            while days >= 365:
                if isMoist(year + 1):
                    days = days - 366
                else:
                    days = days - 365
                year = year + 1
        D=days+1
        while days >= 31:

            if ((mon + 1) == 1 or (mon + 1) == 3 or (mon + 1) == 5 or (mon + 1) == 7 or (mon + 1) == 8 or (
                    mon + 1) == 10 or (
                        mon + 1) == 12) and days >= 31:
                days = days - 31
                mon = mon + 1
            elif ((mon + 1) == 4 or (mon + 1) == 6 or (mon + 1) == 9 or (mon + 1) == 11) and days >= 30:
                days = days - 30
                mon = mon + 1
            elif isMoist(year) and (mon + 1) == 2 and days >= 29:
                days = days - 29
                mon = mon + 1
            elif not isMoist(year) and (mon + 1) == 2 and days >= 28:
                days = days - 28
                mon = mon + 1
        date = days + date
        if (mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12) and date > 31:
            date = date - 31
            mon = mon + 1
        elif (mon == 4 or mon == 6 or mon == 9 or mon == 11) and date > 30:
            date = date - 30
            mon = mon + 1
        elif mon == 2 and isMoist(year) and date > 29:
            date = date - 29
            mon = mon + 1
        elif mon == 2 and not isMoist(year) and date > 28:
            date = date - 28
            mon = mon + 1
        print(year, mon, date)
        if mon<3:
            W = (date + 2 * (mon+12) + 3 * ((mon+12) + 1) / 5 + (year-1) + (year-1) / 4 - (year-1) / 100 + (year-1) / 400)%7
        else:
            W = (date + 2 * mon + 3 * (mon + 1) / 5 + year + year / 4 - year / 100 + year / 400) % 7

        A = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(A[round(W)-1])
