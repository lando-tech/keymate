"""
Launch a watcher on the target directory
"""

import os
from typing import Optional
from threading import Thread
from queue import Queue, Empty
from watchdog.observers import Observer
from .ssh_file_event_handler import SshFileEventHandler


class MainWatch:
    """
    MainWatch facilitates the starting and stopping of the Observer.
    The Observer can optionally be launched in a separate thread.
    """

    def __init__(self, outgoing_queue: Queue) -> None:
        self.outgoing_queue = outgoing_queue
        self.observer = Observer()
        self.watcher_thread: Optional[Thread] = None
        self.running: bool = False

    def start_observer_threaded(self, file_path: Optional[str] = None):
        """
        Helper function to start the observer in a new thread, enabling the daemon.

        Args:
            file_path (str) = None: The path to watch.
        """
        self.watcher_thread = Thread(target=self.start_observer, args=(file_path, True))
        self.watcher_thread.daemon = True
        self.watcher_thread.start()

    def start_observer(
        self, file_path: Optional[str] = None, threaded_mode: bool = False
    ):
        """
        Start the observer and call the mainloop.

        Args:
            file_path (Optional[str]) = None: The path to watch.
            start_threaded (bool) = False: Whether to start the mainloop in threaded mode
        Raises:
            FileNotFoundError: if the directory provided does not exist,
                               or the .ssh directory cannot be found
        """
        watch_dir: str
        event_handler = SshFileEventHandler(self.outgoing_queue)

        if file_path:
            watch_dir = file_path
        else:
            watch_dir = event_handler.ssh_dir

        if os.path.isdir(watch_dir):
            self.observer.schedule(event_handler, watch_dir, recursive=True)
            self.observer.start()
            print(f"Observer started. Monitoring @ {watch_dir}")
            if threaded_mode:
                self.start_mainloop_threaded()
            else:
                self.start_mainloop()
        else:
            raise FileNotFoundError(
                f"Directory: {watch_dir} does not exist. Observer failed to start"
            )

    def start_mainloop_threaded(self):
        """
        Start mainloop in threaded mode.
        'self.stop' must be called in order to stop and rejoin the threads.
        """
        self.running = True
        while self.running:
            try:
                file_object, event_type = self.outgoing_queue.get_nowait()
                # Add to database, pass to function, do something here
            except Empty:
                continue

    def start_mainloop(self):
        """
        Start the mainloop, log events to console, and enable stopping via KeyboardInterrupt.
        Used for testing purposes.
        """
        self.running = True
        try:
            while self.running:
                try:
                    file_object, event_type = self.outgoing_queue.get()
                    print(f"\nEvent type: {event_type}")
                    print(f"File name: {file_object.file_name}")  # type: ignore
                    print(f"File ext: {file_object.file_extension}")  # type: ignore
                    print(f"Creation Time: {file_object.timestamp}")  # type: ignore
                except Empty:
                    print("Queue is empty, continuing...")
                    continue
        except KeyboardInterrupt:
            print("\nObserver stopped. Exiting...")
        finally:
            self.observer.stop()
            self.observer.join()

    def stop(self):
        """
        Stop the observer while running in threaded mode
        """
        self.running = False
        self.observer.stop()
        self.observer.join()

        if (
            hasattr(self, "watcher_thread")
            and self.watcher_thread
            and self.watcher_thread.is_alive()
        ):
            self.watcher_thread.join(timeout=2.0)
