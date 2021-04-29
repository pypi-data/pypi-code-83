from wizzi_utils.open_cv import open_cv_tools as cvt
from wizzi_utils.misc import misc_tools as mt
import numpy as np
import cv2


def load_img_from_web() -> np.array:
    try:
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
    cvt.display_open_cv_image(
        img=img,
        ms=0,  # blocking
        title='stack overflow logo',
        x_y=(70, 0),  # start from x =70 y = 0
        resize_scale_percent=1.7  # enlarge to 170%
    )
    cv2.destroyAllWindows()
    return


def resize_opencv_image_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web()
    print(mt.to_str(img, '\timg'))
    img = cvt.resize_opencv_image(img, scale_percent=0.6)
    print(mt.to_str(img, '\timg re-sized to 60%'))
    return


def unpack_list_imgs_to_big_image_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web()
    gray = cvt.RGB_img_to_gray(img)
    big_img = cvt.unpack_list_imgs_to_big_image(
        imgs=[img, gray, img],
        resize=0,
        grid=(2, 2)
    )
    print('\tVisual test: stack overflow logo 2x2(1 empty)')
    cvt.display_open_cv_image(
        img=big_img,
        ms=0,  # blocking
        title='stack overflow logo',
        x_y=(0, 0),
        resize_scale_percent=0
    )
    cv2.destroyAllWindows()
    return


def display_open_cv_images_test():
    mt.get_function_name(ack=True, tabs=0)
    img = load_img_from_web()
    print('\tVisual test: stack overflow logo 2x1')
    cvt.display_open_cv_images(
        imgs=[img, img],
        ms=0,  # blocking
        title='stack overflow logo',
        x_y=(0, 0),
        resize_scale_percent=0,
        grid=(2, 1)
    )
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
    resize_opencv_image_test()
    unpack_list_imgs_to_big_image_test()
    display_open_cv_images_test()
    gray_to_RGB_and_back_test()
    print('{}'.format('-' * 20))
    return
