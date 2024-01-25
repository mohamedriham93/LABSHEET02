amount = int(input("input amount"))

if amount > 5000 :
    disprice = amount * 15 / 100
else :
    disprice = amount * 10 / 100


print (f"discount {disprice} ")
print (f"Purchasing amount {amount - disprice}")