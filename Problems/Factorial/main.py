factorial = 1
number = int(input())

while number > 0:
    factorial *= number
    number -= 1

print(factorial)
