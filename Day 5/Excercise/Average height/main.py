# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#cannot use len() or sum()
amountOfStudents = 0
sumOfStudentHeights = 0

#loop through the list
for j in range(len(student_heights)):
    #print(student_heights[j])
     sumOfStudentHeights += student_heights[j]
     amountOfStudents += 1

average = round(sumOfStudentHeights/amountOfStudents)
print(f"{average}")




