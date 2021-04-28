import copy
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from tiatoolbox.tools import stainnorm


class TransformerAdapter:
    """
    Parent class for all Adapters. Subclasses need to implement their call method.
    """
    def __init__(self):
        self.is_callable_with_batches = False

    def __call__(self, img_or_imgs): # TODO specify type, as well for subclasses
        raise NotImplementedError


class RandomPrinterAdapter(TransformerAdapter):
    """
    TODO
    """
    def __init__(self, message: str = "RandomPrinterAdapter:"):
        """
        TODO

        Arguments:
            message: TODO
        """

        super().__init__()
        self.message = message
        self.is_callable_with_batches = True

    def __call__(self, img_or_imgs): # TODO specify type
        """
        TODO

        Arguments:
            img_or_imgs: TODO

        Returns:
            TODO: TODO
        """
        print(self.message, np.random.random())
        return img_or_imgs


class CopyAdapter(TransformerAdapter):
    """
    CopyAdapter creating a shallow copy of the input
    """
    def __init__(self, num_of_copies: int = 2):
        """
        TODO

        Arguments:
            num_of_copies: TODO
        """

        super().__init__()
        self.is_callable_with_batches = True
        self.num_of_copies = num_of_copies

    def __call__(self, img_or_imgs) -> dict: # TODO specify type
        """
        TODO

        Arguments:
            img_or_imgs: TODO
            
        Returns:
            TODO: TODO
        """

        result = {}
        for i in range(self.num_of_copies):
            # TODO
            # result.append(img_or_imgs.clone())
            result[str(i)] = copy.copy(img_or_imgs)
        return result


def convert_to_uint8_image(img: Any): # TODO Could either use extra package for typing or wait till we can upgrade to 3.8+: https://numpy.org/devdocs/reference/typing.html#module-numpy.typing
    """
    Convert any image to an unsigned int.
    
    Arguments:
        img: TODO        
            
    Returns:
        TODO: TODO
    """
    
    if img.dtype != np.uint8:
        img = img * 255 + 0.5
        img[img > 255] = 255
        return np.array(img, dtype=np.uint8)
    else:
        return img


class TiaToolBoxStainNorm(TransformerAdapter):
    """
    Stain normailaztion Adapter, using tiatoolbox.tools.stainnorm
    """
    def __init__(self, path_to_target_image:str , method_name: str):
        """
        TODO

        Arguments:
            path_to_target_image: Absolute pathto target image
            method_name: TODO
        """

        super().__init__()
        target = plt.imread(path_to_target_image)
        target = convert_to_uint8_image(target)
        self.stain_normalizer = stainnorm.get_normaliser(method_name)
        self.stain_normalizer.fit(target)
        if hasattr(self.stain_normalizer, "target_concentrations"):
            self.stain_normalizer.target_concentrations = None
        self.is_callable_with_batches = True

    def __call__(self, img_or_imgs):
        """
        TODO

        Arguments:
            img_or_imgs: TODO        
            
        Returns:
            TODO: TODO
        """
        if isinstance(img_or_imgs, list):
            result = []
            for img in img_or_imgs:
                img = convert_to_uint8_image(img)
                normed_sample = self.stain_normalizer.transform(img.copy())
                result.append(normed_sample)
            return result
        else:
            img_or_imgs = convert_to_uint8_image(img_or_imgs)
            return self.stain_normalizer.transform(img_or_imgs.copy())
