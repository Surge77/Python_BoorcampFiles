"""

Python Program for factorial of a number

"""

import math

# for this method math module is required
# this is using math module and using the factorial function
a = int(input("Enter a number: "))
result = math.factorial(a)
print(f"the factorial of {a} is {result}")

# with the help of loop in a function

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
ans = factorial(a)
print(f"the factorial of {a} is {ans}")


# using recursive function

def facto(n):
    if (n==0 or n == 1):
        return 1
    else:
        return  n * facto(n - 1)

ans = factorial(a)
print(f"the factorial of {a} is {ans}")





