# How to create a loop that calculates the Fibonacci sequence and returns the result as a list containing numbers up to a certain limit?

limit = int(input("\nFibonacci dizisi için bir limit giriniz: "))

fib_list = [0, 1]
while fib_list[-1] + fib_list[-2] <= limit:
    fib_list.append(fib_list[-1] + fib_list[-2])
print('\nGirdiginiz sayiya kadar Fibonacci dizisi su sekildedir ;\n',fib_list)