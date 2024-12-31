"""

Write a program to calculate the bill amount for an item given its quantity sold,value,discount,tax

"""

qty = float(input("Enter the quantity of item sold: "))
val = float(input("Enter the value of the item: "))
discount = float(input("Enter the discount percentage: "))
tax = float(input("Enter the tax: "))
amt = qty*val

discount_amt = (amt*discount)/100

sub_total = amt - discount_amt
tax_amt = (sub_total*tax)/100
total_amt = sub_total + tax_amt

print("***********Bill***********")
print("Quantity sold : \t ",qty)
print("price per item : \t",val)
print("\n \t \t _______________")
print("Amount : \t\t",amt)
print("  \t   \t  ______________")
print("Discounted total : \t",sub_total)
print("Tax : \t\t\t +",tax_amt)
print("  \t   \t  ______________")
print("Total amount to be paid ",total_amt)
