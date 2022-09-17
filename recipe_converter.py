from xml.dom import minicompat
from shulker_box_generators import shulker_box_generator
from items import item_stack_sizes

class recipe_converter:
    allowed_crafting_types = ['minecraft:crafting_shaped', 'minecraft:crafting_shapeless']
    def __init__(self, recipe: object):
        self.__type = recipe['type']
        # self.__check_recipe_eligibility()
        try:
            self.__group = recipe['group'] + '_shulker_boxed'
        except:
            self.__group = None
        try:
            self.__recipe_keys: dict = recipe['key']
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
        if self.__group != None:
            return {
                'type': self.__type,
                'group': self.__group
            }
        else:
            return {
                'type': self.__type
            }
    
    def __get_shaped_crafting_recipe(self):
        recipe = self.__get_empty_recipe()

        count_dict = dict()
        for row in self.__pattern:
            for letter in row:
                if letter == ' ':
                    continue
                if letter not in count_dict.keys():
                    count_dict[letter] = 1
                else:
                    count_dict[letter] += 1
        minimum_key = min(count_dict, key=count_dict.get)

        keys = dict()
        for ingredient in self.__recipe_keys.keys():
            try:
                keys[ingredient] = shulker_box_generator(self.__recipe_keys[ingredient]['item']).generate_ingredient_shulker_box(27, ingredient != minimum_key)
            except:
                if self.__recipe_keys[ingredient]['tag'] == 'minecraft:planks':
                    keys[ingredient] = shulker_box_generator(self.__recipe_keys[ingredient]['tag']).generate_ingredient_shulker_box_with_tag(27, ingredient != minimum_key)
        recipe['key'] = keys

        recipe['pattern'] = self.__pattern
        recipe['result'] = shulker_box_generator(self.__result).generate_result_shulker_box(27)
        return recipe

    def __get_shapeless_craftin_recipe(self):
        recipe = self.__get_empty_recipe()

        count_dict = dict()
        for ingredient in self.__ingredients:
            item_id = ingredient['item']
            if item_id not in count_dict.keys():
                count_dict[item_id] = 1
            else:
                count_dict[item_id] += 1
        
        minimum_item_id = min(count_dict, key = count_dict.get)

        ingredients = list()
        for ing in self.__ingredients:
            ingredients.append(shulker_box_generator(ing['item']).generate_ingredient_shulker_box(27, ing['item'] != minimum_item_id))
        recipe['ingredients'] = ingredients
        recipe['result'] = shulker_box_generator(self.__result).generate_result_shulker_box(27)
        return recipe

    def __get_honey_block_recipe(self):
        recipe = self.__get_empty_recipe()
        recipe['key'] = {
            'S': shulker_box_generator('minecraft:honey_bottle').generate_ingredient_shulker_box(27, True, 6.75, 'minecraft:glass_bottle')
        }

        recipe['pattern'] = self.__pattern
        recipe['result'] = shulker_box_generator('minecraft:honey_block').generate_result_shulker_box(6.75)

        return recipe
        

    def get_shulker_boxed_recipe(self):
        if self.__result == 'minecraft:piston':
            asd = 'kutya'
            if asd:
                pass
            pass

        if self.__result == 'minecraft:honey_block':
            return self.__get_honey_block_recipe()
        self.__check_recipe_eligibility()
        if self.__type == 'minecraft:crafting_shaped':
            return self.__get_shaped_crafting_recipe()
        elif self.__type == 'minecraft:crafting_shapeless':
            return self.__get_shapeless_craftin_recipe()
        pass


if __name__ == '__main__':
    pass