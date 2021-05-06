"""Contains GUI layouts."""
from PyQt5 import QtWidgets
from PyQt5.QtCore import QMetaObject, QSize, Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap

from .resources import Traversable, get_svg, root

STYLE_SHEET_FILE: Traversable = root / "style_sheet.qss"
"""The style sheet resource.

:meta hide-value:
"""


def get_icon(name: str) -> QIcon:
    """Create a :py:class:`QIcon` from an svg resource.

    Args:
        name: The name of svg resource (without file extension).

    Returns:
        The created :py:class:`QIcon`.
    """
    pixmap = QPixmap()
    pixmap.loadFromData(get_svg(name))
    icon = QIcon()
    icon.addPixmap(pixmap, QIcon.Normal, QIcon.On)
    return icon


class Task(QtWidgets.QFrame):
    """Horizontal container that stores information about task."""

    def __init__(
        self,
        task_text: str,
        task_time_text: str,
        *args,
        **kwargs,
    ):
        """Initialize task.

        Args:
            task_text: task descritpion that will appear on the screen.
            task_time_text: task time/due-date that will appear on the screen.
        """
        super().__init__(*args, **kwargs)
        self.task_horizontal_layout = QtWidgets.QHBoxLayout(self)

        self.task_button = QtWidgets.QToolButton(self)
        self.task_button.setIcon(get_icon("task"))
        self.task_button.setProperty("class", "Task")

        self.task_description = QtWidgets.QLabel(self)
        self.task_description.setFont(QFont("DejaVu Sans", 14))
        self.task_description.setText(task_text)

        self.task_time = QtWidgets.QLabel(self)
        self.task_time.setFont(QFont("DejaVu Sans", 12, italic=True))
        self.task_time.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.task_time.setText(task_time_text)

        self.task_horizontal_layout.addWidget(self.task_button)
        self.task_horizontal_layout.addWidget(self.task_description)
        self.task_horizontal_layout.addWidget(self.task_time)


class QueueHeader(QtWidgets.QFrame):
    """Horizontal container that stores queue name and control buttons."""

    def __init__(self, queue_name: str, *args, **kwargs):
        """Initialize queue header.

        Args:
            queue_name: name of queue that will appear on the screen.
        """
        super().__init__(*args, **kwargs)
        self.collapse_queue = QtWidgets.QToolButton(self)
        self.collapse_queue.setIcon(get_icon("queue"))
        self.collapse_queue.setProperty("class", ["QueueHeader", "CollapseQueue"])
        self.queue_name = QtWidgets.QLabel(self)
        self.queue_name.setFont(QFont("DejaVu Sans", 22, QFont.Bold))
        self.queue_name.setText(queue_name)

        self.add_task = QtWidgets.QToolButton(self)
        self.add_task.setIcon(get_icon("add"))
        self.add_task.setProperty("class", "QueueHeader")

        self.more = QtWidgets.QToolButton(self)
        self.more.setIcon(get_icon("more"))
        self.more.setProperty("class", "QueueHeader")

        self.queue_horizontal_layout = QtWidgets.QHBoxLayout(self)
        self.queue_horizontal_layout.addWidget(self.collapse_queue)
        self.queue_horizontal_layout.addWidget(self.queue_name)
        self.queue_horizontal_layout.addWidget(self.add_task)
        self.queue_horizontal_layout.addWidget(self.more)


class Queue(QtWidgets.QFrame):
    """Vertical container that stores tasks organized in a queue."""

    def __init__(self, queue_name: str, *args, **kwargs):
        """Initialize queue.

        Args:
            queue_name: queue name, will be used to initialize queue_header attribute.
        """
        super().__init__(*args, **kwargs)
        self.vertical_layout = QtWidgets.QVBoxLayout(self)

        self.queue_header = QueueHeader(queue_name, self)
        self.tasks_frame = QtWidgets.QFrame(self)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding
        )
        self.tasks_frame.setSizePolicy(size_policy)

        self.vertical_layout.addWidget(self.queue_header)
        self.vertical_layout.addWidget(self.tasks_frame)

        self.vertical_task_layout = QtWidgets.QVBoxLayout(self.tasks_frame)
        task = Task("Task 1", "Time", self.tasks_frame)
        self.vertical_task_layout.addWidget(task, 0, Qt.AlignTop)
        self.vertical_task_layout.addStretch(0)


class AsideWindow(QtWidgets.QMainWindow):
    """Main window of the app."""

    def __init__(self, *args, **kwargs):
        """Initialize main window."""
        super().__init__(*args, **kwargs)
        self.resize(653, 612)
        self.setWindowTitle("aside")
        self.setStyleSheet(STYLE_SHEET_FILE.read_text())

        self.central_widget = QtWidgets.QWidget(self)
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.search = QtWidgets.QLineEdit(self.central_widget)

        self.search.setMinimumSize(QSize(200, 20))
        self.search.setFont(QFont("DejaVu Sans Condensed"))
        self.search.setPlaceholderText("Search...")

        self.settings = QtWidgets.QToolButton(self.central_widget)
        self.settings.setObjectName("Settings")
        self.settings.setFocusPolicy(Qt.ClickFocus)
        self.settings.setIcon(get_icon("settings"))

        self.logo = QtWidgets.QLabel(self.central_widget)
        self.logo.setMinimumSize(QSize(330, 125))
        self.logo.setMaximumSize(QSize(330, 125))
        self.logo.setObjectName("Logo")
        pixmap = QPixmap()
        pixmap.loadFromData(get_svg("logo"))
        self.logo.setPixmap(pixmap)
        self.logo.setScaledContents(True)

        self.grid_layout.addWidget(self.search, 1, 0, Qt.AlignLeft)
        self.grid_layout.addWidget(self.settings, 0, 1)
        self.grid_layout.addWidget(self.logo, 0, 0, Qt.AlignCenter)

        queue = Queue("Queue of tasks", self.central_widget)
        self.grid_layout.addWidget(queue, 2, 0, 1, 2)
        self.grid_layout.setColumnStretch(0, 1)
        self.grid_layout.setRowStretch(0, 1)
        self.setCentralWidget(self.central_widget)

        QMetaObject.connectSlotsByName(self)


def main(*argv: str) -> int:  # pragma: no cover
    """Main GUI entrypoint."""
    app = QtWidgets.QApplication(list(argv))
    main_window = AsideWindow()
    main_window.show()
    return app.exec_()
