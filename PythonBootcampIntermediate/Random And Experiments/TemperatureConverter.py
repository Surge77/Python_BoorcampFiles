"""

Write a python program to convert temperature to and from Celsius to Fahrenheit using
choice as if input is 1 then Degree to Fahrenheit, if 2 then Fahrenheit to Degree, if 3 then exit
the program, and any other option wrong choice.

"""

print("1.Degree to Fahrenheit")
print("Fahrenheit to Degree")
print("3.Exit")

while True:
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        Degree = float(input("Enter the temperature in degrees: "))
        Fahrenheit = (Degree * 9/5) + 32
        print(f"{Degree} Celsius is {Fahrenheit:.2f} Fahrenheit")
        break
    elif choice == 2:
        Fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        Degree = (Fahrenheit - 32) * 5/9
        print(f"{Fahrenheit} Fahrenheit is {Degree:.2f} Degree Celsius")
        break
    elif choice == 3:
        print("Exiting program , goodbye")
        break
    else:
        print("Invalid choice,Enter 1, 2 or 3")
