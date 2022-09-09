import os
import json

from recipe_converter import convert_recipe_to_shulkerboxed

# name of directory with recipe JSONs
dir_with_recipes = 'recipes_test'
dir_output = 'recipes_with_shulkerboxes'



if __name__ == '__main__':
    types = list()
    for recipe_file_name in os.listdir(dir_with_recipes): # iterate through files
        full_path = os.path.join(dir_with_recipes, recipe_file_name)

        # check validity
        if os.path.isfile(full_path): # this should be a recipe.json
            with open(full_path) as file_object:
                recipe = json.load(file_object)
                print(f'Loaded recipe {recipe_file_name}')

                try:
                    converted_recipe = convert_recipe_to_shulkerboxed(recipe)
                    print(f'Converted recipe {recipe_file_name} to shulkerboxed')
                    with open(dir_output + '/' + recipe_file_name, 'w') as outfile:
                        json.dump(converted_recipe, outfile, indent = 4)
                    print(f'Shulkerboxed {recipe_file_name} saved!')
                except TypeError as error:
                    print(error)
            pass

    # print(generate_filled_shulker_box("minecraft:diamond", "shulker_box"))
    pass