# Fayl nomi .pdf, .docx, yoki .txt bilan tugashini tekshiring

text = input("Fayl yarating: ")

result = text.endswith(".pdf") or text.endswith(".docx") or text.endswith(".txt")

print(result)