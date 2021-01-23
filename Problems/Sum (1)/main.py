# read sums.txt
file = open("sums.txt", "r")
for line in file:
    first, second = line.split(" ")
    print(int(first) + int(second))
file.close()
