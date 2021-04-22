"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


# # Method 1

# def blur(img):
#     """
#     :param img: SimpleImage, the original image
#     :return new_img: SimpleImage, the blurred image
#     """
#     new_img = SimpleImage.blank(img.width, img.height)
#     for x in range(img.width):
#         for y in range(img.height):
#             img_p = img.get_pixel(x, y)
#             new_img_p = new_img.get_pixel(x, y)
#             if x > 0 and y > 0:
#                 point_1 = img.get_pixel(x - 1, y - 1)
#             if y > 0:
#                 point_2 = img.get_pixel(x, y - 1)
#             if x < img.width - 1 and y > 0:
#                 point_3 = img.get_pixel(x + 1, y - 1)
#             if x > 0:
#                 point_4 = img.get_pixel(x - 1, y)
#             if x < img.width - 1:
#                 point_6 = img.get_pixel(x + 1, y)
#             if x > 0 and y < img.height - 1:
#                 point_7 = img.get_pixel(x - 1, y + 1)
#             if y < img.height - 1:
#                 point_8 = img.get_pixel(x, y + 1)
#             if x < img.width - 1 and y < img.height - 1:
#                 point_9 = img.get_pixel(x + 1, y + 1)
#             if x == 0 and y == 0:
#                 new_img_p.red = (img_p.red + point_6.red + point_8.red + point_9.red) / 4
#                 new_img_p.green = (img_p.green + point_6.green + point_8.green + point_9.green) / 4
#                 new_img_p.blue = (img_p.blue + point_6.blue + point_8.blue + point_9.blue) / 4
#             elif x == 0 and y == img.height - 1:
#                 new_img_p.red = (point_2.red + point_3.red + img_p.red + point_6.red) / 4
#                 new_img_p.green = (point_2.green + point_3.green + img_p.green + point_6.green) / 4
#                 new_img_p.blue = (point_2.blue + point_3.blue + img_p.blue + point_6.blue) / 4
#             elif x == img.width - 1 and y == 0:
#                 new_img_p.red = (point_4.red + img_p.red + point_7.red + point_8.red) / 4
#                 new_img_p.green = (point_4.green + img_p.green + point_7.green + point_8.green) / 4
#                 new_img_p.blue = (point_4.blue + img_p.blue + point_7.blue + point_8.blue) / 4
#             elif x == img.width - 1 and y == img.height - 1:
#                 new_img_p.red = (point_1.red + point_2.red + point_4.red + img_p.red) / 4
#                 new_img_p.green = (point_1.green + point_2.green + point_4.green + img_p.green) / 4
#                 new_img_p.blue = (point_1.blue + point_2.blue + point_4.blue + img_p.blue) / 4
#             elif x == 0 and (y != 0 or y != img.height - 1):
#                 new_img_p.red = (point_2.red + point_3.red + img_p.red + point_6.red + point_8.red + point_9.red) / 6
#                 new_img_p.green = (
#                                               point_2.green + point_3.green + img_p.green + point_6.green + point_8.green + point_9.green) / 6
#                 new_img_p.blue = (
#                                              point_2.blue + point_3.blue + img_p.blue + point_6.blue + point_8.blue + point_9.blue) / 6
#             elif x == img.width - 1 and (y != 0 or y != img.height - 1):
#                 new_img_p.red = (point_1.red + point_2.red + point_4.red + img_p.red + point_7.red + point_8.red) / 6
#                 new_img_p.green = (
#                                               point_1.green + point_2.green + point_4.green + img_p.green + point_7.green + point_8.green) / 6
#                 new_img_p.blue = (
#                                              point_1.blue + point_2.blue + point_4.blue + img_p.blue + point_7.blue + point_8.blue) / 6
#             elif y == 0 and (x != 0 or x != img.width - 1):
#                 new_img_p.red = (point_4.red + img_p.red + point_6.red + point_7.red + point_8.red + point_9.red) / 6
#                 new_img_p.green = (
#                                               point_4.green + img_p.green + point_6.green + point_7.green + point_8.green + point_9.green) / 6
#                 new_img_p.blue = (
#                                              point_4.blue + img_p.blue + point_6.blue + point_7.blue + point_8.blue + point_9.blue) / 6
#             elif y == img.height - 1 and (x != 0 or x != img.width - 1):
#                 new_img_p.red = (point_1.red + point_2.red + point_3.red + point_4.red + img_p.red + point_6.red) / 6
#                 new_img_p.green = (
#                                               point_1.green + point_2.green + point_3.green + point_4.green + img_p.green + point_6.green) / 6
#                 new_img_p.blue = (
#                                              point_1.blue + point_2.blue + point_3.blue + point_4.blue + img_p.blue + point_6.blue) / 6
#             else:
#                 new_img_p.red = (
#                                             point_1.red + point_2.red + point_3.red + point_4.red + img_p.red + point_6.red + point_7.red + point_8.red + point_9.red) / 9
#                 new_img_p.green = (
#                                               point_1.green + point_2.green + point_3.green + point_4.green + img_p.green + point_6.green + point_7.green + point_8.green + point_9.green) / 9
#                 new_img_p.blue = (
#                                              point_1.blue + point_2.blue + point_3.blue + point_4.blue + img_p.blue + point_6.blue + point_7.blue + point_8.blue + point_9.blue) / 9
#     return new_img
#
#
# def main():
#     """
#     TODO: This function shows the original image and blurred one
#     """
#     old_img = SimpleImage("images/smiley-face.png")
#     old_img.show()
#
#     blurred_img = blur(old_img)
#     for i in range(4):
#         blurred_img = blur(blurred_img)
#     blurred_img.show()

# Method 2

def blurred(filename):
    old_img = SimpleImage(filename)
    new_img = SimpleImage.blank(old_img.width, old_img.height)
    for x in range(old_img.width):
        for y in range(old_img.height):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            # find the neighbors
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x+i
                    pixel_y = y+j
                    if 0 <= pixel_x < old_img.width:
                        if 0 <= pixel_y < old_img.height:
                            old_img_p = old_img.get_pixel(pixel_x, pixel_y)
                            r_sum += old_img_p.red
                            g_sum += old_img_p.green
                            b_sum += old_img_p.blue
                            count += 1
            new_img_p = new_img.get_pixel(x, y)
            new_img_p.red = r_sum / count
            new_img_p.blue = b_sum / count
            new_img_p.green = g_sum / count
    return new_img


def main():
    filename = 'images/smiley-face.png'
    blurred_img = blurred(filename)
    for i in range(4):
        blurred_img = blurred(filename)
    blurred_img.show()


if __name__ == '__main__':
    main()
