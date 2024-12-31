"""
Write a program to read the numbers until -1 is encountered.Find the average of positive numbers and negative numbers
entered by the user
"""

neg_count = 0
neg_s = 0
pos_count = 0
pos_s = 0

print("Enter -1 to exit")
num = int(input("Enter the number: "))
while (num!=-1):
    if (num<0):
        neg_count += 1
        neg_s = neg_s + num
    else:
        pos_count += 1
        pos_s = pos_s + num
    num = int(input("Enter the number: "))

pos_avg = float(pos_s)/pos_count
neg_avg = float(neg_s)/neg_count

print(f"THe average of negative numbers is : {neg_avg}")
print(f"THe average of positive numbers is : {pos_avg}")