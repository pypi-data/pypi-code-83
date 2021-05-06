from typing import Optional, Final

import numpy as np

from .checkable_image_entry import CheckableImageEntry
from .layer_data import LayerData

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QImage


class LayerImageEntry(CheckableImageEntry):
    def __init__(self, parent: QWidget, image: QImage, array: np.ndarray, name: str, is_merger: bool = False,
                 layer_index: Optional[int] = None, parent_layers: Optional[list[int]] = None):
        super(LayerImageEntry, self).__init__(parent, image, name, default_check=False)

        self.array: Final[np.ndarray] = array
        self.layer_data: Final[LayerData] = LayerData(None, None, is_merger, parent_layers, layer_index)
