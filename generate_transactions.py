import asyncio
import json
import random
from datetime import datetime

# Определяем возможные категории транзакций
CATEGORIES = ['Food', 'Transport', 'Utilities', 'Entertainment', 'Health', 'Shopping']

async def generate_transaction():
    """Генерирует одну транзакцию."""
    timestamp = datetime.now().isoformat()
    category = random.choice(CATEGORIES)
    amount = round(random.uniform(1, 1000), 2)  # Генерация суммы от 1 до 1000
    return {'timestamp': timestamp, 'category': category, 'amount': amount}

async def save_transactions(transactions, file_index):
    """Сохраняет транзакции в файл и выводит информацию в консоль."""
    filename = f'transactions_{file_index}.json'
    with open(filename, 'w') as f:
        json.dump(transactions, f, indent=4)
    print(f'Saved {len(transactions)} transactions to {filename}')

async def generate_transactions(num_transactions):
    """Генерирует заданное количество транзакций и сохраняет их в файлы."""
    transactions = []
    for i in range(num_transactions):
        transaction = await generate_transaction()
        transactions.append(transaction)

        # Сохраняем каждые 10 транзакций
        if (i + 1) % 10 == 0:
            await save_transactions(transactions, (i + 1) // 10)
            transactions = []  # Сбрасываем список транзакций

    # Сохраняем оставшиеся транзакции, если они есть
    if transactions:
        await save_transactions(transactions, (num_transactions + 9) // 10)

if __name__ == '__main__':
    num_transactions = int(input("Enter the number of transactions to generate: "))
    asyncio.run(generate_transactions(num_transactions))
