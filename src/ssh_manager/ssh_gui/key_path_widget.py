"""
Add doc-string
"""

import os

try:
    from PyQt6.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton, QFileDialog
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
        self.file_browse_btn.clicked.connect(self.open_file_dialog)

        self.fd = QFileDialog()
        self.fd.setDirectory(os.path.join(os.path.expanduser("~"), ".ssh"))

        self.key_name_label = QLabel(name_label)
        self.key_name_entry = QLineEdit()

        self.set_placeholders(path_placeholder, name_placeholder)

    def set_placeholders(self, path_placeholder, name_placeholder):
        """
        Add doc-string
        """
        self.key_path_entry.setPlaceholderText(path_placeholder)
        self.key_name_entry.setPlaceholderText(name_placeholder)

    def emplace_all_widgets(self, start_row, start_col):
        """
        Add doc-string
        """
        self.addWidget(self.key_path_label, start_row, start_col)
        self.addWidget(self.key_path_entry, start_row, start_col + 1)
        self.addWidget(self.file_browse_btn, start_row + 1, start_col + 1)
        self.addWidget(self.key_name_label, start_row + 2, start_col)
        self.addWidget(self.key_name_entry, start_row + 2, start_col + 1)

    def open_file_dialog(self):
        """
        Add doc-string
        """
        directory = self.fd.getExistingDirectory()
        if os.path.isdir(directory):
            self.key_path_entry.setText(directory)

    def export_form_values(self):
        vals = {}
        vals["key-path"] = os.path.join(
            self.key_path_entry.text(), self.key_name_entry.text()
        )
        vals["key-name"] = self.key_name_entry.text()
