num_sum = 0
count = 0

while True:
    new_num = input()
    if new_num == ".":
        break
    else:
        num_sum += int(new_num)
        count += 1

print(num_sum / count)
