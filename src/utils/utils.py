"""File with utility functions
    """


def as_2d_arrays(img):
    w, h = 28, 28
    new_img = [[0 for x in range(w)] for y in range(h)]

    first_index = -1
    for i, value in enumerate(img):
        second_index = i % 28
        if second_index == 0:
            first_index += 1
        new_img[first_index][second_index] = value
    return new_img


def images_with_threshold(images, threshold=1):
    new_images = []
    for image in images:
        new_image = []
        for pixel in image:
            value = 0
            if pixel >= threshold:
                value = 1
            new_image.append(value)
        new_images.append(new_image)
    return new_images


def print_2d_array(array):
    for row in array:
        for val in row:
            if val == 0:
                print('  ', end="")
            else:
                print('@ ', end="")
        print("")


def print_image_and_result(img, result, threshold=1):
    """Prints image and result

    Args:
        img (int[]): image data
        result (int): class of the image
        threshold (int, optional): Grayscale pixel values equal or greater than threshold
        will be printed. Defaults to 1.
    """
    for i, value in enumerate(img):
        # to_print = f"{value} "
        to_print = "  "
        if value >= threshold:
            to_print = "@ "
        if (i+1) % 28 == 0:
            print(to_print, end="\n")
        else:
            print(to_print, end="")
    print("IS: ", result)
