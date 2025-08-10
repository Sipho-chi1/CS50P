def main():
    time=input('What time is it?:')
    time_convert=convert(time)
    if 7<=time_convert<=8:
        print('Breakfast time')
    elif 12<=time_convert<=13:
        print('Lunch time')
    elif 18<=time_convert<=19:
        print('Dinner time')



def convert(time):
    hour, minutes=time.split(':')
    return float(hour) + float(minutes)/60



if __name__=="__main__":
    main()
