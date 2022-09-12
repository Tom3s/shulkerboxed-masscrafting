all_shulker_box_types = [
'minecraft:shulker_box'
]
# ],
# 'minecraft:black_shulker_box',
# 'minecraft:blue_shulker_box',
# 'minecraft:brown_shulker_box',
# 'minecraft:cyan_shulker_box',
# 'minecraft:gray_shulker_box',
# 'minecraft:green_shulker_box',
# 'minecraft:light_blue_shulker_box',
# 'minecraft:light_gray_shulker_box',
# 'minecraft:lime_shulker_box',
# 'minecraft:magenta_shulker_box',
# 'minecraft:orange_shulker_box',
# 'minecraft:pink_shulker_box',
# 'minecraft:purple_shulker_box',
# 'minecraft:red_shulker_box',
# 'minecraft:white_shulker_box',
# 'minecraft:yellow_shulker_box'
# ]


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

def generate_all_shulker_box_variants(item: str, left_over: bool) -> dict:
    single_variant = dict()
    single_variant['tag'] = 'grouping:shulkers'
    single_variant['data'] = {
        'require': generate_filled_shulker_box_nbt(item)
    }
    if left_over:
        single_variant['remainder'] = {'item': 'minecraft:shulker_box' }
    
    return single_variant

def generate_result_shulker_box(item: str):
    return {
        'item': 'minecraft:shulker_box',
        'data': generate_filled_shulker_box_nbt(item)
    }

if __name__ == '__main__':
    pass