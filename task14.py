#14. list.sort bilan joyida o'zgartirish
#Quyidagi ro’yxatni uzunlik bo‘yicha joyida sort qiling:
#words = ["sun", "mountain", "a", "apple"]
#list.sort(key=lambda ...)` ishlatilishi kerak.

words = ["sun", "mountain", "a", "apple"]

sort_word = sorted(words,key=lambda x:len(x),reverse=True)

print(sort_word)