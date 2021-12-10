"""File with utility functions
    """


def as_2d_arrays(img, w=28, h=28):
    """Takes one-dimensional array and returns it in two-dimensional array

    Args:
        img (any[]): One-dimensional array
        w (int, optional): Width. Defaults to 28
        h (int, optional): Height. Defaults to 28

    Returns:
        img (any[][]): Input array as w*h two-dimensional array
    """
    new_img = [[0 for j in range(w)] for i in range(h)]

    first_index = -1
    for i, value in enumerate(img):
        second_index = i % w
        if second_index == 0:
            first_index += 1
        new_img[first_index][second_index] = value
    return new_img


def images_with_threshold(images, threshold=1):
    """Takes one-dimensional images with grayscale values as input,
    returns the images as arrays of ones and zeroes.
    Threshold is the grayscale value.
    Greater numbers than threshold will be one, lower numbers will be zero.

    Args:
        images (list[int[]]): Images as one-dimensional array
        threshold (int, optional): Greyscale value

    Returns:
        list[int[]]: images as lists of ones and zeros
    """
    new_images = []
    for image in images:
        new_images.append(image_with_threshold(image, threshold))
    return new_images


def image_with_threshold(image, threshold=1):
    """Takes one-dimensional image with grayscale values as input,
    returns the image as array of ones and zeroes.
    Threshold is the grayscale value.
    Greater numbers than threshold will be one, lower numbers will be zero.

    Args:
        image (int[]): Image as one-dimensional array
        threshold (int, optional): Greyscale value

    Returns:
        int[]: image as lists of ones and zeros
    """
    new_image = []
    for pixel in image:
        value = 0
        if pixel >= threshold:
            value = 1
        new_image.append(value)
    return new_image


def image_as_2d_string(image):
    """Takes two-dimensional image and returns it as 28*28 string

    Args:
        image (int[][]): Image as two-dimensional array

    Returns:
        string: image as 28*28 string
    """
    retval = ""
    for i in range(len(image)):  # pylint: disable=consider-using-enumerate
        for j in range(len(image[0])):
            char = "○"
            if image[i][j] == 1:
                char = "●"
            retval += "{0:>2}".format(
                char)  # pylint: disable=consider-using-f-string
        retval += "\n"
    return retval
