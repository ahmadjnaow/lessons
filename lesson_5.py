# Множества (set, frozenset) , Словарьь 

# Повторение 
# number = [2,3,4,5,6,7,8,9,9,]

# sum_number = 0 

# for num in number:
#     sum_number += num

# print(f"Сумма числе: {sum_number}")

# numbers = []

# for i in range(1,44):
#     numbers.append(i) 
# print(numbers)

# Set - это тип данных каторая хранить униекальные типы данных ,  у set нет определонный структура
# int, str , bool , float ,  list, tuple , frozensent, sent 

# a = [1,2,3,4,5]
# b = [3,4,5,6,7]
# print(a +b )

# print(set(a+b)) 

# st = {"Geeks","Osh","Bishkek","IT","Osh"}
# print(st)

# email ={"nurbolot@.gmail.com"}
# print(email)
# email.add("geeks@.gmail.com")  # add -  метод дял побовление оргументов для set 
# print(email)
# email.add("ahmadjanow@mail.ru")
# print(email)
# email.add("Ahmadjnaow@mail.ru")
# print(email)
# email.add("geeks@gmail.com")
# print(email)

# email.add(1)
# print(email)
# email.add("1")
# print(email)
# email.remove("geeks@gmail.com")
# print(email)

# email.remove(1)    # remove - для удаление элементов из set 
# email.remove("1")
# print(email)

# email.pop() # pop - удаляет элементы из set 
# print(email)

# fozentset не изменяемый тип данных 
# frst = frozenset({1,2,3,1,2,4,5,6,})
# print(frst)

# dickchinory - словар 

# user = {" name":"Nurbolot","sorname":"Erkinbaev","age":18}
# print(user)
# print(user[" name"])
# print((user["age"]))
# user["car"] = "Tesla"
# print(user)
# print(user["car"])
# print(user[0])

# user[" name"] = "Bekbolot"
# print(user)
# user.pop("age")  # pop - удаляет элементы из словаря
# print(user)


# name = {"name":"Nurbolot"}
# surname = {"surname":"Erkinbaev"}
# name.update(surname)  # update  - объдиняет две словаря 
# print(name)
# kays = name.keys()  # Ключи словаря 
# print(kays)
# values = name.values() #  Значении словаря 
# print(values)
# items = name.items()   #  элементы словаря 
# print(items)