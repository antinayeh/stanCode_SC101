"""
File: blur.py
Name: Antina
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the image you are trying to blur
    :return: the blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(0, img.width):
        for y in range(0, img.height):
            new_img.get_pixel(x, y).red = blur_helper(x, y, img, 0)
            new_img.get_pixel(x, y).green = blur_helper(x, y, img, 1)
            new_img.get_pixel(x, y).blue = blur_helper(x, y, img, 2)
    return new_img


def blur_helper(pixel_x, pixel_y, img, color):
    """
    :param pixel_x: x coordinate of the pixel being blurred
    :param pixel_y: y coordinate of the pixel being blurred
    :param img: the original image
    :param color: a number code that tells you what color rgb (red or green or blue) you are calculating
    :return: the new rgb of one color (red or green or blue) for the pixel
    """

    rgb = 0
    count = 0

    for x in range(pixel_x - 1, pixel_x + 2):
        for y in range(pixel_y - 1, pixel_y + 2):
            skip = False
            if x < 0 or x >= img.width or y < 0 or y >= img.height or (x == pixel_x and y == pixel_y):
                skip = True
            if not skip:
                count += 1
                if color == 0:
                    rgb += img.get_pixel(x, y).red
                elif color == 1:
                    rgb += img.get_pixel(x, y).green
                elif color == 2:
                    rgb += img.get_pixel(x, y).blue
    if count > 0:
        return rgb // count
    return rgb


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
