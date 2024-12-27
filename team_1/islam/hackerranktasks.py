
# Task 1
a = int(input())
b = int(input())
    
print(a+b, a-b, a*b, sep ="\n")

#Task 2
n = int(input())
arr = map(int, input().split())
arr = list(arr)
highest_score = max(arr)
arr = [score for score in arr if score !=highest_score]
runner_up_score=max(arr)
    
print(runner_up_score)

#Task 3

n = int(input())
string = ""
for i in range(1, n+1):
        string +=str(i)
        
print(string)

#Task 4

def student_average (student_marks, query_name):
    for key, value in student_marks.items():
        if key == query_name:
            average_score = sum(value)/len(value)
    print('{:.2f}'.format(average_score))




    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_average (student_marks, query_name)