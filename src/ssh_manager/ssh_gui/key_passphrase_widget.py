"""
Add doc-string
"""

try:
    from PyQt6.QtWidgets import (
        QGridLayout,
        QLabel,
        QLineEdit,
        QRadioButton,
    )
except ModuleNotFoundError:
    print("PyQt6: Module not found")


class KeyPassphraseWidget(QGridLayout):
    """
    Add doc-string
    """

    def __init__(self):
        super().__init__()
        self.passphrase_radio = QRadioButton()
        self.passphrase_entry = QLineEdit()
        self.passphrase_entry.setEchoMode(QLineEdit.EchoMode.Password)

        self.comment_radio = QRadioButton()
        self.comment_entry = QLineEdit()

    def emplace_all_widgets(self, start_row, start_col, step_column: bool = True):
        """
        Add doc-string
        """
        if step_column:
            self.addWidget(self.passphrase_entry, start_row, start_col)
            self.addWidget(self.passphrase_radio, start_row, start_col + 1)

            self.addWidget(self.comment_radio, start_row + 1, start_col)
            self.addWidget(self.comment_entry, start_row + 1, start_col + 1)
        else:
            self.addWidget(self.passphrase_radio, start_row, start_col)
            self.addWidget(self.passphrase_radio, start_row + 1, start_col)

            self.addWidget(self.comment_radio, start_row + 2, start_col)
            self.addWidget(self.comment_entry, start_row + 3, start_col)

    def disable_passphrase_entry(self):
        """
        Add doc-string
        """
        if self.passphrase_radio.isChecked():
            self.passphrase_entry.setEnabled(False)
            self.passphrase_entry.clear()
        else:
            self.passphrase_entry.setEnabled(True)

    def disable_comment_entry(self):
        """
        Add doc-string
        """
        if self.comment_radio.isChecked():
            self.comment_entry.setEnabled(False)
            self.comment_entry.clear()
        else:
            self.comment_entry.setEnabled(True)
