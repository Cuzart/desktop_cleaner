from decouple import config as getenv

import os

# name of the folder and tuple of file extensions
categories = {
    "Bilder":  ('.png', '.jpg', '.jpeg', '.gif', '.svg'),
    "Fotos": ('.cr2', '.heic', '.raw', '.nef'),
    "Musik": ('.mp3', '.wav', '.wma'),
    "Videos": ('.mp4', '.mov', '.avi', '.mkv', '.wmv', '.webm'),
    "Fonts": ('.ttf', '.otf', 'eot', '.woff'),
    "Dokumente": ('.txt', '.pages', '.doc', '.pdf', '.rtf'),
    "Design": ('.ai', '.psd', '.afdesign', '.xcf'),
    "Coding": ('.css', '.html', '.py', '.scss', '.js', '.ts', '.yml')
}


# determine a suiting destination for the file
def get_destination(filename):
    destination_dir = getenv('DESTINATION_DIR')
    
    # individual logic here
    if "Bildschirm" in filename:
        return destination_dir + "/Screenshots"

    # handle each category
    for category in categories:
        if filename.lower().endswith(categories[category]):
            return destination_dir + '/' + category

    return destination_dir + "/Other"


# triggers a desktop notification
def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
