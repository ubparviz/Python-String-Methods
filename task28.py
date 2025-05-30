# Izoh matnidan “yomon” so‘zlarni olib tashlang, so‘ngra tekshiring.

coment = input("Izoh kiriting: ")
text = coment.lower()
yomon_soz = "bad"
result = text.replace(yomon_soz, "")

print(yomon_soz not in result)