"""
WAP using while loop to read the numbers until -1 is encountered.Also,count the number of prime numbers and composite
numbers entered by the user
"""

total_prime = 0
total_composite = 0

while(1):
    num = int(input("Enter number: "))
    if(num==-1):
        break
    isComposite = 0
    for i in range(2,num):
        if (num%i==0):
            isComposite = 1
            break
    if (isComposite):
        total_composite += 1
    else:
        total_prime += 1

print(f"Total composite: {total_composite}")
print(f"Total prime: {total_prime}")