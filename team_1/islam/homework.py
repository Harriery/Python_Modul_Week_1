# Python_Modul_Week_1

# Question 1: Write a Python code that prints numbers from 1 to 10 on the screen.

# for i in range(1,11):
#     print(i)
    
# Question 2: Take a number input from the user and write a Python program that prints even numbers up to this number on the screen. Do this first with 'for' and then with 'while' loops.
# For Loop Solution
# number = int(input("Please type a number: "))

# for i in range (1, number + 1):
#     if i % 2 == 0:
#         print(i)
        
# While Loop Solution
# number = int(input("Please type a number: "))

# i=2

# while i <= number:
#     print(i)
#     i +=2

# Question 3: Write a Python code that receives a start and end value from the user and prints all the numbers between these values ​​(including the end value) on the screen.

# start_number = int(input("Please enter a start number: "))
# end_number = int(input("Please enter an end number: "))

# for i in range(start_number, end_number+1):
#     print(i)

# Question 4: Get a number from the user and write a Python code that prints whether this number is odd or even.

# number = int(input("Please enter a number to check: "))

# if number % 2 ==0:
#     print(f"{number} is an even number." )
    
# else:
#     print(f"{number} is an odd number.")

# Question 5: Write a Python program that takes a positive integer input from the user and calculates its factorial. Factorial is the product of all positive integers between a number itself and 1. For example: if the user entered 5, the program should give the following output: Enter a number from the user: 5 Factorial: 120

# number = int(input("Please eneter a positive integer: "))

# faktorial = 1
# for i in range(1, number+1):
#      faktorial*=i
    
# print(faktorial)
    

# Question 6: Write a Python code that receives a number from the user and checks whether this number is prime.

# pri_number = int(input("Please enter an integer bigger than 1: "))

# is_prime = True  

# for n in range(2, pri_number):
#     if pri_number % n == 0:
#         print(f"{pri_number} is not prime.")
#         is_prime = False  
#         break  

# if is_prime:
#     print(f"{pri_number} is prime.")




# Question 7: How to create a loop that calculates the Fibonacci sequence and returns the result as a list containing numbers up to a certain limit?

# limit = int(input("Please enter a limit number: "))

# fib = [0,1]

# while True:
#     next_number = fib[-1]+fib[-2]
#     if next_number>limit:
#         break
#     fib.append(next_number)
# print(f"The fibonacci squence up to {limit} is {fib}")

# Question 8: Write a Python code that takes a word from the user and prints the reverse of this word on the screen.

# word = input("Please write a word to be reversed: ")

# print(word[::-1])

# Question 9: How to create a combination of loop and conditional statement that takes a word input from the user and checks whether that word is a palindrome (the same when read backwards)?

# first_word = input("Please write a word to check if palindrome: ")

# rev_word = first_word[::-1]

# if first_word == rev_word:
#     print(f"{first_word} is a polindrome.")
# else:
#     print(f"{first_word} is not a polindrome.")

# Question 10: Write the code that calculates the person's weight index and returns the result as underweight, overweight or overweight according to the index value. (You can look on the internet for the weight index calculation) To do this, ask the user for their weight and height measurements. weight index If it is below 25, it is weak, Between 25-30 is normal, If you are over 30-40, you are overweight. If you are over 40, you are overweight.

# print("Welcome to Weight Index Calculator")
# weight = float(input("Please enter your weight: "))
# height = float(input("Please enter your height: "))

# weight_index = weight/height**height

# if weight_index < 18.5:
#     print("You are weak.")
    
# elif weight_index >= 18.5 and weight_index <= 24.9 :
#     print("You are healthy.")
    
# elif weight_index >= 25 and weight_index < 29.9:
#     print("You are overweight.")
    
# else:
#     print("You are obese.")
# Question 11: How to write a Python program that finds the largest of three numbers entered by a user?
# print("Enter 3 numbers to find the largest")
# number_1 = int(input("Please enter the first number: "))
# number_2 = int(input("Please enter the second number: "))
# number_3 = int(input("Please enter the third number: "))

# if number_1 > number_2 and number_1 > number_3:
#     print("The first number is the largest.")
    
# elif number_2 > number_1 and number_2 > number_3:
#     print("The second number is the largest.")
    
# elif number_3 > number_1 and number_3 > number_2:
#     print("The third number is the largest.")
    

    
    
# Question 12: Get Midterm and Final grades from a student for any course. The sum of 40% of the midterm exam grade and 60% of the final grade will give the year-end average. If the average is below 50, "FAILED" will appear on the screen, and if it is 50 or above, "SUCCESSFUL" will be displayed on the screen. This printing process is 4 lessons. and the lessons will be written one after the other.
# print("Welcome to Grade Calculator")

# for i in range(4):
#     course_name = input(f"Please enter the name of the course {i+1}: ")    
#     mid_exam = float(input(f"Please enter your {course_name} midterm exam grade: "))
#     fin_exam = float(input(f"Please enter your {course_name}  final exam grade: "))
#     year_average = (mid_exam * 0.4) + (fin_exam * 0.6)
    
#     print(f"{course_name} average:{year_average}")

#     if year_average < 50:
#         print("FAILED")
    
#     elif year_average >= 50:
#         print("SUCCESSFUL")
    
# print("-" * 30)