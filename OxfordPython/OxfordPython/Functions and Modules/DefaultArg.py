"""
Points to remember:

1.All the keyword arguments passed should match one of the arguments accepted by the function
2.The order of keyword arguments is not important
3.In no case an arguments should receive a value more than once
4.You can specify any number of default arguments in your function
5.If you have default arguments then they must be written after the non default arguments,This means that non deafult
arguments cannot follow default arguments.Therefore the line of code given in the following example will produce erro

program to demonstrate default arguments

In below code the parameter name does not have a default value and is therefore mandatory.that is,you must specify a
value for this parameter during the function call.but the parameter course has already been given default value so it is
optional,If value is provided it will overwrite the default value and in case a value is not specified during function
call the one provided in the function definition as the default value will be used
"""

def display(name, course = "BTech"):
    print("Name : ", name)
    print("Course : ", course)

display(course="BCA",name="Arav")
display(name="Reyansh")