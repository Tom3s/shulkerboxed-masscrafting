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