"""
WAP to enter a binary number and convert it into decimal
"""

binary_num = int(input("Enter the decimal number: "))

decimal_num = 0
i = 0

while(binary_num!=0):
    remainder = int(binary_num%10)
    decimal_num = int(decimal_num+remainder*(2**i))
    binary_num = int(binary_num/10)
    i = i+1
print(f"The binary equivalent = ",decimal_num)