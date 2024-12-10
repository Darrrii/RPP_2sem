import asyncio
import json
from collections import defaultdict

async def process_transactions(filename):
    """Обрабатывает файл с транзакциями, группируя их по категории и суммируя суммы."""
    with open(filename, 'r') as f:
        transactions = json.load(f)

    category_totals = defaultdict(float)

    for transaction in transactions:
        category_totals[transaction['category']] += transaction['amount']

    # Выводим результаты
    for category, total in category_totals.items():
        print(f'Category: {category}, Total Amount: {total:.2f}')

if __name__ == '__main__':
    filename = input("Enter the filename of the transactions to process: ")
    asyncio.run(process_transactions(filename))
