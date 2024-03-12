import sys
import os
from PIL import Image

# grab the first and second argument

# check if new folder exists, if not create it

# loop through Pokedex,
# convert images to png
# save to the new folder

oldFolder = sys.argv[1]
newFolder = sys.argv[2]

if not os.path.exists(newFolder):
    os.makedirs(newFolder)

for filename in os.listdir(oldFolder):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{oldFolder}{filename}')
    # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
    img.save(f'{newFolder}/{clean_name}.png', 'png')
    print('all done!!')
