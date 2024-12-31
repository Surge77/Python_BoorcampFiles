"""

Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.

"""

# Hint: There are 43,560 square feet in an acre

width = float(input("Enter width of field in feet: "))
length = float(input("Enter length of field in feet: "))

SQFT_per_acre = 43560

# computing the area in acres
# To convert Square Feet to Acre, you have to divide the unit by 43,560,
area = length * width / SQFT_per_acre

print(f"Area of the field is {area} acres")
