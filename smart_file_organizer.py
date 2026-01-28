import os
import shutil
from datetime import datetime

# CHANGE THIS PATH TO YOUR TEST FOLDER
TARGET_FOLDER = r"C:\DBDA\2026\Test_Folder"

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

LOG_FILE = os.path.join(TARGET_FOLDER, "organizer.log")


def write_log(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")


def get_category(extension):
    for folder, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return folder
    return "Others"


def move_file(file_path, category_folder):
    filename = os.path.basename(file_path)
    destination_folder = os.path.join(TARGET_FOLDER, category_folder)

    # Create folder if not exists
    os.makedirs(destination_folder, exist_ok=True)

    destination_path = os.path.join(destination_folder, filename)

    # Handle duplicate file names
    counter = 1
    file_name, file_ext = os.path.splitext(filename)
    while os.path.exists(destination_path):
        new_name = f"{file_name}_{counter}{file_ext}"
        destination_path = os.path.join(destination_folder, new_name)
        counter += 1

    shutil.move(file_path, destination_path)
    write_log(f"Moved: {filename} to {category_folder}")


def organize_files():
    print("Organizing files...\n")

    for item in os.listdir(TARGET_FOLDER):
        item_path = os.path.join(TARGET_FOLDER, item)

        # Skip folders
        if os.path.isdir(item_path):
            continue

        _, extension = os.path.splitext(item)
        category = get_category(extension)

        try:
            move_file(item_path, category)
            print(f"{item} moved to {category}")
        except Exception as e:
            write_log(f"Error moving {item}: {e}")
            print(f"Error moving {item} to {e}")


    print("\n File organization completed!")


if __name__ == "__main__":
    organize_files()
