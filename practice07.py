def ask_question(question):
    user_answer = input(f"{question} ").strip()
    return user_answer
    """ Foydalanuvchiga savol berish
    Args:
        question: Beriladigan savol
        user_answer: Foydalanuvchi kiritadigan javob
    Returns: Foydalanuvchi javobi.
    """
    
def check_answer(user_answer, correct_answer):
    result = user_answer.lower() == correct_answer.lower()
    return result
    """ Javob to'g'riligini tekshiradi
    Args: 
        user_answer: foydalanavchi kiritgan javob
        correct_answer: to'g'ri javob
    Returns:
       True agar to'g'ri bo'lsa
    """

def main():
    question = "O'zbekiston poytaxti qayer?"
    correct_answer = "Toshkent"

    user_answer = ask_question(question)
    is_correct = check_answer(user_answer, correct_answer)

    if is_correct:
        print("To'g'ri topdingiz.")
    else:
        print(f"Topolmadingiz, to'g'ri javob \"{correct_answer}\"")

main()
