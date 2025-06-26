#10. Matndan raqamlarni ajratish
#Berilgan matndan faqat sonlarni ajrating:
#text = ["apple", "34", "banana", "100", "abc", "75"]
#Natija: `['34', '100', '75']`

text = ["apple", "34", "banana", "100", "abc", "75"]

# num_list = []

# for i in text:
#     if i.isdigit():
#         num_list.append(i)
# print(num_list)      

num = filter(str.isdigit,text)
print(list(num))