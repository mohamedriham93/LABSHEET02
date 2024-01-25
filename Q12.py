cost_price = int(input("Enter cost price: "))
selling_price = int(input("Enter selling price: "))

final_price = selling_price - cost_price

if final_price < 0 :
    print (final_price ," Loss")

elif final_price == 0 :
    print ("No Gain")

else :
    print (final_price, " Gain")