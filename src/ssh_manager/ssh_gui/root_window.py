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
    m_frame = MainFrame(app.root)
    m_frame.set_frame_title(
        title="KeyGen", font_config=ARIAL_REG_16, grid_column=0, grid_row=0, colspan=2
    )
    m_frame.set_keytype_combobox(
        list_values=["rsa", "ed25519"], font_config=ARIAL_REG_16, col=0, row=1
    )
    app.set_win_size(400, 400)
    app.root.mainloop()
