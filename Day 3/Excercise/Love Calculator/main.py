# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
word1 = "love"
word2 = "true"

#lowercase name1
name1 = name1.lower()

#lowercase name2
name2 = name2.lower()

#combine name
name = name1 + " " + name2

#count how many times letters in love occur
countLove = 0
for i in word1:
    #print (i)
    countLove += name.count(i)

countTrue = 0
for j in word2:
    #print (j)
    countTrue += name.count(j)

#concat the two numbers
#print("Count Love " + str(countLove))
#print("Count True " + str(countTrue))
count = str(countTrue) + str(countLove)
#print(count)

#calculate compatibility
if int(count) < 10 or int(count) >90:
    print(f"Your score is {count}, you go together like coke and mentos")
elif int(count) > 40 and int(count) <50:
    print(f"Your score is {count}, you are alright together")
else:
    print(f"Your score is {count}")
