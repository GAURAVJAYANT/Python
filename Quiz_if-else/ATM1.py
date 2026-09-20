print("Welcome to ICICI Bank")

Amount = 10000

pin = int(input("Enter the code here:-"))

if pin == 1234:

    print("Correct pin code entered")

    transaction = input("Choose the option you want (credit/debit): ")

    if transaction == "credit":

        credit = int(input("Enter the amount: "))

        print("Updated Balance:", Amount + credit)

    elif transaction == "debit":

        debit = int(input("Enter the withdraw amount: "))

        print("Updated Balance:", Amount - debit)

    else:

        print("Invalid transaction type")

else:

    print("Incorrect PIN")