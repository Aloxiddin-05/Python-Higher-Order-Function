#6. Email domenlarini ajratish
#Quyidagi email ro’yxatidan faqat `gmail.com` domeniga tegishlilarni ajrating.
#emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]


emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]

# list_email = []
# for i in emails:
#     if i.endswith("@gmail.com"):
#         list_email.append(i)

# print(list_email)

emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]

emails_1 = list(filter(lambda email: email.endswith("@gmail.com"), emails))

print(emails_1)
