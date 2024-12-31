"""
Lambda functions or anonymous functions:

These functions are not declared by using def keyword instead created by using lambda keyword
Lambda functions contain only a single line

syntax:

lambda arguments: expression

Points to remember:

1.Lambda functions have no name
2.Lambda functions can take any number of arguments
3.Lambda functions can return just one value in the form of an expression
4.Lambda functions definition does not have an explicit return statement but it always contains an expression which is
returned
5.They are a one-liner version of a function and hence cannot contain multiple expressions
6.They cannot access variables other than those in their parameter list
7.Lambda functions cannot even access global variables
8.you can pass Lambda functions as arguments in other functions
"""

sum = lambda x, y: x+y
print("sum = ",sum(3,5))