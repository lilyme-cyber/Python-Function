def is_palindrome(text):
    """
    Berilgan matn palindrome (teskari o‘qilganda ham bir xil) ekanligini tekshiradi.

    Parametr:
        text (str): Tekshiriladigan so‘z yoki gap

    Returns:
        bool: True agar palindrome bo‘lsa, aks holda False
    """
    cleaned = text.lower().replace(" ", "")  # faqat kichik harflar va bo‘shliqsiz
    return cleaned == cleaned[::-1]


def main():
    """
    Foydalanuvchidan matn qabul qilib, u palindrome ekanligini bildiradi.
    """
    print("Palindrome Tekshiruv Dasturi")
    text = input("So‘z yoki gap kiriting: ")

    if is_palindrome(text):
        print("Bu matn palindrome!")
    else:
        print("Bu matn palindrome emas.")


# Dastur ishga tushiriladi
main()

      