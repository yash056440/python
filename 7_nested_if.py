p1 = input("Enter person1 name : ")
d1 = int(input("Enter day (Birth day): "))
m1 = input("Enter month (Birth month): ")

p2 = input("Enter person2 name : ")
d2 = int(input("Enter day (Birth day): "))
m2 = input("Enter month (Birth month): ")

one = "Aries"
two = "Taurus"
three = "Gemini"
four = "Cancer"
five = "Leo"
six = "Virgo"
seven = "Libra"
eight = "Scorpio"
nine = "Sagittarius"
ten = "Capricorn"
eleven = "Aquarius"
twelve = "Pisces"

zs1 = ""
zs2 = ""

if m1 == "march":
    if d1 >= 21:
        zs1 = one
    else:
        zs1 = twelve
elif m1 == "april":
    if d1 <= 19:
        zs1 = one
    else:
        zs1 = two
elif m1 == "may":
    if d1 <= 20:
        zs1 = two
    else:
        zs1 = three
elif m1 == "june":
    if d1 <= 21:
        zs1 = three
    else:
        zs1 = four
elif m1 == "july":
    if d1 <= 22:
        zs1 = four
    else:
        zs1 = five
elif m1 == "august":
    if d1 <= 22:
        zs1 = five
    else:
        zs1 = six
elif m1 == "september":
    if d1 <= 22:
        zs1 = six
    else:
        zs1 = seven
elif m1 == "october":
    if d1 <= 22:
        zs1 = seven
    else:
        zs1 = eight
elif m1 == "november":
    if d1 <= 21:
        zs1 = eight
    else:
        zs1 = nine
elif m1 == "december":
    if d1 <= 21:
        zs1 = nine
    else:
        zs1 = ten
elif m1 == "january":
    if d1 <= 19:
        zs1 = ten
    else:
        zs1 = eleven
elif m1 == "february":
    if d1 <= 18:
        zs1 = eleven
    else:
        zs1 = twelve
else:
    zs1 = "Invalid month"

print(f"{p1}'s zodiac sign is {zs1}")

if m2 == "march":
    if d2 >= 21:
        zs2 = one
    else:
        zs2 = twelve
elif m2 == "april":
    if d2 <= 19:
        zs2 = one
    else:
        zs2 = two
elif m2 == "may":
    if d2 <= 20:
        zs2 = two
    else:
        zs2 = three
elif m2 == "june":
    if d2 <= 21:
        zs2 = three
    else:
        zs2 = four
elif m2 == "july":
    if d2 <= 22:
        zs2 = four
    else:
        zs2 = five
elif m2 == "august":
    if d2 <= 22:
        zs2 = five
    else:
        zs2 = six
elif m2 == "september":
    if d2 <= 22:
        zs2 = six
    else:
        zs2 = seven
elif m2 == "october":
    if d2 <= 22:
        zs2 = seven
    else:
        zs2 = eight
elif m2 == "november":
    if d2 <= 21:
        zs2 = eight
    else:
        zs2 = nine
elif m2 == "december":
    if d2 <= 21:
        zs2 = nine
    else:
        zs2 = ten
elif m2 == "january":
    if d2 <= 19:
        zs2 = ten
    else:
        zs2 = eleven
elif m2 == "february":
    if d2 <= 18:
        zs2 = eleven
    else:
        zs2 = twelve
else:
    zs2 = "Invalid month"

print(f"{p2}'s zodiac sign is {zs2}")

print(p1, "->", zs1)
print(p2, "->", zs2)
