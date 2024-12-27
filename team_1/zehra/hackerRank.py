#https://www.hackerrank.com/challenges/python-arithmetic-operators/copy-from/414863112

if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a+b)
print(a-b)
print(a*b)


#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/submissions/code/415196918

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sayi = list(arr)

    sayilar = sorted(set(sayi))

    print(sayilar[-2])


#https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

toplam = 0

for i in student_marks[query_name]:
    toplam += i
ort = float(toplam) / len(student_marks[query_name])

print(f"{ort:.2f}")


#https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())

    a = []
    b = ""
    for i in range(1, n + 1):
        a.append(i)

    b = ''.join(map(str, a))
    print(b)