
import os
import logging
import win32file
import threading


def check(pathF):
    hDir = win32file.CreateFile(pathF, 1, 7, None, 3, 0x02000000, None)
    while True:
        results = win32file.ReadDirectoryChangesW(hDir, 1024, True, 0x1F, None, None)
        for action, file in results:
            print(f"{actions[action]}: {file}")
            logging.info(f"{actions[action]}: {file}")




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


logging.basicConfig(
    filename='log.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


print("Enter exit to leave")
threading.Thread(target=check,daemon= True, args=(pathF,)).start()

while True:
    command = input()
    if command == "exit":
        break









