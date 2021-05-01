from importlib.resources import open_text

from ..memo.load import _load_memo_file
from . import data


def test_RorataJins_example() -> None:
    with open_text(data, "RorataJin's example.txt", encoding="shift-jis-2004") as f:
        ...
