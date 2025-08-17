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


class KeySizeWidget(QGridLayout):
    """
    Add doc-string
    """

    def __init__(self, label: str, values: list[str], key_type_combo: QComboBox):
        super().__init__()
        self.key_size_combo = QComboBox()
        self.key_size_combo.addItems(values)
        self.key_size_label = QLabel(label)
        self.key_type_combo = key_type_combo
        self.key_type_combo.currentTextChanged.connect(self.disable_key_size)

    def set_key_size_values(self, values: list[str]):
        """
        Add doc-string
        """
        self.key_size_combo.addItems(values)

    def emplace_all_widgets(
        self, start_row: int, start_col: int, step_column: bool = True
    ):
        """
        Add doc-string
        """
        self.addWidget(self.key_size_label, start_row, start_col)
        if step_column:
            self.addWidget(self.key_size_combo, start_row, start_col + 1)
        else:
            self.addWidget(self.key_size_combo, start_row + 1, start_col)

    def disable_key_size(self):
        """
        Add doc-string
        """
        if self.key_type_combo.currentText() == "ed25519":
            self.key_size_combo.setEnabled(False)
            self.key_size_combo.setCurrentText("")
        else:
            self.key_size_combo.setEnabled(True)
