#2. Har bir sonni kvadratga oshiring
#`map()` yordamida quyidagi ro'yxatdagi har bir sonni kvadratga oshiring.
#nums = [1, 2, 3, 4, 5]

nums = [1, 2, 3, 4, 5]

# def map_nums(num):
#     return pow(num,2)

# kvadrat = list(map(map_nums,nums))
# print(kvadrat)

num_lambda = list(map(lambda x:pow(x,2),nums))
print(num_lambda)