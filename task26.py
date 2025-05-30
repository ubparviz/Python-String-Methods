# GitHub usernames faqat a-z, A-Z, 0-9, - dan iborat bo‘lishi kerak, 
# isalpha() bilan tekshirishdan oldin replace("-", "") bilan - belgilarini olib tashlang.

username = input("Usernameni kiriting: ")

replace = username.replace("-","")
result = replace.isalpha()

print(result)