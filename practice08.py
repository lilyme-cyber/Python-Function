def c_to_f(celsius):
    return round((celsius * 9/5) + 32, 2)
    """  Selsiydan Farengeytga o‘tkazadi.

    Args:
        celsius: Selsiy qiymati

    """

def f_to_c(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)
    """   Farengeyttan Selsiyga o‘tkazadi.

    Args:
        fahrenheit: Farengeyt qiymati
    """

def main():
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    choice = input("Qaysi yo'nalishda aylantirmoqchisiz (1/2)? ")

    if choice == "1":
        celsius = float(input("Celsius haroratini kiriting: "))
        fahrenheit = c_to_f(celsius)
        print(f"{celsius}°C = {fahrenheit}°F")
    elif choice == "2":
        fahrenheit = float(input("Fahrenheit haroratini kiriting: "))
        celsius = f_to_c(fahrenheit)
        print(f"{fahrenheit}°F = {celsius}°C")
    else:
        print("Noto‘g‘ri tanlov!")

main()
