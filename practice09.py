def deposit(balance, amount):
    new_balance = balance + amount
    return new_balance

def withdraw(balance, amount):
    if amount <= balance:
        new_balance = balance - amount
    else:
        new_balance = balance
    return new_balance

def check_balance(balance):
    print(f"sizning balancinigiz = {balance}")

balance = 100.0

# deposit
amount = float(input("Qancha deposit qilmoqchisiz? "))
balance = deposit(balance, amount)
check_balance(balance)

# withdraw
amount = float(input("Qancha pul chiqarmoqchisiz? "))
balance = withdraw(balance, amount)
check_balance(balance)
