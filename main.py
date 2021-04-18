from watchdog.observers import Observer
from decouple import config as getenv
from EventHandler import EventHandler
from functions import notify
import time

event_handler = EventHandler()

observed_dir = getenv('SOURCE_DIR')
observer = Observer()
observer.schedule(event_handler, observed_dir, recursive=True)
observer.start()

notify("Hey 👋", "We will watch " + observed_dir + " for now and keep it clean.")

try:
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    observer.stop()
    notify("Stopped ✋", "You are on your own now.")
observer.join()
