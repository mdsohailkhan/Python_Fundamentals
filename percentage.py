total_amount=int(input("please enter an number "))

if(total_amount>200):
    print((20/100)*total_amount,"$ off","of your",total_amount,"$")
   # coupon_20=(20/200)*total_amount
    print("after discount your total amount to pay is",total_amount-(20/100)*total_amount,"$")
    
elif(total_amount>100):
    print((10/100)*total_amount,"$ off","of your",total_amount,"$")
   # coupon_10=(10/100)*total_amount
    print("after discount your total amount to pay is",total_amount-(10/100)*total_amount,"$")
    