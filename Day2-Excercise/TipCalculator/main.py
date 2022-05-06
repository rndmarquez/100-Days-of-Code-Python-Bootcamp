#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#welcome the user
print("Welcome to the tip calculator!")

#ask user for total bill
totalBill = float(input("What as the total bill?"))

#ask user how much tip they would like to give? 
totalTip = input("How much tip would you like to give? 10, 12, or 15?")

#need to add check for 10, 12, 15
#while totalTip != 10 or totalTip != 12 or totalTip != 15:
#  totalTip = input("Tip can only be 10, 12, or 15. How much tip would you like to give? 10, 12, or 15?")

#eneter how many people to split the bill
numberOfPeople = int(input("How many people to split the bill?"))

tip = 1.0+ float(totalTip)/100
tip = "{:.2f}".format(tip)

totalPerPerson = (totalBill)/(numberOfPeople) * float(tip)
totalPerPerson = "{:.2f}".format(totalPerPerson)


print(f"Each person should pay: ${totalPerPerson}")
