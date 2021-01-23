text = input()
words = text.split(" ")
for word in words:
    # finish the code here
    temp = word.lower()
    if temp.startswith("https://") or temp.startswith("http://") or temp.startswith("www."):
        print(word)
