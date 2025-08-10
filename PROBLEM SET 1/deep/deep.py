def deep():
    answer=input('What is the answer of life, the universe and everything?:')

    if answer.lower()=='forty-two' or answer.lower()=='forty two':
        print('Yes')
    else:
        try:
            if int(answer)==42:
                print('Yes')
            else:
                print('No')
        except ValueError:
            print('No')
deep()
