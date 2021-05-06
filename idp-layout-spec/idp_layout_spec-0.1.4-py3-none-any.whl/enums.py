from enum import Enum


# TODO: 检查使用 .value
class AlignEnum(Enum):
    Left = 1
    Center = 2
    Right = 3


# TODO: 检查使用 .value
class WeltEnum(Enum):
    Left = 1
    Top = 2
    Right = 3
    Bottom = 4


# TODO: 检查使用 .value
class UOMEnum(Enum):
    CM = "cm"
    MM = "mm"
    PX = "px"


class LayerTypeEnum(Enum):
    Text = "text"
    Image = "image"


class ScenarioTypeEnum(Enum):
    未知 = 0
    户外 = 1
    网络广告 = 2
    单张 = 3
    微推海报 = 4
    现场行架 = 5
    现场x展架 = 6
    灯箱 = 7
    道旗 = 8
    围挡 = 9