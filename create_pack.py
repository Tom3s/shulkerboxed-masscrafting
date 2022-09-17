import os
import shutil

pack_name = 'Shulker.Boxed.Mass.Crafting'
version = 'v1.2'

os.mkdir('./temp', mode=0o777)
os.mkdir('./temp/data', mode=0o777)
os.mkdir('./temp/data/crafting', mode=0o777)
os.mkdir('./temp/data/crafting/recipes', mode=0o777)

with open('./temp/pack.mcmeta', 'w') as meta:
    meta.write('{"pack":{"pack_format":10,"description":"Shulker Boxed Mass Crafting by u/Tom3s \\nNBT Crafting mod by u/Siphalor required!!"}}')



src = './recipes_with_shulkerboxes'
dest = './temp/data/crafting/recipes'

for file_name in os.listdir(src):
    src_file = os.path.join(src, file_name)
    dest_file = os.path.join(dest, file_name)

    if os.path.isfile(src_file):
        shutil.copy(src_file, dest_file)

#shutil.copy('./piston.json', dest + '/piston.json')

shutil.make_archive(f'{pack_name}-{version}', 'zip', './temp')

shutil.rmtree('./temp')
