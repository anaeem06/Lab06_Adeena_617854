def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    return None

a = float(input("First number: "))
op = input("Operator (+, -, *, /): ")
b = float(input("Second number: "))
print("Result:", calculate(a, b, op))