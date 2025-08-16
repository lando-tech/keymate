"""
Add docstring
"""

from tkinter import font


class WidgetConfig:
    """
    Configuration class for setting widget values
    """

    def __init__(self, family, size, weight, padx, pady):
        self.font = font.Font(family=family, size=size, weight=weight)
        self.padx = padx
        self.pady = pady
