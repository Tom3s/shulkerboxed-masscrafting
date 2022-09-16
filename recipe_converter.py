from shulker_box_generators import shulker_box_generator
from items import item_stack_sizes

class recipe_converter:
    allowed_crafting_types = ['minecraft:crafting_shaped', 'minecraft:crafting_shapeless']
    def __init__(self, recipe: object):
        self.__type = recipe['type']
        self.__group = recipe['group'] + '_shulker_boxed'

        try:
            self.__recipe_keys = recipe['key']
            self.__pattern = recipe['pattern']
        except:
            self.__recipe_keys = None
            self.__pattern = None
        
        try:
            self.__ingredients = recipe['ingredients']
        except:
            self.__ingredients = None

        self.__result = recipe['result']['item']
        try:
            self.__result_count = recipe['result']['count']
        except:
            self.__result_count = 1
        pass

    def __check_recipe_eligibility(self):
        if self.__type not in recipe_converter.allowed_crafting_types:
            raise TypeError('Invalid crafting type')
        if item_stack_sizes[self.__result] != 64:
            raise MemoryError('Non 64 stack output')
        
        if self.__result_count > 1:
            raise ValueError('Recipe output too high')

    def __get_empty_recipe(self):
        recipe = {
            'type': self.__type,
            'group': self.__group
        }
        return recipe
    
    def __get_shaped_crafting_recipe(self):
        recipe = self.__get_empty_recipe()
        recipe['pattern'] = self.__pattern
        keys = dict()
        for ingredient in self.__recipe_keys.keys():
            keys[ingredient] = shulker_box_generator(ingredient['item']).generate_ingredient_shulker_box(27)
        recipe['key'] = keys
        recipe['result'] = shulker_box_generator(self.__result).generate_result_shulker_box(27)
        return recipe

    def __get_shapeless_craftin_recipe(self):
        recipe = self.__get_empty_recipe()
        ingredients = list()
        for ing in self.__ingredients:
            ingredients.append(shulker_box_generator(ing['item']).generate_ingredient_shulker_box(27))
        recipe['ingredients'] = ingredients
        recipe['result'] = shulker_box_generator(self.__result).generate_result_shulker_box(27)
        return recipe

    def get_shulker_boxed_recipe(self):
        self.__check_recipe_eligibility()
        if self.__type == 'minecraft:crafting_shaped':
            return self.__get_shaped_crafting_recipe()
        elif self.__type == 'minecraft:crafting_shapeless':
            return self.__get_shapeless_craftin_recipe()
        pass


if __name__ == '__main__':
    pass