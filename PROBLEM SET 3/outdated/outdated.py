def outdated():
    months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    while True:
        date=input('Date: ').strip()
        if not date:
            continue
        try:
            if  '/' in date:
                month,day,year=date.split('/')
                if not (month.isdigit() and day.isdigit() and year.isdigit()):
                     continue
            else:
                if ',' not in date:
                    continue
                month,day,year=date.replace(',',' ').split()
            if month.title() in months:
                month_digit=months.index(month.title())+1
            elif month.isdigit():
                month_digit=int(month)
            else:
                continue
            day=int(day)
            year=int(year)
            if not 1<=day<=31:
                continue
            if not 1<=month_digit<=12:
                continue
            print(f'{year}-{month_digit:02d}-{int(day):02d}')
            break
        except ValueError:
            continue
outdated()