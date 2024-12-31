"""
WAP that inverts a dictionary.That is,It makes key of one dictionary value of another and vice versa
"""


Dict = {'Roll_No' : '16/001', 'Name' : 'Arav', 'Course' : 'Btech'}

inverted = {}

for key,val in Dict.items():
    inverted[val] = key

print("Dict :",Dict)
print("Inverted Dict: ",inverted)