#8. Yoshi bo'yicha sortlash
#Quyidagi lug’atdagi odamlarni yosh bo’yicha o’sish tartibida saralang.


people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]

sort_age = list(sorted(people,key=lambda x:x["age"]))
print(sort_age)

