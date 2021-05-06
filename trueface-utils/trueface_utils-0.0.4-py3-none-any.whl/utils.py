"""utility methods"""
import numpy as np
import cv2
import requests
import hashlib
import redis

class RedisQueue(object):
    """Simple Queue with Redis Backend"""
    def __init__(self, name, namespace='queue', **redis_kwargs):
       """The default connection parameters are: host='localhost', port=6379, db=0"""
       self.__db= redis.Redis(**redis_kwargs)
       self.key = '%s:%s' %(namespace, name)

    def qsize(self):
        """Return the approximate size of the queue."""
        return self.__db.llen(self.key)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.qsize() == 0

    def put(self, item):
        """Put item into the queue."""
        self.__db.rpush(self.key, item)

    def get(self, block=True, timeout=None):
        """Remove and return an item from the queue. 

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)
            return item
            
        if item:
            item = item[1]
        return item

    def get_nowait(self):
        """Equivalent to get(False)."""
        return self.get(False)

    def publish(self):
        pass

def md5(fname=None, string=None):
    hash_md5 = hashlib.md5()
    if fname:
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    elif string:
        hash_md5.update(string)
    return hash_md5.hexdigest()


def download_file(url):
        r = requests.get(url, stream=True)
        return r.content


def read_image(path):
        return cv2.imread(path)


def iou(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)

    # return the intersection over union value
    return iou


def rect_area(rect):
    return (rect[2] - rect[0]) * (rect[3] - rect[1])


def get_rect_overlap_area(rect_a, rect_b):
    x1_a, y1_a, x2_a, y2_a = rect_a
    x1_b, y1_b, x2_b, y2_b = rect_b

    overlap_width = min(x2_a, x2_b) - max(x1_a, x1_b)
    overlap_height = min(y2_a, y2_b) - max(y1_a, y1_b)

    if overlap_width > 0 and overlap_height > 0:
        return overlap_width * overlap_height
    else:
        return 0


def rect_overlap_ratio(rect_a, rect_b):
    if rect_area(rect_a) > rect_area(rect_b):
        rect_overlapping = rect_a
        rect_overlapped = rect_b
    else:
        rect_overlapping = rect_b
        rect_overlapped = rect_a
    overlap_area = get_rect_overlap_area(
        rect_overlapping, bbox_to_rect(rect_overlapped))
    return overlap_area / float(rect_area(rect_overlapping))


def iou_rect(box_a, box_b):
    overlap_area = get_rect_overlap_area(box_a, box_b)
    box_a_width = box_a[2] - box_a[0]
    box_a_height = box_a[3] - box_a[1]
    box_b_width = box_b[2] - box_b[0]
    box_b_height = box_b[3] - box_b[1]
    area_a = box_a_width * box_a_height
    area_b = box_b_width * box_b_height
    union_area = area_a + area_b - overlap_area

    if overlap_area > 0:
        return overlap_area / float(union_area)
    else:
        return 0


def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)


def adjust_brightness_and_contrast(image, alpha=1, beta=1):
    new_image = np.array([])
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y, x, c] = np.clip(
                    alpha * image[y, x, c] + beta, 0, 255)
    return new_image


def rect_center(rect):
    x1, y1, x2, y2 = rect
    return (x1 + x2) / 2.0, (y1 + y2) / 2.0


def bbox_center(bbox):
    x, y, w, h = bbox
    return int(x + (w / 2)), int(y + (h / 2))


def rect_to_bbox(rect):
    x_object = int(rect[0])
    y_object = int(rect[1])
    w_object = int(int(rect[2]) - int(rect[0]))
    h_object = int(int(rect[3]) - int(rect[1]))

    return x_object, y_object, w_object, h_object


def det_to_rect(det, frame):
    height = frame.shape[0]
    width = frame.shape[1]
    return [int(det[2] * width), int(det[3] * height),
            int(det[4] * width), int(det[5] * height)]


def bbox_to_rect(bbox):
    """
    Convert a bounding box to a rectangle

    Args:
        bbox: array with coordinates [top_left_x, top_left_y, width, height]

    Returns:
        rectangle: array with coordinates [top_left_x, top_left_y, bottom_right_x, bottom_right_y]
    """
    return [int(bbox[0]), int(bbox[1]), int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3])]


def cosine_probability(clf, cosine_similarity):
    x = cosine_similarity * clf.coef_ + clf.intercept_

    return 1 / (1 + np.exp(-x))


palette = (2 ** 11 - 1, 2 ** 15 - 1, 2 ** 20 - 1)
def compute_color_for_labels(label):
    """
    Simple function that adds fixed color depending on the class
    """
    color = [int((p * (label ** 2 - label + 1)) % 255) for p in palette]
    return tuple(color)


def draw_boxes(img, bbox, identities=None, offset=(0,0)):
    for i,box in enumerate(bbox):
        x1,y1,x2,y2 = [int(j) for j in box]
        x1 += offset[0]
        x2 += offset[0]
        y1 += offset[1]
        y2 += offset[1]
        # box text and bar
        id = int(identities[i]) if identities is not None else 0    
        color = compute_color_for_labels(id)
        label = '{}{:d}'.format("", id)
        t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_PLAIN, 2 , 2)[0]
        cv2.rectangle(img,(x1, y1),(x2,y2),color,3)
        cv2.rectangle(img,(x1, y1),(x1+t_size[0]+3,y1+t_size[1]+4), color,-1)
        cv2.putText(img,label,(x1,y1+t_size[1]+4), cv2.FONT_HERSHEY_PLAIN, 2, [255,255,255], 2)
    return img