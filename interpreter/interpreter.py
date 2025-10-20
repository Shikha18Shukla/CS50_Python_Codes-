expression = input("Expression: ")

if " " in expression:
    x, operator, z = expression.split()
else:
    operator = ""
    for char in expression:
        if char in "+-*/":
            operator = char
            break
    if operator:
        x, z = expression.split(operator)

try:
    x = float(x)
    z = float(z)

    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        result = x / z

    print(f"{result}\n", end="")  
except:
    print("Invalid expression format. Use format like 3 + 4 or 3+4")

