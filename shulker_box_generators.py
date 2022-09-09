all_shulker_box_types = [
'shulker_box',
'black_shulker_box',
'blue_shulker_box',
'brown_shulker_box',
'cyan_shulker_box',
'gray_shulker_box',
'green_shulker_box',
'light_blue_shulker_box',
'light_gray_shulker_box',
'lime_shulker_box',
'magenta_shulker_box',
'orange_shulker_box',
'pink_shulker_box',
'purple_shulker_box',
'red_shulker_box',
'white_shulker_box',
'yellow_shulker_box'
]


def generate_filled_shulker_box_nbt(item: str) -> object:
    filled_box = dict()

    filled_box["BlockEntityTag"] = dict()
    
    list_of_items = list()

    for i in range(27):
        item_object = {
            "Slot": i,
            "Count": 64,
            "id": item
        }
        list_of_items.append(item_object)
    
    filled_box["BlockEntityTag"]["id"] = "minecraft:shulker_box"
    filled_box["BlockEntityTag"]["Items"] = list_of_items

    return filled_box

def generate_all_shulker_box_variants(item: str, left_over: bool) -> list:
    list_of_variants = list()
    for box in all_shulker_box_types:
        single_variant = dict()
        single_variant['item'] = box
        single_variant['data'] = {
            'require': generate_filled_shulker_box_nbt(item)
        }
        if left_over:
            single_variant['remainder'] = {'item': box }
        list_of_variants.append(single_variant)
    
    return list_of_variants

def generate_result_shulker_box(item: str):
    return {
        'item': 'minecraft:shulker_box',
        'data': generate_filled_shulker_box_nbt(item)
    }

if __name__ == '__main__':
    pass