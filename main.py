import os
import json

from recipe_converter import recipe_converter

# name of directory with recipe JSONs
dir_with_recipes = 'recipes_original' # this is taken from minecraft.jar/data/crafting/recipes
dir_output = 'recipes_with_shulkerboxes'



if __name__ == '__main__':
    types = list()
    # debug logs
    successful_conversions = open('./logs/succesful.txt', 'w')
    output_too_high = open('./logs/too_high.txt', 'w')
    tag_recipes = open('./logs/tagged.txt', 'w')
    non_crafting_table = open('./logs/non_crafting_table.txt', 'w')
    non_64_stackables = open('./logs/non_64.txt', 'w')
    for recipe_file_name in os.listdir(dir_with_recipes): # iterate through files
        full_path = os.path.join(dir_with_recipes, recipe_file_name)


        # check validity
        if os.path.isfile(full_path): # this should be a recipe.json
            with open(full_path) as file_object:
                recipe = json.load(file_object)
                print(f'Loaded recipe {recipe_file_name}')

                try:
                    converted_recipe = recipe_converter(recipe).get_shulker_boxed_recipe()
                    print(f'Converted recipe {recipe_file_name} to shulkerboxed')
                    with open(dir_output + '/' + recipe_file_name, 'w') as outfile:
                        json.dump(converted_recipe, outfile, indent = 4)
                    print(f'Shulkerboxed {recipe_file_name} saved!')
                    successful_conversions.write(recipe_file_name + '\n')
                except TypeError as error:
                    # print(error + 'asdasdasdasd')
                    non_crafting_table.write(recipe_file_name + '\n')
                except ValueError as error:
                    print(f"{error} for recipe {recipe_file_name}")
                    output_too_high.write(recipe_file_name + '\n')
                except KeyError as error:
                    print(f"Recipe {recipe_file_name} failed - {error}")
                    tag_recipes.write(recipe_file_name + '\n')
                except MemoryError as error:
                    print(f"Recipe {recipe_file_name} failed - {error}")
                    non_64_stackables.write(recipe_file_name + '\n')
                except:
                    print('Uncaught error')
            pass
        
    successful_conversions.close()
    output_too_high.close()
    tag_recipes.close()
    non_crafting_table.close()
    # print(generate_filled_shulker_box("minecraft:diamond", "shulker_box"))
    pass