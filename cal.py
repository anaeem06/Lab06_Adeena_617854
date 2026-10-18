def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: division by zero"
        return a / b
    elif op == "%":
        return a % b
    elif op == "//":
        return a // b
     elif op in ("%", "//"):
        if b == 0:
            return "Error: division by zero"
        return a % b if op == "%" else a // b
    elif op == "**":
        return a ** b
    return "Error: unknown operator"

a = float(input("First number: "))
op = input("Operator (+, -, *, /, %, //, **): ")
b = float(input("Second number: "))
print("Result:", calculate(a, b, op))