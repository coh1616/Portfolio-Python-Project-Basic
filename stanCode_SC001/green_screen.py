"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, The background image to replace green areas in figure_img
    :param figure_img: SimpleImage, The original image with green areas needs to be replaced
    :return figure_img: SimpleImage, The new figure image with background
    """
    for x in range(background_img.width):
        for y in range(background_img.height):
            figure_p = figure_img.get_pixel(x, y)
            bigger = max(figure_p.red, figure_p.blue)
            if figure_p.green > bigger*2:
                background_p = background_img.get_pixel(x, y)
                figure_p.red = background_p.red
                figure_p.green = background_p.green
                figure_p.blue = background_p.blue
    return figure_img


def main():
    """
    TODO: The function displays the image with background
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
