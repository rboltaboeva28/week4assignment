# How to build things (Product -> {Material: Qty})
blueprints = {
    "Robot": {"Steel": 50, "Microchip": 5, "Wire": 20},
    "Drone": {"Plastic": 10, "Microchip": 2, "Battery": 1},
    "Console": {"Plastic": 50, "Microchip": 10, "Wire": 5}
}

# What we have right now
warehouse_stock = {
    "Steel": 200,
    "Plastic": 100,
    "Microchip": 20, # We have 20, but we might need more!
    "Wire": 100,
    "Battery": 50
}

# What we need to build today
production_queue = ["Robot", "Drone", "Robot", "Console"]
