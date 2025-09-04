import sys
import pandas as pd

def transfer():
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)<3:
        sys.exit("Too few command-line arguments")

    filename_1=sys.argv[1]
    filename_2=sys.argv[2]

    if not filename_1.endswith(".csv") or not filename_2.endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        info=pd.read_csv(filename_1)
    except FileNotFoundError:
        sys.exit("File does not exist")

    info["name"]=info["name"].str.strip()
    info[["last","first"]]=info["name"].str.split(",",n=1,expand=True)
    info["first"]=info["first"].str.strip()
    info["last"]=info["last"].str.strip()
    info=info[["first","last","house"]]
    info.to_csv(filename_2,index=False)

transfer()