import pyfiglet
import sys
import random
def figlet():
    output=input('Input: ')
    try:
        if len(sys.argv)==1:
            random_font=random.choice(pyfiglet.FigletFont.getFonts())
            print('Output:\n ',pyfiglet.figlet_format(output,font=random_font))
        elif len(sys.argv)==3:
            if  sys.argv[1] not in ('-f','--font') or sys.argv[2] not in pyfiglet.FigletFont.getFonts():
                print('Invalid usage')
                sys.exit(1)
            else:
                print('Output: ',pyfiglet.figlet_format(output,font=sys.argv[2]))
        else:
            print('Invalid usage')
            sys.exit(1)
    except Exception as e:
        print(f'Error{e}')
        sys.exit(1)
figlet()

