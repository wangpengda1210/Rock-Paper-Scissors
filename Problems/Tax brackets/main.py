income = int(input())

percent = 28
if income <= 15527:
    percent = 0
elif income <= 42707:
    percent = 15
elif income <= 132406:
    percent = 25

calculated_tax = income * percent / 100
print(f"The tax for {income} is {percent}%. That is {calculated_tax:.0f} dollars!")
