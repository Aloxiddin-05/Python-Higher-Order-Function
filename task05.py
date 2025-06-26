#5. `lambda` bilan ko'paytirish
#Har bir elementni 5 ga ko'paytirish uchun `map()` va `lambda`dan foydalaning.
#nums = [2, 4, 6, 8]

nums = [2, 4, 6, 8]

# def kopaytirish(num):
#     return num * 5

# kop_num = list(map(kopaytirish,nums))
# print(kop_num)

kopaytirish = list(map(lambda n:n*5,nums))
print(kopaytirish)