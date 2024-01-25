side1 = float(input("enter side 1: "))
side2 = float(input("enter side 2: "))
side3 = float(input("enter side 3: "))

if side1 == side2 == side3 :
    output =("Equilateral")

elif side1 == side2 or side1 == side3 or side2 == side3:
        output = ("Isosceles")
else:
    output = ("Scalene")

print (output)