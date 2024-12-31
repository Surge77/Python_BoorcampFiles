"""
WAP to make a list of cubes


Note:You can also create an empty list by using the built in list type object.For ex: by writing L = list(),an empty
list L is created
"""

cubes = [] # an empty list

for i in range(11):
    cubes.append(i**3)

print("Cubes of numbers from 1-10 : ",cubes)

# program to combine three lines of code into one

cubess = [i**3 for i in range(11)]

print(cubess)