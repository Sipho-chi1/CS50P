import sys
from PIL import Image, ImageOps
def merge():
    if len(sys.argv)<3:
        sys.exit(" Too few command line arguments")
    elif len(sys.argv)>3:
        sys.exit(" Too many command line arguments")
    if not sys.argv[1].endswith((".png",".jpeg",".jpg"))or not sys.argv[2].endswith((".png",".jpeg",".jpg")):
        sys.exit(" Invalid input")
        input=sys.argv[1]
        output=sys.argv[2]
    try:
        person=Image.open(input)
        shirt=Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("File does not exist")
    size=(shirt.width,shirt.width)
    person = ImageOps.fit(person, size)
    x=0
    y=person.height - shirt.height
    pos=(x,y)
    person.paste(shirt,pos,shirt)
    person.save(output)

merge()
