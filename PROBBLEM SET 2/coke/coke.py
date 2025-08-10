def coke():
    total_coin_inserted=0
    coins=[25,10,5]
    while total_coin_inserted<50:
        try:
            coin_insert=int(input('Insert Coin:'))
            if coin_insert in coins:
                total_coin_inserted+=coin_insert
                if total_coin_inserted<50:
                    print (f'Amount Due: {50-total_coin_inserted}')
                elif total_coin_inserted>=50:
                    print(f'Change Owed: {total_coin_inserted-50}')
            elif coin_insert not in coins:
                    print('Amount Due: 50')

        except ValueError:
            print ('Amount Due: 50')

coke()

