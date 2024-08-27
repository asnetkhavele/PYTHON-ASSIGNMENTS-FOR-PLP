def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
price = float(input("10000: "))
discount_percent = float(input("10: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print the final price
print(f"The final price after applying the discount is: ${final_price:.2f}")
