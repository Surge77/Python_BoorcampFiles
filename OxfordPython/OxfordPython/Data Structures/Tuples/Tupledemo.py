"""

Like lists,Tuple is another data structure supported by python.It is very similar to lists but differs in two things:

1.A tuple is a sequence of immutable objects.This means that while you can change the value of one or more items in a
list,you cannot change the values in a tuple
2.Second,tuples use parentheses to define its elements whereas list use square brackets


"""

# Necessity of comma in tuple, if we remove this comma this will become type int class

Tup = (10,)

print(type(Tup))

# USE OF divmod() function

quo, rem = divmod(100,3)

print("Quotient: ",quo)
print("Remainder: ",rem)

# accessing and updating tuples

tup1 = (1,2,3,4,5)
tup2 = (6,7,8,9,10)

tup3 = tup1 + tup2
print(tup3)

# slice operations to retrieve values in a tuple
tup4 = (1,2,3,4,5,6,7,8,9,10)

print("tup4[3:6] : ",tup4[3:6])
print("tup4[:8] : ",tup4[:8])
print("tup4[4:] : ",tup4[4:])
print("tup4[:] : ",tup4[:])

# deleting a tuple

Tup1 = (1,2,3,4)

del Tup1
print(Tup1)