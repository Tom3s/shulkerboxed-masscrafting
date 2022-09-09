import os
import shutil

pack_name = 'Shulker Boxed Mass Crafting'

os.mkdir('./temp', mode=0o777)
os.mkdir('./temp/data', mode=0o777)
os.mkdir('./temp/data/crafting', mode=0o777)
os.mkdir('./temp/data/crafting/recipes', mode=0o777)

with open('./temp/pack.mcmeta', 'w') as meta:
    meta.write('{"pack":{"pack_format":10,"description":"\u00A75\u00A7l\u00A7oShulker Boxed Mass Crafting\u00A7r by \u00A7bu/Tom3s\u00A7r \\n\u00A7c\u00A7lNBT Crafting\u00A7r mod by \u00A7bu/Siphalor \u00A7rrequired!!"}}')


src = './recipes_with_shulkerboxes'
dest = './temp/data/crafting/recipes'

for file_name in os.listdir(src):
    src_file = os.path.join(src, file_name)
    dest_file = os.path.join(dest, file_name)

    if os.path.isfile(src_file):
        shutil.copy(src_file, dest_file)

shutil.make_archive(pack_name, 'zip', './temp')

shutil.rmtree('./temp')
