import numpy as np
import cv2
import random

from calculation.pixel import Pixel

class PostProcessor:

    @staticmethod
    def image_coloring(image: np.ndarray, rgb_mask: list) -> np.ndarray:
        """

        :param image: it have processed image
        :param rgb_mask: predicted mask array
        :return:
        """
        for i in range(len(rgb_mask[0])):
            image[rgb_mask[1][i], rgb_mask[0][i], 0] = 5  # y and x coordinates coloring
            image[rgb_mask[1][i], rgb_mask[0][i], 2] = 200  # y and x coordinates coloring

        return image

    @staticmethod
    def vis_bbox(image: np.ndarray, bbox: list, **kwargs) -> np.ndarray:

        """
            Draw bbox,info box on image
        :param image: images to be processed
        :param bbox: [xmin, ymin, xmax, ymax]
        :param kwargs: classname,box,args (string) :custom box for value
        :return: box drawn image
        """

        overlay = image.copy()
        alpha = 0.4  # Transparency factor.
        pixel = 0
        pixel_height = 17
        header_list = []
        header_pix_x = 4
        header_pix_y = 13
        for key, value in kwargs.items():
            text = str(key).capitalize() + ' : ' + str(value)
            x = bbox[0]
            x2 = bbox[2]
            if key == 'classname':
                y, y2 = bbox[1], bbox[1] - 30
                color = (0, 0, 200)
                header_value = (text, (x + header_pix_x, y - header_pix_y))
                header_list.append((text, (x + header_pix_x, y - header_pix_y)))
            elif key == 'box':
                if value:
                    y, y2 = bbox[1], bbox[3]
                    color = (250, 100, 0)
                else:
                    continue
            else:
                y, y2 = bbox[3] + pixel, bbox[3] + pixel_height
                color = (0, 200, 0)
                header_value = (text, (x + header_pix_x, y + header_pix_y + pixel))
                pixel += 8

            header_list.append(header_value)
            cv2.rectangle(overlay, (x, y), (x2, y2), color, -1)
            image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
            pixel_height += 11

        for i in range(len(header_list)):
            cv2.putText(image_new, header_list[i][0], header_list[i][1], cv2.FONT_HERSHEY_DUPLEX, 0.4, (0, 0, 0), 1)

        return image_new

    @staticmethod
    def get_coloured_mask(mask: list) -> list:
        """
        random_colour_masks
          parameters:
            - image - predicted masks
          method:
            - the masks of each predicted object is given random colour for visualization
        """
        colours = [[0, 255, 0], [0, 0, 255], [255, 0, 0], [0, 255, 255], [255, 255, 0], [255, 0, 255], [80, 70, 180],
                   [250, 80, 190], [245, 145, 50], [70, 150, 250], [50, 190, 190]]
        r = np.zeros_like(mask).astype(np.uint8)
        g = np.zeros_like(mask).astype(np.uint8)
        b = np.zeros_like(mask).astype(np.uint8)
        r[mask == 1], g[mask == 1], b[mask == 1] = colours[random.randrange(0, 10)]
        coloured_mask = np.stack([r, g, b], axis=2)
        return coloured_mask

    def get_mask_polygon_to_rectangle(mask: list) -> list:
        """

        :return:
        """
        maskx = np.any(mask, axis=0)
        masky = np.any(mask, axis=1)
        xmin = np.argmax(maskx)
        ymin = np.argmax(masky)
        xmax = len(maskx) - np.argmax(maskx[::-1])
        ymax = len(masky) - np.argmax(masky[::-1])

        return xmin, ymin, xmax, ymax

    @staticmethod
    def get_segmentation(mask: list, x0: int, y0: int, horizon: int, image: np.ndarray) -> np.ndarray:
        """

        :param mask:
        :param x0:
        :param y0:
        :param horizon:
        :param image:
        :return:
        """
        maskRaw = mask[0]
        mask_ = maskRaw.mul(255).byte().cpu().numpy()
        contours, _ = cv2.findContours(
            mask_.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        if contours:
            contour = np.flip(contours[0], axis=1)
            contour = contour.ravel().tolist()
            segmentation = Pixel.calc_origin(y0, x0, contour, 1, 1, horizon)
            cv2.drawContours(image, segmentation, -1, (255, 0, 0), 2, cv2.LINE_AA)

        else:
            segmentation = None

        return segmentation

    @staticmethod
    def get_histogram_matcher(detect_1: np.ndarray, detect_2: np.ndarray) -> float:
        # The histogram size refers to the number of bins in the histogram.
        h_bins = 50
        s_bins = 60
        histSize = [h_bins, s_bins]
        # hue varies from 0 to 179, saturation from 0 to 255
        h_ranges = [0, 180]
        s_ranges = [0, 256]
        ranges = h_ranges + s_ranges  # concat lists
        # Use the 0-th and 1-st channels
        channels = [0, 1]

        # Calculate the Hist for each images
        # Calculate the histogram and normalize it
        hist_img1 = cv2.calcHist([detect_1], channels, None, histSize, ranges, accumulate=False)
        cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        hist_img2 = cv2.calcHist([detect_2], channels, None, histSize, ranges, accumulate=False)
        cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

        # find the metric value
        metric_val = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_BHATTACHARYYA)
        del hist_img1, hist_img2

        return metric_val
