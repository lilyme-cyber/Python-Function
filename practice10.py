def is_strong_password(password):
    return len(password) >= 8
    """
    Parol kuchliligini tekshiradi.

    Args:
        password: Kiritilgan parol

    Returns:
        bool: True agar parol uzunligi 8 yoki undan ko‘p bo‘lsa
    """

def main():
    password = input("Parol kiriting: ")

    if is_strong_password(password):
        print("Kuchli parol.")
    else:
        print("Parol kuchsiz. Kamida 8 ta belgidan iborat bo‘lishi kerak.")

main()
