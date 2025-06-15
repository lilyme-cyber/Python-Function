def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)
    """
    BMI (Body Mass Index) ni hisoblaydi.

    Args:
        weight (float): Og‘irlik (kg)
        height (float): Bo‘y (metr)

    Returns:
        float: Hisoblangan BMI qiymati
    """


def bmi_status(bmi):
    if bmi < 18.5:
        return "Ozgin"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Semiz"
        """
    BMI asosida vazn holatini aniqlaydi.

    Args:
        bmi (float): BMI qiymati

    Returns:
        str: BMI holati — 'Ozg'in', 'Normal', 'Semiz'
    """

def main():
    weight = float(input("Vazningizni kiriting (kg): "))
    height = float(input("Bo'yingizni kiriting (metrlarda): "))

    bmi = calculate_bmi(weight, height)
    status = bmi_status(bmi)

    print(f"\nBMI: {bmi}")
    print(f"Holati: {status}")

main()
