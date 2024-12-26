# 1- https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
 
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Example
 
# Print the following:
# 8
# -2
# 15
 
a = int(input())
b = int(input())
    
print(a+b)
print(a-b)
print(a*b)


# 2. https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()
print(arr[-2])

# arr = list(map(int, input().split())) : We split the data received from the user by spaces, convert each element to an integer and convert it to a list.
# arr = list(set(arr))                  : We used set() to remove duplicate numbers in the list. Set keeps only unique elements.
# arr.sort()                            : We sorted the list, with the largest element coming last.
# arr[-2]                               : We get the second largest number, the element before the end of the list.




# 3- https://www.hackerrank.com/challenges/python-print/problem
list_number =[]
n = int(input("enter a number"))

for i in range(1, n+1):
    list_number.append(i)
    
str_number ="".join(map(str, list_number))
print(str_number)

# input(): Takes an integer n from the user.
# range(): Generates numbers from 1 to n.
# append(): Adds each number to the list (list_number).
# map(): Converts all list elements to strings.
# join(): Combines the string elements into a single string without spaces.

# 4- https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())            # n sayisi kadar for dongusu calisir.
student_marks = {}
for _ in range(n):
    name, *line = input().split()   # girdi: "Ali 70 80 90"     ->  ["Ali", "70", "80", "90"]   ->  name = "Ali"  line = ["70", "80", "90"]
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
scores = student_marks[query_name]
average = sum(scores) / len(scores)
print(f"{average:.2f}")  # 2 ondalık basamak göstermek için


#Girdi Alır:

#İlk olarak kaç öğrenci olduğunu (n) alır.
#Ardından her bir öğrenci için isim ve notları girdi olarak alır.
#Sözlük Oluşturur:

#Her öğrencinin ismini bir anahtar (key), notlarını ise bir liste olarak student_marks sözlüğüne ekler.
#Sorgu Çalıştırır:

#Kullanıcıdan sorgulamak istediği öğrencinin adını alır ve o öğrencinin notlarını bulur.
#Ortalama Hesaplar ve Yazdırır:

#Notların ortalamasını hesaplar ve sonucu yazdırır.


#1- Öğrencileri ve notlarını toplama:
# student_marks[name] = scores
# Bu işlem for döngüsü içinde olur ve her öğrencinin adı (name) ile notları (scores) sözlüğe eklenir.

#2- Kullanıcının sorgulaması:
# query_name = input()
# scores = student_marks[query_name]

# Kullanıcıdan bir isim (örneğin "Ali") alırız ve bu ismi kullanarak sözlükten ilgili notlara ulaşırız.

numbers = ["1", "2", "3", "4"]

# map fonksiyonu kullanılır
result = map(int, numbers)

print(result)  # Bu bir map object: <map object at 0x...>

# Listeye çevrildiğinde elemanları görürüz
print(list(result))  # [1, 2, 3, 4]
