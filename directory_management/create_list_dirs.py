import os

os.mkdir("test_folder")

os.makedirs("nested/folder/example", exist_ok=True)

print(os.listdir())

print(os.getcwd())