# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.__author = author
#
#     def get_titile(self):
#         return self.title
#
#     def get_author(self):
#         return self.__author
#
#     @property
#     def suthor(self, author):
#         self.__author = author
#
#
# book_1 = Book( "Python", "User")
# print(book_1.title)
# book_1.title = "Java"
# print(book_1.title)
# print(book_1.author)
# book_1.author = "Person"
# print(book_1.author)
#
#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            print("Soory, the age cannot be nagative")
        else:
            self.__age = age



person_1 = Person("John", 25)
print(person_1.age)
person_1.age = 22
print((person_1.age))

class Person:
    def __self__(self, name, age, color):
        self.name = name
        self.age = age
        self.__color = color

    @property
    def age(self):
        return self.__color

    @age.setter
    def age(self, color):
        if color in ['blue', 'blacak', 'white']:
            self.__color = color
        else:
            print("Sorry, the color must be blue, black or white")
            print(f"The dog color can't be {color}")




