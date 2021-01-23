num = input()
min_num = num

while num != ".":
    if float(num) < float(min_num):
        min_num = float(num)
    num = input()

print(min_num)
