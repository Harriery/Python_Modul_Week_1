# Arithmetic Operators

a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# Find Second Maximum Number in a List

 n = int(input())
    arr = map(int, input().split())
    arr= list(set(arr))
    arr.remove(max(arr))
    print(max(arr))


# Print Function

n = int(input())
    rakamlar=[]
    for sayi in range(n+1):
        rakamlar.append(sayi)
    rakamlar.remove(rakamlar[0])
    print(''.join(map(str,rakamlar)))


# Finding the Percentage