word = input()
result = word[0]

for i in range(1, len(word)):
    c = word[i]

    if c.isupper():
        result += "_" + c
    else:
        result += c

print(result.lower())
