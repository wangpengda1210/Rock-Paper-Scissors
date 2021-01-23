money = int(input())

if money >= 6769:
    amount = money // 6769
    print(amount, "sheep")
elif money >= 3848:
    print("1 cow")
elif money >= 1296:
    amount = money // 1296
    if amount > 1:
        print(amount, "pigs")
    else:
        print("1 pig")
elif money >= 678:
    print("1 goat")
elif money >= 23:
    amount = money // 23
    if amount > 1:
        print(amount, "chickens")
    else:
        print("1 chicken")
else:
    print("None")
