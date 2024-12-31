"""
Points to remember:

1.At the first line,it should always be short and concise highlighting the summary of the object's purpose.
2.It should not specify information like the objects name or type
3.It should begin with a capital letter and end with a period.
4.Triple quotes are used to extend the docstring to multiple lines.The docstring specified can be accessed through
the __doc__ attribute of the function
5.In case of multiple lines in the documentation string,the second line should be blank,to separate the summary from the
rest of the description.The other lines should be one or more paragraphs describing the objects calling conventions
its side effects etc.
6.The first non blank line after the first line of the documentation string determines the amount of indentation
for the entire documentation string
7.Unlike comments,docstring are retained throughout the runtime of the program,So the user can inspect them during
program execution
"""



def func():
    """The program just prints a message."""
    """
    These three important points must be included in function docstring
    
    objective:
    Input parameters:
    Return value:
    
    """
    print("Hello world!!")

print(func.__doc__)