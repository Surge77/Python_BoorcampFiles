"""
WAP to use format sequences while printing a string

In the output we can see that %s has been replaced by a string and %d has been replaced by an integer value.The values
to be substituted are provided at the end of line--in brackets prefixed by % You can either supply these values directly
or by using variables,Note that the number and type of values in the tuple should match the number and type of format
sequences or conversion specification in the string,otherwise error is returned
"""

name = "Aarish"

age = 8

print("Name = %s and Age = %d" %(name,age))
print("Name = %s and Age = %d" %("Anika",5))
