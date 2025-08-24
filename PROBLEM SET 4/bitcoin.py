import requests
import sys
def bitcoin():
    if len(sys.argv)<2:
        sys.exit("Command-Line Argument is missing")
    try:
        amount=float(sys.argv[1])
    except ValueError:
        sys.exit("Command-Line Argument is not a number")
    try:
        response = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=ed05f4903b3275f037e676f7faa46673164473a450a56c55ba40855c96998fdc')
        data=response.json()
        price=float(data['data']['priceUsd'])*amount
    except requests.RequestException:
            sys.exit()
    print(f'${price:,.4f}')
if __name__ == "__main__":
    bitcoin()