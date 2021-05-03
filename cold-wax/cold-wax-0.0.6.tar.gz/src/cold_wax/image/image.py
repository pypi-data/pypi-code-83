import cv2


def read_image(image_path, resize=None, normalise=False):
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if image is None:
        raise TypeError
    if image.size == 0:
        raise TypeError

    if image.shape[-1] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
    else:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

    if resize:
        image = cv2.resize(image, resize)
    if normalise and image[:, :, 0].mean() > 1:
        image /= 255
    return image


def show_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imshow('image', image)
    while cv2.waitKey(10) != ord('q'):
        pass


def show_images(images):
    for i, image in enumerate(images):
        cv2.imshow('image{}'.format(i), image)
    while cv2.waitKey(10) != ord('q'):
        pass
