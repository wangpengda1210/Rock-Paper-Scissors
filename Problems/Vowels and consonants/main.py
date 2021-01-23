for letter in input():
    if not letter.isalpha():
        break
    elif letter in "aeiou":
        print("vowel")
    else:
        print("consonant")
