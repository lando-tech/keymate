import tkinter as tk
from main_frame import MainFrame
from widget_config import WidgetConfig
from fonts import ARIAL_BOLD_16, ARIAL_REG_16

# from tkinter import ttk
# from tkinter import messagebox
# import os
# import sys

# Add parent directory to path to import keygen
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from keygen import KeyGen


class RootWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SSH Key Manager")
        # self.key_gen = KeyGen()
        # self.setup_ui()

    def set_win_size(self, width: int, height: int):
        self.root.minsize(width, height)


if __name__ == "__main__":
    app = RootWindow()
    m_frame = MainFrame(app.root)
    m_frame.set_frame_title(WidgetConfig("Keymate", font_config=ARIAL_BOLD_16, col=0, row=0, colspan=2))
    m_frame.set_keytype_combobox(WidgetConfig(list_values=["rsa", "ed25519"], font_config=ARIAL_REG_16, col=0, row=1))
    app.set_win_size(400, 400)
    app.root.mainloop()
