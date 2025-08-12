"""
Handle file system events for the .ssh directory (Keys directory on macOS)
and add them to a queue for processing
"""

import os
from queue import Queue
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from .file_object import FileObject
from enum import Enum, auto


class FileEventType(Enum):
    """
    Simple Enum class to hold FileSystem event types
    """

    CREATED = auto()
    DELETED = auto()
    MODIFIED = auto()


class SshFileEventHandler(FileSystemEventHandler):
    """
    Watch the .ssh or Keys directory for file system changes
    """

    def __init__(self, outgoing_queue: Queue):
        # For Windows and Linux
        self.ssh_dir = os.path.join(os.path.expanduser("~"), ".ssh")
        # For macOS
        self.keys_dir = os.path.join(os.path.expanduser("~"), "Keys")
        self.outgoing_files: Queue = outgoing_queue

    def on_created(self, event: FileSystemEvent):
        """
        Put a FileObject and FileEventType to the outgoing queue
        after creation event.
        """
        if event.is_directory:
            pass
        else:
            f_obj = FileObject(str(event.src_path))
            self.outgoing_files.put((f_obj, FileEventType.CREATED))

    def on_deleted(self, event: FileSystemEvent) -> None:
        """
        Put a FileObject and FileEventType to the outgoing queue
        after deletion event.
        """
        if event.is_directory:
            pass
        else:
            f_obj = FileObject(str(event.src_path))
            self.outgoing_files.put((f_obj, FileEventType.DELETED))

    def on_modified(self, event: FileSystemEvent):
        """
        Put a FileObject and FileEventType to the outgoing queue
        after modification event.
        """
        if event.is_directory:
            pass
        else:
            f_obj = FileObject(str(event.src_path))
            self.outgoing_files.put((f_obj, FileEventType.MODIFIED))
