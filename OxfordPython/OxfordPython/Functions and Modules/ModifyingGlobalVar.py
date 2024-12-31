"""
If we have a global variable and then create another global variable using the global statement then changes made in
the variable will be reflected everywhere in the program
"""
var = "Good"

def show():
    global var
    var = "Morning"
    print("In function var is - ",var)

show()
print("Inside function,var1 is - ",var) # accessible as it is global variable
var = "Fantastic"
print("Outside function after modification var is = ",var)