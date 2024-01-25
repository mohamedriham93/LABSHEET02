speed = int(input("Enter Speed: "))

if 31 <= speed <= 40:
    fine = 50
elif 41 <= speed <= 50:
    fine = 75
elif speed > 50:
    fine = 100
else:
    fine = 0


print (f"The fine for speeding at {speed} mph is {fine} pounds.")