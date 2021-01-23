quantity = int(input())
final = int(input())
time = 12

while quantity / 2 >= final:
    time += 12
    quantity /= 2

print(time)
