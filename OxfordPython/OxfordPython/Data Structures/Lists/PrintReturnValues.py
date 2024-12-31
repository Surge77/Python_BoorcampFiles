"""
Note: insert(),remove(),and sort() methods only modify the list and do not return any values.If you print the return
values of these methods,you will get none,This is a design principle that is applicable to all mutable data structures in
python.The code below illustrates this point

WAP to print the return values

Programming tip: It is safer to avoid aliasing when you are working with mutable objects

When one list is assigned to another list using the assignment operator (=) then a new copy of the list is not made.
Instead assignment makes the two variables point to the one list in memory.This is also known as aliasing

An alias is a second name for a piece of data.In python,aliasing happens whenever one variable value is assigned to
another variable

"""
num_list = [100,200,300,400]
print(num_list.insert(2,250))