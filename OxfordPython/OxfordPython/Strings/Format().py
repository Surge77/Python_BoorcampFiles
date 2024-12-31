"""
WAP to demonstrate format() function

The format() is used with strings in a very versatile and powerful function used for formatting strings.Format strings
have curly braces{} as placeholders or replacements fields which gets replaced.We can even use positional arguments or
keyword arguments to specify the order of fields that have to be replaced.
"""

str = "{}, {} and {}".format('sun','moon','stars')
print("\n The default sequence of arguments is : " +  str)
str2 = "{1}, {0} and {2}".format('sun','moon','stars')
print("\n The positional sequence of arguments (1,0 and 2) is : " + str2 )
str3 = "{c}, {b} and {a}".format(a='sun',b='moon',c='stars')
print("\n The keyword sequence of arguments is : " + str3)