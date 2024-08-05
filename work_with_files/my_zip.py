# a = [1, 2, 3]
# b = [4, 5, 6, 7, 8, 9]
# c = [11, 12]
#
# names = ["Argen", "Aji", "Amantyr"]
# surnames = ["Kenzhegulov", "Turganbaev", "Nurlanbekuulov"]
#
# print(tuple(zip(names, surnames)))
# print(dict(zip(names, surnames)))

a, b = map(int, input().split())
print(tuple(map(lambda x: x ** 2, [i for i in range(a, b, 1)])))


def get_time(tunc):
    def wrapper(/args, **kwargs):
    str_time = datetime.now()
