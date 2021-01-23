time = 10 + int(input())

if time >= 24:
    print("Wednesday")
elif time < 0:
    print("Monday")
else:
    print("Tuesday")
