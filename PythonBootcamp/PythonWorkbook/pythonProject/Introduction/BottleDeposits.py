"""

In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.

observations:
1.to input the number of drink containers and the size of container
2.containers of one liter or less -> $0.10
3.containers of more than one liter ->$0.25
4.with each size displaying the refund amount

"""

print("1.Deposit for containers of one liter or less: $0.10")
print("2.Deposit for containers of more than one liter: $0.25")

can1 = 0.10
can2 = 0.25

containers1 = int(input("Enter the number of containers of one liter or less : "))
containers2 = int(input("Enter the number of containers of more than one liter : "))
container_count = containers2 + containers1

bottle1 = containers1*can1
bottle2 = containers2*can2

refund = bottle2 + bottle1

print(f"You received ${refund:.2f} of refund for returning {container_count} containers")

