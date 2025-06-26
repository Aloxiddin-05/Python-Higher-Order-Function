#9. Eng uzoq ismni toping
#`max()` va `lambda` yordamida eng uzun ismni toping:
#names = ["Ali", "Valijon", "Sami", "Diyorbek"]

names = ["Ali", "Valijon", "Sami", "Diyorbek"]

# max_name = names[0]

# for i in names:
#     if len(i) > len(max_name):
#         max_name = i

# print([max_name])

max_name = max(names,key=lambda x:len(x))
print(max_name)