"""
Add doc-string
"""

try:
    from PyQt6.QtWidgets import (
        QComboBox,
        QGridLayout,
        QLabel,
    )
except ModuleNotFoundError:
    print("PyQt6: Module not found")


class KeyTypeWidget(QGridLayout):
    """
    Add doc-string
    """

    def __init__(self, label: str, values: list[str]):
        super().__init__()
        self.key_type_combo = QComboBox()
        self.set_key_type_values(values)
        self.key_type_label = QLabel(label)

    def set_key_type_values(self, values: list[str]):
        """
        Add doc-string
        """
        self.key_type_combo.addItems(values)

    def emplace_all_widgets(
        self, start_row: int, start_col: int, step_column: bool = True
    ):
        """
        Add doc-string
        """
        self.addWidget(self.key_type_label, start_row, start_col)
        if step_column:
            self.addWidget(self.key_type_combo, start_row, start_col + 1)
        else:
            self.addWidget(self.key_type_combo, start_row + 1, start_col)

    def emplace_key_type_combo(self, col: int, row: int):
        """
        Add doc-string
        """
        self.addWidget(self.key_type_combo, row, col)

    def emplace_key_type_label(self, col: int, row: int):
        """
        Add doc-string
        """
        self.addWidget(self.key_type_label, row, col)
