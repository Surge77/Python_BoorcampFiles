"""
WAP that defines a list of countries that are a member of BRICS Check whether a country is a member of brics or not
"""

country = ["Brazil","India","china","Russia","South Africa"]

is_member = input("Enter the name of country: ")

if is_member in country:
    print(f"{is_member} is part of BRICS")
else:
    print(f"{is_member} is not a part of BRICS")