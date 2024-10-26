amount_due = 50
money = [5, 10,25]

while amount_due > 0:
    print("Amount Due: " + str(amount_due))
    inserted_money = int(input("Instert Coin: "))
    if inserted_money in money:
        amount_due -= inserted_money
    else:
        continue

if amount_due <= 0:
    amount_due = amount_due*-1
    print("Change Owed: " + str(amount_due))
