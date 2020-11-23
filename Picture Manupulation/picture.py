from PIL import Image, ImageEnhance, ImageFilter


def resize_images(image_names, new_size=(300, 300)):
    for image_name in image_names:
        img = Image.open(image_name)
        img = img.resize(new_size)
        img.save("resized_" + image_name)


'''
images =['spider.jpg', 'black.jpg', 'deadpool.jpg']
resize_images(images)

spider_img=Image.open('spider.jpg')
spider_img.show()
spider_img =spider_img.crop((100,100,400,400))
spider_img.show()
'''
"""
deadpool_img=Image.open('deadpool.jpg')
deadpool_img.show()

grey_scale=deadpool_img.convert('L')
grey_scale.show()

edge_detect = deadpool_img.filter(ImageFilter.FIND_EDGES)
edge_detect.show()

contrast=ImageEnhance.Contrast(deadpool_img).enhance(1.3)
contrast.show()

bright=ImageEnhance.Brightness(contrast).enhance(2)
bright.show()
"""

black_img = Image.open('black.jpg')
black_img.show()
width, height = black_img.size

for x in range(width):
    for y in range(height):
        pixel_coordinate = (x, y)
        r, g, b = black_img.getpixel(pixel_coordinate)
        neg_color = (255 - r, 255 - g, 255 - b)
        black_img.putpixel(pixel_coordinate, neg_color)

black_img.show()
