def add(a, b):

    return a + b
    """Ikki sonni qo'shadi
     Args:
        a birinchi son
        b ikkinchi son
    Returns:
           Qo'shilgan natija
    """
 
def subtract(a, b):
    return a - b
    """Ikki sonni ayiradis
    Args:
        a birinchi son
        b ikkinchi son
    Returns:
           Ayitilgan natija
    """

def multiply(a, b): 
    return a * b
    """Ikki sonni ko'paytiradi
    Args:
        a birinchi son
        b ikkinchi son
    Returns:
           ko'paytirilgan natija
    """

def divide(a, b): 
    if b == 0:
        return "Nolga bo'lish mumkin emas"
    return a / b 
    """Ikki sonni bo'ladi
    Args:
        a birinchi son
        b ikkinchi son
    Returns:
           Bo'lingan natija
    """

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