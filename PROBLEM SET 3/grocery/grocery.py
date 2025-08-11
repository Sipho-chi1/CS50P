def grocery():
    list_foods=[]
    while True:
        try:
            food=input()
            if food:
                list_foods.append(food.upper())
                list_foods.sort()
            for x,item in enumerate(list_foods,1):
                print(f'{x} {item}')
        except EOFError:
            break            
grocery()
