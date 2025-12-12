def calculate_item_total(quantity, unit_price):
    return quantity * unit_price

def apply_bulk_discount(total, quantity):
    if quantity >= 10:
        discount = total * 0.1
    elif quantity >= 5:
        discount = total * 0.05
    else:
        discount = 0
    return discount

def calculate_tax(subtotal, tax_rate):
    return subtotal * (tax_rate / 100)

def is_eligible_for_free_shipping(subtotal):
    return subtotal >= 50


def process_order(item_name, quantity, unit_price, tax_rate):
    item_total = calculate_item_total(quantity, unit_price)
    bulk_discount = apply_bulk_discount(item_total, quantity)
    subtotal = item_total - bulk_discount
    tax = calculate_tax(subtotal, tax_rate)
    final_total = subtotal + tax
    shipping_eligibility = is_eligible_for_free_shipping(final_total)
    print(f"Order receipt for: {item_name}")
    print(f"   Quantity: {quantity} @ {unit_price} each")
    print(f"   Item total: ${item_total:.2f}")
    print(f"   Bulk discount: -${bulk_discount:.2f}")
    print(f"   Subtotal: ${subtotal:.2f}")
    print(f"   Tax({tax_rate}%): ${tax:.2f}")
    print(f"   Final Total: ${final_total:.2f}")
    if subtotal >= 50:
        print("   Eligible for free shipping")
    else:
        print(f"   Need ${50-subtotal:.2f} more for free shipping")
    
    print("-"*40)



print("SHOPPING CART CALCULATOR")
print("="*40)
process_order("Notebooks", 12, 3.50, 8)
process_order("Pens", 6, 1.25, 8)
process_order("Paper", 3, 4.99, 8)