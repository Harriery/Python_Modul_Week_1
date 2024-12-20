# Write a Python code that receives a number from the user and checks whether this number is PRIME.

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