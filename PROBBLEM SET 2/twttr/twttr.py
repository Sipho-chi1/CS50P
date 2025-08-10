def twttr():
    string=input("Input:").split()
    for x in range(len(string)):
        for vows in string[x]:
            if vows.lower()in['a','e','i','o','u']:
                string[x]=string[x].replace(vows,'')
    print('Output: ',' '.join(string))
twttr()
