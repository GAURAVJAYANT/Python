print("Welcome to ICICI Bank")

Amount = 10000

pin = int(input("Enter the PIN here: "))

if pin == 1234:

    print("Correct PIN entered")

    transaction = input("Choose the option (credit/debit): ").lower()

    if transaction == "credit":

        credit = int(input("Enter the amount: "))

        Amount = Amount + credit

        print("Amount credited:", credit)
        print("Updated Balance:", Amount)

    elif transaction == "debit":

        debit = int(input("Enter the withdrawal amount: "))

        if debit <= 0:

            print("Invalid withdrawal amount")

        elif debit > Amount:

            print("Insufficient balance")
            print("Available Balance:", Amount)

        else:

            Amount = Amount - debit

            print("Amount debited:", debit)
            print("Updated Balance:", Amount)

    else:

        print("Invalid transaction type")

else:

    print("Incorrect PIN")