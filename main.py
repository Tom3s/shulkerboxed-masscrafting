import os
import json
from shulker_box_generators import generate_filled_shulker_box

# name of directory with recipe JSONs
dir_with_recipes = 'recipes_original'



if __name__ == '__main__':
    types = list()
    for recipe_file_name in os.listdir(dir_with_recipes): # iterate through files
        full_path = os.path.join(dir_with_recipes, recipe_file_name)

        # check validity
        if os.path.isfile(full_path): # this should be a recipe.json
            with open(full_path) as file_object:
                recipe = json.load(file_object)

                curr_type = recipe["type"]
                if curr_type not in types:
                    types.append(curr_type)

            pass

    # print(generate_filled_shulker_box("minecraft:diamond", "shulker_box"))
    print(types)
    pass