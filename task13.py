#13. Top 3 eng uzun so‘z
#Matndagi eng uzun 3 ta so‘zni toping:
#sentence = "Functional programming in Python is very powerful and elegant"
#Foydalaning: `sorted()`, `lambda`, `split()`, `[:3]`

sentence = "Functional programming in Python is very powerful and elegant"
result = sentence.split(" ")

sort_word = sorted(result,key=lambda x:len(x),reverse=True)[:3]
print(sort_word)

