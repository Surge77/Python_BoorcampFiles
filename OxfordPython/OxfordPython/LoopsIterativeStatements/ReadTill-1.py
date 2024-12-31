"""
Write a program to read the numbers until -1 is encountered.Also count the negative,positives, and zeroes entered by the
user
"""

negatives = positives = zeroes = 0

while(1):
    num = int(input("Enter -1 to exit: "))
    if (num == -1):
        break
    elif (num == 0):
        zeroes += 1
    elif (num>0):
        positives +=1
    elif (num<0):
        negatives +=1
    else :
        print("Enter a valid number")

print(f"Count of positive numbers entered : {positives}")
print(f"Count of negative numbers entered : {negatives}")
print(f"Count of zeroes entered : {zeroes}")