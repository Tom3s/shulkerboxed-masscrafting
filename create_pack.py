import os
import shutil

pack_name = 'Shulker Boxed Mass Crafting'

os.mkdir('./temp', mode=0o777)
os.mkdir('./temp/data', mode=0o777)
os.mkdir('./temp/data/crafting', mode=0o777)
os.mkdir('./temp/data/crafting/recipes', mode=0o777)
os.mkdir('./temp/data/grouping', mode=0o777)
os.mkdir('./temp/data/grouping/items', mode=0o777)

with open('./temp/pack.mcmeta', 'w') as meta:
    meta.write('{"pack":{"pack_format":10,"description":"Shulker Boxed Mass Crafting by u/Tom3s \\nNBT Crafting mod by u/Siphalor required!!"}}')

with open('./temp/data/grouping/items/shulkers.json', 'w') as shulkers:
    shulkers.write('{\n\t"values": [\n\t\t"minecraft:shulker_box",\n\t\t"minecraft:black_shulker_box",\n\t\t"minecraft:blue_shulker_box",\n\t\t"minecraft:brown_shulker_box",\n\t\t"minecraft:cyan_shulker_box",\n\t\t"minecraft:gray_shulker_box",\n\t\t"minecraft:green_shulker_box",\n\t\t"minecraft:light_blue_shulker_box",\n\t\t"minecraft:light_gray_shulker_box",\n\t\t"minecraft:lime_shulker_box",\n\t\t"minecraft:magenta_shulker_box",\n\t\t"minecraft:orange_shulker_box",\n\t\t"minecraft:pink_shulker_box",\n\t\t"minecraft:purple_shulker_box",\n\t\t"minecraft:red_shulker_box",\n\t\t"minecraft:white_shulker_box",\n\t\t"minecraft:yellow_shulker_box"\n\t]\n}')



src = './recipes_with_shulkerboxes'
dest = './temp/data/crafting/recipes'

for file_name in os.listdir(src):
    src_file = os.path.join(src, file_name)
    dest_file = os.path.join(dest, file_name)

    if os.path.isfile(src_file):
        shutil.copy(src_file, dest_file)

shutil.make_archive(pack_name, 'zip', './temp')

shutil.rmtree('./temp')
