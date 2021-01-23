with_s = []

for word in input().split():
    if word.endswith("s"):
        with_s.append(word)

print("_".join(with_s))
