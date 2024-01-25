# Tip Calculator

total_bill = float(input("Welcome to the Tip Calculator.\nWhat was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_per_person = round((total_bill + total_bill*(tip_percent/100))/people, 2)

print(f"Each person should pay: ${bill_per_person}")
