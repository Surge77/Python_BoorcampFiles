"""
A set is created by placing all the elements inside curly brackets {}, separated by comma or by using the built-in
function set().The syntax:

set_variable = {val1,val2.......}

-Since sets are unordered,indexing have no meaning.
-Set operations do not allow users to access or change an element using indexing or slicing.

In Python, sets are unordered collections, which means that the order of the elements in a set is not guaranteed.
When you iterate over a set, the elements will be returned in an arbitrary order. This is because sets are implemented
as hash tables, which do not have a good notion of iteration order.
If you need to iterate over a set in a specific order, you can use the sorted() function to sort the elements of the set
before iterating over them.
"""

s = {2,4,5}

print(s)

# iterate through a set

a = set("hello good morning")

for i in a:
    print(i,end=" ")