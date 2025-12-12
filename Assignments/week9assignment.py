def calculate_total(invoice_text):
    subtotal = 0.0
    tax_rate = 0.0
    discount = 0.0
    text = invoice_text.split("\n")
    for line in text:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if "TAX:" in line:
            tax_rate = float(parts[1].replace("%", "")) / 100
        elif "DISCOUNT:" in line:
            discount = float(parts[1].replace("$", ""))
        else:
            price = float(parts[-1].replace("$", ""))
            quantity = int(parts[2])
            subtotal += quantity * price
    subtotal_after_discount = subtotal - discount
    tax_amount = subtotal_after_discount * tax_rate
    grand_total = (subtotal - discount) * (1 + tax_rate)
    return f"${grand_total:.2f}"

# Test Case 1: Standard invoice with items, tax, and discount
invoice1 = """Laptop @ 1 x $1250.00
Mouse @ 2 x $25.50
TAX: 8%
DISCOUNT: $50.00"""
print(calculate_total(invoice1))

# Test Case 2: Invoice with no discount
invoice2 = """Book @ 3 x $15.00
Pen @ 10 x $1.50
TAX: 5%"""
print(calculate_total(invoice2))

# Test Case 3: Invoice with zero tax and a discount
invoice3 = """Monitor @ 1 x $300.00
Keyboard @ 1 x $75.00
DISCOUNT: $25.00
TAX: 0%"""
print(calculate_total(invoice3))