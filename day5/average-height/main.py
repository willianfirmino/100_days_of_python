# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

sum_studants = 0
count_studants = 0
for i in student_heights:
  sum_studants += i
  count_studants += 1

print(round(sum_studants/count_studants))


