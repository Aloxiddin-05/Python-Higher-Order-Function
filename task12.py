#12. Talabalarni baho bo‘yicha tartiblang
#Baholar bo‘yicha saralash (kichikdan katta):


students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]

sorted_students = list(sorted(students,key=lambda x:x["grade"]))
print(sorted_students)