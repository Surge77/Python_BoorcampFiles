"""
WAP to print the elements in the list using an iterator

iterator: You can create an iterator using the built-in iter() function.The iterator is used to loop over the elements
of the list.For this,the iterator fetches the value and then automatically points to the next elements in the list
when it is used with the next() method
"""

num_list = [1,2,3,4,5]
it = iter(num_list)

for i in range(len(num_list)):
    print("Element at index ",i,"is : ",next(it))