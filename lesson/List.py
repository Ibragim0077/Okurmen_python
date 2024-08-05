# class Cat:
#     name = "Musiya"
#     sge = 2
#
# cat_1 = Cat()
# cat_2 = Cat()
# print(cat_1.name)
# print(cat_1.age)
# cat_2.name =

# class Empooyee:
#     first_name = "Arsen"
#     last_name = "Kenzhgulov"
#     age = 22
#     gender = "Male"
#
#     def get_info(self):
#         print(self.first_name)
#         print(self.last_name)
#         print(self.age)
#         print(self.gender)
#         print()
#
# employee_1 = Empooyee()
# employee_1.get_info()
#
# employee_2 = Empooyee()
# employee_2.first_name = "Ali"
# employee_2.last_name = "Turganbaiev"
# employee_2.age = 15
# employee_2.g
#
# def set_fir_name(self, first_name):
#     self.first_name = first_name
#
# def

# class Point:
#     x = 5
#     y = 4
#
#
# p1 = Point()
# print(p1,__doc__)
# print(dir(p1))
# print(hasattr(p1, 'y'))
# print(getattr(p1, "z", "z attribute not found"))
# setattr(p1, 'z', 10)
#
# print(getattr(p1, 'z'))
# delattr(p1, 'z')
# print(getattr(p1, 'z' 'z attribute not found'))

# """
# getattr(obj, name [, default]) — возвращает значение атрибута объекта;
# hasattr(obj, name) — проверяет на наличие атрибута name в obj;
# setattr(obj, name, value) — задает значение атрибута (если атрибут не существует, то он создается);
# delattr(obj, name) — удаляет атрибут с именем name.
# """
#
# people = []
#
# class Person:
#     first_name = ""
#     last_name = ""
#     email = ""
#     age = 0
#     gender = "Other"
#
#     def get_info(self):
#         print(f'Name: {self.first_name} {self.last_name}')
#         print(f'Email: {self.email}')
#         print(f'Age: {self.age}')
#         print(f'Gender: {self.gender}')
#         print('\n')
#
#     def get_first_name(self):
#         return self.first_name
#
#     def get_last_name(self):
#         return self.last_name
#
#     def get_email(self):
#         return self.email
#
#     def get_age(self):
#         return self.age
#
#     def get_gender(self):
#         return self.gender
#
#     def set_first_name(self, first_name):
#         self.first_name = first_name
#
#     def set_last_name(self, last_name):
#         self.last_name = last_name
#
#     def set_email(self, email):
#         self.email = email
#
#     def set_age(self, age):
#         self.age = age
#
#     def set_gender(self, gender):
#         self.gender = gender
#
#     def add_person(self, first_name, last_name, email, age, gender):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.age = age
#         self.gender = gender
#
#
# def get_all_person():
#     for per in people:
#         per.get_info()
#
#
#
#
#
# while True:
#     print("1. Add person")
#     print("2. Get people")
#     print("3. Exit")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         person = Person()
#         first_name = input("Enter your first name: ")
#         last_name = input("Enter your last name: ")
#         email = input("Enter your email: ")
#         age = int(input("Enter your age: "))
#         gender = input("Enter your gender: ")
#
#         person.add_person(first_name, last_name, email, age, gender)
#         people.append(person)
#
#     elif choice == "2":
#         get_all_person()
#
#     if choice == "3":
#         break

class Car:
    name = 'Merseds-Benz'
    brand = 'CLS'
    year = 2024

    def info(self):
        print(f"Name: {self.name}")
        print(f'Brand: {self.brand}')
        print(f'Year: {self.year}')

car_1 = Car()
car_1.name = "Mersedes-Benz"
car_1.brand = "CLS"
car_1.year = 2024
car_1.info()