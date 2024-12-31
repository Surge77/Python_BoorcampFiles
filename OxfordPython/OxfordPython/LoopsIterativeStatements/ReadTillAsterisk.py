"""
WAP to read a character till a * is encountered.Also count the number of uppercase,lowercase, and numbers entered by user

programming tip: Statement inside while loop are repeatedly executed until condition is true.Once it becomes false the
                    next section of code is executed
"""

print("Enter * to exit")
ch = input("Enter any character: ")

num_count = 0
low_count = 0
up_count = 0

if (ch>='0' and ch <='9'):
    num_count += 1
elif (ch>='a' and ch <= 'z'):
    low_count +=1
elif (ch>='A' and ch <= 'A'):
    up_count +=1

while (ch!='*'):
    ch = input("Enter any character: ")
    if (ch >= '0' and ch <= '9'):
        num_count += 1
    elif (ch >= 'a' and ch <= 'z'):
        low_count += 1
    elif (ch >= 'A' and ch <= 'A'):
        up_count += 1

print(f"Number of lowercase characters are: {low_count}")
print(f"Number of uppercase characters are: {up_count}")
print(f"Number of numerals are: {num_count}")


