"""
FilePermissions dataclass for FileObject permissions management
"""

from dataclasses import dataclass


@dataclass
class FilePermissions:
    """
    Simple dataclass to signal file permissions for the file_object.FileObject class
    """

    read: bool
    write: bool
    exec: bool
