def calculate_tax(salary):
    if salary > 5_000_000:
        tax = salary * 0.2
    else:
        tax = salary * 0.13
    return tax


def calculate_net_salary(salary, tax):
    net_salary = salary - tax
    return net_salary


salary = 10_000_000
tax = calculate_tax(salary)
print(tax)

net_salary = calculate_net_salary(salary, tax)
print(net_salary)