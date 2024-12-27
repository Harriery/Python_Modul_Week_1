# 6- Write a Python code that receives a number from the user and checks whether this number is PRIME.

sayi=int(input('\nBir sayi giriniz :'))
def is_prime(sayi):
    if sayi <= 1:
        return False
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True
if is_prime(sayi):
    print(sayi,'bir asal sayidir.')
else:
    print(sayi,'bir asal sayi degildir.')






# 7- How to create a loop that calculates the Fibonacci sequence and returns the result as a list containing numbers up to a certain limit?

limit = int(input("\nFibonacci dizisi için bir limit giriniz: "))

fib_list = [0, 1]
while fib_list[-1] + fib_list[-2] <= limit:
    fib_list.append(fib_list[-1] + fib_list[-2])
print('\nGirdiginiz sayiya kadar Fibonacci dizisi su sekildedir ;\n',fib_list)




# 11- How to write a Python program that finds the largest of three numbers entered by a user?

sayi1 = int(input("\nBirinci sayiyi giriniz: "))
sayi2 = int(input("Ikinci sayiyi giriniz: "))
sayi3 = int(input("Ucuncu sayiyi giriniz: "))

if sayi1 >= sayi2 and sayi1 >= sayi3:
    buyuk = sayi1
elif sayi2 >= sayi1 and sayi2 >= sayi3:
    buyuk = sayi2
else:
    buyuk = sayi3
print('\nEn buyuk sayi :',buyuk)