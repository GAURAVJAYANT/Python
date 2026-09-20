print("Enter marks here:-")

marks = int(input("Enter marks here:-"))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter marks between 0 and 100.")

elif marks >= 90:
    print("You got A grade")

elif marks >= 80 and marks <= 89:
    print("You got B grade")

elif marks >= 70 and marks <= 79:
    print("You got C grade")

elif marks >= 60 and marks <= 69:
    print("You got D grade")

else:
    print("You got F grade")