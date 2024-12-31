"""
Write a program to calculate the sum and average of first 10 numbers

"""

i = 0
s = 0

while (i<=10):
    s = s + i
    i += 1

average = float(s)/10

print(f"Sum = {s}  Average = {average}")

