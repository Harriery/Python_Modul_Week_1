# How to write a Python program that finds the largest of three numbers entered by a user?

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