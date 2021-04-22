"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

# Constants
THRESHOLD = 1.30     # Controls the threshold of detecting green screen pixel
BLACK_PIXEL = 120   # Controls the upper bound for black pixel


def main():
    """
    TODO: This function replaces green screen with the background
    Idea: There is an assignment this week and I haven't prepared for the final exam.
          Therefore, I combined me with The Scream from Edvard Munch to express my current state.
    """
    bg = SimpleImage('image_contest/image_1.jpg')
    fg = SimpleImage('image_contest/image_2.jpg')
    bg.make_as_big_as(fg)
    combine_img = combine(bg, fg).show()


def combine(back, me):
    """
    : param1 back: SimpleImage, the background image
    : param2 me: SimpleImage, green screen figure image
    : return me: SimpleImage, me image with the green screen pixels replaced by pixels of back
    """
    for x in range(back.width):
        for y in range(back.height):
            fg_p = me.get_pixel(x, y)
            avg = (fg_p.red + fg_p.green + fg_p.blue)//3
            total = fg_p.red + fg_p.green + fg_p.blue
            if fg_p.green > avg*THRESHOLD and total > BLACK_PIXEL:
                bg_p = back.get_pixel(x, y)
                fg_p.red = bg_p.red
                fg_p.green = bg_p.green
                fg_p.blue = bg_p.blue
    return me


if __name__ == '__main__':
    main()
