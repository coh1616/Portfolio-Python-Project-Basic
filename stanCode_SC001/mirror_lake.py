"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return blank_img: SimpleImage, The image flipped vertically
    """
    img = SimpleImage(filename)
    blank_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            # Colored
            img_p = img.get_pixel(x, y)

            # Blank1
            b1_p = blank_img.get_pixel(x, y)
            b1_p.red = img_p.red
            b1_p.green = img_p.green
            b1_p.blue = img_p.blue

            # Blank2
            b2_p = blank_img.get_pixel(x, blank_img.height-1-y)
            b2_p.red = img_p.red
            b2_p.green = img_p.green
            b2_p.blue = img_p.blue
    return blank_img


def main():
    """
    TODO: The function shows the original image and the one flipped vertically
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
