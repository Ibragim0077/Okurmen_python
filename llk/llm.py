class Animal:
    type = "dangerous" #атрибут класса
    def __init__(self, name):
        self.name = name # фтрибут объекта


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


ob_1 = Animal("Lion")
ob_2 = Animal("Tiger")
print(ob_1.type)
print(ob_2.type)
print(ob_1.name)
print(ob_2.name)
Animal.type = "DNGEROUS"
print(ob_1.type)
print(ob_1.type)
