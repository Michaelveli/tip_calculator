
print("Welcome to the tip calculator")
bill = input("What was the total bill ? ")
#casting bill to int
bill = float(bill)
tip_percentage = input("What percentage tip would you like to give?")
tip_percentage = float(tip_percentage)
tip_percentage = tip_percentage / 100
people = int(input("How many people to split the bill ? "))


tip = ((bill / people) * tip_percentage)

total= round((bill/people)+tip, 2)

total = "{:.2f}".format((total))
print(f"Each person should pay: ${total}")

