# Tip Calculator

total_bill = float(input("Welcome to the Tip Calculator.\nWhat was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_per_person = (total_bill + total_bill*(tip_percent/100))/people
final_bill = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_bill}")
