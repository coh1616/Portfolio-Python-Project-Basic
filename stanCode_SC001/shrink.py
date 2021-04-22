"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image
    :return blank_img: SimpleImage, the compressed one half the width and height of the original
    """
    img = SimpleImage(filename)
    blank_img = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(img.width):
        for y in range(img.height):
            img_p = img.get_pixel(x, y)
            b_p = blank_img.get_pixel(x//2, y//2)
            b_p.red = img_p.red
            b_p.green = img_p.green
            b_p.blue = img_p.blue
    return blank_img


def main():
    """
    TODO: The function displays the original image and the one half the width and height of the original
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
