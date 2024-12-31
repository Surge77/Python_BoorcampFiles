"""
WAP to demonstrate name clash variables in case of nested functions

If a variable in the inner function is defined with the same name as that of a variable defined in the outer function
then a new variable is created in the inner function.

programming tip: Try to avoid the use of global variables and global statement
"""

def outer_func():
    var = 10
    def inner_func():
        var = 20
        print("Inner variable = ",var)
    inner_func()
    print(("Outer variable = ",var))

outer_func()