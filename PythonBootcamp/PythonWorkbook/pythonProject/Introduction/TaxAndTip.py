"""

The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all the values
are displayed using two decimal places.

observations:
1.Input the cost of meal in float from user
2.Compute tax and tip. tip -> 18 percent of meal amount without tax, tax -> 5 % gst
3.compute the tax amount , tip amount , and the grand total including tax and tip in dollars
4.format the output using two decimal places

"""

# reading the cost of meal from the user
meal_cost = float(input("Enter the cost of meal: "))

tax_rate = 0.05
tip_rate = 0.18

# computing the tax and tip amount
tax_amount = meal_cost * tax_rate
tip_amount = meal_cost * tip_rate
grand_total = meal_cost + tax_amount + tip_amount

# printing the final result
print(f"The tax is ${tax_amount:.2f} and tip is ${tip_amount:.2f} making the total of ${grand_total}")





