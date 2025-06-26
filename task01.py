#1. Foydali sonlarni ajratish
#Berilgan ro'yxatdan musbat sonlarni `filter()` yordamida ajrating.
#numbers = [4, -2, 0, 7, -9, 3, -1, 5]

numbers = [4, -2, 0, 7, -9, 3, -1, 5]

def musbat(num):
    return num > 0

number_filter = list(filter(musbat,numbers))
print(number_filter)