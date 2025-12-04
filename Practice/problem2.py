def fix_inventory_codes(codes):
    new_list = []
    for c in codes:
        code = c.replace(" ", "").replace("-", "").upper()
        new_list.append(code)
        if len(code) < 3:
            new_list.remove(code)
    return new_list
raw_codes = [
    "abc-123",
    "  X-99 ",
    "prod 456",
    "a-1",       # Too short after cleaning (becomes "A1")
    "super-item"
]

# Run the function
fixed_codes = fix_inventory_codes(raw_codes)
print(fixed_codes)