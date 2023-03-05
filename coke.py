def main():
    insert_coin()


def insert_coin():
    amount_due=50
    coinInserted = 0

    while True:
        insertCoin = int(input("Insert Coin: "))
        if insertCoin in [25,10,5]:
            amount_due = amount_due - insertCoin
            coinInserted = coinInserted + insertCoin
            
        
        if coinInserted >= 50:
            changeOwed = coinInserted - 50
            print(f"Change Owed: {changeOwed}")
            break
            

        else:
            print(f"Amount Due: {amount_due}")
            
    

main()

           


    
