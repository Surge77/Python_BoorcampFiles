"""
WAP to calculate simple Interest.Suppose the customer is a senior citizen.He is being offered 12 percent interest and
for all other customers ROI is 10 percent
"""

def interest(p,y,s):
    if (s=='y'):
        SI = float((p*y*12)/100)
    else:
        SI = float((p * y * 10) / 100)
    return SI

p = float(input("Enter the principle amount: "))
y = float(input("Enter the number of years: "))
senior = input("Is the customer senior citizen (y/n): ")

print("The Interest = ",interest(p,y,senior))
