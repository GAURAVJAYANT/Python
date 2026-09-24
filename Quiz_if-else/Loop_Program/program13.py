print("Check number even or odd")
#even=0
number = int(input("Enter the value here:-"))
for i in range(1,1+number):
    if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")