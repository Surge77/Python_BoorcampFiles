"""
WAP that uses string formatting feature to print the key value pairs stored in the dictionary

Python allows you to use string formatting feature with dictionaries,So you can use %s,%d,%d to represent string,integer,
floating point number or any other data
"""

Dict = {'Sneha': 'Btech','Mayank': 'BCa'}


for key,val in Dict.items():
     print("%s is studying in %s"% (key,val))