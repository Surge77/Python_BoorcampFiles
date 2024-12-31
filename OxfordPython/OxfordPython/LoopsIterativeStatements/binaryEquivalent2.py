"""
Write a program to enter a decimal number.Calculate and display the binary equivalent of this number


Assignment: WAP to convert a decimal number into octal and hexadecimal.
Hint: Instead of dividing by 2,divide by  and 16 respectively
"""

decimal_num = int(input("Enter the decimal number: "))

binary_num = 0
i = 0

while(decimal_num!=0):
    remainder = int(decimal_num%2)
    binary_num = int(binary_num+remainder*(10**i))
    decimal_num = int(decimal_num/2)
    i = i+1
print(f"The binary equivalent = ",binary_num)