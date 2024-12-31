"""

Python program to compute simple interest

"""

principle_amount = int(input("Enter principle amount: "))
interest_rate = float(input("Enter interest rate : "))
time_period = int(input("Enter time period (in years): "))

SI = principle_amount*interest_rate*time_period
print(f"the simple interest is {SI} percent")


# this is using functions
def simple_interest(principal, rate, time):
    interest = principal * rate * time
    return interest

principal = 1000  # Principal amount
rate = 0.05  # Annual interest rate (in decimal form)
time = 3  # Time in years

interest = simple_interest(principal, rate, time)
print("Simple Interest: ", interest)  # Output: Simple Interest:  150.0
