def is_valid_phone_number(phone):
    return phone.isdigit() and len(phone) == 9
    """ Telefon raqam 9 xonali ekanligini tekshirish.
    Args:
        phone: telefon raqam 
    Rerurns:
         bool: True agar 9 xonali bo‘lsa, aks holda False
    """

number = input("Telefon raqam kiriting: ")

if is_valid_phone_number(number):
    print("True")
else:
    print("False")
