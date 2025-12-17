data = """Apples,50,100
Bananas,120,100
Cherries,5,20
Dates,50,50
Eggs,10,24"""

with open("inventory.csv", "w") as f:
    f.write(data)

with open("inventory.csv", "r") as file, open("reorder_list.txt", "w") as file2:
    for line in file:
        parts = line.strip().split(",")
        product = parts[0]
        stock = int(parts[1])
        minimum = int(parts[2])
        if stock < minimum:
            needed = minimum - stock
            file2.write(f"Item: {product} | Order Amount: {needed}\n")