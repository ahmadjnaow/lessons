#  Оброботчин ошибок Try Exept , *args, **kwargs 

# try, exsept 
# args, kwargs 
# def name(num1,num2):
#     try:
#         print(num1/num2)
#     except ZeroDivisionError:
#         print("На 0 делить нельзя ! :")

# name(101,0)


# def calculator(num1, num2, a):
#     try:
#         if a == "+":
#             return num1 + num2
#         elif a == "-":
#             return num1 - num2
#         elif a == "*":
#             return num1 * num2
#         elif a == "/":
#             if num2 == 0:
#                 return "На 0 делить нельзя"
#             else:
#                 return num1 / num2
#         else:
#             return "Error"
#     except TypeError:
#         return "Нельзя использовать буквы!"

# # Пример использования
# result = calculator(10, 5, "+")
# print(result)  # Выведет: 15

# result = calculator(10, 0, "/")
# print(result)  # Выведет: "На 0 делить нельзя"

# result = calculator(10, 5, "^")
# print(result)  # Выведет: "Error"



# def lister(objekt1,objekt2,objekt3,objekt4,objekt5,objekt6,objekt7,objekt8,objekt9,objekt10):
    
#     list1 = []
#     list1.append(objekt2)
#     list1.append(objekt3)
#     list1.append(objekt4)
#     list1.append(objekt5)
#     list1.append(objekt6)
#     list1.append(objekt7)
#     list1.append(objekt8)
#     list1.append(objekt9)
#     list1.append(objekt10)
#     print(list1)
# lister("NUrbolot","Hikmatillo","Mergul","Aida","Sohiba","Nuriddin","Anas","Zikirullo","Saud","Akmal")

# def lister(*name):
#     list1 = []
#     for result in name:
#         list1.append(result)
#     print(list1)
# lister("NUrbolot","Hikmatillo","Mergul","Aida","Sohiba","Nuriddin","Anas","Zikirullo","Saud","Akmal")

# def pizza(*ing):

#     for result in ing:
#         print(f"Вы добавили в питсу {result}")
# pizza("майанез","сыр","граыбы","майанез")

# def make_pizza(**Kwargs):
#     for key , value  in Kwargs.items():
#         print(f'Размер - {value}. Адрес - {value}')
# make_pizza(size = "большой", addres = "Geeks" )

