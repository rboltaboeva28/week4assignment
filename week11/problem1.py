def sum_valid_prices(price_list):
    total = 0.0
    for price in price_list:
        if price == "Free":
            continue
        if "$" in price:
            price = price.replace("$", "")
        try:   
            price = float(price)
            total += price
        except :
            print(f"Skipping invalid price: {price}")
    return total


raw_prices = ["$12.50", "Free", "error_404", "$5.00", "2.50", "N/A"]
total = sum_valid_prices(raw_prices)
print(f"Total: ${total}") 