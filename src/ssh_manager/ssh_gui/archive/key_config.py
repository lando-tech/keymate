"""
add doc-string
"""

from tkinter import ttk
import tkinter as tk
from tkinter import font
from tkinter import filedialog


class KeyTypeConfig:
    """
    add doc-string
    """

    def __init__(self, root, font_config):
        self.root = root
        self.keytype_combobox = ttk.Combobox(
            master=self.root, state="readonly", font=font_config
        )
        self.keytype_combobox.bind("<<ComboboxSelected>>", self.set_keytype_action)
        self.keysize_combobox = ttk.Combobox(master=self.root, state="readonly")

    def configure_keytype_combobox(self, **kwargs):
        """
        Configure the Key-type Combo-box
        """
        self.keytype_combobox.config(
            font=kwargs.get("font_config"),
            values=kwargs.get("key_type_values"),
        )
        label = ttk.Label(
            master=self.root,
            text=kwargs.get("key_type_label"),
        )
        label.pack(padx=kwargs.get("padx"), pady=kwargs.get("pady"))
        self.keytype_combobox.pack(padx=kwargs.get("padx"), pady=kwargs.get("pady"))

    def configure_keysize_combobox(self, **kwargs):
        """
        Configure the Key-size Combo-box
        """
        self.keysize_combobox.config(
            values=kwargs.get("key_size_values"), font=kwargs.get("font_config")
        )
        label = ttk.Label(
            master=self.root, text=kwargs.get("key_size_label"), font=kwargs.get("font")
        )
        label.pack(padx=kwargs.get("padx"), pady=kwargs.get("pady"))
        self.keysize_combobox.pack(padx=kwargs.get("padx"), pady=kwargs.get("pady"))

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


class KeyPathConfig:
    """
    Add doc-string
    """

    def __init__(self, root):
        self.root = root
        self.key_path = ttk.Entry(master=self.root)
        self.browse_btn = tk.Button(master=self.root)
        self.key_name_entry = ttk.Entry(master=self.root)
        self.dir_path = ""

    def configure_keypath_entry(self, **kwargs):
        """
        Configure the Key-path Entry widget
        """
        self.key_path.config(font=kwargs.get("font_config"), width=kwargs.get("width"))
        label = ttk.Label(
            master=self.root,
            text=kwargs.get("key_path_label"),
            font=kwargs.get("font_config"),
        )
        label.pack(padx=kwargs.get("padx"), pady=kwargs.get("pady"))

        self.key_path.pack(padx=kwargs.get("padx"), pady=kwargs.get("pady"))

    def configure_keyname_entry(self, **kwargs):
        """
        Configure the Key-name Entry widget
        """
        self.key_name_entry.config(
            font=kwargs.get("font_config"), width=kwargs.get("width")
        )
        label = ttk.Label(
            master=self.root,
            text=kwargs.get("key_name_label"),
            font=kwargs.get("font_config"),
        )
        label.pack(padx=kwargs.get("padx"), pady=kwargs.get("pady"))
        self.key_name_entry.pack(padx=kwargs.get("padx"), pady=kwargs.get("pady"))

    def configure_file_finder(self, **kwargs):
        """
        Configure the file browser button
        """
        self.browse_btn.config(
            text="Browse", command=self.open_directory, font=kwargs.get("font_config")
        )
        self.browse_btn.pack(padx=kwargs.get("padx"), pady=kwargs.get("pady"))

    def set_key_path_text(self):
        """
        Set the keypath to self.dir_path
        """
        self.key_path.insert(0, self.dir_path)

    def open_directory(self):
        """
        Get the chosen directory
        """
        self.dir_path = filedialog.askdirectory()
        if self.dir_path:
            self.set_key_path_text()


class KeyConfig:
    """
    add doc-string
    """

    def __init__(self, root, font_config: font.Font, padx: int, pady: int):
        self.root = root
        self.font_config = font_config
        self.padx = padx
        self.pady = pady
        self.keytype_config = KeyTypeConfig(self.root, self.font_config)
        self.keypath_config = KeyPathConfig(self.root)

    def configure_keytype_opts(self, **kwargs):
        """
        Add doc-string
        """
        self.keytype_config.configure_keytype_combobox(
            font_config=self.font_config,
            padx=self.padx,
            pady=self.pady,
            key_type_values=kwargs.get("key_type_values"),
            key_type_label=kwargs.get("key_type_label"),
        )
        self.keytype_config.configure_keysize_combobox(
            font_config=self.font_config,
            padx=self.padx,
            pady=self.pady,
            key_size_values=kwargs.get("key_size_values"),
            key_size_label=kwargs.get("key_size_label"),
        )

    def configure_keypath_opts(self, **kwargs):
        """
        Add doc-string
        """
        self.keypath_config.configure_keypath_entry(
            key_path_label=kwargs.get("key_path_label"),
            font_config=self.font_config,
            padx=self.padx,
            pady=self.pady,
        )
        self.keypath_config.configure_file_finder(
            font=self.font_config, padx=self.padx, pady=self.pady
        )
        self.keypath_config.configure_keyname_entry(
            key_name_label=kwargs.get("key_name_label"),
            font_config=self.font_config,
            padx=self.padx,
            pady=self.pady,
        )
