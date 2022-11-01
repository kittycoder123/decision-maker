print({"press 1 to calculate area of square and 2 to celceus to fareheit"})
decision=int(input("enter the number "))
if decision==1:
 s=int(input("enter the length of the square ")) 
 formula=s*s
 print("area of the given square is ",formula)
else:
 temprature=float(input("enter the temperature "))
 farenhiet=(temprature*1.8)+32
 print("the temperature in farenhiet is ",farenhiet,"F")