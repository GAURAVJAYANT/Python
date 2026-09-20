print("Calculate electricity bill")
unit =int (input("Enter electricity uniy consumption:-"))
if(unit<0):
    print("Negative value")
elif(unit<0 or unit<=100):
    print(unit*5)
elif(unit<=101 and unit<=200):
    print(unit*7)
elif(unit<=201 and unit<=300):
    print(unit*10)
else:
    (unit*15)