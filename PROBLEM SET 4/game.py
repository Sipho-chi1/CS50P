import random
def game():
    while True:
        try:
            n=int(input('Level: '))
            break
        except ValueError:
            continue
    guess=random.randint(1,n)
    while True:
        try:
            input_num=int(input('Guess: '))
        except ValueError:
            continue
        if input_num>0:
            if input_num<guess:
                print('Too small!')
                continue
            elif input_num>guess:
                print('Too large!')
                continue
            else:
                print('Just right!')
                break
game()
