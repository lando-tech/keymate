from typing import Optional
from fonts import ARIAL_REG_14


class WidgetConfig:
    def __init__(
        self,
        title: str = "",
        list_values: list[str] = [],
        font_config: tuple[str, int, str] = ARIAL_REG_14,
        col: int = 0,
        row: int = 0,
        colspan: int = 0,
        rowspan: int = 0
    ) -> None:
        self.title: str = title
        self.list_values: list[str] = list_values
        self.dict_values = {}
        self.font_config: tuple[str, int, str] = font_config
        self.grid_column: int = col
        self.grid_row: int = row
        self.colspan: int = colspan
        self.rowspan: int = rowspan
