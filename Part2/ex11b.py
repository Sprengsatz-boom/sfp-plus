#the calculating portion
def calculate(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b

#the output
print(calculate(10, "+", 10))
print(calculate(10, "-", 10))
print(calculate(10, "*", 10))
print(calculate(10, "/", 10))