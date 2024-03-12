from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.convert('L')
# crooked = filtered_img.rotate(180)
# resize = crooked.resize((300,300))
# resize.save("grey.png", "png")

# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save('grey.png', 'png')

img = Image.open('./astro.jpg')
# new_img = img.resize((200, 300))
img.thumbnail((300, 300))
img.save('thumbnail.jpg')
