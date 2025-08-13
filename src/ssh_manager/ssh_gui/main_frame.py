"""
add doc-string
"""

from tkinter import ttk
from tkinter import Tk


class MainFrame:
    """
    add doc-string
    """

    def __init__(self, root: Tk) -> None:
        self.frame = ttk.Frame(root, padding="5")
        self.frame.grid(column=0, row=0, sticky="nsew")
        self.frame_title = ttk.Label(master=self.frame)
        self.keytype_combobox = ttk.Combobox(master=self.frame, state="readonly")

    def set_frame_title(self, **kwargs):
        """
        Set the title for the main frame
        """
        self.frame_title.config(
            text=kwargs.get("title"), font=kwargs.get("font_config")
        )
        self.frame_title.grid(
            column=kwargs.get("col"),
            row=kwargs.get("row"),
            columnspan=kwargs.get("colspan"),
        )

    def set_keytype_combobox(self, **kwargs):
        """
        Configure the Key-type Combo-box
        """
        self.keytype_combobox.config(
            values=kwargs.get("list_values"), font=kwargs.get("font_config")
        )
        self.keytype_combobox.grid(column=kwargs.get("col"), row=kwargs.get("row"))
