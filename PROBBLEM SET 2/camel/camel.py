def camel():
    words=[]
    text=input('text:')
    caps=0
    for x in range(1,len(text)):
        if text[x].isupper():
            words.append(text[caps:x])
            caps=x
    words.append(text[caps:])
    print('_'.join(words).lower())
camel()

