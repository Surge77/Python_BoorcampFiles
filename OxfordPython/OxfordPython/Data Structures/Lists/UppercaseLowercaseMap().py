"""
WAP that converts strings of all uppercase characters into strings of all lowercase characters using the map() function

Map() function applies a particular function to every element of a list.Its syntax is same as the filter function

"""

def to_lower(str):
    return str.lower()


list1 = ["HELLO","WELCOME","TO","THE","WORLD"]

list2 = list(map(to_lower,list1))

print("The list in lowercase characters is: ",list2)

