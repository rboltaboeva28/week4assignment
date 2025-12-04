recipe = {
    "flour": 500,
    "sugar": 200,
    "eggs": 3,
    "milk": 100,
    "vanilla": 5
}

pantry = {
    "flour": 400,       # We have some, but not enough (need 100 more)
    "eggs": 10,         # We have plenty (need 0)
    "milk": 100,        # We have exact amount (need 0)
    # sugar is missing completely (need 200)
    # vanilla is missing completely (need 5)
}

def generate_list(recipe, pantry):
    shopping_list = {}
    for item, amount in recipe.items():
        exist = pantry.get(item,0)
        needed = amount - exist
        if needed > 0:
            shopping_list[item] = needed
    print("Shopping List: ")
    for item, amount in shopping_list.items():
        print(f"{item}: {amount}")

generate_list(recipe, pantry)           

    