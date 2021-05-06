from __future__ import annotations

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QImage, QMouseEvent

from .image_entry import ImageEntry
from .layer_data import LayerData

from typing import Callable, Any, Final


class ClusterImageEntry(ImageEntry):
    def __init__(self, parent: QWidget, image: QImage, image_path: str, array_path: str, name: str,
                 layers_data: list[LayerData]):
        """
        Instantiate a ClusterImageEntry object
        :param parent: The widget calling the method
        :param image: The image that will be used to draw the preview thumbnail
        :param image_path: The path of the cluster image
        :param name: The name that will be showed below the thumbnail
        :param layers_data: A list of LayerData containing all the information about a layer
        """
        super(ClusterImageEntry, self).__init__(parent, image, image_path, name, array_path)
        self.layers_data: Final[list[LayerData]] = layers_data
        self.__mouse_double_click_actions: list[Callable[[ClusterImageEntry], Any]] = []

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        for action in self.__mouse_double_click_actions:
            action(self)

    def layer_count(self) -> int:
        return len(self.layers_data)

    def add_layer_data(self, layer_data: LayerData) -> None:
        self.layers_data.append(layer_data)

    def get_layer_data(self, index: int) -> LayerData:
        return self.layers_data[index]

    def remove_layer_data(self, index: int) -> LayerData:
        return self.layers_data.pop(index)

    def register_mouse_double_click_action(self, action: Callable[[ClusterImageEntry], Any]):
        self.__mouse_double_click_actions.append(action)
