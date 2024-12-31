"""
Difference between List and dictionary

There are two main differences between a list and dictionary

-First,a list is an ordered set of items.But,a dictionary is a data structure that is used for matching one item(key)
with another (value)
-Second,in list you can use indexing to access a particular items.But these indexes should be a number.In dictionaries
you can use any type (immutable) of value as an index.For ex: when we write Dict['Name'] Name acts as an index but it is
not a number but a string
-Third,lists are used to loop up a values whereas dictionary is used to take one value and look up another value.For this
reason dictionary is also known as lookup table

The main advantage of dictionary is that you don't need to search for a value one by one in the entire set of values,you
can find the value instantly

-the key value pair may not displayed in the order in which it was specified while defining the dictionary.This is
because python uses complex  algorithms called hashing to provide fast access to the items stored in the dictionary.
This also makes dictionary preferable over list and tuples

When to use which data structure:

-Use lists to store a collection of data that deos not need random access
-Use lists if the data has to be modified frequently
-Use set if you want to ensure that every element in the data structure must be unique
-Use tuples when you want that you data should not be altered
"""