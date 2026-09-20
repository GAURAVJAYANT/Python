print("Calculate electricity bill")

unit = int(input("Enter electricity unit consumption: "))

if unit < 0:
    print("Invalid units")

elif unit <= 100:
    print("Electricity Bill:", unit * 5)

elif unit <= 200:
    print("Electricity Bill:", unit * 7)

elif unit <= 300:
    print("Electricity Bill:", unit * 10)

else:
    print("Electricity Bill:", unit * 15)