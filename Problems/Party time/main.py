guests = []

while True:
    new_guest = input()
    if new_guest == ".":
        break
    else:
        guests.append(new_guest)

print(guests)
print(len(guests))
