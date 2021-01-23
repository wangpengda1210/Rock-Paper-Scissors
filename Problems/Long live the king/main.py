x = int(input())
y = int(input())

if x == 1 or x == 8:
    if y == 1 or y == 8:
        print(3)
    else:
        print(5)
elif y == 1 or y == 8:
    print(5)
else:
    print(8)
