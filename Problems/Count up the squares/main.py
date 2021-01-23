# put your python code here
num_sum = int(input())
square_sum = num_sum ** 2

while num_sum != 0:
    next_num = int(input())
    num_sum += next_num
    square_sum += next_num ** 2

print(square_sum)
