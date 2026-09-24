def name():
    print("Hello World")

name()

def add(a,b):
    return a+b

result = add(5, 3)
print("Result:", result)

#enter the value of a and b from input
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
result = add(a, b)
print("Result:", result)