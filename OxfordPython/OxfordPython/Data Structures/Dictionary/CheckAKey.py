"""
WAP to check a single key in a dictionary

The in keyword can be used to check whether a single key is present in the dictionary
"""

Dict = {'Roll_No' : '16/001', 'Name' : 'Arav', 'Course' : 'Btech'}

if 'Course' in Dict:
    print(Dict['Course'])