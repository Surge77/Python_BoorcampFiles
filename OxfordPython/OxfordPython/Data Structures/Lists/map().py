"""
Map() function applies a particular function to every element of a list.Its syntax is same as the filter function

map(function,sequence)

After applying the specified function on the sequence,the map() function returns the modified list.The map() function
calls function(items) for each item in the sequence and returns a list of the return values

Key Points to remember:

-If there is only one item in the sequence,then its value is returned
-If the sequence is empty,an exception is raised
-Creating a list in a very extensive range will generate a memoryerror or overflowerror 
"""

def add_2(x):
    x += 2
    return x

num_list = [1,2,3,4,5,6,7]

print("original list : ",num_list)
new_list = list(map(add_2,num_list))
print("the modified list is :",new_list)


# Program to pass more than one sequence to the map() function

def add(x,y):
    return x+y

list1 = [1,2,3.4,5]
list2 = [6,7,8,9,10]
list3 = list(map(add,list1,list2))
print(f"Sum of {list1} and {list2} is {list3}")