"""
WAP to add a new item in dictionary
"""

Dict = {'Roll_No' : '16/001', 'Name' : 'Arav', 'Course' : 'Btech'}

print("Dict[Roll_No",Dict['Roll_No'])
print("Dict[NAME]",Dict['Name'])
print("Dict[COURSE]",Dict['Course'])

Dict['Marks'] = 95  # new entry

print("Dict[MARKS] = ", Dict['Marks'])