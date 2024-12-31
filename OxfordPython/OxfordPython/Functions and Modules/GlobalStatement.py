"""
WAP to demonstrate use of global statement
"""

var = "Good"

def show():
    global var1
    var1 = "Morning"
    print("In function var is - ",var)

show()
print("outside function,var1 is - ",var1) # accessible as it is global variable
print("var is = ",var)