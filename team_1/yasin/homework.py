#Question 1: Write a Python code that prints numbers from 1 to 10 on the screen
number= []
for i in range(1, 11):
    number.append(i)
    
print(number)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#*********************************************************************************************

#Question 3: Write a Python code that receives a start and end value from the user 
# and prints all the numbers between these values ​​(including the end value) on the screen.

list =[]
while True:
    number1= int(input("enter first value :"))
    number2 = int(input("enter second value :"))
    for i in range (number1 +1, number2):
        list.append(i)
    break
print(list)     

#**********************************************************************************************
#Question 9:
# How to create a combination of loop and conditional statement that
#  takes a word input from the user and checks whether that word is a palindrome (the same when read backwards)?
while True:
    user_input= input("Enter a word :")
    if user_input == ''.join(reversed(user_input)):
        print(f"That word is a palindrom..:{user_input} ") 
        break
    else:
        print("That word is not a palindrom..!")
        
#**********************************************************************************************
#- Question 12: 
# Get Midterm and Final grades from a student for any course.
#  The sum of 40% of the midterm exam grade and 60% of the final grade will give the year-end average. If the average is below 50, "FAILED" will appear on the screen, and if it is 50 or above,
#  "SUCCESSFUL" will be displayed on the screen. This printing process is 4 lessons. and the lessons will be written one after the other.


while True:

    midterm_exam = int(input("enter your midterm exam grade :"))
    final_exam = int (input ("enter your final exam grade :"))
    average = ((midterm_exam * 40)/100 + (final_exam * 60)/100)
    if  average >= 50:
        print(average, "SUCCESSFUL")
        break
    else:
        print("FAILED!!")   





#*************************************************************************************************
# Question 2: 
# Take a number input from the user and write a Python program that prints even numbers up to this number on the screen. 
# Do this first with 'for' and then with 'while' loops.

# with for loops
list1 = []   
number3 = int(input("Enter a number "))
for i in range(0, number3):
    if i % 2 == 0:
        list1.append(i)
print(list1)

# with while loops
number4 = int(input("Enter a number "))
number5 = 0
while number5 <= number4:
    print(number5)
    number5 += 2


#*************************************************************************************************    
# Question 4: Get a number from the user and write a Python code that prints whether this number is odd or even.



# ************************************************************************************************
#Question 6: 
# Write a Python code that receives a number from the user and checks whether this number is prime

prime_number = int(input("Enter a number :"))

if prime_number > 1:
    for i in range(2, prime_number +1):
        if prime_number % i != 0:
            print(i, "That is not prime number")
            continue
        else:
            print(i, "That is a prime number !!")
else:
    print("That is not prime number")