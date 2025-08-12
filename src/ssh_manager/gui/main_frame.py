from tkinter import ttk
from tkinter import Tk
from widget_config import WidgetConfig


class MainFrame:
    def __init__(self, root: Tk) -> None:
        self.frame = ttk.Frame(root, padding="5")
        self.frame.grid(column=0, row=0, sticky="nsew")
        self.frame_title = ttk.Label(master=self.frame)
        self.keytype_combobox = ttk.Combobox(master=self.frame, state="readonly")

    def set_frame_title(self, config: WidgetConfig):
        self.frame_title.config(text=config.title, font=config.font_config)
        self.frame_title.grid(
            column=config.grid_column, row=config.grid_row, columnspan=config.colspan
        )

    def set_keytype_combobox(self, config: WidgetConfig):
        self.keytype_combobox.config(values=config.list_values, font=config.font_config)
        self.keytype_combobox.grid(column=config.grid_column, row=config.grid_row)
