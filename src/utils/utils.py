"""File with utility functions and constants
    """


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


def print_image_and_result(self, img, result, threshold=1):
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
