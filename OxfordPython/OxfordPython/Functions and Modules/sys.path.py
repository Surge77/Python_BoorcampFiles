"""
WAP to print the sys.path variable

Python also allows you to pass command line arguments to your program.This can be done using the sys module.The argv
variable in this module keeps a track of command line arguments passed to the .py script
"""

import sys
from math import pi,sqrt

print("pi = ",pi)

print(sqrt(49))

print("\n Pythonpath = \n",sys.path)

print(sys.argv)