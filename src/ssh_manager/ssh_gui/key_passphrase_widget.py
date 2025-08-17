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

    def __init__(
        self, passphrase_label: str, comment_label: str, comment_placeholder: str
    ):
        super().__init__()
        self.passphrase_label = QLabel(passphrase_label)
        self.passphrase_entry = QLineEdit()
        self.passphrase_entry.setEchoMode(QLineEdit.EchoMode.Password)

        self.confirm_label = QLabel("Confirm Passphrase:")
        self.confirm_passphrase = QLineEdit()
        self.confirm_passphrase.setEchoMode(QLineEdit.EchoMode.Password)

        self.comment_label = QLabel(comment_label)
        self.comment_entry = QLineEdit()
        self.comment_entry.setPlaceholderText(comment_placeholder)

    def emplace_all_widgets(self, start_row, start_col):
        """
        Add doc-string
        """
        self.addWidget(self.passphrase_label, start_row, start_col)
        self.addWidget(self.passphrase_entry, start_row, start_col + 1)

        self.addWidget(self.confirm_label, start_row + 1, start_col)
        self.addWidget(self.confirm_passphrase, start_row + 1, start_col + 1)

        self.addWidget(self.comment_label, start_row + 2, start_col)
        self.addWidget(self.comment_entry, start_row + 2, start_col + 1)
