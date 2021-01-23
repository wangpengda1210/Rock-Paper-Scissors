words = input().split()
new_list = []

for i in range(len(words)):
    if i == 0:
        new_list.append(words[i])
    else:
        new_list.append(words[i].capitalize())

print("".join(new_list))
