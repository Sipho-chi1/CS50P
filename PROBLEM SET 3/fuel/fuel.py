def fuel():
    fuel_gage =input('Fraction: ')
    x,y=fuel_gage.split('/')
    x=int(x)
    y=int(y)
    if '/' in fuel_gage and y!=0 and x<=y and not x>y:
        percentage=round(x/y*100)
        if percentage>=99:
            print('F')
        elif percentage>=1:
            print(f'{percentage}%')
        else:
            print('E')
    else:
        print('E')

if __name__ == '__main__':
    fuel()