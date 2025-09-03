def main():
    fuel_gage=input('Fraction: ')
    percentage=convert(fuel_gage)
    print(gauge(percentage))


def convert(fraction):
    x,y=fraction.split('/')
    x=int(x)
    y=int(y)
    if y!=0 and x<=y and x<y:
        return round(x/y*100)
    elif x==y:
        return 100
    elif y==0:
        raise ZeroDivisionError
    elif not x<=y or x>y:
        raise ValueError
    elif not x>=0 or x<0:
        raise ValueError
    
def gauge(percentage):
        if percentage>=99:
            return'F'
        elif percentage>=1:
            return f'{percentage}%'
        else:
            return'E'



if __name__ == "__main__":
    main()