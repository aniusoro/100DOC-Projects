#Tip calculator
print("Welcome to the tip calculator.")

#user inputs their total bill
bill = float(input("What was your total bill? $"))

#user chooses what percentage of tip they would like to give
tip = float(input("What percentage tip would you like to give? 10,12, or 15? "))

#asks user how many people are splitting the bill
people = int(input("How many people to split the bill? "))

#the amount for each person to pay
amount = round(((bill / people) * (1 + tip / 100)), 2 )

#final message
print (f"Each person should pay ${amount}")
