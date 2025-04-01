# Function that calculates the final price after applying the discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price 

# Example
print(calculate_discount(100, 25))
print(calculate_discount(100, 10)) 

# Get user input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

print("Final price:", final_price)
