print("Welcome to World Bank ATM")

correct_pin = 1234
balance = 10000

pin = int(input("Enter your ATM PIN: "))

if pin == correct_pin:

    print("PIN is correct")
    print("Current Balance:", balance)

    transaction = input(
        "Enter transaction type (credit/debit): "
    ).lower()

    amount = int(input("Enter amount: "))

    if transaction == "credit":

        balance = balance + amount

        print("Amount credited:", amount)
        print("Updated Balance:", balance)

    elif transaction == "debit":

        if amount <= balance:

            balance = balance - amount

            print("Amount debited:", amount)
            print("Updated Balance:", balance)

        else:

            print("Insufficient balance")
            print("Available Balance:", balance)

    else:

        print("Invalid transaction type")

else:

    print("Incorrect PIN")