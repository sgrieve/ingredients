from measurement.utils import guess

def read_recipe(recipe_file):
    ingredients = []
    with open(recipe_file) as f:
        for line in f.readlines():
            ingredient = line.split(',')
            ingredients.append([ingredient[0],
                                float(ingredient[1]),
                                ingredient[2].strip()])
    return ingredients


def parse_ingredients(ingredients):
    ingredient_dict = {}
    for ingredient in ingredients:
        if ingredient[2] != 'n':
            measurement = guess(ingredient[1], ingredient[2])
            ingredient_dict[ingredient[0]] = measurement
        else:
            ingredient_dict[ingredient[0]] = ingredient[1]

    return ingredient_dict


def combine_ingredients(*ingredient_dicts):

    combined_ingredients = {}
    for ingredients in ingredient_dicts:

        for ingredient, amount in ingredients.items():
            if ingredient in combined_ingredients:
                combined_ingredients[ingredient] += amount
            else:
                combined_ingredients[ingredient] = amount

    return combined_ingredients


def format_shopping_list(combined_ingredients):

    head = '''<!DOCTYPE html>
    <html>
    <body>

    <h1>Shopping List</h1>

    <form>'''

    foot = '''</form>

    </body>
    </html>'''

    with open('index.html', 'w') as f:
        f.write(head)
        for ingredient, amount in combined_ingredients.items():
            if isinstance(amount, float):
                f.write('<input type="checkbox"> {}: {}<br>'.format(ingredient,
                                                                round(amount, 1)))
            else:
                f.write('<input type="checkbox"> {}: {} {}<br>'.format(ingredient,
                                                                   amount.value,
                                                                   amount.unit))

        f.write(foot)


i = parse_ingredients(read_recipe('katsu.txt'))
j = parse_ingredients(read_recipe('paella.txt'))

a = (combine_ingredients(i, j))

format_shopping_list(a)
