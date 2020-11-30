# Day 5 of 100 For Loops, Range and Code Blocks

# fruits = ["apple", "orange", "peach"]
# for fruit in fruits:
#     print(fruit + " pie")
#     print(fruit + " juice")
# print(fruits[1])

# total = 0
# heights = input("Input the list of heights.\n").split(", ")
# for i in range(0, len(heights)):
#     heights[i] = int(heights[i])
#     total = total + heights[i]
# average = round(total / len(heights), 2)
# print(f"Sum of heights is: {total}")
# print(f"The average of all heights is: {average}")

# scores = input("Enter a list of scores\n").split(", ")
# for i in range(0, len(scores)):
#     scores[i] = int(scores[i])
# print("The largest score is:", max(scores))

# 2 Ways of adding even numbers
# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)
#
# total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)

# Fizz Buzz Exercise

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my Password Generator")
letterNumber = int(input("How many letters would you like in your password?\n"))
numberNumber = int(input("How many numbers would you like in your password?\n"))
symbolNumber = int(input("How many symbols would you like in your password?\n"))
characters = letterNumber + numberNumber + symbolNumber


randomLetters = (random.sample(letters, letterNumber))
randomNumbers = (random.sample(numbers, numberNumber))
randomSymbols = (random.sample(symbols, symbolNumber))

password = (randomLetters + randomNumbers + randomSymbols)
random.seed(3)
random.shuffle(password)
print(''.join(password))

