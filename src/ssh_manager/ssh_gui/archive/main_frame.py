"""
add doc-string
"""

from tkinter import ttk
import tkinter as tk
from tkinter import Tk
import os
from ssh_manager.ssh_gui.key_config import KeyConfig
from ssh_manager.keygen import KeyGen


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
        self.key_config = KeyConfig(
            self.frame, font_config=font_config, padx=pad[0], pady=pad[1]
        )
        self.generate_btn = tk.Button(
            master=self.frame, font=font_config, padx=pad[0], pady=pad[1]
        )

    def set_frame_title(self, **kwargs):
        """
        Set the title for the main frame
        """
        self.frame_title.config(
            text=kwargs.get("title"), font=kwargs.get("font_config") # pyright: ignore[reportArgumentType]
        )
        self.frame_title.pack(padx=kwargs.get("padx"), pady=kwargs.get("pady")) # pyright: ignore[reportArgumentType]

    def configure_generate_button(self, label):
        """
        Configure the generate button
        """
        self.generate_btn.config(text=label, command=self.generate_ssh_keys)
        self.generate_btn.pack()

    def generate_ssh_keys(self):
        """
        Generate the key pair from the form options and save to disk
        """
        key_gen = KeyGen()
        key_opts = self.get_key_form_values()
        file_path = key_opts.get("key-path") + os.path.sep + key_opts.get("key-name") # type: ignore
        if key_opts.get("key-type") == "rsa":
            priv_key, pub_key = key_gen.generate_rsa_keypair(key_opts.get("key-size")) # type: ignore
            key_gen.save_keypair(file_path, priv_key, pub_key)
            print(f"Keys saved to {file_path}")
        else:
            priv_key, pub_key = key_gen.generate_ed25519_keypair()
            key_gen.save_keypair(file_path, priv_key, pub_key)
            print(f"Keys saved to {file_path}")

    def get_key_form_values(self):
        """
        Add doc-string
        """
        values = {}
        values["key-name"] = self.key_config.keypath_config.key_name_entry.get()
        values["key-path"] = self.key_config.keypath_config.key_path.get()
        values["key-type"] = self.key_config.keytype_config.keytype_combobox.get()
        if values["key-type"] == "rsa":
            values["key-size"] = int(
                self.key_config.keytype_config.keysize_combobox.get()
            )
        else:
            values["key-size"] = 0

        return values
