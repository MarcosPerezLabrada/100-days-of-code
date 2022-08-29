print("Welcome to the tip calculator")
bill=int(input("What was the total bill?\n"))
people=int(input("How many people to split the bill?\n"))
percentage=int(input("What percentage tip would you like to give?\n"))
payment=(bill+(bill*percentage)/100)/people
print("Each person should pay: $"+str(payment))