mark = int(input("Enter Mark: "))

if mark < 70:
    grade = "D"

elif mark < 79:
    grade = "C"

elif mark < 89:
    grade = "B"

else:
    grade = "A"

print (grade)
