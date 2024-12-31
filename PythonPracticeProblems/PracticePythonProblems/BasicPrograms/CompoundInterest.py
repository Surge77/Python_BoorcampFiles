"""

Python program to find compound interest


"""

def compound_interest(principal, rate, time, compounding):
    # Convert annual interest rate from percentage to decimal
    rate = rate / 100

    # Calculate compound interest
    amount = principal * pow((1 + (rate/compounding)), (compounding*time))
    interest = amount - principal

    return interest

# Get user input
principal = float(input("Enter starting principle please. "))
rate = float(input("Enter annual interest amount as a percentage. (e.g. 15 for 15%) "))
time = int(input("Enter the amount of years. "))
compounding = int(input("Enter Compound intrest rate.(daily, monthly, quarterly, half-year, yearly) "))

# Calculate compound interest
interest = compound_interest(principal, rate, time, compounding)

# Display the result
print ("The compound interest after", time, "years is", interest)
