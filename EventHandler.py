from watchdog.events import FileSystemEventHandler
from functions import get_destination, notify
from decouple import config as getenv
import os


observed_dir = getenv('SOURCE_DIR')


class EventHandler(FileSystemEventHandler):
    @staticmethod
    def on_modified(event):
        # only get files
        files = [f for f in os.listdir(observed_dir) if os.path.isfile(os.path.join(observed_dir, f))]

        for file in files:
            old_path = observed_dir + "/" + file
            new_dir = get_destination(file)
            new_path = str(new_dir) + "/" + str(file)

            # try to move the file
            try:
                os.rename(old_path, new_path)
            except FileNotFoundError:
                print("Error", "No such path found {0}".format(new_dir))
                os.mkdir(new_dir)
                os.rename(old_path, new_path)

        # print amount of moved files
        if len(files) > 0:
            print(str(len(files)) + "were moved from" + observed_dir)

