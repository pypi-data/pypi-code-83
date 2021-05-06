import abc
from typing import List, Optional, Tuple, Union

from cached_property import cached_property
from graphic_coloring_engine.core import DominantColor
from pydantic import Field

from . import BaseModel
from .coordinate import Coordinate, Size
from .enums import LayerTypeEnum, WeltEnum
from .text import Segment, RGB_TUPLE


class GroupMixin:
    groupLabel: Optional[str] = None
    groupOpacity: Optional[int] = None


class FileLayer(BaseModel, GroupMixin, abc.ABC):
    """psd 解析出来的图层信息"""

    xmin: int
    ymin: int
    ymax: int
    xmax: int

    type: LayerTypeEnum
    label: str  # psd 中的图层标注
    order: int  # 图层顺序
    side: List[WeltEnum]  # 贴边信息
    opacity: int  # 0-255

    @cached_property
    def coordinate(self) -> Coordinate:
        return Coordinate(**self.dict())

    @cached_property
    def has_side_line_or_corner(self) -> bool:
        return len(self.side) in (1, 2) and set(self.side) not in [{1, 3}, {2, 4}]

    @property
    def width_used(self):
        return self.width or self.xmax - self.xmin

    @cached_property
    def area_used(self):
        return self.area or self.coordinate.area

    @property
    def height_used(self):
        return self.height or self.ymax - self.ymin

    # def format(self, size: Optional[Size] = None, **kwargs) -> "FileLayer":
    #     """格式化图层, 重置一些字段, 返回一个新对象"""
    #     self_mixin = dict(
    #         **kwargs,
    #         label=self.label,
    #         xmin=0,
    #         ymin=0,
    #         order=self.order,
    #         type=self.type,
    #         path=self.path,
    #         flipHorizontal=1,
    #         flipVertical=1,
    #         side=self.side,
    #         scale=1,
    #         width=size.x or 0,
    #         height=size.y or 0,
    #     )
    #     if self.type == LayerTypeEnum.Text.value:
    #         layer = FileLayer(
    #             **self_mixin,
    #             fontSize=self.fontSize,
    #             fontFamily=self.fontFamily,
    #             color=self.color,
    #             text=self.text,
    #             defaultSrc=self.defaultSrc,
    #             lineHeightPx=self.lineHeightPx,
    #             letterSpacingPx=self.letterSpacingPx,
    #             fontFamilyPath=self.fontFamilyPath,
    #             writeDirection=self.writeDirection,
    #             segment=self.segment,
    #         )
    #     else:
    #         # 其他图层
    #         layer = FileLayer(
    #             **self_mixin,
    #             previewPath=self.previewPath,
    #             thumbnailPath=self.thumbnailPath,
    #         )
    #     return layer

    @cached_property
    def aspect_ratio(self) -> float:
        return self.coordinate.aspect_ratio


class EditedCommonFileLayerMixin:
    """前端编辑后保存的图片通用数据结构 mixin"""
    width: Optional[int] = None
    height: Optional[int] = None
    scale: Optional[float] = None
    scaleX: Optional[float] = None
    scaleY: Optional[float] = None
    rotation: Optional[int] = None
    flipHorizontal: Optional[int] = None
    flipVertical: Optional[int] = None
    align: Optional[str] = None
    libId: Optional[int] = None
    newSrc: Optional[str] = None
    newSrcXmin: Optional[int] = None
    newSrcYmin: Optional[int] = None
    deltaStr: Optional[str] = None


class EditedImageFileLayerMixin(EditedCommonFileLayerMixin):
    """前端编辑后保存的图片图层数据结构 mixin"""

    pass


class EditedTextFileLayerMixin(EditedCommonFileLayerMixin):
    """前端编辑后保存的文字图层数据结构 mixin"""

    lineHeight: Optional[int] = None
    letterSpacing: Optional[int] = None


class TextFileLayer(FileLayer, EditedTextFileLayerMixin):
    type: LayerTypeEnum = LayerTypeEnum.Text

    # 文字独有
    text: str
    fontFamily: str
    fontFamilyPath: str
    fontSize: int
    color: RGB_TUPLE
    defaultSrc: str  # psd 中的图层渲染快照, 图片地址
    lineHeightPx: int
    letterSpacingPx: int
    area: int  # bbox 面积
    writeDirection: int
    segment: List[Segment]


class ImageFileLayer(FileLayer, EditedImageFileLayerMixin):
    type: LayerTypeEnum = LayerTypeEnum.Image
    area: int  # 背景图的话 = 画布面积, 非背景图保存的是不透明区域的像素面积

    # 图片独有
    path: str  # 原始图片路径
    previewPath: str
    thumbnailPath: str
    dominantColors: List[DominantColor] = Field(default_factory=list)


class File(BaseModel):
    """psd 文件详情"""

    preview: str
    thumbnail: str
    original: str
    updateTime: int
    type: str
    path: str
    size: str  # FIXME
    createTime: int
    name: str
    width: int
    createUser: int
    id: int
    height: int
    md5: str
    status: int

