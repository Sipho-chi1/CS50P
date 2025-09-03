def main():
      string=input('Greeting: ')
      print(value(string))
    


def value(greeting):
    if greeting.lower().startswith('hello') or greeting.lower()==' hello ':
        return '$0'
    elif greeting.lower().startswith('h'):
        return '$20'
    else:
        return '$100'

if __name__ == "__main__":
    main()