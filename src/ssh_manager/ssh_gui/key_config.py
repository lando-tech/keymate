"""
add doc-string
"""

from tkinter import ttk
from tkinter import filedialog


class KeyConfig:
    """
    add doc-string
    """

    def __init__(self, root, font_config: tuple[str, int, str], padx: int, pady: int):
        self.root = root
        self.font = font_config
        self.padx = padx
        self.pady = pady

        self.keytype_combobox = ttk.Combobox(master=self.root, state="readonly")
        self.keytype_combobox.bind("<<ComboboxSelected>>", self.set_keytype_action)
        self.keysize_combobox = ttk.Combobox(master=self.root, state="readonly")
        self.key_path = ttk.Entry(master=self.root)
        self.browse_btn = ttk.Button(master=self.root)
        self.dir_path = ""

    def configure_keytype_combobox(self, **kwargs):
        """
        Configure the Key-type Combo-box
        """
        self.keytype_combobox.config(
            values=kwargs.get("list_values"),
            font=self.font,
        )
        label = ttk.Label(master=self.root, font=self.font, text=kwargs.get("label"))
        label.pack(padx=self.padx, pady=self.pady)
        self.keytype_combobox.pack(padx=self.padx, pady=self.pady)

    def configure_keysize_combobox(self, **kwargs):
        """
        Configure the Key-size Combo-box
        """
        self.keysize_combobox.config(values=kwargs.get("list_values"), font=self.font)
        label = ttk.Label(master=self.root, text=kwargs.get("label"), font=self.font)
        label.pack(padx=self.padx, pady=self.pady)
        self.keysize_combobox.pack(padx=self.padx, pady=self.pady)

    def configure_keypath_entry(self, **kwargs):
        """
        Configure the Key-path Entry widget
        """
        self.key_path.config(font=self.font, width=kwargs.get("width"))
        label = ttk.Label(master=self.root, text=kwargs.get("label"), font=self.font)
        label.pack(padx=self.padx, pady=self.pady)
        self.key_path.pack(padx=self.padx, pady=self.pady)

    def configure_file_finder(self, **kwargs):
        """
        Configure the file browser button
        """
        self.browse_btn.config(text="Browse", command=self.open_directory)
        self.browse_btn.pack(padx=self.padx, pady=self.pady)

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

    def open_directory(self):
        self.dir_path = filedialog.askdirectory()
