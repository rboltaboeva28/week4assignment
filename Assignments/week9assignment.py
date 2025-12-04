def calculate_total(invoice_text):
    text = invoice_text.split("\n")
    total = 0
    for line in text:
        if "TAX" in line:
            tax_str = line.replace("TAX:", "".replace("%", ""))
            tax = float(tax_str) / 100
        elif "@" in line and "x$" in line:
            parts = line.split("$")
            price = float(parts[1])
            quantity = parts[0]
        elif "DISCOUNT" in line:
            ...
