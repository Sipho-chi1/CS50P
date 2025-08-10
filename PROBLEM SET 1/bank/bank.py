def bank():
    greeting=input('Greeting:')
    if greeting.lower().startswith('hello') or greeting.lower()==' hello ':
        print('$0')
    elif greeting.lower().startswith('h'):
        print('$20')
    else:
        print('$100')
bank()
