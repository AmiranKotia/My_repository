# def square_sum(numbers):
#     for number in numbers:
#         number = number ** 2
#         summ = sum(number ** 2 for number in numbers)
#         return summ
# # OR
#     return sum(number ** 2 for number in numbers)
    
# print(square_sum([10, 12, 15]))



# def maps(a):
#     double = []
#     for num in a:
#         double.append(num * 2)
#     return double

# arr = [1, 2, 3]
# print(maps(arr))


# def smash(words):
#     sentence = " ".join(words)
#     return sentence

# words = ["Hello", "world,", "this", "is", "great!"]
# print(smash(words))


# def count_positives_sum_negatives(arr):
#     if arr is None or len(arr) == 0:
#         return []
#     count = sum(1 for i in arr if i > 0)
#     summ = sum(i for i in arr if i < 0)
#     arr2 = [count, summ]
#     return arr2

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# print(count_positives_sum_negatives(arr))

# # OR

# def count_positives_sum_negatives(arr):
#     if arr is None or len(arr) == 0:
#         return []
    
#     count_positive = 0
#     sum_negative = 0
    
#     for num in arr:
#         if num > 0:
#             count_positive += 1
#         elif num < 0:
#             sum_negative += num
    
#     return [count_positive, sum_negative]

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# print(count_positives_sum_negatives(arr))



# def feast(beast, dish):
#     if beast[0] == dish[0] and beast[-1] == dish[-1]:
#         return True
#     else:
#         return False
    
# print(feast("crock", "clock"))



# def count_sheep(n):
#     count = ""
#     for i in range(1, n + 1):
#         count += f"{i} sheep..."
#     return count
    
# print(count_sheep(5))

# # OR

# def count_sheep(n):
#     return ''.join(f"{i} sheep..." for i in range(1,n+1))

# print(count_sheep(6))


# # Reverse a string:
# def solution(string):
#     return string[::-1]

# print(solution("Hello"))



# def dna_to_rna(dna):
#     rna = ""
#     for i in dna:
#         if i == "G":
#             rna += i
#         elif i == "C":
#             rna += i
#         elif i == "A":
#             rna += i
#         elif i == "T":
#             rna += "U"
#     return rna
# print(dna_to_rna("GCAT"))

# OR

# def dna_to_rna(dna):
#     return dna.replace("T", "U")

# print(dna_to_rna("GCAT"))



# def remove_char(s):
#     return s[1:-1]
# print(remove_char("Hello"))



# def reverse_seq(n):
#     lst = []
#     return lst.append(range(n, 0, -1))

# print(reverse_seq(5))


# def xo(s):
#     s = s.lower()
#     xcount = s.count("x")
#     ocount = s.count("o")
#     if xcount == ocount:
#         return True
#     else:
#         return False
    
# print(xo("xoxo"))  
# print(xo("XxOo"))
# print(xo("xoXO"))  
# print(xo("abc"))   
# print(xo("xooxo"))

# # OR

# def xo(s):
#     return s.lower().count('x') == s.lower().count('o')

# print(xo("xoxo"))     
# print(xo("xooxo"))



# def can_pass(word):
#     for i in range(len(word) - 1):
#         if word[i] == word[i + 1]:
#             return True
#     return False

# words_to_test = ["moon", "sun", "slippers", "sandals", "yelling", "shouting", "fast", "speed", "sheet", "blanket", "glasses", "contacts"]
# for word in words_to_test:
#     print(word, ":", can_pass(word))



# def accum(st):
#     result = ""
#     for i, j in enumerate(st):
#         result += j.upper() + j.lower() * i + "-"
#     return result.rstrip("-")

# # # OR

# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

# print(accum("abcd"))



# def positive_sum(arr):
#     return sum(i for i in arr if i > 0)

# arra = [1, -4, 7, 12, -8]
# print(positive_sum(arra))



# def find_average(numbers):
#     if numbers == []:
#         return []
#     return sum(numbers) / len(numbers)

# # OR
# def find_average(numbers):
#     try:
#         return sum(numbers) / len(numbers)
#     except ZeroDivisionError:
#         return 0

# numbers = [12,12,5,45,416,8]
# print(find_average(numbers))



# def is_isogram(string):
#     isogram = ""
#     for i in string.lower():
#         if i in isogram:
#             return False
#         isogram += i
#     return True
# # # OR
# def is_isogram(string):
#     return len(string) == len(set(string.lower())) # A set is a collection of unique elements, meaning that each element in a set appears only once. By converting the string to a set, duplicate characters are automatically removed, leaving only the unique characters of the string.

# print(is_isogram("golle"))



# def summation(num):
#     total = 0
#     for i in range(1, num +1):
#         total += i
#     return total
# # OR
# def summation(num):
#     return sum(range(1, num + 1))

# print(summation(15))



# def better_than_average(class_points, your_points):
#     return True if your_points > sum(class_points) / len(class_points) else False
#     # # OR 
#     return your_points > sum(class_points) / len(class_points)

# class_points = [60, 85, 73, 50, 96, 90, 100, 69, 87, 92]
# print(better_than_average(class_points, 50))



# import math

# def is_triangle(a, b, c):
#     # s = (a + b + c)/2
#     # A = math.sqrt(s*(s-a)*(s-b)*(s-c))
#     # return A > 0
# # OR
#     s = (a + b + c)/2
#     return (s * (s-a)*(s-b)*(s-c)) ** 0.5 > 0

# print(is_triangle(2, 2, 3))



# def repeat_str(repeat, string):
#     return string * repeat

# print(repeat_str(5, "Hello"))



# def to_jaden_case(string):
#     words = string.split()
#     return " ".join(i.capitalize() for i in words)

# print(to_jaden_case("hello world, this is jaden."))



# def sum_two_smallest_numbers(numbers):
#     return sorted(numbers)[0] + sorted(numbers)[1]
# # OR
#     return sum(sorted(numbers)[:2])

# numbers = [12, 456, 123, 54, 6, 541, 3, 5]
# print(sum_two_smallest_numbers(numbers))



# def are_you_playing_banjo(name):
#     return name + " plays banjo" if name[0].lower() == "r" else name + " does not play banjo"

# print(are_you_playing_banjo("Vicky"))



# def friend(x):
#     # real_friend = []
#     # for i in x:
#     #     if len(i) == 4:
#     #         real_friend.append(i)
#     # return real_friend
# # # OR
#     return [i for i in x if len(i) == 4]

# x = ["Ryan", "Kieran", "Jason", "Yous"]
# print(friend(x))



# def string_to_array(s):
#     return s.split(" ")

# print(string_to_array('Robin Singh'))



# def lovefunc(flower1, flower2):
#     return (flower1 % 2 == 0 and flower2 % 2 == 1) or (flower2 % 2 == 0 and flower1 % 2 == 1)
# # OR
#     return (flower1+flower2)%2

# print(lovefunc(5,6))



# def digitize(n):
#     return [int(x) for x in str(n)[::-1]]

# print(digitize(123456789))



# def minimum(arr):
#     min = arr[0]
#     for i in arr:
#         if i <= min:
#             min = i
#     return min
# def maximum(arr):
#     max = 0
#     for i in arr:
#         if i >= max:
#             max = i
#     return max
# # OR
# def minimun(arr):
#     return min(arr)
# def maximum(arr):
#     return max(arr)

# arr = [12, 56, 4, 68, 123, 487, 697, 3154, 3, 948]
# print(f"Min = {minimun(arr)}, Max = {maximum(arr)}")




# def square_digits(num):
#     num_str = str(num)
#     squared = ""
#     for i in num_str:
#         squared += str(int(i) ** 2)
#     return int(squared)

# print(square_digits(8254))



# def remove_exclamation_marks(s):
#     return s.replace("!", "")

# s = "Hey! I am OK!"
# print(remove_exclamation_marks(s))



# def greet(name):
#     return f"Hello, {name} how are you doing today?"

# name = input("Please write your name: ")
# print(greet(name))



# def nb_year(p0, percent, aug, p):
#     n = 0
#     while p0 < p:
#         p0 = int(p0 + p0 * percent/100 + aug)
#         n += 1
#     return n

# print(nb_year(1000, 2, 50, 1200))



# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return distance_to_pump <= mpg * fuel_left

# print(zero_fuel(50, 25, 2))



# def century(year):
#     return (year + 99) // 100

# print(century(1901))



# def likes(names):
#     if len(names) == 0:
#         return "no one likes this"
#     elif len(names) == 1:
#         return f"{names[0]} likes this"
#     elif len(names) == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif len(names) == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     else:
#         return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

# print(likes(["Peter", "Jacob", "Ann", "Kyle", "Hugh"]))



# def rps(p1,p2):
#     if p1 == p2:
#         return "Draw!"
#     elif (p1 == "rock" and p2 == "scissors") or (p1 == "paper" and p2 == "rock") or (p1 == "scissors" and p2 == "paper"):
#         return "Player 1 won!"
#     else:
#         return "Player 2 won!"

# print(rps("paper", "rock"))



# def min_max(array):
#     prices = []
#     prices.append(min(array))
#     prices.append(max(array))
#     return prices

# arr = [0, 1, 2, 454]
# print(min_max(arr))



# def get_grades(s1, s2, s3):
#     average = (s1 + s2 + s3) / 3
#     if 90 <= average <= 100:
#         grade = "A"
#     elif 80 <= average < 90:
#         grade = "B"
#     elif 70 <= average < 80:
#         grade = "C"
#     elif 60 <= average < 70:
#         grade = "D"
#     elif 0 <= average < 60:
#         grade = "F"
#     return grade

# print(f"The average score is: {get_grades(85, 80, 85)}")



# def bmi(weight, height):
#     indx = weight / height**2
#     if indx <= 18.5:
#         return "Underweight"
#     elif indx <= 25.0:
#         return "Normal"
#     elif indx <= 30.0:
#         return "Overweight"
#     return "Obese"

# print(bmi(70, 1.81))



# def greet(a):
#     return a + b
# a = "Hello "
# b = "world!"
# print(greet("Hey "))



# from pymongo import MongoClient

# client = MongoClient("localhost", 27017)

# db = client.admin
# collections = db.some_collection

# for collection in collections.find():
#     print(collection)



# def make_negative(number):
#     return number - number * 2 if number > 0 else number

# print(make_negative(2))



# def make_upper_case(s):
#     return s.title()
    
# print(make_upper_case("jet it oue"))



# def bool_to_word(boolean):
#     return "Yes" if boolean else "No"



# def milliseconds(h, m, s):
#     if h <= 24 and m < 60 and s < 60:
#         return (h * 3600 + m * 60 + s) * 1000
#     else:
#         return False


# print(milliseconds(24,1,0))



# def switch_it_up(number):
#     transfer = {
#         0: "Zero",
#         1: "One",
#         2: "Two",
#         3: "Three",
#         4: "Four",
#         5: "Five",
#         6: "Six",
#         7: "Seven",
#         8: "Eight",
#         9: "Nine",
#         10: "Ten"
#     }
#     return transfer[number]

# print(switch_it_up(0))



# def human_cat_dog_years(human_years):
#     if human_years == 1:
#         cat_years = 15
#     elif human_years == 2:
#         cat_years = 24
#     elif human_years > 2:
#         cat_years = 24 + (human_years - 2) * 4
    
#     if human_years == 1:
#         dog_years = 15
#     elif human_years == 2:
#         dog_years = 24
#     elif human_years > 2:
#         dog_years = 24 + (human_years - 2) * 5

#     return [human_years, cat_years, dog_years]

# print(human_cat_dog_years(15))

# # OR 

# def human_years_cat_years_dog_years(x):
#     return [f"Human years  {x}, Cat years: {24+(x-2)*4 if (x != 1) else 15}, Dog years: {24+(x-2)*5 if (x != 1) else 15}"]

# print(human_years_cat_years_dog_years(3))



# def count(s):
#     # i_count = {}
#     # for i in s:
#     #     if i in i_count:
#     #         i_count[i] += 1
#     #     else:
#     #         i_count[i] = 1
#     # return i_count

#     return {i: s.count(i) for i in s}

# print(count("abbunalesaaterascvajhgjhasfasgfdf"))



# def delete_nth(order, max_e):
#     max = []
#     for i in order:
#         if max.count(i) < max_e:
#             max.append(i)
#     return max

# print(delete_nth([1,2,3,1,2,1,2,3,3,2,1,3,1,2,3], 2))



# def validate_pin(pin):
#     return True if pin.isdigit() and len(pin) == 4 or pin.isdigit() and len(pin) == 6 else False

# pin = input("Type your pin: ")
# print(validate_pin(pin))




# def find_needle(haystack):
#     return f"found the needle at position {haystack.index("needle")}"

# lst = ["hay", "junk", "hay", "hay", "moreJunk", "randomJunk", "some", "needle"]
# print(find_needle(lst))




# def leap(year):
#     return f"The year {year} is a leap year" if year % 4 == 0 else f"The year {year} is not a leap year."

# year = int(input("What year do you want to check? "))
# print(leap(year))



# vowels = ["a", "e", "i", "o", "u"]
# string = input("Type any word: ")
# count = 0
# for i in string:
#     if i in vowels:
#         count += 1
# print(f"There are {count} vowels in the word {string}.")



# about = input("Tell me something about yourself in 10 words: ")
# count = 0
# for i in about.split(" "):
#     count += 1
# if count == 11:
#     print(f"You exceeded the limit by {count - 10} word.")
#     print(f"Total word count: {count}")
# elif count > 11:
#     print(f"You exceeded the limit by {count - 10} words.")
#     print(f"Total word count: {count}")
# else:
#     print("That is very interesting.")
#     print(f"Total word count: {count}")



# def fibonacci(num):
#     fibo = [0, 1]
#     i = 2
#     while i <= num:
#         next_fibo = fibo[i - 1] + fibo[i - 2]
#         fibo.append(next_fibo)
#         i += 1
#     return fibo

# print(fibonacci(3))




# def combined(one, two):
#     comb = one + two
#     comb.sort()
#     return comb

# first = [12,13,15,11,14,18,17,16,19,20]
# second = [2,3,5,1,4,8,7,9,6,10]
# print(combined(first, second))



# def multiplication_table(n):
#     i = 1
#     while i <= 10:
#         print(f"{n}x{i} = {i*n}")
#         i+=1
# multiplication_table(10)



