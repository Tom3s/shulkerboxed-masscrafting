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
        self.__stack_size = item_stack_sizes[item]
        pass

    def __generate_nbt_with_stack_count(self, stack_count: float):
        
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
            extra_item = generate_item_in_slot(floor(stack_count), decimal * self.__stack_size, self.__item)
            list_of_items.append(extra_item)

        shulker_box["BlockEntityTag"]["id"] = "minecraft:shulker_box"
        shulker_box["BlockEntityTag"]["Items"] = list_of_items

        return shulker_box

    def generate_ingredient_shulker_box(self, stack_count: float) -> dict:
        ingredient = dict()
        ingredient['tag'] = 'c:shulker_boxes'
        ingredient['data'] = {
            'require': self.__generate_nbt_with_stack_count(stack_count)
        }

        return ingredient

    def generate_result_shulker_box(self, stack_count: float) -> dict:
        result = dict()
        result['item'] = 'minecraft:shulker_box'
        result['data'] = self.__generate_nbt_with_stack_count(stack_count)

        return result
        

if __name__ == '__main__':
    pass