"""

Write a program to count the number of characters present in the string.
without using len() function

"""

user_text = input("Enter a string: ")

index = 0

for _ in user_text:
    index += 1

print("The total number of characters in string are: ",index)


print(f"The total no of characters is {len(user_text)}")