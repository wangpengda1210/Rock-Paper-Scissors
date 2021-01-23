digits = ['zero', 'one', 'two', 'three', 'four', 'five',
          'six', 'seven', 'eight', 'nine']

number = input()
for i in number:
    digit = int(i)
    print(digits[digit])
