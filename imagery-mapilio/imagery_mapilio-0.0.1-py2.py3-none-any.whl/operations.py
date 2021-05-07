import os
import numpy as np
import cv2

from helper.generator import Generator
from imagery.postprocessor import PostProcessor

class Operation:

    @staticmethod
    def image_write(outPath: str, path: str, image: np.ndarray):
        cv2.imwrite(os.path.join(outPath, os.path.basename(path)), image, [cv2.IMWRITE_JPEG_QUALITY, 80])

    @staticmethod
    def image_action(image: np.ndarray, finalBox: list, class_name: str, writePaths: str,
                     rgb_mask: list, copyImage: np.ndarray, config: dict):
        """

        :param image:
        :param finalBox: detected object bounding box
        :param class_name: detected objects category name
        :param writePaths: where will it write
        :param rgb_mask:
        :param copyImage:
        :param config:
        :return: write local directory and detected objects as a array
        """
        xmin, ymin, xmax, ymax = [int(item) for item in finalBox]

        detectedObject = copyImage[ymin:ymax, xmin:xmax]
        imageNumber = os.path.basename(writePaths[1]).split(".")[0]
        imageSaveType = os.path.basename(writePaths[1]).split(".")[1]
        # saveName = imageNumber + "_{}.".format(writePaths[2]) + imagesaveType
        saveName = imageNumber + "_{}.".format(Generator.unique_matchId_generator()) + imageSaveType
        detectedObjectPath = os.path.join("Exports", "ObjectsImage", saveName)
        cv2.imwrite(detectedObjectPath, detectedObject)

        if config.processedimageWrite:
            cX = int((xmin + xmax) / 2)
            cY = int((ymin + ymax) / 2)

            cv2.putText(image, class_name, (cX, cY),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            if rgb_mask:
                image = np.array(image)
                image = PostProcessor.image_coloring(image, rgb_mask)

        del copyImage

        return detectedObjectPath, image

    @staticmethod
    def image_read_rgb_as_hsv(detectedObjectPath: str) -> np.ndarray:
        return cv2.imread(detectedObjectPath, cv2.COLOR_RGB2HSV)