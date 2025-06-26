#7. Narxlarni \$ belgisiz olish
#Quyidagi narxlar ro’yxatidan `$` belgisiz faqat raqamlarni ajrating (lambda bilan).
#prices = ["$120", "$340", "$50", "$90"]


prices = ["$120", "$340", "$50", "$90"]

# def yangi_praces(prace):
#     return prace[1:]

# belgisiz_price = list(map(yangi_praces,prices))



belgisiz_price = list(map(lambda x : x[1:],prices))
print(belgisiz_price)