from typing import Tuple

from idp_layout_spec import BaseModel

RGB_TUPLE = Tuple[int, int, int]


class Segment(BaseModel):
    """文字区间颜色标注"""

    color: RGB_TUPLE
    fontSize: int
    text: str
