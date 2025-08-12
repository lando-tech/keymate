from queue import Queue
from .main_watch import MainWatch

watcher = MainWatch(Queue())
watcher.start_observer(threaded_mode=False)
