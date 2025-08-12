"""
The file object module is a cross platform wrapper object for files.
"""

from pathlib import Path
from .file_permissions import FilePermissions
from time import strftime


class FileObject:
    """
    Object to hold file data and manage permissions

    Example:
        >>> f_obj = FileObject('/your/file/path')
        >>> owner = FilePermissions(read=True, write=True, exec=False)
        >>> group = FilePermissions(read=True, write=False, exec=False)
        >>> other = FilePermissions(read=True, write=False, exec=False)
        >>> f_obj.set_permissions(owner, group, other)
        >>> print(f_obj.file_permissions)
        >>> print(f_obj.file_name)
        >>> print(f_obj.file_extension)
    """

    def __init__(self, file_path: str):
        self.path_obj = Path(file_path)
        self.file_path: str = str(self.path_obj)
        self.file_name: str = self.path_obj.name
        self.file_extension: str = self.path_obj.suffix
        self.has_extension: bool = bool(self.path_obj.suffix)
        self.timestamp: str = strftime("%d %b, %Y -- %H:%M:%S")
        self.file_permissions: int = int(oct(0o600), 8)

    def set_permissions(
        self,
        owner: FilePermissions,
        group: FilePermissions,
        other: FilePermissions,
    ):
        """
        Set the permissions for the file object

        Args:
            owner (FilePermissions): The permissions for the owner of the file
            group (FilePermissions): The permissions for the user group
            other (FilePermissions): The permissions for all others
        """
        owner_oct: int = self.get_permissions(owner)
        group_oct: int = self.get_permissions(group)
        other_oct: int = self.get_permissions(other)
        permissions = f"{owner_oct}{group_oct}{other_oct}"
        self.file_permissions = int(permissions, 8)
        self.path_obj.chmod(self.file_permissions)

    def get_permissions(self, permissions: FilePermissions) -> int:
        """
        Convert FilePermissions object to octal permission value.

        Calculates the octal digit (0-7) representing the permission combination:
        - Read: 4, Write: 2, Execute: 1
        - Combinations are additive (e.g., read+write = 6, read+write+exec = 7)

        Args:
            permissions (FilePermissions): Object containing read, write, and exec flags

        Returns:
            int: Octal digit from 0-7 representing the permission combination
        """
        if permissions.read and permissions.write and permissions.exec:
            return 7
        if permissions.read and permissions.write and not permissions.exec:
            return 6
        if permissions.read and not permissions.write and permissions.exec:
            return 5
        if permissions.read and not permissions.write and not permissions.exec:
            return 4
        if not permissions.read and permissions.write and permissions.exec:
            return 3
        if not permissions.read and permissions.write and not permissions.exec:
            return 2
        if not permissions.read and not permissions.write and permissions.exec:
            return 1
        if not permissions.read and not permissions.write and not permissions.exec:
            return 0
        return 0  # Fallback, should never reach here
