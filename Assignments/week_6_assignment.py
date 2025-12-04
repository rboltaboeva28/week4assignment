def calculate_total_profit(dish_tuple):
    name, cat, cost, price, ordered = dish_tuple
    return (price - cost) * ordered


def find_most_profitable_dish(menu_data):
    best_name = ''
    best_profit = -1
    for dish in menu_data:
        profit = calculate_total_profit(dish)
        if not best_name:
            best_name = dish[0]
            best_profit = profit
        elif profit > best_profit:
            best_name = dish[0]
            best_profit = profit
        elif profit == best_profit:
            if dish[0] < best_name:
                best_name = dish[0]
    return best_name


def get_dishes_in_category(menu_data, category_name):
    result = []
    for dish in menu_data:
        if dish[1] == category_name:
            result.append(dish[0])
    result.sort()
    return result


def get_category_popularity(menu_data):
    categories = {}
    for dish in menu_data:
        cat = dish[1]
        ordered = dish[4]
        if not cat in categories:
            categories[cat] = 0
        categories[cat] += ordered
    output = []
    for cat in categories:
        output.append((cat, categories[cat]))
    output.sort()
    return output


def analyze_menu(menu_data):
    most_profitable = find_most_profitable_dish(menu_data)
    main_course_dishes = get_dishes_in_category(menu_data, "Main Course")
    category_summary = get_category_popularity(menu_data)
    return (most_profitable, main_course_dishes, category_summary)

menu_data = [
    ('Bruschetta', 'Appetizer', 2.50, 8.50, 150),  # Profit: 900
    ('Steak Frites', 'Main Course', 9.00, 24.00, 200), # Profit: 3000
    ('Caesar Salad', 'Appetizer', 3.00, 10.00, 250), # Profit: 1750
    ('Pasta Carbonara', 'Main Course', 5.50, 18.50, 300),# Profit: 3900
    ('Tiramisu', 'Dessert', 4.00, 9.00, 400)      # Profit: 2000
]

print(analyze_menu(menu_data))