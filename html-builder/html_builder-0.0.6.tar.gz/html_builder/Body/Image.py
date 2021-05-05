from html_builder import EmptyElement


class Image(EmptyElement):
    """src is a image source,alt是图片替换文本,is_lazy是表示是否延迟加载"""

    def _getEleKey(self):
        return 'img'

    __width = None
    __height = None

    def __init__(self,
                 src: str,
                 alt: str = 'can not load image',
                 is_lazy: bool = True):
        self.__src = src
        self.__alt = alt
        self.__is_lazy = is_lazy

    def setSize(self, width: int, height: int):
        self.__width = width
        self.__height = height
        return self

    def _getAttrs(self) -> dict:
        rt = {
            'src': self.__src,
            'alt': self.__alt,
        }
        if self.__width is not None and self.__height is not None:
            rt['width'] = self.__width
            rt['height'] = self.__height
        if self.__is_lazy:
            rt['loading'] = 'lazy'
        return rt
