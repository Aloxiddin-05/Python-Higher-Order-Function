#11. Juft sonlarning kvadratlari
#Faqat juft sonlarni tanlab, ularning kvadratlarini `filter()` + `map()` bilan hisoblang.
#nums = list(range(1, 21))

nums = list(range(1, 21))

filter_num = filter(lambda x: x%2 == 0,nums)

kvadrat = list(map(lambda x: pow(x,2),filter_num))

print(kvadrat)