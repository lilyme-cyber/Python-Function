def get_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif 50 <= score <= 59:
        return "E"
    elif 0 <= score < 50:
        return "F"
    else:
        return "Xato! Ball 0 va 100 orasida bo‘lishi kerak."


score = input("Balingizni kiriting: ")


if score.isdigit():
    score = int(score)
    result = get_grade(score)
    print(f"Sizning bahoyingiz: {result}")
else:
    print("Iltimos, faqat son kiriting.")
