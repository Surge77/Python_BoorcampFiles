"""
WAP to print the fibonacci series using recursion
"""

def fib(n):
    if (n<2):
        return 1
    else:
        return (fib(n-1)+fib(n-2))


n = int(input("Enter the number of terms: "))

for i in range(n):
    print("Fibonacci (",i,") = ",fib(i))