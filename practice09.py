def deposit(balance, amount):
    new_balance = balance + amount
    return new_balance
    """
    Balansga pul qo‘shadi.

    Args:
        balance (float): Hozirgi balans
        amount (float): Qo‘shiladigan miqdor

    Returns:
        float: Yangi balans
    """


def withdraw(balance, amount):
    if amount <= balance:
        new_balance = balance - amount
    else:
        new_balance = balance
    return new_balance
    """
    Balansdan pul yechadi.

    Args:
        balance (float): Hozirgi balans
        amount (float): Yechiladigan miqdor

    Returns:
        float: Yangi balans

    Raises:
        ValueError: Agar balans yetarli bo‘lmasa
    """

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
