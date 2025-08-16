"""
Add docstring
"""

import tkinter as tk
from ssh_manager.ssh_gui.main_frame import MainFrame
from ssh_manager.ssh_gui.fonts import ARIAL_REG_16

# from tkinter import ttk
# from tkinter import messagebox
# import os
# import sys

# Add parent directory to path to import keygen
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from keygen import KeyGen

PADX = 5
PADY = 5


class RootWindow:
    """
    The root window for the GUI application
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SSH Key Manager")
        # self.key_gen = KeyGen()
        # self.setup_ui()

    def set_win_size(self, width: int, height: int):
        """
        Set the window size (width, height)

        Args:
            width (int): The starting width of the window
            height (int): The starting height of the window
        """
        self.root.minsize(width, height)

    def configure_global_listbox_font(self, font_config: tuple[str, int, str]):
        """
        Set the font for the Listbox widget
        """
        self.root.option_add("*TCombobox*Listbox.font", font_config)


if __name__ == "__main__":
    app = RootWindow()
    app.configure_global_listbox_font(ARIAL_REG_16)
    m_frame = MainFrame(app.root, ARIAL_REG_16, (PADX, PADY))
    m_frame.key_config.configure_keytype_opts(
        key_type_values=["rsa", "ed25519"],
        key_size_values=["2048", "3072", "4096"],
        key_type_label="Key-type",
        key_size_label="Key-size",
    )
    m_frame.key_config.configure_keypath_opts(
        key_path_label="Key-path",
        key_name_label="Key-name",
    )
    m_frame.configure_generate_button(label="Generate")
    app.set_win_size(400, 400)
    app.root.mainloop()
