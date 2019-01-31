import shutil, os, zipfile

for file in os.listdir():
    if file.endswith('xlsx'):
        print(file)
        shutil.copy(file, file + '--bk')