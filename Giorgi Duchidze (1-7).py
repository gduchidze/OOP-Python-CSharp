#Task 1
# class Rectangle:
#     def __init__(self, width, height, color):
#         self.width = width
#         self.height = height
#         self.color = color
#
#     def perimeter(self):
#         return 2*(self.width+self.height)
#     def area(self):
#         return self.width * self. height
# obj1 = Rectangle(5, 1, 'Blue')
# obj2 = Rectangle(3, 3, 'Green')
# obj3 = Rectangle(7, 3, 'Purple')
# print(obj1.area())

#task2
# class Car:
#     def __init__(self, color, model, makeYear, fuelType):
#         self.color = color
#         self.model = model
#         self.makeYear = makeYear
#         self.fuelType = fuelType
#     def __str__(self):
#         return f'Car Color - {self.color}, Car Model - {self.model}, Car Makeyear - {self.makeYear},' \
#                f' Car Fuel Type - {self.fuelType}'
# obj1 = Car('Red','Mercedes','2015','Gas')
# obj2 = Car('Blue','BMW','2013','Gas')
# obj3 = Car('Orange','Audi','2009','Disel')
# print(obj1)
# print(obj2)
# print(obj3)

#Task3
# class Dog:
#     def __init__(self, breed, size, age, color):
#         self.breed = breed
#         self.size = size
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         return f' Breed = {self.breed}, Size = {self.size}, Age = {self.age},' \
#                 f' Color = {self.color}'
# obj1 = Dog('Neapolitan Mastiff','Large','5 years','Black')
# obj2 = Dog('Maltese','Small','2 years','white')
# obj3 = Dog('Chow Chow','Medium','3 years','Brown')
# print(obj1)
# print(obj2)
# print(obj3)

#Task4
# class Celsius:
#     def __init__(self, temperature=0):
#         self.__temperature = temperature
#     def get_temp(self):
#         return self.__temperature
#     def set_temp(self, text):
#         self.__temperature = text
#     def del_temp(self):
#         del self.__temperature
#     degree = property(get_temp, set_temp, del_temp )
# obj1 = Celsius('30 °C')
# obj2 = Celsius('35 °C')
# print(obj1.degree)
# print(obj2.degree)

#Task 5
# class BankAccount:
#     def __init__(self, account_name, balance=0):
#         self.__account_name = account_name
#         self.__account_balance = balance
#     def  get_account_name(self):
#         return self.__account_name
#     def set_account_name(self, account_name):
#         self.__account_name = account_name
#     def set__account_balance(self, balance):
#         self.__account_balance = balance
#     def get__account_balance(self):
#         return self.__account_balance
#     def deposit(self, money):
#         self.__account_balance += money
#         print(f"თანხის შეტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {self.__account_balance} ლარი")
#
#     def withrow(self, money):
#         if self.__account_balance >= money:
#          self.__account_balance -= money
#          print(f"თანხის გამოტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {self.__account_balance} ლარი")
#         else:
#             print("არასაკმარისი თანხაა")
#
#
# account = BankAccount("Giorgi Abashidze")
# print("კლიენტის სახელი და გვარი:", account.get_account_name())
# money = 100
# account.set__account_balance(money)
# print("რა თანხა გაქვთ ამჟამად ანგარიშზე?", account.get__account_balance())
# print("შეიტანეთ შესაბამისი კოდი რომელი ოპერაციის შესრულებაც გსურთ: თანხის შეტანა 1, თანხის გამოტანა 2"       )
# answer = int(input("თანხის შეტანა 1, თანხის გამოტანა 2 "))
#
# if answer == 1:
#     money2 = int(input("რა თანხის შეტანა გსურთ? "))
#     print(money2
#           )
#     (account.deposit(money2))
#     print("თანხის შეტანა შესრულებულია. ")
#
# elif answer ==2:
#     money3 = int(input("რა თანხის გამოტანა გსურთ? "))
#     print(money3)
#     (account.withrow(money3))

#Task7

# import math
#
# class Point:
#   def __init__(self, x=0, y=0):
#     self.__x = x
#     self.__y = y
#
#   def __str__(self):
#     return f'({self.__x}, {self.__y})'
#
#   def formula(self, other):
#     return math.sqrt((other.__x - self.__x) ** 2 + (other.__y - self.__y) ** 2)
#
# obj1 = Point(int(input("x1 = ")), int(input("y1 = ")))
# obj2 = Point(int(input("x2 = ")), int(input("y2 = ")))
#
# print(f" {obj1} და {obj2} წერტილს შორის მანძილი არის  {obj1.formula(obj2)} .")


















































