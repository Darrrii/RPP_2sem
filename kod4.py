TAX_BRACKETS = [
    (10000, 0.1),
    (20000, 0.15),
    (float('inf'), 0.2)
]

def calculate_tax(income):
    """Calculates tax based on income using defined tax brackets."""
    for limit, rate in TAX_BRACKETS:
        if income <= limit:
            return income * rate

if __name__ == "__main__":
    # Примеры вызовов функции
    incomes = [5000, 15000, 25000]  # Примеры доходов
    for income in incomes:
        tax = calculate_tax(income)
        print(f"Income: ${income}, Tax: ${tax}")
