"""
WAP using for loops to calculate that average of first n natural numbers
"""

n = int(input("Enter a number: "))

avg = 0.0
s = 0
for i in range(0,n+1):
    s = s+i

avg = s/i

print(f"The sum of first n natural numbers is : {s}")
print(f"The average of first n natural numbers is : {avg}")