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
