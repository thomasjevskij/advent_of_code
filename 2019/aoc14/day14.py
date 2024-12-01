def parse_input():
    with open(0) as f:
        lines = [l.strip() for l in f.readlines()]
    recipes = {}
    for l in lines:
        recipe, result = l.split(' => ')
        amt, name = result.split()
        ingredients = tuple(recipe.split(', '))

        recipes[name] = (int(amt), ingredients)
    return recipes

def make(thing, recipes):
    amt, recipe = recipes[thing]
    print(f'{thing}:')
    for s in recipe:
        a, ing = s.split()
        print(int(a), ing)
    print('')

def p1(recipes):
    for k in recipes:
        make(k, recipes)

def p2(recipes):
    print('Not done yet.')

recipes = parse_input()

p1(recipes)
p2(recipes)
