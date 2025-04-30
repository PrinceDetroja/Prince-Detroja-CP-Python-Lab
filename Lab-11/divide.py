x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
try:
    z = x/y
    print(z)
except ZeroDivisionError:
    print("Division by zero gives infinite")
z=x*y
print(z)