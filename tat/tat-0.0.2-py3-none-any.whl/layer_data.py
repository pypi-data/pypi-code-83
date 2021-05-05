from typing import Optional, Final


class LayerData:
    def __init__(self, image_path: str, array_path: str, is_merger=False, parent_layers: Optional[list[int]] = None,
                 layer_index: Optional[int] = None):
        self.image_path: Final[str] = image_path
        self.array_path: Final[str] = array_path
        self.is_merger: Final[bool] = is_merger
        self.parent_layers: Final[Optional[list[int]]] = parent_layers
        self.layer_index: Final[Optional[int]] = layer_index

    def get_name(self) -> str:
        if self.is_merger:
            assert self.parent_layers is not None
            return "m " + self.indices2str(self.parent_layers)
        assert self.layer_index is not None
        return str(self.layer_index)

    @staticmethod
    def indices2str(indices: list[int]) -> str:
        indices_str = ""
        for i in indices:
            indices_str += str(i) if i == indices[0] else f"+{str(i)}"
        return indices_str
