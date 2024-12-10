def calculate_shipping(country, weight):
    shipping_costs = {
        "USA": {True: 10, False: 20},
        "Canada": {True: 15, False: 25},
        "Other": {True: 30, False: 50}
    }
    is_lightweight = weight < 5
    return shipping_costs.get(country, shipping_costs["Other"])[is_lightweight]

if __name__ == "__main__":
    # Примеры вызовов функции
    country = "USA"
    weight = 4  # Пример веса
    cost = calculate_shipping(country, weight)
    print(f"Shipping cost for {weight}kg to {country}: ${cost}")

    country = "Canada"
    weight = 6  # Пример веса
    cost = calculate_shipping(country, weight)
    print(f"Shipping cost for {weight}kg to {country}: ${cost}")

    country = "Mexico"  # Пример страны, не в списке
    weight = 3
    cost = calculate_shipping(country, weight)
    print(f"Shipping cost for {weight}kg to {country}: ${cost}")
