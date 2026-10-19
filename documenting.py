import urllib.parse
import os
import logging
import win32file
import threading
import webbrowser
import queue
import shutil
import time

def check(pathF):
    hDir = win32file.CreateFile(pathF, 1, 7, None, 3, 0x02000000, None)
    while True:
        results = win32file.ReadDirectoryChangesW(hDir, 1024, True, 0x1F, None, None)
        for action, file in results:
            if action == 1 and "לא מאושר" in file:
                continue

            print(f"{actions[action]}: {file}")
            logging.info(f"{actions[action]}: {file}")
            if action == 1:
                time.sleep(1)
                if file.endswith(IMAGE_EXTENSIONS):
                    src_file = os.path.join(pathF, file)
                    dst_file = os.path.join("images", file)
                    if os.path.exists(src_file):
                        shutil.copy(src_file, dst_file)

if not os.path.exists("images"):
    os.makedirs("images")

IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.jfif')


actions = {
    1: "new file",
    2: "deleted file",
    3: "changed file",
    4: "name of file changed from",
    5: "name of file changed to"
}

while True:
    pathF = input("enter a root of a folder: ")
    if os.path.isdir(pathF):
        break
    print("invalid path")

logger = logging.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('log.log', mode='a', encoding='utf-8')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)


print("Enter exit to leave")
threading.Thread(target=check,daemon= True, args=(pathF,)).start()

while True:
    command = input("enter a pic: ")
    if command == "exit":
        break

url = f"https://www.google.com/search?q={command}&tbm=isch"
webbrowser.open(url)











