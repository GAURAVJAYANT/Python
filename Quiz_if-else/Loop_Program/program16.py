largest = 0

for i in range(5):
    number = int(input("Enter the value here: "))

    if number > largest:
        largest = number

print("Largest number =", largest)