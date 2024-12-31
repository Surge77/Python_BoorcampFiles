"""
The filer() function constructs a list from those elements of the list for which a function returns true.The syntax of
filter function is given as,

filter(function, sequence)

WAP that creates a list of numbers from 1-20 that are either divisible by 2 or divisible by 4 without using
the filter function
"""


div_2_4 = []
for i in range(2,22):
    if (i%4==0 or i%2==0):
        div_2_4.append(i)

print(div_2_4)



