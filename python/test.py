# name = "John Smith"
# age = 20
# new_patient = True
# if new_patient:
#     print(name, age)

# birth_year = input("What year were you born? ")
# age = 2024 - int(birth_year)
# print("You are " + str(age) + " years old.")

# lbs = input("What is your weight in lbs? ")
# kgs = float(lbs) / 2.20462
# print("You weight " + str(kgs) + " kilograms")

# weight = input("Enter weight: ")
# unit = input("(L)bs or (K)g: ")
# if unit.lower() == "l":
#     kg = int(weight) / 2.020462
#     print(f"Your weight is {kg} kilograms.")
# elif unit.lower() == "k":
#     lbs = int(weight) * 2.020462
#     print(f"Your weight is {lbs} pounds")
# else:
#     print("Error!")

# course = '''
# - Hola Juan!
# - Hola Esteban!
# - Donde esta esa biblioteca?
# - Esta es la casa de mi tia.
# - No, gracias. Soy alergico a los crustancios.
# '''
# if course[-4] == "o":
#   print(True)
# else:
#   print(False)

# char = input("Please enter 10 characters or less: ")
# while len(char) > 10:
#     print("Character limit exceeded")
#     char = input("Please enter 10 characters or less: ")
# else:
#     print(char)

# course = "Let's get it started!"
# print(len(course))
# print(20 - course.find("start"))
# print(course.replace("start", "finish"))
# print("started" in course)

# # Math:
# x = 10
# x += 3
# x //= 3
# print(x)
# import math
# print(math.sqrt(5.6))

# # Temperature:
# temperature = 11
# if temperature > 35:
#     print("It's a hot day, dress lightly")
# elif 15 < temperature <= 20:
#     print("It's a chilly day, wear warm clothes")
# elif temperature < 15:
#     print("It's cold outside, stay really worm")
# else:
#     print("It's a nice weather, wear whatever you want")
# print("Have a nice day")

# # Down payment:
# price = 1000000
# credit = "good"
# if credit == "good":
#     down_payment = price * 0.1
# else:
#    down_payment = price * 0.2
# print(f"Down payment: ${down_payment}")

# # Loan:
# high_income = True
# good_credit = True
# criminal_record = True
# if high_income and good_credit and not criminal_record:
#     eligible = True
# elif (high_income or good_credit) or (not criminal_record or high_income) or (not criminal_record or good_credit):
#     eligible = "Needs further inspection"
# else:
#     eligible = False
# print(f"Eligible for loan: {eligible}")

# # Temperature converter:
# celsius = 21
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius} Celsius is {fahrenheit} Fahrenheit")

# # Characters length:
# name = input("Enter your name: ")
# if len(name) < 3:
#     print("Name should be at least 3 characters long.")
#     input("Enter a different name: ")
# elif len(name) > 50:
#     print("Name should be 50 characters max.")
#     input("Enter a different name: ")
# else:
#     print("Nice name!")

# Guessing game:
# number = 2
# guess_count = 0
# guess = int(input("Guess the number from 1 to 9: "))
# while guess_count < 3:
#     guess_count += 1
#     if guess == number:
#         print("You won!")
#         break
#     guess = int(input("Guess again: "))
# else:
#     print("You lost!")
    
# # Car game:
# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start" and started == False:
#         print("Car started.")
#         started = True
#     elif command == "start" and started:
#         print("Car is already started...")
#     elif command == "stop" and started:
#         print("Car stopped.")
#         started = False
#     elif command == "stop" and started == False:
#         print("Car is already stopped...")
#     elif command == "help":
#         print('''start - start the car.
# stop - stop the car.
# quit - end the game.''')
#     elif command == "quit":
#         print("Game Over!")
#         break
#     else:
#         print("Sorry, me no understand...")

# # For loop:
# prices = [10, 20, 30, 40, 50]
# total = 0
# for i in prices:
#     total += i
# print(f"Total price is {total}")

# # Nested for loop:
# for i in range(4):
#     for j in range(3):
#         print(f"({i}, {j})")

# numbers = [2, 2, 2, 2, 6]
# for i in numbers:
#     output = ''
#     for count in range(i):
#         output += "X"
#     print(output)

# # Lists:
# names = ["Juba", "Kote", "Zura", "Vaja"]
# names[0] = "Jumber"
# print(names[0:3])
# numbers = [1, 21, 6, 321, 5632, 123, 456, 654, 5, 1548]
# largest = 0
# for i in numbers:
#     if i > largest:
#         largest = i
# print(largest)

# # 2D lists:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0][2])
# for i in matrix:
#     for j in i:
#         print(f"{j} sheep")
# print("10")

# # List methods:
# numbers = [5,3,4,8,5,2,9,1,7,6]
# numbers.append(2)
# print(numbers)
# numbers.insert(2, 6)
# print(numbers)
# numbers.remove(8)
# print(numbers)
# print(numbers.index(9))
# print(5 in numbers)
# print(numbers.count(5))
# numbers.sort()
# numbers.reverse()
# print(numbers)
# numbs = numbers.copy()
# numbers.clear()
# print(numbers)

# numbers = [2,4,6,4,2,1,5,7,9,8,3,2,1,5,6,8]
# uniques = []
# for i in numbers:
#     if i not in uniques:
#         uniques.append(i)
#         uniques.sort()
# print(uniques)

# # Tuples:
# numbers = (1,5,3,4,6,2,8,7,9)
# numbers.count(5)
# numbers.index(2)
# Unpacking:
# coordinates = (1, 2, 3)
# x, y, z = coordinates
# names = ["Katia", "Lapsha", "Ucha", "Zako"]
# a, b, c, d = names
# print(b)

# # Dictionaries:
# customer = {
#     "name": "Amiran Kotia",
#     "age": 27,
#     "email": "amo@gmail.com",
#     "verified": True
# }
# customer["age"] = 28
# customer["gender"] = "male"
# print(customer.get("age"), customer.get("gender"))

# #  Numbers converter:
# phone = input("Phone: ")
# numbers = {
#     "0" : "Zero",
#     "1" : "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = ""
# for i in phone:
#     output += numbers.get(i) + " "
# print(output)

# # Emoji converter:
# def converter():
#     separator = user.split()
#     emojis = {
#         ":)": "🙂",
#         ":(": "🙁",
#         ":D": "😄",
#         ";)": "😉",
#         ":/": "😕",
#         "X(": "😣",
#         ":X": "😘",
#         ":P": "😋"
#     }
#     output = ""
#     for i in separator:
#         output += emojis.get(i, i) + " "
# user = input("> ")
# converter()
# print(output)

# # Functions:
# def greeting(name, surname):
#     print(f"Hi there {name} {surname}!")
#     print("Welcome!")
# print("Start")
# greeting("Sam", "Sonia")
# # Keyword argument:
# greeting(surname="Makua", name="Saba")
# print("Finish")

# def square(number):
#     return number*number
# print(square(3))

# Handling errors:
# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(risk)
# except ValueError:
#     print("Invalid value")
# except ZeroDivisionError:
#     print("Age can't be 0")


# # Davaleba 1:
# number1 = 56
# number2 = 13
# number3 = 941
# sum = number1 + number2 + number3
# print(sum)

# # Davaleba 2:
# celsius = 30
# fahrenheit = (celsius * 9/5) + 32
# print(fahrenheit)

# # Davaleba 3:
# length = int(input("შეიყვანეთ კუბის გვერდის სიგრძე: "))
# surface_area = length ** 2 * 6
# volume = length ** 3
# print(f"ამ კუბის ზედაპირის ფართობი არის {surface_area} სანტიმეტრი, ხოლო მოცულობა {volume} კუბური სანტიმეტრი.")


# # Quiz game:
# print("Welcome to the quiz game!")
# def quiz():
#     question = input("Do you want to play my game? yes / no ").lower()
#     score = 0
#     if question == "yes":
#         print("Okay, let's play! 😈")
#         answer1 = int(input("How old is the bible? "))
#         if answer1 == 2000:
#             score += 1
#         answer2 = int(input("What year was John Doe killed? "))
#         if answer2 == 1964:
#             score += 1
#         answer3 = int(input("What is an average person's lifespan? "))
#         if answer3 == 70:
#             score += 1
#         answer4 = int(input("How many continents are there on Earth? "))
#         if answer4 == 7:
#             score += 1
#         answer5 = int(input("In what year did the Titanic sink? "))
#         if answer5 == 1912:
#             score += 1
#         answer6 = int(input("What is the boiling point of water in degrees Celsius? "))
#         if answer6 == 100:
#             score += 1
#         answer7 = int(input("How many bones are there in the adult human body? "))
#         if answer7 == 206:
#             score += 1
#         answer8 = int(input("How many planets are there in our solar system? "))
#         if answer8 == 8:
#             score += 1
#         answer9 = int(input("If a farmer has 30 sheep and all but 20 die, how many are left? "))
#         if answer9 == 20:
#             score += 1
#         answer10 = int(input("How many months have 28 days? "))
#         if answer10 == 12:
#             score += 1
#         if score > 5:
#             print(f"You passed the test with {score/10*100}%. You shall live 🙂")
#         else:
#             print(f"You scored {score/10*100}% and failed the test. Good luck in the afterlife 👹")
#     else:
#         again = input("Are you sure? ").lower()
#         if again != "yes":
#             quiz()
#         else:
#             print("Maybe next time...🥱")
# quiz()

# # Guess random number:
# import random
# random_number = random.randrange(11)
# guess_count = 0
# print(random_number)
# while guess_count < 3:
#     if guess_count == 0:
#         guess = int(input("Guess a number from 0 to 10. You have 3 tries: "))
#     else:
#         guess = int(input("Guess again: "))
#     if guess == random_number:
#         print("You guessed right!")
#         print("You won!!!")
#         break
#     print("Wrong!")
#     guess_count += 1
# else:
#     print("You lost.")
#     print("Better luck next time.")





# # Saklaso 1:
# balance = 300
# tax = 5
# withdraw = float(input("რა თანხის განაღდება გსურთ? "))
# tax_added = (withdraw / 100 * tax)
# if balance >= withdraw + tax_added:
#     print(f"თქვენ დაგემატათ მოხმარების საკომისიო 5%. დარჩენილი ბალანსია {balance - (withdraw + tax_added)} ლარი")
# elif balance - (withdraw + tax_added) <= 0:
#     print("თქვენ არ გაქვთ საკმარისი ბალანსი ანგარიშზე.")


# # Saklaso 2:
# num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
# num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
# operator = input("შეიყვანეთ მათემატიკური ოპერატორი: ")
# if operator == "+":
#     print(f"პასუხია: {num1 + num2}")
# elif operator == "-":
#     print(f"პასუხია: {num1 - num2}")
# elif operator == "/":
#     print(f"პასუხია: {num1 / num2}")
# elif operator == "*":
#     print(f"პასუხია: {num1 * num2}")
# elif operator == "**":
#     print(f"პასუხია: {num1 ** num2}")
# elif operator == "%":
#     print(f"პასუხია: {num1 % num2}")
# elif operator == "//":
#     print(f"პასუხია: {num1 // num2}")
# else:
#     print("ამოუცნობი ოპერატორი.")


# # Davaleba 1:
# grade = float(input("შეიყვანეთ მოსწავლის ქულა: "))
# if grade >= 91:
#     print("შეფასება: A")
# elif grade >= 81 and grade <= 90:
#     print("შეფასება: B")
# elif grade >= 71 and grade <= 80:
#     print("შეფასება: C")
# elif grade >= 61 and grade <= 70:
#     print("შეფასება: D")
# elif grade >= 51 and grade <= 60:
#     print("შეფასება: E")
# elif grade <= 50:
#     print("შეფასება: F")


# # Davaleba 2:
# number = int(input("Please write a number: "))
# if number % 2 == 0:
#     print("This number is even.")
# elif number % 2 == 1:
#     print("This number is odd.")
# else:
#     print("Please write a number.")


# # Davaleba 3:
# text = input("Please write any text: ")
# contains = ["small", "tall", "middle"]
# for word in text.split():
#     if word in contains:
#         print(word)
#         break
# else:
#     print("The words 'small', 'tall' and 'middle' are not in the text.")


# for i in range(10, 1-1, -1):
#     print(i)

# number = 0
# for _ in range(10):
#     number += 1
#     print(number)


# # Saklaso 1:
# while True:
#     num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
#     num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
#     operator = input("შეიყვანეთ მათემატიკური ოპერატორი: ")
#     if operator == "+":
#         print(f"პასუხია: {num1 + num2}")
#     elif operator == "-":
#         print(f"პასუხია: {num1 - num2}")
#     elif operator == "/":
#         print(f"პასუხია: {num1 / num2}")
#     elif operator == "*":
#         print(f"პასუხია: {num1 * num2}")
#     elif operator == "**":
#         print(f"პასუხია: {num1 ** num2}")
#     elif operator == "%":
#         print(f"პასუხია: {num1 % num2}")
#     elif operator == "//":
#         print(f"პასუხია: {num1 // num2}")
#     elif operator == "exit":
#         print("კალკულატორი გამოირთო.")
#         break
#     else:
#         print("ამოუცნობი ოპერატორი.")


# # Davaleba 1:
# total_sum = 0
# while True:
#     number = input("Write a number: ")
#     if number == "sum":
#         print(f"Total sum: {total_sum}")
#         break
#     elif int(number) > 0:
#         total_sum = total_sum + int(number)



# # Davaleba 2:
# total_sum = 0
# while True:
#     number = int(input("Write a number: "))
#     if number == 0:
#         print(f"Total sum: {total_sum}")
#         break
#     elif int(number) > 0:
#         total_sum = total_sum + int(number)



# # Davaleba 3:
# import random

# rand = random.randint(1, 10)
# number = int(input("გამოიცანით ციფრი 1-დან 10-ის ჩათვლით: "))
# count = 0
# while True:
#     if number == rand:
#         print(f"თქვენ გამოიცანით ციფრი: {rand}")
#         count += 1
#         break
#     else:
#         if rand > number:
#             print("შეყვანილი ციფრი ნაკლებია ჩაფიქრებულ ციფრზე.")
#             number = int(input("ხელახლა სცადეთ: "))
#             count += 1
#         elif rand < number:
#             print("შეყვანილი ციფრი მეტია ჩაფიქრებულ ციფრზე.")
#             number = int(input("ხელახლა სცადეთ: "))
#             count += 1
# print(f"{count} ცდაში.")


# text = input("Enter text: ")
# # count = text.count("is")
# # print(f"'is' is used {count} times in the text.")
# count = 0
# for i in text.split():
#     if "is" in i:
#         count += 1
# print(count)


# # Davaleba 1(04.03.24):
# text = input("Please enter text: ")
# polyndrom = ""
# for i in reversed(text):
#     polyndrom += i
# if polyndrom == text:
#     print(True)
# else:
#     print(False)


# # Davaleba 2:
# text = input("Please enter text: ")
# for i in text:
#     ascii_value = ord(i)
# print(f"The ASCII value of your text is {ascii_value}")



# # Lists(04.03.24):
# a = [1,2,3,4,5,6,7,8,9]
# b = [11,12,13,14,15,16,17,18,19]
# c = a+b
# print(c)

# lst = [x for x in range(1,11)]
# print(lst)

# lst = [[1, 2, 3], 
#        [4, 5, 6], 
#        [7, 8, 9]
#        ]
# lst[0][1] = .2

# print(lst)


# lst = [1,2,5,4,6,7,8,5,1,3,5,4,8]
# sum = 0
# for i in lst:
#     sum += i
# print(sum)

# lst = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9 , 12, 34, 49]
# sum = lst[2] + lst[8] + lst[13]
# print(sum)

# import random

# lst = ["book", "table", "chair", "TV", "couch"]
# rand = random.choice(lst)
# for i in lst:
#     print(i)
# guess = input("Guess the word from the list: ")
# while True:
#     if guess.lower() == rand.lower():
#         print("You won!")
#         break
#     else:
#         print("Wrong")
#         guess = input("Guess again: ")



# # Saklaso 06/03 (functions and methods):
# numbers = [1,34,12,123,5,23,234,124,53]
# print(sum(numbers))

# import math

# print(math.ceil(math.sqrt(5)))

# print(math.pow(12, 3))

# rad = math.radians(180)
# print(rad)

# cos = math.cos(100)
# print(cos)

# # amat erti da igive funkcia akvs, abrunebs dadebitad mititebul ricxvs
# x = math.fabs(-20)
# y = abs(-20)

# # yvelaze didi saerto gamyofis povna:
# x = math.gcd(12, 20, 40)
# print(x)

# # faqtorialis gamotvla:
# x = math.factorial(10)
# print(x)

# def square(x):
#     return x ** 2    
# print(square(565))


import math

# def fact(x):
#     return math.factorial(x)
# x = int(input("Write a number: "))
# print(fact(x))

# numbers = [2,412,123,4132,5,124,123,25,234]
# def summ():
#     return sum(numbers)
# print(summ())

    
# def fib(n):
#     lst = [0, 1]
#     for i in range(2, n):
#         next = lst[-1] + lst[-2]
#         lst.append(next)
#     return lst

# print(fib(10))


# # # Davaleba 1:
# import random

# lst = ["book", "table", "chair", "TV", "couch"]
# rand = random.choice(lst)
# for i in lst:
#     print(i)
# guess = input("Guess the word from the list: ")
# while True:
#     if guess.lower() == rand.lower():
#         print("You won!")
#         break
#     else:
#         print("Wrong")
#         guess = input("Guess again: ")



# # # Davaleba 2:
# my_list = [43, '22', 12, 66, 210, ["hi"]]
# # a.
# print(my_list.index(210))
# # b.
# my_list.append("hello")
# print(my_list)
# # c.
# del my_list[2]
# print(my_list)
# # d.
# my_list_2 = [54, 456, 87, ["hello", "bye"], True, "Hi"]



# # # Davaleba 3:
# mtrx = [
#     [5, 6, 7],
#     [3, 9, 1],
#     [8, 4, 2]
# ]
# transposed = []
# for i in range(len(mtrx[0])):
#     new_row = []
#     for j in range(len(mtrx)):
#         new_row.append(mtrx[j][i])
#     transposed.append(new_row)
# for row in transposed:
#     print(row)


# # Davaleba:
# def square(num1, num2, num3, num4):
#     lst = [num1, num2, num3, num4]
#     return lst[0] ** 2, lst[1] ** 2, lst[2] ** 2, lst[3] **2
# print(square(2, 8, 5, 7))



# # 11.03 saklaso:
# def main(*args):
#     return args
# for i in main("s", "S", "112"):
#     print(i)

# # Unpacking and wrapping:
# def main(name, age):
#     print("Name:" , name, "Age:" , age)
# lst = ["Amo", 27]
# main(*lst)


# def main(*value):
#     total = sum(value)
#     return total
# print(main(10,20,12,434,134,120,9))


# def calc(*value):
#     total = sum(value)
#     average = total / len(value)
#     return total, average
# new_total, new_average = calc(1,2,3,4,5,6,7,8,9)
# print(new_total)
# print(new_average)


# def circle_area(pi):
#     def whole_area(radius):
#         return pi * radius ** 2
#     return whole_area
# func = circle_area(math.pi)
# print(func(3))


# def fact(num):
#     if num <= 1:
#         return 1
#     else:
#         return num * fact(num - 1)
# print(fact(5))



# def nums(n):
#     if n >= 1:
#         print(n)
#         return nums(n - 1)
# print(nums(7))


# gl_str = 'global'
# def local():
#     gl_str = "local"
#     return gl_str
# print(local())


# int_list = [10,20,30]
# def local(num):
#     int_list.append(num)
#     return int_list
# print(local(40))



# # Need explanation how this def work
# import random

# arr = [i for i in range(1,31)]
# random.shuffle(arr)
# print(arr)

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr

# print(bubble_sort(arr))


# import random

# arr = [i for i in range(1,31)]
# random.shuffle(arr)
# print(arr)

# def select_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr

# print(select_sort(arr))


# def even_or_odd():
#     number = int(input("Please write any number: "))
#     if number%2 == 0:
#         print(f"The number {number} is even.")
#     else:
#         print(f"The number {number} is odd.")
#     return number

# even_or_odd()


# # Davaleba 7 20/03/24
# def print_pettern(num):
#     for i in range(1,num+1):
#         for j in range(1,i+1):
#             print(j, end = "")
#         print()

# print_pettern(10)



# # Davaleba 1:
# try:
#     number = int(input("Please write a number: "))
#     print("Correct!")
# except ValueError:
#     print("Error! Your input is not a number.")    



# # Davaleba 2:
# def divide(num1, num2):
#     equasion = num1/num2
#     return equasion

# num1 = int(input("Type the first number: "))
# num2 = int(input("Type the second number: "))
# print(divide(num1, num2))



# # Davaleba 3:


# Leqcia 10, 20/03/24:
# import random

# x = [i for i in range(1,100)]
# random.shuffle(x)
# print(x)


# lst = ["kote", "gia", "vaja"]

# for i, value in enumerate(lst):
#     print(i, value)


import random

# x = [i for i in range(1,10)]
# random.shuffle(x)

# print(x)
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
    
#     return -1

# print(linear_search(x, 3))


# baza = [[1, "it"], [2, "step"], [3, "academy"]]

# def linear_search(arr, target):
#     for key, value in enumerate(arr):
#         if value[1] == target:
#             return key
        
# print(linear_search(baza, "academy"))



# Binary search:
# x = [i for i in range(1,10)]

# print(x)

# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1

#         else:
#             high = mid - 1
#     return -1

# print(binary_search(x, 5))



# x = [i for i in range(1,10)]

# def binary_recursive(arr, target, low, high):
#     if low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             return binary_recursive(arr, target, mid + 1, high)
#         else:
#             return binary_recursive(arr, target, low, mid - 1)
#     return -1

# print(binary_recursive(x, 3, 0, len(x) - 1))



# # შექმენით ფუნქცია, რომელიც მიიღებს ორ არგუმენტს: ლისტს და პროცენტს, უნდა დაგვიბრუნოს საბოლოო ფასდაკლებული ღირებულება ლისტში
# x = [100, 200, 180, 260]

# def discount(lst, percentage):
#     discounted = []
#     for i in lst:
#         discounted.append(i - (i / 100 * percentage))
#     return discounted
    
# print(discount(x, 50))


# დაწერეთ ლამბდა ფუნქცია, რომელიც დააბრუნებს სამის ჯერად რიცხვებს, ამის შემდეგ დაწერეთ ფუნქცია, რომელსაც ატრიბუტებად გადაეწოდება ლისტი და ლამბდა ფუნქცია, 
# ხაზობრივი ძიების და ლამბდა ფუნქციის დახმარებით შეავსეთ ახალი ლისტი(ინდექსებით) და დააბრუნეთ მოცემული ლისტი. 
# (ფუნქციამ უნდა დააბრუნოს ლისტი, რომელშიც შენახული იქნება სამის ჯერადი რიცხვების ინდექსები)
## Chemi amoxsna:
# threes = lambda num: [num * i for i in range(1, 4)]
# def lambda_func(lst, func):
#     return[func(num) for num in lst]

# numbers = [3, 6, 9]
# print(lambda_func(numbers, threes))

## Mastavleblis amoxsna:
# threes = lambda x: x % 3 == 0
# lst = [i for i in range(1, 10)]
# def main(lst, func):
#     lst1 = []
#     for i, item in enumerate(lst):
#         if func(item):
#             lst1.append(i)

#     return lst1

# print(main(lst, threes))



# # Davaleba 1:
# import random

# x = [i for i in range(100)]

# def sort(x):
#     sorted_list = sorted(x)
#     reverse = sorted(x, reverse = True)
#     return sorted_list, reverse
# print(sort(x))


# # Davaleba 2:
# import random

# arr = [i for i in range(100)]
# random.shuffle(arr)

# def sort(arr):
#     x = len(arr)
#     for i in range(x):
#         swapped = False
#         for j in range(0, x - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr

# print(sort(arr))


# arr = [i for i in range(100)]
# random.shuffle(arr)

# def sort(arr):
#     x = len(arr)
#     for i in range(x):
#         min_index = i
#         for j in range(i + 1, x):
#             if arr[j] > arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr

# print(sort(arr))


# # Davaleba 1:
# def missing(lst):
#     n = len(lst) + 1
#     total = n * (n + 1) // 2
#     lst_sum = sum(lst)
#     missing_number = total - lst_sum
#     return missing_number

# lst1 = [1, 2, 3, 4, 5, 6, 8, 9]
# print(f"The missing number is: {missing(lst1)}")


# # Davaleba 2:
# def repeated(nums, target):
#     left = 0
#     right = len(nums) - 1
#     result = -1
    
#     while left <= right:
#         mid = left + (right - left) // 2
        
#         if nums[mid] == target:
#             result = mid
#             right = mid - 1
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
            
#     return result

# nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
# target = 9

# result_index = repeated(nums, target)

# print(f"განმეორებითი რიცხვის ინდექსი არის: {result_index}")



# # DICTIONARIES (27.03.24):
# dictionary = {"name": "Amo", "surname": "Kotia", "age": 27}
# dictionary2 = dict(name = "Amo", surname = "Kotia", age = 27)
# dictionary3 = [("name", "Amo"), ("surname", "Kotia"), ("age", 27)]
# print(dictionary)
# print(dictionary2)
# print(dict(dictionary3))

# magazia = {
#     "Rdzis nawarmi": ["yveli", "arajani", {"mawoni": ["brendi1", "brendi2"]}]
# }
# print(magazia["Rdzis nawarmi"][-1]["mawoni"][0])



# dictionary = {"age": 10, "number": 20}
# number = int(input("Sheiyvanet ricxvi: "))

# for key, value in dictionary.items():
#     if value > number:
#         print(f'"{key}": {value}')




# def to_dict(sentence):
#     my_dict = {}
#     for i in sentence.split():
#         my_dict[i] = my_dict.get(i, 0) + 1
#     return my_dict

# sentence = input("Daweret winadadeba: ")
# print(to_dict(sentence))
# # OR
# def main(winadadeba):
#     words = winadadeba.split()
#     word_count = {}
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count

# print(main("Ravaxar to me viyo"))



# my_dict = {
#     "+": lambda x, y: x + y,
#     "-": lambda x, y: x - y,
#     "*": lambda x, y: x * y,
#     "/": lambda x, y: x / y
# }

# num1 = int(input("Sheiyvanet pirveli ricxvi: "))
# num2 = int(input("Sheiyvanet meore ricxvi: "))
# operator = input("Sheiyvanet operatori: ")

# if operator in my_dict:
#     operation = my_dict[operator]
#     result = operation(num1, num2)
#     print(f"Pasuxia: {result}")




# def add_to_translate(my_dict):
#     word = input("Sheiyvanet dasamatebeli sityva: ")
#     translate = input("Sheiyvanet sityvis targmani: ")
#     my_dict[word] = translate

# def search(my_dict):
#     word = input("Sheiyvanet sadziebo sityva: ")
#     return my_dict.get(word)

# my_dict = {"hello": "gamarjoba"}
# add_to_translate(my_dict)
# print(search(my_dict))

# # OR

# eng_to_geo = {
#     "hello": "gamarjoba"
# }

# def translate(word):
#     return eng_to_geo.get(word.lower(), "Agnishnuli sityva ar moidzebna.")

# def add_to_translate(eng, qart):
#     eng_to_geo[eng.lower()] = qart.lower()
#     return eng_to_geo

# add_to_translate("goodbye", "naxvamdis")

# def main():
#     while True:
#         action = input("Airchiet: damateba / modzebna / gamosvla: ")
#         if action == "gamosvla":
#             break
#         elif action == "damateba":
#             eng_sityva = input("Chaweret inglisuri sityva: ")
#             geo_sityva = input("Chaweret qartuli targmani: ")
#             print(add_to_translate(eng_sityva, geo_sityva))
#         elif action == "modzebna":
#             search = input("Ra sityvas edzebt?: ")
#             print(translate(search))
#         else:
#             print("Gtxovt...")

# main()


# capitals = {"USA": "Washington D.C.", "Georgia": "Bilisi", "Spain": "Madrid", "Germany": "Berlin"}
# print(dir(capitals))
# print(help(capitals))

# capitals.get("Georgia")
# capitals.update({"Italy": "Milan"})
# capitals.update({"USA": "New York"})
# capitals.pop("Germany")  # Removes a specific item
# capitals.popitem()  # Removes the last key, value pair
# capitals.clear()  # Removes all the key, value pairs

# keys = capitals.keys()

# values = capitals.values()
# for i in values:
#     if i[0].lower() == "b":
#         print(f"{i} does start with B")
#     else:
#         print("Does not start with B")

# items = capitals.items()  # Returns a dictionary object. Gets both, keys and values
# for key, value in items:
#     print(f"{key}: {value}")



# # Davaleba 1:
# lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# lst = [(* i [:-1], 100) for i in lst]
# print(lst)


# # Davaleba 2:
# lst = [12, 64, 87, 98, 4135, 846, 87, 878, 10]
# min = lst[0]
# max = lst[0]
# for i in lst:
#     if i > max:
#         max = i
# for i in lst:
#     if i <= min:
#         min = i
# print(f"The maximum value is {max}")
# print(f"The minimum value is {min}")


# # Davaleba 3:
# Input = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# Output = []
# for i in Input:
#     average = sum(i)/len(i)
#     Output.append(average)
# print(Output)



# cities = {
#     "Georgia": [{"Kartli": ["Tbilisi", "Mtskheta", "Rustavi"]}, 
#                 {"Samegrelo": ["Abasha", "Senaki", "Martvili"]}, 
#                 {"Adjara": ["Batumi", "Kobuleti"]}],
#     "Spain": ["Madrid", "Barcelona", "Granada", 
#               {"Islands": ["Ibiza", "Mallorca", "Menorca"]}]
#     }

# for key, value in cities.items():
#     print(f"{key}: {value[0]}")



# # CSV - excelis msgavsi tipis faili; Binaruli failebi; Failebis sxvadasxva direktorialshi importi



def new():
    pass

def wer(number):
    return f"{number} is an odd number" if number % 2 == 1 else f"{number} is an even number"

print(wer(4345213412))

print("hello")