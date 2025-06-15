from datetime import datetime

def calculate_year(birth_year):
    current_year = datetime.now().year 
    age = current_year - birth_year
    return age
    """ Yoshni hisoblash.
    Args:
        birth_year -> tu'g'ilgan yil 
        current_year -> hozirgi yil
    Return:
          Hisoblangan yosh.
    """


birth_year = int(input("To'g'ilgan yilingizni kiriting: "))
age = calculate_year(birth_year)

print(f" Sizning yoshingiz {age} da!")