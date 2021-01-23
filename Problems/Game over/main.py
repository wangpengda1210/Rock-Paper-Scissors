scores = input().split()
# put your python code here
correct = 0
wrong = 0

for score in scores:
    if score == "C":
        correct += 1
    else:
        wrong += 1
        if wrong >= 3:
            print("Game over")
            print(correct)
            break
else:
    print("You won")
    print(correct)
