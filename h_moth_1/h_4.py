# Задание 1

# it_company = ("Google", "Amazon", "Microsoft")
# it_company_list = list(it_company)
# it_company_list.append("Tesla")
# it_cmpaniy_update = tuple(it_company_list)
# print(it_cmpaniy_update)

# Задание  6

# company = ("Tesala","Apple","Google","Netflix","Meta","OpenAI","Mikrasoft","Amazon","Epam","Alibaba Group","GeeksStudio","HAAD","Bilayn","Huawei","Twitter","intel","Tencent","Xiaomi","PayPal","Uber")

# updated_company = company[:2] + company[9:]

# for element in updated_company:
#     print(element)

# new_elements = ("Придложение", "машины", "Операционная система", "Ноутбуки и телефони", "Исквуственый инетелкт")
# updated_company = updated_company[:2] + new_elements + updated_company[:9]

# print(updated_company)

# for element in updated_company:
#     print(element)

# Задание 2 
# company = ("Tesala","Apple","Google","Netflix","Meta","OpenAI","Mikrasoft","Amazon","Epam","Alibaba Group","GeeksStudio","HAAD","Bilayn","Huawei","Twitter","intel","Tencent","Xiaomi","PayPal","Uber")
# print(company[7])
 
# Задание 3
# company = ("Tesala","Apple","Google","Netflix","Meta","OpenAI","Mikrasoft","Amazon","Epam","Alibaba Group","GeeksStudio","HAAD","Bilayn","Huawei","Twitter","intel","Tencent","Xiaomi","PayPal","Uber")

# list_company = list(company)
# list_company[2] = "Apple"  # Обновляем значение "Google" на "Apple" в списке

# updated_company = tuple(list_company)

# print(updated_company)

# Задание 4
# company = ("Tesala","Apple","Google","Netflix","Meta","OpenAI","Mikrasoft","Amazon","Epam","Alibaba Group","GeeksStudio","HAAD","Bilayn","Huawei","Twitter","intel","Tencent","Xiaomi","PayPal","Uber")

# print(company[1:6])

# Задание 5

# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language', 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3', 'overview')
# print(text_tuple.count("Python"))

# Задание 7

# my_list = []

# for num in range(1,100):
#     my_list.append(num)
# print(my_list)

# Задание 8

# my_list = []

# for num in range(1,1000):
#     my_list.append(num)

# if min(my_list) == 1 and max(my_list) == 1000:
#     print("Список с 1 до 1000")
# elif min(my_list) == 1 and max(my_list) != 100:
#     print("Список с 1 , но не до 1000")
# print(sum(my_list))
 
# Задание 9
# for i in range(1,497):
#     if i % 2 == 0:
#         print(i)

# Задание 10
# while True :
#     a = int(input("Введите первое число : "))
#     b =  int(input("Введите второе  число : "))
#     metod = input(" Что делаем + , - , *, / :")

#     if metod == "+":
#         print(a + b)
#     elif metod == "-":
#         print(a - b)
#     elif metod == "*":
#         print(a * b)
#     elif metod == "/":
#         print(a / b)
# Доп задание
# 1

# import random
# attemps = 5
# while attemps > 0:
#     comp = random.choice(["камень","ножница","бумага"])
#     user = input("Выберите : ")

#     if comp == "камень":
#         if user  == "ножница":
#             print("Вы проиграли комп выбрал ", comp )
#         if user == "бумага":
#             print("Вы выиграли комп выбрал ", comp)
#         if user == "камень":
#             print("Ничья комп выбрал",comp)

#     elif  comp == "бумага":
#         if user  == "камень ":
#             print("Вы проиграли комп выбрал ", comp )
#         if user == "ножница":
#             print("Вы выиграли комп выбрал ", comp)
#         if user == "бумага":
#             print("Ничья комп выбрал",comp)

#     elif  comp == "ножница":
#         if user  == "бумага":
#             print("Вы проиграли комп выбрал ", comp )
#         if user == "камень":
#             print("Вы выиграли комп выбрал ", comp)
#         if user == "ножница":
#             print("Ничья комп выбрал",comp)

#     attemps -= 1
#     print("У вас осталось",attemps,"попыток")  

# print("Игра окончена ") 

# 2

# while True:
#     user = int(input("Введиет ваш восрост : "))
#     if user >= 18 :
#         print("Доступ разрешен")
#         break
#     else:
#         print(" Извините пользование данным ресурсом с 18 лет :")

# 3

# user = input("Введите строку :")                  
# print(user[::-1])   