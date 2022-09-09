from copy import deepcopy
import shulker_box_generators

allowed_types = ['minecraft:crafting_shaped', 'minecraft:crafting_shapeless']

def check_recipe_eligibility(recipe: object) -> object:
    if recipe['type'] not in allowed_types:
        raise TypeError('Invalid crafting type')
    try:
        count = int(recipe['result']['count'])
        if count > 1:
            raise ValueError('Recipe output too high')
    except ValueError:
        raise ValueError('Invalid count data')
    except KeyError: # no count attribute found
        pass

def convert_shaped_recipe(recipe: object) -> object:
    #raise TypeError('not yet implemented')
    new_recipe = deepcopy(recipe)
    special_key = ' '
    for dict_key in new_recipe['key']:
        if special_key == ' ':
            special_key = dict_key
        item_identifier = new_recipe['key'][dict_key]['item']
        new_recipe['key'][dict_key] = shulker_box_generators.generate_all_shulker_box_variants(item_identifier, True)
    
    new_recipe['key']['^'] = shulker_box_generators.generate_all_shulker_box_variants(recipe['key'][special_key]['item'], False)

    for i in range(new_recipe['pattern'].__len__()):
        if special_key not in new_recipe['pattern'][i]:
            continue
        new_recipe['pattern'][i] = new_recipe['pattern'][i].replace(special_key, '^', 1)
        break
    
    new_recipe['result'] = shulker_box_generators.generate_result_shulker_box(recipe['result']['item'])
    return new_recipe

def convert_shapeless_recipe(recipe: object) -> object:
    new_recipe = deepcopy(recipe)
    new_recipe['ingredients'] = list()
    box_used = False
    for ingredient in recipe['ingredients']:
        item_identifier = ingredient['item']
        new_recipe['ingredients'].append(shulker_box_generators.generate_all_shulker_box_variants(item_identifier, box_used))
        box_used = True

    new_recipe['result'] = shulker_box_generators.generate_result_shulker_box(recipe['result']['item'])
    return new_recipe

def convert_recipe_to_shulkerboxed(recipe: object) -> object:
    
    check_recipe_eligibility(recipe) # recipe can be converted to shulker boxed

    if recipe['type'] == 'minecraft:crafting_shaped':
        return convert_shaped_recipe(recipe)
    elif recipe['type'] == 'minecraft:crafting_shapeless':
        return convert_shapeless_recipe(recipe)
    pass

if __name__ == '__main__':
    pass