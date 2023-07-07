import os
print(os.path.getsize(r'D:\auto\appium_project\venv'))


def get_folder_size(folder):
    size = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    return size
size = get_folder_size((r'D:\auto\appium_project\venv'))
print(size / 1024 /1024)