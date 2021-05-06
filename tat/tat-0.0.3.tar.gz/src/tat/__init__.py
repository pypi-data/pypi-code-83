from PySide6.QtWidgets import QApplication
from .image_entry import ImageEntry
from .cluster_image_entry import ClusterImageEntry
from .checkable_image_entry import CheckableImageEntry
from .layer_image_entry import LayerImageEntry
from .preview_window import PreviewWindow
from .cluster_editor import ClusterEditor
from .main_window import MainWindow
from .layer_data import LayerData


def run() -> int:
    app = QApplication()
    app.main_window = MainWindow()
    app.main_window.show()
    return app.exec_()
