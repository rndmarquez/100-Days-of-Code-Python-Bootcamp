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
for j in student_heights:
     sumOfStudentHeights += j
     amountOfStudents += 1

average = round(sumOfStudentHeights/amountOfStudents)
print(f"{average}")





