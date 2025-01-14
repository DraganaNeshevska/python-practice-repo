#test weighted scoring model formula and exponential decay functions

# Sample data for the user's price preference
user_min_price = 1000  # Minimum price preference
user_max_price = 2000  # Maximum price preference

# Example price for a product
product_price = 1500  # Replace this with any price you want to test

# Check if the price is within the user's price preference
price_within_preference = 1 if user_min_price <= product_price <= user_max_price else 0

# Print the result
print(f"The price {product_price} is within the user's preference: {price_within_preference}")
