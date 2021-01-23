# put your python code here
numbers = input().split()
value = input()
positions = []

for i in range(len(numbers)):
    if numbers[i] == value:
        positions.append(str(i))

if len(positions) == 0:
    print("not found")
else:
    print(" ".join(positions))
