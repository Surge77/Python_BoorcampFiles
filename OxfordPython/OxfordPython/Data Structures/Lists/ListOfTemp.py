"""
WAP that converts a list of temperatures in celsius into Fahrenheit
"""

def convert_to_F(Temp_C):
    return ((float(9)/5)*Temp_C+32)

Temp_in_c = (36.5,37,37.6,39)

Temp_in_F = list(map(convert_to_F,Temp_in_c))

print("List of temperatures in celsius: ",Temp_in_c)
print("List of temperatures in fahrenheit: ",Temp_in_F)