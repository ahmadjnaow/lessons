# Задание 1

# def sesons(a):
#     if a == 12 or a == 1 or a == 2:
#         print("Зима")
#     elif a == 3 or a == 4 or a == 5:
#         print("Весна")
#     elif a == 6 or a == 7 or a == 8:
#         print("Лето")
#     elif a == 9 or a == 10 or a == 11:
#         print("Осень")
#     else:
#         print("Некорректный номер месяца ! : ")
# sesons(12)   

# # Задание 2

# def bank(a,years):
#     a = a
#     years = years * (a/10) 
#     print(a + years)
    
# bank(2000,1)

# # Задание 3

# def num(list1,list2):
#     sum_num = sum(list1) + sum(list2)
#     print("Общая сумма:", sum_num)
#     sum_devision = sum_num / 10
#     print("Результат деления на 10:", sum_devision)


# Задание 4
# def number(num):
#     for i in range(num):
#         print(f"{i+1}. 0")
# number(20) 

# Задание 5

# a = ["Astana","alma", "less","kurt","liii"]

# def str_list(list):
#     a = []
#     for value in list:
#         if 'A' not in value and 'a' not in value and 'I' not in value and 'i' not in value:
#             a.append(value)
#     print(a)
# str_list(a)  

#Доп залание         
#1 
# def is_isogram(word):
 
#     word = word.lower()
    
   
#     letters = set()
    
    
#     for letter in word:
       
#         if letter in letters:
#             return False
       
#         letters.add(letter)
    
   
#     return True
# is_isogram("Hello world")

# 2
# def reverse_integer(n):
#     reversed_n = int(str(n)[::-1])  
#     print(reversed_n)
# reverse_integer(56)

#3
# def chat_bot():
#     while True:
#         user_input = input("Вы: ")
        
#         if not user_input:
#             print("Бот: Как классно, когда ты молчишь. Продолжай в том же духе!")
#         elif user_input.isupper():
#             print("Бот: Успокойся")
#         else:
#             print("Бот: Конечно!")

# chat_bot()