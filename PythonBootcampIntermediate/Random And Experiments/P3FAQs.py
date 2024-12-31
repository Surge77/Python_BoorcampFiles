"""
1. What is indexing?
2. What is the purpose of split and join method in python?
3. In Python, What is slicing?
4. What do you mean string immutable?
5. What is the use of id() function?
6. What is negative index in Python?
7. How to convert a string to all lowercase?
8. How to replace all occurrences of old substring in string with new string?
9. How will you change case for all letters in string?
10. How to check whether the string consisting of alphanumeric characters?

1. ->In Python, indexing refers to the process of accessing individual elements of an iterable (like a string, list,
     tuple, etc.) using their position or index within the sequence. Indexing starts at 0, meaning the first element
     has an index of 0, the second has an index of 1, and so on.

 2. ->The split() and join() methods in Python are used for string manipulation:
      split() Method:
      The split() method is used to split a string into a list of substrings based on a specified delimiter.
      By default, the delimiter is a space.

      join() Method:
      The join() method is used to concatenate elements of an iterable (such as a list) into a single string,
      using a specified delimiter.

3. ->Slicing is the extraction of a part of a string, list, or tuple. It enables users to access the specific range of
elements by mentioning their indices. Syntax: Object [start:stop:step] “Start” specifies the starting index of a slice.
“Stop” specifies the ending element of a slice.

4. ->Python strings are "immutable" which means they cannot be changed after they are created (Java strings also use
     this immutable style).

5. ->The id() function in Python returns a unique identifier for an object. The identifier is an integer that represents
     the object's memory address. The id() function is used to:
     -Determine if two variables reference the same object
     -Check if two objects or variables refer to the same memory location
     -Return the object's "identity"

6. ->Negative indexing in Python is a way to access elements of a sequence from the end, starting from -1 for the last
     element. This can be useful for accessing elements from the end of a data structure without having to know the exact
     length of the data structure.

7. ->The lower() method converts all uppercase characters in a string into lowercase characters and returns it.

8. ->In Python, you can replace all occurrences of an old substring in a string with a new substring using the replace()
     method. The replace() method takes two arguments: the old substring to be replaced and the new substring that will
     replace it

9. ->Use .upper() to change the case of a string

10. ->In Python, you can use the isalnum() function to check if a string is alphanumeric. This function returns a Boolean value of True if all characters in the string are alphanumeric, and False if not.
A character is alphanumeric if it is either an alphabetic character or a number. This includes letters (a-z, A-Z) and numbers (0-9).
You can also check if a string is alphanumeric by using its ASCII code:
48–57: Numeric characters
97–122: Lowercase alphabetic characters
65–90: Uppercase alphabetic characters

"""