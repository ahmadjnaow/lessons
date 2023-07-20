# Tuple(картеж ) , Цикл 

# names = ("Nurbolot", "Жаныш", "Adina","Hikmatillo") # кортеж
# surname = ["Nurbolot", "Жаныш", "Adina","Hikmatillo"] # лист 
# print(names)
# print(surname)
# surname.remove("Nurbolot")   # В листе можно удалить эленменты лист изменяемы тип данных 
# names.remove("Nurbolot")   # В кортеже не можем удалить так как он не изменяемый тип данных 
# print(surname) 
# print(names)

# dats = ("Лето")
# data = ("Лето",)

# print(type(dats))
# print(type(data))       #  Определяем тип данных 

# data = tuple("Осень")
# print(type(data))

# data = (2023, "Hikmatillo","Ahmadjanow","Danayrjnaovich", 15, 4.5,True)
# print(f"Здраствуйте {data[2]} {data[1]} {data[3]} \n Вам {data[0]} испольниться {data[4]}")  #  Выводим текст "Здраствуйте Хикматиллло Ахмаджанов 
#                                                                                                     # вам 15 испольнится "
# print('Hello world. I\'m backend developer' )


# while True:  #  Бесконечный цикл программы для определение времени года 
#     data = ("Лето","осень","Зима","Весна")
#     user = int(input("Ввелите число от 1 до 12 "))

#     if user == 12 or user == 1 or user == 2 :
#         print(data[2])
#     elif user == 3 or user ==  4 or user == 5 :
#         print(data[3])
#     elif user == 5 or user ==  6 or user == 7 or user == 8 :
#         print(data[0])
#     elif user == 9 or user ==  10 or user == 11:
#         print(data[1])
#     else:
#         print("Ошибка")

# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# for i in numbers:
#     if i % 2 == 0:
#         print(i)
#     else:
#         print("Не делиться")

# for numbers in range(1,6):
#     print(numbers)

# for hello in range(100):
#     print("Hello world")

# name = "Nurbolot"
# for n in name:
#     print(n) 


# count = 0 
# while count < 1000000000000:
#     print(count)
#     count += 1 
