# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:           #on every  yeardivisible by 4
    if year % 100 == 0:     #EXCEPT on year that is divible by 100
        if year % 400 == 0:
            print("Leap Year")
        else: 
            print("Not Leap Year") 
    else:
       print("Leap Year")      
else:
    print("Not Leap Year")


