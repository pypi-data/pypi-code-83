from wizzi_utils.open_cv import open_cv_tools as cvt
from wizzi_utils.misc import misc_tools as mt
import numpy as np
# noinspection PyPackageRequirements
import cv2


def load_img_from_web() -> np.array:
    try:
        # noinspection PyCompatibility
        from urllib.request import urlopen
        img_url = 'https://cdn.sstatic.net/Sites/stackoverflow/img/logo.png'
        resp = urlopen(img_url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    except (ModuleNotFoundError, ImportError) as e:
        mt.exception_error(e)
        image = mt.np_random_integers(size=(240, 320, 3), low=0, high=255)
        image = image.astype('uint8')
    return image


def get_cv_version_test():
    mt.get_function_name(ack=True, tabs=0)
    print('\t{}'.format(cvt.get_cv_version()))
    return


def imread_imwrite_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web()
    path = './temp.png'
    cvt.save_img(path, img, ack=True)
    img_loaded = cvt.load_img(path, ack=True)
    print(mt.to_str(img_loaded, '\timg'))
    mt.delete_file(path, ack=True)
    return


def list_to_cv_image_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web()
    img_list = img.tolist()
    print(mt.to_str(img_list, '\timg_list'))
    img = cvt.list_to_cv_image(img_list)
    print(mt.to_str(img, '\timg'))
    return


def display_open_cv_image_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web()
    print('\tVisual test: stack overflow logo')
    loc = (70, 200)  # move to X,Y
    resize = 1.7  # enlarge to 170%
    cvt.display_open_cv_image(
        img=img,
        ms=1,  # not blocking
        title='stack overflow logo moved to {} and re-sized to {}'.format(loc, resize),
        loc=loc,  # start from x =70 y = 0
        resize_scale_percent=resize
    )
    loc = 'top_right'  # move to top right corner
    resize = 1.7  # enlarge to 170%
    cvt.display_open_cv_image(
        img=img,
        ms=0,  # blocking
        title='stack overflow logo moved to {} and re-sized to {}'.format(loc, resize),
        loc=loc,  # start from x =70 y = 0
        resize_scale_percent=resize
    )
    cv2.destroyAllWindows()
    return


def display_open_cv_image_loop_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web()
    loc = (70, 200)  # move to X,Y
    resize = 1.7  # enlarge to 170%
    title = 'stack overflow logo moved to {} and re-sized to {} - 100 iterations'.format(loc, resize)
    print('\tVisual test: {}'.format(title))
    for i in range(100):
        cvt.display_open_cv_image(
            img=img,
            ms=1,  # not blocking
            title=title,
            loc=loc,  # start from x =70 y = 0
            resize_scale_percent=resize
        )
        if i == 0:  # move just first iter
            loc = None
    cv2.destroyAllWindows()
    return


def resize_opencv_image_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web()
    print(mt.to_str(img, '\timg'))
    img = cvt.resize_opencv_image(img, scale_percent=0.6)
    print(mt.to_str(img, '\timg re-sized to 60%'))
    return


def move_cv_img_x_y_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web()
    options = [(0, 0), (100, 0), (0, 100), (150, 150), (400, 400), (250, 350)]
    print('\tVisual test: move to all options {}'.format(options))
    print('\t\tClick Esc to close all')
    for x_y in options:
        title = 'move to ({})'.format(x_y)
        cv2.imshow(title, img)
        cvt.move_cv_img_x_y(title, x_y)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


def move_cv_img_by_str_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web()
    options = ['top_right', 'top_center', 'top_left', 'bottom_right', 'bottom_center', 'bottom_left']
    print('\tVisual test: move to all options {}'.format(options))
    print('\t\tClick Esc to close all')
    for where_to in options:
        title = 'move to {}'.format(where_to)
        cv2.imshow(title, img)
        cvt.move_cv_img_by_str(img, title, where=where_to)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


def unpack_list_imgs_to_big_image_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web()
    gray = cvt.RGB_img_to_gray(img)
    big_img = cvt.unpack_list_imgs_to_big_image(
        imgs=[img, gray, img],
        resize=None,
        grid=(2, 2)
    )
    title = 'stack overflow logo 2x2(1 empty)'
    print('\tVisual test: {}'.format(title))
    cvt.display_open_cv_image(
        img=big_img,
        ms=0,  # blocking
        title=title,
        loc=(0, 0),
        resize_scale_percent=None
    )
    cv2.destroyAllWindows()
    return


def display_open_cv_images_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web()
    title = '2x1 grid'
    print('\tVisual test: {}'.format(title))
    loc1 = (0, 0)
    cvt.display_open_cv_images(
        imgs=[img, img],
        ms=1,  # blocking
        title='{} loc={}'.format(title, loc1),
        loc=loc1,
        resize_scale_percent=None,
        grid=(2, 1)
    )
    loc2 = 'bottom_center'
    cvt.display_open_cv_images(
        imgs=[img, img],
        ms=0,  # blocking
        title='{} loc={}'.format(title, loc2),
        loc=loc2,
        resize_scale_percent=None,
        grid=(2, 1)
    )
    cv2.destroyAllWindows()
    return


def display_open_cv_images_loop_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web()
    loc = (70, 200)  # move to X,Y
    title = 'stack overflow logo moved to {} - 100 iterations'.format(loc)
    print('\tVisual test: {}'.format(title))
    for i in range(100):
        cvt.display_open_cv_images(
            imgs=[img, img],
            ms=1,  # blocking
            title=title,
            loc=loc,
            resize_scale_percent=None,
            grid=(2, 1)
        )
        if i == 0:  # move just first iter
            loc = None
    cv2.destroyAllWindows()
    return


def gray_to_RGB_and_back_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web()
    print(mt.to_str(img, '\timgRGB'))
    gray = cvt.RGB_img_to_gray(img)
    print(mt.to_str(img, '\timg_gray'))
    img = cvt.gray_scale_img_to_RGB_form(gray)
    print(mt.to_str(img, '\timgRGB'))
    return


def test_all():
    print('{}{}:'.format('-' * 5, mt.get_base_file_and_function_name()))
    get_cv_version_test()
    imread_imwrite_test()
    list_to_cv_image_test()
    display_open_cv_image_test()
    display_open_cv_image_loop_test()
    resize_opencv_image_test()
    move_cv_img_x_y_test()
    move_cv_img_by_str_test()
    unpack_list_imgs_to_big_image_test()
    display_open_cv_images_test()
    display_open_cv_images_loop_test()
    gray_to_RGB_and_back_test()
    print('{}'.format('-' * 20))
    return
