from rmn import RMN
import cv2

m = RMN()

def show(img, name="disp", width=1000):
    """
    name: name of window, should be name of img
    img: source of img, should in type ndarray
    """
    cv2.namedWindow(name, cv2.WINDOW_GUI_NORMAL)
    cv2.resizeWindow(name, width, 1000)
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# image = cv2.imread("/home/luan/Pictures/anya/10515325_10201741975224801_4313838181617108580_o.jpg")
# image = cv2.imread("/home/luan/Downloads/132996309_516580649316233_116680661079249659_n.jpg")
# assert image is not None
# 
# results = m.detect_emotion_for_single_frame(image)
# 
# print(results)
# 
# image = m.draw(image, results)
# 
# show(image)
m.video_demo()
# if cv2.waitKey(1) == ord("q"):
#     cv2.destroyAllWindows()
