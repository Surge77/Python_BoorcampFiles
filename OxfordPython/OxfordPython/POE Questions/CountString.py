"""
Write a python program to count the number of
characters present in the string.

"""
import collections
str = "Tejas"

count = 0
for c in str:
    count = count + 1

print(count)

print("The total characters in the string are",len(str))


s = collections.Counter(str) # this counts the number of times each character in string occurs
print(s)
