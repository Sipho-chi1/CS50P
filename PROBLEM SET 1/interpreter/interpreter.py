def interpreter():
    expression=input('expression:')
    operators=['-','+','*','/']
    for operator in operators:
        if operator in expression:
            x,z=expression.split(operator)
            x=float(x)
            z=float(z)
            if operator=='+':
                print(x+z)
            elif operator=='-':
                print(x-z)
            elif operator=='*':
                print(x*z)
            elif operator=='/':
                if z==0:
                    print('0 cant be divisable by the denominator')
                else:
                    print(x/z)
interpreter()
