# Задание 1

# age = int(input("Сколько вам лет ? :"))

# if age < 18 :
#     print("Вы являетесь не совершелетным ! ")
# elif age >= 18 and age < 65:
#     print("Вы являетесь взрослым : ")
# else:
#     print("Вы являетесь пожылым :")

# Задание 2

# num1 = int(input("Введите 1- число :"))
# num2 = int(input("Введите 2- число :"))
# num3 = int(input("Введите 3- число :"))

# if num1 < num2 and num1 < num3 :
#     print("наименьшое число ", num1)

# elif num2 > num1 and num2 > num3 :
#     print("наименьшое число", num2)
# else:
#     print("наименьшое число", num3)

# Задание 3

# my_list = ["Moskow", "Nwe York", "Osh","Astana", "Bishkek","Mikinground", "Не бойся ", "Smack That ","The reel Slim Shaydi","Candy Shop", "Mersedes Benz ", "Tesla","BMW","Tayota","lexsus"]
# my_list.pop(2)
# my_list.pop(7)
# print(my_list)

# Задание 4

# my_list = ["Moskow", "Nwe York", "Osh", "Bishkek","Mikinground", "Не бойся ", "Smack That ", "Mersedes Benz ", "Tesla","BMW","Tayota",]
# my_list.pop(2)
# my_list.pop(7)

# my_list.append("Astana")
# my_list.append("Чай")
# my_list.append("Asu")
# my_list.append("Burger")
# my_list.append("Вода")
# print(my_list)

# Задание 5 
# nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# nums.pop(2)
# nums.pop(15)

# nums.insert(0,5)
# nums.insert(0,9)
# print(nums)

#  Задание 6

# numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8 ,909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3]
# numbers.sort()
# print(numbers)

# Задание 7
 
# numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8 ,909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3]
# numbers.sort()
# numbers.reverse()
# print(numbers)

# Задание 8

# numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8 ,909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3]
# print(numbers.count(2))
# print(numbers.count(5))
# print(numbers.count(3))

# Задание 9 
 
# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# addition = (nums[0] + nums[1])+ (nums[2] + nums[3]) + (nums[4] + nums[5]) + (nums[6] + nums[7]) + (nums[8] + nums[9]) + (nums[10] + nums[11]) + (nums[12] + nums[13]) + (nums[14] + nums[15]) + (nums[16] + nums[17]) + (nums[18] + nums[19])
# output = addition / 20
# print(output)

# Доп задание 
#1 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# min_number = min(numbers) # мин находить наи меньшое значение 
# print("Наименьший элемент:", min_number)

#2
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# min_number = max(numbers) # max находить наи большая  значение 
# print("Наибольший элемент:", min_number)

#3
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# min_number = sum(numbers) # sum находить сумму элеменотов 
# print("Сумма элементов ", min_number)

#4
# playlist = ["Song 1","Song 2","Song 3","Song 4","Song 5","Song 6","Song 7","Song 8","Song 9","Song 10"]
# playlist.remove("Song 4")
# playlist.remove("Song 8")
# playlist.insert(3,"Song 8")
# playlist.insert(7,"Song 4")
# print(playlist)

#5
# nums = [ ]
# for num in range(1,21):
#     nums.append(num)
# for result in nums:
#     if result % 2 == 0 :
#         print(result)