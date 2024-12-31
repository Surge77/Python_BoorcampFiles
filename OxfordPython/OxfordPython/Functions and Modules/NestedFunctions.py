"""
WAP to demonstrate the access of variables in inner and outer functions

In case of nested functions (Function inside another function) the inner function can access variables defined in both
outer as well as inner function, but the outer function can access variables defined only in the outer function
"""

def outer_func():
    outer_var = 10
    def inner_func():
        inner_var = 20
        print("Outer variable = ",outer_var)
        print("Inner variable = ",inner_var)
    inner_func()
    print("Outer variable = ", outer_var)
    # print("Inner variable = ", inner_var) # not accessible
outer_func()