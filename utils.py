def calculate(n1, n2, op):
    try:
        a = float(n1)
        b = float(n2)
    except ValueError:
        return "Invalid input"

    if op == "add":
        return a + b
    elif op == "subtract":
        return a - b
    elif op == "multiply":
        return a * b
    elif op == "divide":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operation"

    
