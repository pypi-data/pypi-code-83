import os
import random

import imagesize
import numpy as np
import pandas as pd
from PIL import Image
from tiatoolbox.dataloader import wsireader

from ..helper import helper


class Reader:
    """
    Parent class for all readers. Subclasses need to implement their call method.
    """

    def __init__(self):
        pass

    def __call__(self, row, path_to_image):
        raise NotImplementedError


class ReadTestImageV2(Reader):
    """
    TODO
    """

    def __init__(
        self,
        image_size: int = 100,
        to_hash_added: int = 0,
        num_of_circles: int = 10,
        return_mask: bool = False,
        return_coordinats: bool = False,
        return_bbox: bool = False,
    ):
        """
        TODO

        Arguments:
            image_size: TODO
            to_hash_added: TODO
            num_of_circles: TODO
            return_mask: TODO
            return_coordinats: TODO
            return_bbox: TODO
        """

        super().__init__()
        self.img_size = image_size
        self.to_hash_added = to_hash_added
        self.return_mask = return_mask
        self.return_coordinats = return_coordinats
        self.return_bbox = return_bbox
        self.num_of_circles = num_of_circles

    def create_test_image(self, row: int) -> dict:
        """
        TODO

        Arguments:
            row: TODO

        Returns:
            TODO: TODO
        """

        img = np.ones([self.img_size, self.img_size, 3], dtype=np.uint8) * 255

        hash_of_row = row["__hash_of_row__"] + self.to_hash_added

        r = random.Random(hash_of_row)

        result = {}

        for i in range(self.num_of_circles):
            coordinates = (r.randint(5, self.img_size - 5), r.randint(5, self.img_size - 5))
            if "coordinates" in result:
                result["coordinates"].append(coordinates)
            else:
                result["coordinates"] = [coordinates]
            radius = r.randint(10, 25)
            mask = helper.create_circular_mask(self.img_size, self.img_size, coordinates, radius)

            img[mask] -= 128
            img[mask, r.randint(0, 2)] -= 128

            if "mask" in result:
                result["mask"] += np.array(mask, dtype=np.uint8)
            else:
                result["mask"] = np.array(mask, dtype=np.uint8)
            bbox = [
                coordinates[0] - radius,
                coordinates[1] - radius,
                coordinates[0] + radius,
                coordinates[1] + radius,
                i,
            ]
            if bbox[0] < 0:
                bbox[0] = 0
            if bbox[1] < 0:
                bbox[1] = 0
            if bbox[2] >= self.img_size:
                bbox[2] = self.img_size - 1
            if bbox[3] >= self.img_size:
                bbox[3] = self.img_size - 1
            if "bbox" in result:
                result["bbox"].append(bbox)
            else:
                result["bbox"] = [bbox]
        result["img"] = img
        if self.return_mask is False:
            result.pop("mask")
        if self.return_coordinats is False:
            result.pop("coordinates")
        if self.return_bbox is False:
            result.pop("bbox")
        return result

    def __call__(self, row_or_df, path_to_image: str):
        """
        TODO

        Arguments:
            row_or_df: TODO
            path_to_image: Absolute path to to image.

        Returns:
            TODO: TODO
        """

        if isinstance(row_or_df, pd.DataFrame):
            imgs = {}

            for _, row in row_or_df.iterrows():
                result = self.create_test_image(row)
                for k in result:
                    if k in imgs:
                        imgs[k].append(result[k])
                    else:
                        imgs[k] = [result[k]]
            return imgs
        else:
            return self.create_test_image(row_or_df)


class ReadTestImage(Reader):
    """
    TODO
    """

    def __init__(
        self,
        image_size: int = 100,
        to_hash_added: int = 0,
        return_mask: bool = False,
        return_coordinats: bool = False,
        return_bbox: bool = False,
    ):
        """
        TODO

        Arguments:
            image_size: TODO
            to_hash_added: TODO
            return_mask: TODO
            return_coordinats: TODO
            return_bbox: TODO

        """

        super().__init__()
        self.img_size = image_size
        self.to_hash_added = to_hash_added
        self.return_mask = return_mask
        self.return_coordinats = return_coordinats
        self.return_bbox = return_bbox

    def create_test_image(
        self,
        row,
    ):
        """
        TODO

        Arguments:
            row: TODO

        Returns:
            TODO: TODO
        """

        img = np.ones([self.img_size, self.img_size, 3], dtype=np.uint8) * 255

        hash_of_row = row["__hash_of_row__"] + self.to_hash_added

        pos = 0
        set_color = 255

        r = random.Random(hash_of_row)

        while pos < self.img_size:
            next_length = r.randint(8, 50)
            pos2 = pos + next_length

            if set_color == 255:
                img[pos:pos2, : int(self.img_size / 2), 0] = set_color
                img[pos:pos2, : int(self.img_size / 2), 1] = r.randint(0, 64)
                img[pos:pos2, : int(self.img_size / 2), 2] = r.randint(0, 64)
            else:
                img[pos:pos2, : int(self.img_size / 2), 0] = r.randint(0, 255)
                img[pos:pos2, : int(self.img_size / 2), 1] = r.randint(0, 64)
                img[pos:pos2, : int(self.img_size / 2), 2] = r.randint(0, 64)

            if set_color == 255:
                img[pos:pos2, int(self.img_size / 2) :, 0] = r.randint(0, 64)
                img[pos:pos2, int(self.img_size / 2) :, 1] = set_color
                img[pos:pos2, int(self.img_size / 2) :, 2] = r.randint(0, 64)
            else:
                img[pos:pos2, int(self.img_size / 2) :, 0] = r.randint(0, 64)
                img[pos:pos2, int(self.img_size / 2) :, 1] = r.randint(0, 255)
                img[pos:pos2, int(self.img_size / 2) :, 2] = r.randint(0, 64)

            pos += next_length
            if set_color == 0:
                set_color = 255
            else:
                set_color = 0

        result = {}
        result["img"] = img
        if self.return_mask:
            result["mask"] = np.array(np.mean(img, axis=2) > 96, dtype=np.uint8)
            result["multi_label_mask"] = (
                1 * (img[:, :, 0] > 128) + 2 * (img[:, :, 1] > 128) + 4 * (img[:, :, 2] > 32)
            )
        if self.return_coordinats:
            result["coordinates"] = []
            for _ in range(10):
                result["coordinates"].append(
                    [r.randint(5, self.img_size - 5), r.randint(5, self.img_size - 5)]
                )
        if self.return_bbox:
            result["bbox"] = []
            for _ in range(3):
                x = r.randint(5, self.img_size - 150)
                y = r.randint(5, self.img_size - 150)
                result["bbox"].append([x, y, x + r.randint(50, 150), y + r.randint(50, 150)])

        return result

    def __call__(self, row_or_df, path_to_image):
        """
        TODO

        Arguments:
            row_or_df: TODO
            path_to_image: TODO

        Returns:
            TODO: TODO
        """

        if isinstance(row_or_df, pd.DataFrame):
            imgs = {}

            for _, row in row_or_df.iterrows():
                result = self.create_test_image(row)
                for k in result:
                    if k in imgs:
                        imgs[k].append(result[k])
                    else:
                        imgs[k] = [result[k]]
            return imgs
        else:
            return self.create_test_image(row_or_df)


def expression_to_string_value(expression, interpreter, row):
    """
    TODO

    Arguments:
        expression: TODO
        interpreter: TODO
        row: TODO

    Returns:
        TODO: TODO
    """

    if expression in row:
        return row[expression]
    elif callable(expression):
        return expression(row)
    elif callable(interpreter):
        return interpreter(row, expression)
    else:
        return expression


class ReadFromImageFile(Reader):
    """
    TODO
    """

    def __init__(
        self,
        expression,
        interpreter=helper.read_from_row,
        return_image_size=None,
        x_column: str = "__x__",
        y_column: str = "__y__",
    ):
        """
        TODO

        Arguments:
            expression: TODO
            interpreter: TODO
            return_image_size: TODO
            x_column: TODO
            y_column: TODO
        """

        super().__init__()
        self.expression = expression
        self.interpreter = interpreter
        self.return_image_size = return_image_size
        self.x_column = x_column
        self.y_column = y_column

    def crop(self, img, x, y):
        """
        TODO

        Arguments:
            img: TODO
            x: TODO
            y: TODO

        Returns:
            TODO: TODO
        """

        shifted_x, shifted_y = 0, 0
        start_x = int(x - self.return_image_size / 2)
        if start_x < 0:
            shifted_x = -start_x
            start_x = 0
        start_y = int(y - self.return_image_size / 2)
        if start_y < 0:
            shifted_y = -start_y
            start_y = 0
        end_x = start_x + self.return_image_size - shifted_x
        end_y = start_y + self.return_image_size - shifted_y
        img = img[start_x:end_x, start_y:end_y]
        if img.shape[0] != self.return_image_size or img.shape[1] != self.return_image_size:
            img_black_boarder = np.zeros(
                [self.return_image_size, self.return_image_size, img.shape[2]], dtype=img.dtype
            )
            img_black_boarder[
                shifted_x : shifted_x + img.shape[0], shifted_y : shifted_y + img.shape[1]
            ] = img
            return img_black_boarder
        else:
            return img

    def load_from_row(self, row, path_to_image):
        """
        TODO

        Arguments:
            row: TODO
            path_to_image: TODO

        Returns:
            TODO: TODO
        """

        path = expression_to_string_value(self.expression, self.interpreter, row)
        path_to_file = os.path.join(path_to_image, path)
        # img = plt.imread(path_to_file)
        img = np.array(Image.open(path_to_file))
        if len(img.shape) == 3 and img.shape[-1] == 4:
            img = img[..., :3]
        if self.return_image_size:
            if self.x_column in row:
                x = row[self.x_column]
            else:
                x = img.shape[0] / 2.0
            if self.y_column in row:
                y = row[self.y_column]
            else:
                y = img.shape[1] / 2.0

            img = self.crop(img, x, y)

        # img = np.swapaxes(img, 0, 2)
        # img = torch.as_tensor(img)
        return img

    def get_image_size(self, row, path_to_image):
        """
        TODO

        Arguments:
            row: TODO
            path_to_image: TODO

        Returns:
            TODO: TODO
        """

        path = expression_to_string_value(self.expression, self.interpreter, row)
        path_to_file = os.path.join(path_to_image, path)
        return imagesize.get(path_to_file)

    def __call__(self, row_or_df, path_to_image):
        """
        TODO

        Arguments:
            row_or_df: TODO
            path_to_image: TODO

        Returns:
            TODO: TODO
        """

        if isinstance(row_or_df, pd.DataFrame):
            imgs = []
            for _, row in row_or_df.iterrows():
                imgs.append(self.load_from_row(row, path_to_image))
            return imgs  # torch.stack(imgs)
        else:
            return self.load_from_row(row_or_df, path_to_image)


class ReadFromWSI(Reader):
    """
    TODO
    """

    def __init__(
        self,
        return_image_size,
        expression,
        interpreter=helper.read_from_row,
        mpp: float = 0.5,
        x_column: str = "__x__",
        y_column: str = "__y__",
        use_center_coordinates: bool = True,
    ):
        """
        TODO

        Arguments:
            return_image_size: TODO
            expression: TODO
            interpreter: TODO
            mpp: TODO
            x_column: TODO
            y_column: TODO
            use_center_coordinates: TODO

        """

        super().__init__()
        if isinstance(return_image_size, int):
            self.return_image_size = (return_image_size, return_image_size)
        else:
            self.return_image_size = return_image_size
        self.expression = expression
        self.interpreter = interpreter
        self.mpp = mpp
        self.x_column = x_column
        self.y_column = y_column
        self.use_center_coordinates = use_center_coordinates

    def load_from_row(self, row, path_to_image):
        """
        TODO

        Arguments:
            row: TODO
            path_to_image: Absolute path to image.

        Returns:
            TODO: TODO
        """

        path = expression_to_string_value(self.expression, self.interpreter, row)
        path_to_file = os.path.join(path_to_image, path)

        wsi_reader = wsireader.get_wsireader(input_img=path_to_file)

        if self.use_center_coordinates is False:
            patch = wsi_reader.read_rect(
                location=(int(row[self.x_column]), int(row[self.y_column])),
                resolution=self.mpp,
                units="mpp",
                size=self.return_image_size,
            )
        else:
            x = row[self.x_column]
            y = row[self.y_column]

            x -= (self.return_image_size[0] / 2) * self.mpp / wsi_reader.info.mpp[0]
            y -= (self.return_image_size[1] / 2) * self.mpp / wsi_reader.info.mpp[0]

            patch = wsi_reader.read_rect(
                location=(int(x), int(y)),
                resolution=self.mpp,
                units="mpp",
                size=self.return_image_size,
            )
        return patch

    def read_thumbnail(self, row, path_to_image, mpp, return_min_mpp=False):
        """
        TODO

        Arguments:
            row: TODO
            path_to_image: TODO
            mpp: TODO
            return_min_mpp: TODO

        Returns:
            TODO: TODO
        """

        path = expression_to_string_value(self.expression, self.interpreter, row)
        path_to_file = os.path.join(path_to_image, path)

        print(path_to_file)

        wsi_reader = wsireader.get_wsireader(input_img=path_to_file)

        wsi_thumb = wsi_reader.slide_thumbnail(resolution=mpp, units="mpp")

        if return_min_mpp:
            return wsi_thumb, wsi_reader.info.mpp
        else:
            return wsi_thumb

    def __call__(self, row_or_df, path_to_image):
        """
        TODO

        Arguments:
            row_or_df: TODO
            path_to_image: TODO

        Returns:
            TODO: TODO
        """

        if isinstance(row_or_df, pd.DataFrame):
            imgs = []
            for _, row in row_or_df.iterrows():
                imgs.append(self.load_from_row(row, path_to_image))
            return imgs  # torch.stack(imgs)
        else:
            return self.load_from_row(row_or_df, path_to_image)


class ReadValueFromCSV(Reader):
    """
    TODO
    """

    def __init__(self, expression, interpreter=helper.read_from_row, encoded_values=None):
        """
        TODO

        Arguments:
            expression: TODO
            interpreter: TODO
            encoded_values: TODO

        """

        super().__init__()
        self.expression = expression
        self.interpreter = interpreter
        self.encoded_values = encoded_values

    def load_from_row(self, row):
        """
        TODO

        Arguments:
            row: TODO

        Returns:
            TODO: TODO
        """

        loaded_value = expression_to_string_value(self.expression, self.interpreter, row)
        if self.encoded_values:
            if loaded_value in self.encoded_values:
                return self.encoded_values.index(loaded_value)
            else:
                return len(self.encoded_values)
        return loaded_value

    def __call__(self, row_or_df, path_to_image):
        """
        TODO

        Arguments:
            row_or_df: TODO
            path_to_image: TODO

        Returns:
            TODO: TODO
        """

        if isinstance(row_or_df, pd.DataFrame):
            values = []
            for _, row in row_or_df.iterrows():
                values.append(self.load_from_row(row))
            return values
        else:
            return self.load_from_row(row_or_df)
