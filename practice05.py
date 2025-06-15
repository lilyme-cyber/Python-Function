def check_guess(secret, guess):
    result = secret == guess
    return result
    """ Sirli sonni topish
    Args:
        secret: sirli son
        guess: foydalanuvchi taxmin qilgan son
    Returns: secret va guess bir xil bo'lsa true
    """


def print_result(is_correct):
    if is_correct:
        print("To'g'ri topdingiz.")
    else:
        print("Topolmadingiz.")
    """ Natijani chiqaradi - to'g'ri yoki noto'g'ri.
    Args: 
         is_correct (bool): True agar taxmin to‘g‘ri bo‘lsa
    Returns : None
    """

secret = 65
guess = int(input("Sirli sonni toping:"))

is_correct = check_guess(secret, guess)
print_result(is_correct)
