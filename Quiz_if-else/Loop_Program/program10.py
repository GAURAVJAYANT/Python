largest = 0

for i in range(5):
    number = int(input("Enter number: "))

    if number > largest:
        largest = number

print("Largest number:", largest)