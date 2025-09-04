import sys
import csv
from tabulate import tabulate

def pizza():
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)<2:
        sys.exit("Too few command-line arguments")

    filename=sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")
    
    try:
        with open(filename) as file:
            reader=csv.reader(file)
            table=list(reader)
        header=table[0]
        row=table[1:]
        print(tabulate(row,headers=header,tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

pizza()

       
    