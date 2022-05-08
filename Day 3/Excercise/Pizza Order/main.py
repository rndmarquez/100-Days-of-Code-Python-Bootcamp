# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#initalize bill;
bill = 0

#uppercase all inputs
size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()

#check all inputs

#size small $15, medium $20, large $25
if size == "S":
    bill += 15
    if add_pepperoni =="Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni =="Y":
        bill += 3
else:
    bill += 25
    if add_pepperoni =="Y":
        bill += 3

if extra_cheese =="Y":
        bill += 1

#format bill  to 2 decimal places
#bill = float(bill)
#bill = "{:.2f}".format(bill)
print(f"Your final bill is: ${bill}.")
