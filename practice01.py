def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    if b == 0:
        return "Nolga bo'lish mumkin emas"
    return a / b 

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
operation = input("Amalni tanlang(+, -, *, /): ")

if operation == "+":
    result = add(a, b)  
elif operation == "-":
    result = subtract(a, b)  
elif operation == "*":
    result = multiply(a, b) 
elif operation == "/":
    result = divide(a, b) 
else:
    result = "Noto'g'ri amal tanlandi!" 

print(result)