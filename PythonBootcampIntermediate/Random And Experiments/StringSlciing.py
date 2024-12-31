"""
String Slicing
"""
a = "Gate Smashers"
#   so on          -4 -3 -2 -1 negative indexing
# G a t e _ S m a s h  e  r  s
# 0 1 2 3 4 5 6 7 8 9 10 11 12 positive indexing
#indexing always starts from 0
#the array string slicing method is as follows [start:stop:stepsize]

print(len(a))
print(a[:]) #Prints all the elemnents in string
print(a[5:10]) # It always start with the exact start number but ends on 9 i.e on n-1
print(a[:10]) #If we dont specify start it automatically starts from 0th index till one less from end
print(a[5:]) # now here spaces are also considered while indexing and if we dont specify end it will print the whole string till end
print(a[-8:-3]) #here subtract the length of string by the corresponding number to get index
#here 13-8 = 5 which will be the start and 13 - 3 = 10 which is the end and ofcourse till end -1
print(a[5::2]) # here start and step size is specified but no end
print(a[::-1]) #if we want to print the whole string in reverse
print(a[5:12].upper()) # we can also do additional operations like here we converted this to uppercase
print(a[5:12].lower()) # similarly to lower case
