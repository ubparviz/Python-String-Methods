# Bo‘sh joylarni olib tashlab, satr bo‘sh emasligini tekshiring

text = str.strip(input("Matn kiritng: "))

result = text.startswith(" ") or text.endswith(" ")

print(result)