# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.__balance = balance
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self, balance):
#         self.__balance = balance
#
#     def deposit(self, amount):
#         self.__balance += amount
#
#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("Amount cannoy be greater than balance.")
#         else:
#             self.__balance -= amount
#
#     def get_blance(self):
#         return self.__balance
#
#
# bo_1 = BankAccount('123')
# bo_2 = BankAccount('456',100)
#
# bo_1.deposit(200)
# bo_2.deposit(50)
# print(bo_1.deposit)
# print(bo_2.deposit)
# bo_1.withdraw(100)
# bo_2.withdraw(100)
# print(bo_1.balance)
# print(bo_2.balance)
# bo_1.withdraw((200))
# bo_2.withdraw((200))
# print(bo_1.balance)
# print(bo_2.balance)

# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#
#     class Employee(Person):
#         def __init__(self, name, work):
#             super().__init__(name)
#             self.__work =work
#
#     @property
#     def work(self):
#         return  self.__work
#
#
# employee__1 = Employee(name ='Arsen',work = "IT")
# print(employee__1.name)
# employee__1.name == 'Ali'
# print(employee__1.work)
# person_1 = Person("John")
# print(person_1.name)


class Empioyee:
    def  __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def disply(self):
        print(self.name, self.salary)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class WorkingStudent(Empioyee, Student):
    def __init__(self, name, age, salary):

        Empioyee.__init__(self, name, salary)
        Student.__init__(self, name, age)


workingStudent = WorkingStudent('Jack', 25, 10000)
workingStudent.disply()
print(WorkingStudent.__init__())
print(WorkingStudent.mro())