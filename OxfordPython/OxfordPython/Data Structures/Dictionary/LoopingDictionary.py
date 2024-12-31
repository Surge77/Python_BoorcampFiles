"""
Program to access items in a dictionary using for loop
"""

Dict = {'Roll_No' : '16/001', 'Name' : 'Arav', 'Course' : 'Btech'}

print("Keys : ",end=" ")

for key in Dict:
    print(key,end=" ")  # accessing only keys

print("\nValues: ",end=" ")

for val in Dict.values():
    print(val,end=" ") # accessing only values

print("\nDicitonary :",end=" ")

for key,val in Dict.items():
    print(key,val,end=" ") # accessing key and values
