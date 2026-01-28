# Smart File Organizer (Python Automation Project)

A Python automation tool that organizes files in a folder into categorized subfolders based on file extensions.

This project demonstrates practical file handling, automation, and error handling using core Python modules.

---

## Features

- Automatically scans a target folder  
- Categorizes files by type (Images, Videos, Documents, etc.)  
- Creates folders automatically if they don’t exist  
- Handles duplicate file names safely  
- Moves unknown file types to an **Others** folder  
- Maintains a log file with timestamps of all file movements  
- Includes error handling to prevent crashes  

---

## Technologies Used

- Python 3  
- Built-in modules:
  - `os` – File and directory operations  
  - `shutil` – Moving files  
  - `datetime` – Timestamp logging  

---

## 📂 File Categories

| Folder Name | File Types |
|-------------|------------|
| Images | .jpg, .jpeg, .png, .gif |
| Videos | .mp4, .mkv, .avi |
| Documents | .pdf, .docx, .txt, .xlsx, .pptx |
| Music | .mp3, .wav |
| Archives | .zip, .rar |
| Others | Any unknown extension |

---

## How to Run

1. Open smart_file_organizer.py
2. Set your folder path:
   TARGET_FOLDER = r"C:\Path\To\Folder"
3. Add files inside the folder
4. Run:
   python smart_file_organizer.py

## Output

After running, your folder will be organized like this:

Target Folder/
│
├── Images/
├── Videos/
├── Documents/
├── Music/
├── Archives/
├── Others/
└── organizer.log

The organizer.log file stores all file movement details with timestamps.

## What I Learned
- File handling using Python
- Automation using os and shutil
- Logging and error handling
- Writing production-style scripts

## Resume Description

Developed a Python-based Smart File Organizer that automates file management by categorizing files based on extensions, creating folders dynamically, handling duplicate filenames, and logging operations with proper error handling.


