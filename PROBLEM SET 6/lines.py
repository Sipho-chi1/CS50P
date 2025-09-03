import sys

def lines():

    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
        
    file_path=sys.argv[1]

    if not file_path.endswith(".py"):
        sys.exit("Not a Python file")
    try:
        with open(file_path)as file:
             lines=[line for line in file if line.strip() !="" and not line.strip().startswith("#")]
        print(len(lines))
    except FileNotFoundError:
        sys.exit("File does not exist")
lines()

