"""
WAP to demonstrate the use of del statement and clear() function
"""

Dict = {'Roll_No' : '16/001', 'Name' : 'Arav', 'Course' : 'Btech'}

print("Dict[Roll_No",Dict['Roll_No'])
print("Dict[NAME]",Dict['Name'])
print("Dict[COURSE]",Dict['Course'])
del Dict['Course'] # deletes a key value pair
print("After deleting course",Dict)

Dict.clear() # deletes all entries
print("After clear dictionary has no items",Dict)

del Dict # deletes the variable dict from memory
print("Dict does not exist.......")
print(Dict)