# calculator.py
import sys

if len(sys.argv) != 3:
    print("Usage: python calculator.py <num1> <num2>")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[2])

print("Addition: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b if b != 0 else "Cannot divide by zero")
