max_cat = 0
max_cafe = ""

while True:
    cafe = input()
    if cafe == "MEOW":
        break
    else:
        cafe_inf = cafe.split(" ")
        cafe_name = cafe_inf[0]
        cafe_cat = int(cafe_inf[1])
        if cafe_cat > max_cat:
            max_cat = cafe_cat
            max_cafe = cafe_name

print(max_cafe)
