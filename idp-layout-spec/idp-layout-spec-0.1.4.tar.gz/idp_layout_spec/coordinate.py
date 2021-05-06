from typing import Callable, Union

from cached_property import cached_property

from . import BaseModel
from .utils.calc import div


class Coordinate(BaseModel):

    xmin: float
    ymin: float
    xmax: float
    ymax: float

    @cached_property
    def valid_xmin(self) -> float:
        return max(0, self.xmin)

    @cached_property
    def valid_ymin(self) -> float:
        return max(0, self.ymin)

    @cached_property
    def size(self) -> "Size":
        return Size(x=self.width, y=self.height)

    @cached_property
    def width(self) -> float:
        return max(self.xmax - self.xmin, 0)

    @cached_property
    def height(self) -> float:
        return max(self.ymax - self.ymin, 0)

    @cached_property
    def area(self) -> float:
        return self.size.area

    def scale(
        self, w_scale: float, h_scale: float, as_type: Callable[[float], float]
    ) -> "Coordinate":
        return Coordinate(
            xmin=as_type(self.xmin * w_scale),
            ymin=as_type(self.ymin * h_scale),
            xmax=as_type(self.xmax * w_scale),
            ymax=as_type(self.ymax * h_scale),
        )

    def crop(self, size: "Size") -> "Coordinate":
        return Coordinate(
            xmin=self.valid_xmin,
            ymin=self.valid_ymin,
            xmax=max(0.0, min(size.x - 1, self.xmax)),
            ymax=max(0.0, min(size.y - 1, self.ymax)),
        )

    def intersection_iou(self, coord: "Coordinate") -> float:
        if not self.area or not coord.area:
            return 0.0
        intersect_y = min(self.ymax, coord.ymax) - max(self.ymin, coord.ymin) + 1
        min_rect_y = min(self.ymax - self.ymin + 1, coord.ymax - coord.ymin + 1)

        intersect_x = min(self.xmax, coord.xmax) - max(self.xmin, coord.xmin) + 1
        min_rect_x = min(self.xmax - self.xmin + 1, coord.xmax - coord.xmin + 1)

        inter = min(0.0, div(intersect_x, min_rect_x), div(intersect_y, min_rect_y))
        return inter

    @cached_property
    def aspect_ratio(self) -> float:
        return self.size.aspect_ratio


class Size(BaseModel):
    x: float
    y: float

    @cached_property
    def aspect_ratio(self) -> float:
        return div(self.x, self.y)

    def scale(
        self,
        w_scale: float,
        h_scale: float,
        as_type: Callable[[float], Union[float, int]],
    ) -> "Size":
        return Size(
            x=as_type(self.x * w_scale),
            y=as_type(self.y * h_scale),
        )

    @cached_property
    def area(self):
        return self.x * self.y

    def as_int(self):
        return Size(x=int(self.x), y=int(self.y))
