from copy import deepcopy
import shulker_box_generators

from items import non_64_stack, allowed_types

def check_recipe_eligibility(recipe: object) -> object:
    if recipe['type'] not in allowed_types:
        raise TypeError('Invalid crafting type')
    if recipe['result']['item'] in non_64_stack:
        raise MemoryError('Non 64 stack output')
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

    count_dict = dict()

    for row in recipe['pattern']:
        for letter in row:
            if letter == ' ':
                continue
            if letter not in count_dict.keys():
                count_dict[letter] = 1
            else:
                count_dict[letter] += 1

    minimum_key = min(count_dict, key=count_dict.get)

    for dict_key in new_recipe['key']:
        item_identifier = new_recipe['key'][dict_key]['item']
        new_recipe['key'][dict_key] = shulker_box_generators.generate_all_shulker_box_variants(item_identifier, dict_key != minimum_key)
    
    new_recipe['result'] = shulker_box_generators.generate_result_shulker_box(recipe['result']['item'])
    return new_recipe

def convert_shapeless_recipe(recipe: object) -> object:
    new_recipe = deepcopy(recipe)
    new_recipe['ingredients'] = list()
    
    count_dict = dict()

    for ingredient in recipe['ingredients']:
        item_id = ingredient['item']
        if item_id not in count_dict.keys():
            count_dict[item_id] = 1
        else:
            count_dict[item_id] += 1
    
    minimum_item_id = min(count_dict, key = count_dict.get)

    for ingredient in recipe['ingredients']:
        item_identifier = ingredient['item']
        new_recipe['ingredients'].append(shulker_box_generators.generate_all_shulker_box_variants(item_identifier, item_identifier != minimum_item_id))

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