# Foydalanuvchining email manzili @ bilan boshlanmasligi va .com bilan tugashini tekshiring

text = input("Email kiritng: ")

email = text.endswith(".com") and text[0] != "@"

print(email)