# put your python code here
count = 0
num_sum = 0

for i in range(int(input()), int(input()) + 1):
    if i % 3 == 0:
        count += 1
        num_sum += i

print(num_sum / count)
