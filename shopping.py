# Prompt the user to enter the name of the first product and store it in a variable
product_1 = input("Please enter the name of the first product: ")

# Prompt the user to enter the name of the second product and store it in a variable
product_2 = input("Please enter the name of the second product: ")

# Prompt the user to enter the name of the third product and store it in a variable
product_3 = input("Please enter the name of the third product: ")

# Prompt the user to enter the price of the first product and handle non-numeric input
while True:
    try:
        price_of_product_1 = float(input("Please enter the price of the first product, including the amount of cents: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Prompt the user to enter the price of the second product and handle non-numeric input
while True:
    try:
        price_of_product_2 = float(input("Please enter the price of the second product, including the amount of cents: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Prompt the user to enter the price of the third product and handle non-numeric input
while True:
    try:
        price_of_product_3 = float(input("Please enter the price of the third product, including the amount of cents: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


# Calculate the total price of all three products and store it in a variable
total_price_of_products = price_of_product_1 + price_of_product_2 + price_of_product_3

# Calculate the average price of all three products and round it to 2 decimal places, then store it in a variable
average_price_of_products = round(total_price_of_products / 3, 2)

# Print out a string that includes the names of all three products, their total price, and their average price
print("The total of {}, {}, and {} is R{} and the average price of the items is R{:.2f}".format(product_1, product_2, product_3, total_price_of_products, average_price_of_products))
