import shutil
import os

shutil.copy("example.txt", "backup.txt")

if os.path.exists("backup.txt"):
    os.remove("backup.txt")