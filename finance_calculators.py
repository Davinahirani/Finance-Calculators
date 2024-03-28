import math

print("Welcome to the Finance Calculator!")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# Prompt the user to choose an option
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Validate the user's input and proceed accordingly
if user_choice == "investment":
    # Ask for input values
    deposit_amount = float(input("Enter the amount of money that you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years you plan on investing: "))
    interest = input("Enter 'simple' or 'compound' for interest calculation: ").lower()

    # Calculate interest
    if interest == "simple":
        amount = deposit_amount * (1 + interest_rate * years)
    elif interest == "compound":
        amount = deposit_amount * math.pow((1 + interest_rate), years)

    print("Total amount after {} years: {:.2f}".format(years, amount))

elif user_choice == "bond":
    # Ask for input values
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    months = int(input("Enter the number of months you plan to take to repay the bond: "))

    # Calculate monthly repayment
    i = interest_rate / 12
    repayment = (i * present_value) / (1 - (1 + i)**(-months))

    print("Monthly repayment: {:.2f}".format(repayment))

else:
    print("Error: Invalid input! Please enter 'investment' or 'bond' to proceed.")
