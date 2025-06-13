# def calculate_year(current_year, birth_year):
# age = current_year - birth_year
# return age

# current_year = int(input("Hozirgi yilni kiriting: "))
# birth_year = int(input("Yilingizni kiriting: "))

# age = calculate_year(current_year, birth_year)
# print(f"Sizning yoshingiz {age}da!")

# new code - hozirgi yilni avtomatik aniqlash

from datetime import datetime

def calculate_year(birth_year):
    current_year = datetime.now().year #hozirgi yilni aniqlash
    age = current_year - birth_year
    return age


birth_year = int(input("To'g'ilgan yilingizni kiriting: "))
age = calculate_year(birth_year)

print(f" Sizning yoshingiz {age} da!")