def main():
    string=input("Input:").split()
    print('Output:',shorten(string))

def shorten(word):
        for vows in word:
            if vows.lower()in['a','e','i','o','u']:
                word=word.replace(vows,'')
        return word

if __name__ == "__main__":
    main()