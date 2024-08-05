# class:
#     def __init__(self, x, y):
#         self.x = x # атрибут обекта
#         self.y = y # атрибут обекта
#
#     def ares(self):
#         return self.x * self.y
#
#     @staticmethod
#     def info(a, b):
#         print("Tnis is a ststic method")
#         print(a + b)
#
#
# Shape.info(3, 4)
# ob_1 = Shape(1, 2)
# ob_1.info(3, 4)
# print(ob_1.area())


class Counter:
    count = 0

    def __del__(self, name):
        self.name = name
        Counter.count += 1


    @staticmethod
    def get_count_objects():
        print(f"ALL objects = {Counter.count}")


obj1 = Counter("ob_1")
obj2 = Counter("ob_2")
Counter.get_count_ob()
obj3 = Counter("ob_3")
Counter.get_count_ob()


