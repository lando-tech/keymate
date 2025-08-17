"""
Add doc-string
"""

try:
    from PyQt6.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton
except ModuleNotFoundError:
    print("PyQt6: Module not found")


class KeyPathWidget(QGridLayout):
    """
    Add doc-string
    """

    def __init__(
        self, path_label: str, name_label: str, path_placeholder, name_placeholder
    ):
        super().__init__()
        self.key_path_label = QLabel(path_label)
        self.key_path_entry = QLineEdit()
        self.file_browse_btn = QPushButton("Browse")

        self.key_name_label = QLabel(name_label)
        self.key_name_entry = QLineEdit()

        self.set_placeholders(path_placeholder, name_placeholder)

    def set_placeholders(self, path_placeholder, name_placeholder):
        """
        Add doc-string
        """
        self.key_path_entry.setPlaceholderText(path_placeholder)
        self.key_name_entry.setPlaceholderText(name_placeholder)

    def emplace_all_widgets(self, start_row, start_col, step_column: bool = True):
        """
        Add doc-string
        """
        self.addWidget(self.key_path_label, start_row, start_col)
        if step_column:
            self.addWidget(self.key_path_entry, start_row, start_col + 1)
            self.addWidget(self.file_browse_btn, start_row + 1, start_col + 1)
            self.addWidget(self.key_name_label, start_row + 2, start_col)
            self.addWidget(self.key_name_entry, start_row + 2, start_col + 1)
        else:
            self.addWidget(self.key_path_entry, start_row + 1, start_col)
            self.addWidget(self.file_browse_btn, start_row + 1, start_col)
            self.addWidget(self.key_name_label, start_row + 2, start_col)
            self.addWidget(self.key_name_entry, start_row + 3, start_col)
