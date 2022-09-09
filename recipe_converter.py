
allowed_types = ['minecraft:crafting_shaped', 'minecraft:crafting_shapeless']

def check_recipe_eligibility(recipe: object) -> object:
    pass

def convert_recipe_to_shulkerboxed(recipe: object) -> object:
    if recipe['type'] not in allowed_types:
        raise TypeError('Invalid crafting type')
    try:
        count = int(recipe['result']['count'])
        if count > 1:
            raise ValueError('Recipe output too high')
    except:
        pass


    pass

if __name__ == '__main__':
    pass