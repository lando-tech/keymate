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

        self.keytype_label = ttk.Label(master=self.frame, text="Key-type")
        self.keytype_combobox = ttk.Combobox(master=self.frame, state="readonly")
        self.keytype_combobox.bind("<<ComboboxSelected>>", self.set_keytype_action)

        self.keysize_label = ttk.Label(master=self.frame, text="Key-size")
        self.keysize_combobox = ttk.Combobox(master=self.frame, state="readonly")

    def set_frame_title(self, **kwargs):
        """
        Set the title for the main frame
        """
        self.frame_title.config(
            text=kwargs.get("title"), font=kwargs.get("font_config")
        )
        self.frame_title.pack(padx=kwargs.get("padx"), pady=kwargs.get("pady"))

    def configure_keytype_combobox(self, **kwargs):
        """
        Configure the Key-type Combo-box
        """
        self.keytype_combobox.config(
            values=kwargs.get("list_values"),
            font=kwargs.get("font_config"),
        )
        self.keytype_label.pack(padx=kwargs.get("padx"), pady=kwargs.get("pady"))
        self.keytype_combobox.pack(padx=kwargs.get("padx"), pady=kwargs.get("pady"))

    def configure_keytype_label(self):
        pass

    def configure_keysize_combobox(self, **kwargs):
        """
        Configure the Key-size Combo-box
        """
        self.keysize_combobox.config(
            values=kwargs.get("list_values"), font=kwargs.get("font_config")
        )
        self.keysize_combobox.pack()

    def configure_keyzise_label(self, **kwargs):
        pass

    def set_keytype_action(self, event):
        """
        Disable the Key-size Combo-box if 'ed25519' is selected and clear selection.
        Re-enable if 'rsa' is selected.
        """
        value = self.keytype_combobox.get()
        if value == "ed25519":
            self.keysize_combobox.config(state=["disabled"])
            self.keysize_combobox.set(value="")
        elif value == "rsa":
            self.keysize_combobox.config(state="readonly")
