"""
WAP to create a list of numbers in the range 1 to 10.Then delete all the even numbers from the list and print the final
list

The enumerate() function is a built-in function in Python that takes an iterable object as an argument and returns an
 enumerate object. The enumerate object yields a tuple containing a counter and the value of the iterable at that position.
This can be useful for iterating over a sequence and keeping track of the current index.

"""

num_list = []

for i in range(1,11):
    num_list.append(i)

print("Original list is: ",num_list)

for index,i in enumerate(num_list):
    if (i%2==0):
        del num_list[index]

print("List after deleting even numbers: ",num_list)