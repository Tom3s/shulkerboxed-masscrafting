from math import floor
from items import item_stack_sizes

def generate_item_in_slot(slot: int, count: int, id: str):
    return {
        "Slot": slot,
        "Count": count,
        "id": id
    }

class shulker_box_generator:
    def __init__(self, item: str) -> None:
        self.__item = item
        try:
            self.__stack_size = item_stack_sizes[item]
        except:
            self.__stack_size = 1
        pass

    def generate_nbt_with_stack_count(self, stack_count: float):
        
        if (stack_count > 27):
            raise ValueError(f"Error in method generate_shulker_box_nbt_with_items() ({__name__}): item count too high!")

        shulker_box = dict()

        shulker_box["BlockEntityTag"] = dict()
        
        list_of_items = list()

        for i in range(floor(stack_count)):
            item_object = generate_item_in_slot(i, self.__stack_size, self.__item)
            list_of_items.append(item_object)
        
        decimal = stack_count % 1
        if decimal != 0.0:
            extra_item = generate_item_in_slot(floor(stack_count), int(decimal * self.__stack_size), self.__item)
            list_of_items.append(extra_item)

        shulker_box["BlockEntityTag"]["id"] = "minecraft:shulker_box"
        shulker_box["BlockEntityTag"]["Items"] = list_of_items

        return shulker_box

    def generate_ingredient_shulker_box(self, stack_count: float, remainder: bool = False, remainder_stacks: float = 0.0, remainder_item: str = None) -> dict:
        ingredient = dict()
        ingredient['tag'] = 'c:shulker_boxes'
        ingredient['data'] = {
            'require': self.generate_nbt_with_stack_count(stack_count)
        }

        if remainder:
            ingredient['remainder'] = {}
            ingredient['remainder']['item'] = 'minecraft:shulker_box'
            if remainder_stacks != 0.0:
                ingredient['remainder']['data'] = shulker_box_generator(remainder_item).generate_nbt_with_stack_count(remainder_stacks)

        return ingredient

    def generate_ingredient_shulker_box_with_tag(self, stack_count: float, remainder: bool = False, remainder_stacks: float = 0.0, remainder_item: str = None):
        values = [
            "minecraft:oak_planks",
            "minecraft:spruce_planks",
            "minecraft:birch_planks",
            "minecraft:jungle_planks",
            "minecraft:acacia_planks",
            "minecraft:dark_oak_planks",
            "minecraft:crimson_planks",
            "minecraft:warped_planks",
            #"minecraft:mangrove_planks"
        ]

        variants = list()

        for plank in values:
            variants.append(shulker_box_generator(plank).generate_ingredient_shulker_box(stack_count, remainder, remainder_stacks, remainder_item))

        return variants


    def generate_result_shulker_box(self, stack_count: float) -> dict:
        result = dict()
        result['item'] = 'minecraft:shulker_box'
        result['data'] = self.generate_nbt_with_stack_count(stack_count)

        return result


if __name__ == '__main__':
    pass