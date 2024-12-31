"""
Write a program that creates two dictionaries.One that stores conversion values from meters to centimeters and other that
stores values from centimeters to meters
"""

m_cm = {x: x*100 for x in range(1,11)}
temp = m_cm.values()

cm_m = {x : x/100 for x in temp}

print("Meters : Centimeters",m_cm)
print("Centimeters : Meteres",cm_m)