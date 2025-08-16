"""
add doc-string
"""

from tkinter import ttk
from tkinter import Tk
from ssh_manager.ssh_gui.key_config import KeyConfig


class MainFrame:
    """
    add doc-string
    """

    def __init__(
        self, root: Tk, font_config: tuple[str, int, str], pad: tuple[int, int]
    ) -> None:
        self.frame = ttk.Frame(root, padding="5")
        self.frame.grid(column=0, row=0, sticky="nsew")
        self.frame_title = ttk.Label(master=self.frame)
        self.font = font_config
        self.key_config = KeyConfig(self.frame, self.font, pad[0], pad[1])

    def set_frame_title(self, **kwargs):
        """
        Set the title for the main frame
        """
        self.frame_title.config(
            text=kwargs.get("title"), font=kwargs.get("font_config")
        )
        self.frame_title.pack(padx=kwargs.get("padx"), pady=kwargs.get("pady"))
