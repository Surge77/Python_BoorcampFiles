"""
WAP that creates a dictionary of radius of circle and its circumference
"""

print("Enter -1 to exit: ")

Circumference = {}

while True:
    r = int(input("Enter radius: "))
    if r == -1:
        break
    else:
        Dict = {r:2*3.14*r}
        Circumference.update(Dict)

print(Circumference)