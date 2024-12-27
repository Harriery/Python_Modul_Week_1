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



#Question 4: Get a number from the user and write a Python code that prints whether this number is odd or even.

sayi=int(input("bir sayi degeri giriniz:"))

if sayi % 2 == 0 :
    print("girdiginiz deger cift sayidir")

else:
    print("girdiginiz deger tek sayidir")



#Question 8: Write a Python code that takes a word from the user and prints the reverse of this word on the screen.

kelime=input("bir kelime yaziniz:")

ters_kelime=kelime[::-1]

print(ters_kelime)