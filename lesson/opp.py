# a: int = 5
# a = "Bishkek"
# print(a)
# import random

# def get_info(name: str, age: int) -> str:
#     print(name)

# import random
# a, b = map(int, input().split())
# if a > b:
#     print("b > a")
# else:
#     print(age)
# #     return f'{name} is {age} years old'
# #
# # print(get_info.__annotations__)
# #
# # def get_sum(nums: dict[int, str]) -> int:
# #     return  sum(nums)
# #
# #
# # get_sum({i: "one", 2: "two"})
# #
# #
# #
# # get_info(name: "Arsen", age 4)
# #     print(random.randint(a, b))
# #
#
# # cities = [i for i in input().split()]
# # count = int(input())
# # print(random.sample(cities, count))
#
# # data = 10
# #
# # if isinstance(data, str):
# #     print("Bul dat str tibinde")
# # elif isinstance(data, int):
# #     print("bul bat int tibnide")
# # elif isinstance(data, float):
# #      print("bul bat float tibinde")
# # elif
#
# n, m = map(int, input().split())
#
# numbers = [
#      [int(i) for i in input().split()]
#      for j in range(n)
# ]
#
# res_sum = []
# for j in range(n):
#     s = 0
#     for f in range(m):
#         s += numbers[j][j]
#     res_sum.append(s)
# print(*res_sum)
#
# n, m = map(int, input().split())
#
# numbers = [
#      [int(i) for i in input().split()]
#      for j in range(n)
# ]
#
# res_sux = []
# res_sin = []
# for i in range(n):
#     res_sux.append(max(numbers[i]))
#     res_sin.append((min(numbers[i])))
# print