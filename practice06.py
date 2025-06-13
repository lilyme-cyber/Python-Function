def is_valid_phone_number(phone):
    return phone.isdigit() and len(phone) == 9

number = input("Telefon raqam kiriting: ")

if is_valid_phone_number(number):
    print("True")
else:
    print("False")
