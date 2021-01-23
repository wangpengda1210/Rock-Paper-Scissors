height = int(input())
width = 2 * height - 1

for i in range(1, height + 1):
    print(("#" * (2 * i - 1)).center(width))
