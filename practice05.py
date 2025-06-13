def check_guess(secret, guess):
    result = secret == guess
    return result


def print_result(is_correct):
    if is_correct:
        print("To'g'ri topdingiz.")
    else:
        print("Topolmadingiz.")

secret = 65
guess = int(input("Sirli sonni toping:"))

is_correct = check_guess(secret, guess)
print_result(is_correct)
