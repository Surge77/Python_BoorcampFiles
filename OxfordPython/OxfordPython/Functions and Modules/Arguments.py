"""
Types of Function Arguments:

1.Required Arguments -> number of Arguments in the function call should match with number of arg specified
2.Keyword Arguments
3.Default Arguments
4.Variable Length arguments
"""

# Keyword Arguments

def display(str,int_x,float_y):
    print("The string is : ",str)
    print("The integer value is : ",int_x)
    print("The floating point value is : ",float_y)

display(float_y=5673.093,str="hello",int_x=1234)
# here we can also assign other variables instead of directly passing the values


