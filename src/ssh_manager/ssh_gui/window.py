"""
add doc-string
"""

import sys
from ssh_manager.ssh_gui.key_type_widget import KeyTypeWidget
from ssh_manager.ssh_gui.key_size_widget import KeySizeWidget
from ssh_manager.ssh_gui.key_path_widget import KeyPathWidget
from ssh_manager.ssh_gui.key_passphrase_widget import KeyPassphraseWidget

try:
    from PyQt6.QtWidgets import (
        QApplication,
        QComboBox,
        QLayout,
        QWidget,
        QPushButton,
        QDialog,
        QVBoxLayout,
        QHBoxLayout,
        QGridLayout,
        QLabel,
        QLineEdit,
        QFileDialog,
    )
except ModuleNotFoundError:
    print("PyQt6: Module not found")


class SshKeyForm(QWidget):
    """
    Add doc-string
    """

    def __init__(self, layout: QLayout):
        super().__init__()
        self.setWindowTitle("keymate")
        self.setGeometry(100, 100, 600, 600)
        self.layout = layout
        self.setLayout(self.layout)

    def init_ui(self):
        """
        Show main window
        """
        key_type_layout = KeyTypeWidget("Key-type:", ["rsa", "ed25519"])
        key_type_layout.setSpacing(5)
        key_type_layout.emplace_all_widgets(0, 0)

        key_size_layout = KeySizeWidget(
            "Key-size:", ["2048", "3072", "4096"], key_type_layout.key_type_combo
        )
        key_size_layout.setSpacing(5)
        key_size_layout.emplace_all_widgets(0, 0)

        key_path_layout = KeyPathWidget("Key-path:", "Key-name:", "~/.ssh", "id_rsa")
        key_path_layout.setSpacing(5)
        key_path_layout.emplace_all_widgets(0, 0)

        key_passphrase_layout = KeyPassphraseWidget(
            "Passphrase:", "Comment:", "user@this_computer"
        )
        key_passphrase_layout.setSpacing(5)
        key_passphrase_layout.emplace_all_widgets(0, 0)
        generate_button = QPushButton("Generate Key Pair")

        self.layout.addLayout(key_type_layout)
        self.layout.addLayout(key_size_layout)
        self.layout.addLayout(key_path_layout)
        self.layout.addLayout(key_passphrase_layout)
        self.layout.addWidget(generate_button)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SshKeyForm(QVBoxLayout())
    win.init_ui()
    sys.exit(app.exec())
