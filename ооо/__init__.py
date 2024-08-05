class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")


tom = Person("Ибагим", 17)
tom.display_info()

bob = Person("Акбар",17 )
bob.display_info()

