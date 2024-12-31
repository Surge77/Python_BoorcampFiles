"""
WAP to demonstrate variable length arguments

In some situations,it is not known in advance how many arguments will be passed to a function.In such cases python allows
programmers to make function calls with arbitrary (or any) number of arguments.When we use arbitrary arguments or
variable length arguments,then the function definition uses an asterisk (*) before the parameter name.
Syntax:

def function_name([arg1, arg2,....] *var_args_tuple ):
    function statements
    return [expressions]

Points to remember:

1.the arbitrary number of arguments passed to the function basically forms a tuple
2.Inside the called function,for loop is used to access the arguments
3.the variable length arguments if present in the function definition should be the last in the list of formal parameter
4.Any formal parameters written after the variable-length arguments must be keyword only arguements

A function cannot be used on the right side of an assignment statement therefore writing total(a,b) = s is invalid
"""

def func(name, *fav_subjects):
    print(name,"Likes to read ")
    for subject in fav_subjects:
        print(subject)

func("Goransh","MAths","JAVA","Python","science")

func("Richa","C","Golang")

func("Krish")