def is_strong_password(password):
    return len(password) >= 8

def main():
    password = input("Parol kiriting: ")

    if is_strong_password(password):
        print("Kuchli parol.")
    else:
        print("Parol kuchsiz. Kamida 8 ta belgidan iborat bo‘lishi kerak.")

main()
