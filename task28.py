# Izoh matnidan “yomon” so‘zlarni olib tashlang, so‘ngra tekshiring.

text = str.lower(input("Izoh kiriting: "))
yomon_soz = "bad"
result = text.replace(yomon_soz, "")

print(yomon_soz not in result)