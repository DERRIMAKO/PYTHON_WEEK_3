def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price  # Return original price if discount is less than 20%

# Example usage:
print(calculate_discount(100, 25))  # Output: 75.0
print(calculate_discount(100, 10))  # Output: 100 (No discount applied)
