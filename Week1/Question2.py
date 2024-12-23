#Question 2: Take a number input from the user and write a Python program that prints even numbers up to this number on the screen. Do this first with 'for' and then with 'while' loops.

sayi=int(input("bir sayi giriniz:"))

for i in range(sayi):
   if i % 2 == 0 :
       print(i,"bir cift sayidir")

n=0
while n<sayi:
    if n % 2 == 0 :
        print(n, "bir cift sayidir")
    n += 1