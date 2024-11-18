import os
import shutil

FOLDER_TYPES = {
              "Documents": [".doc", ".docx"],
              "PDFs": [".pdf"],
              "Text Files": [".txt"],
              "Images": [".jpg", ".jpeg", ".png", ".gif"],
              "Spreadsheets": [".xls", ".xlsx", ".csv"],
              "Presentations": [".ppt", ".pptx"],
              "Videos": [".mp4", ".avi"],
              "Others": []
             }


def make_folders():
    for folder in FOLDER_TYPES:
        os.mkdir(os.path.join(directory, folder))


def organize_files():
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):  # Checks whether it is a file or not.
            file_extension = os.path.splitext(file)[1]  # Extracted file extension.
            moved = False  # A flag to check whether the file is moved to respected folder or not.
            for folder, extensions in FOLDER_TYPES.items():
                if file_extension in extensions:
                    moved = True
                    shutil.move(os.path.join(directory, file), os.path.join(directory, folder))
                    break  # If found suitable folder then leave the loop.
            if not moved:
                shutil.move(os.path.join(directory, file), os.path.join(directory, "Others", file))


while True:
    directory = input("Enter directory: ")
    if os.path.exists(directory) and os.path.isdir(directory):
        make_folders()
        organize_files()
        print("\n-------------------Your Folder is organized!!!------------------")
        break
    else:
        print("\nPlease enter a valid directory.")
