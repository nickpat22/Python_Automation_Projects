# Directory Scanner & Automation

A Python-based automation script that periodically scans a specified directory, identifies empty files (zero-byte files), deletes them, and generates log reports containing file information.

This project demonstrates the practical use of Python file handling, directory traversal, command-line arguments, and task scheduling.

## Features

- Scans the specified directory and its subdirectories.
- Identifies empty files (files with zero bytes).
- Automatically deletes identified empty files.
- Calculates and records file sizes.
- Generates timestamp-based log files.
- Displays total files scanned and empty files deleted.
- Performs directory scanning automatically at one-minute intervals.
- Supports command-line help and usage instructions.

## Technologies Used

- **Language:** Python
- **File System Operations:** OS Module
- **Command-Line Arguments:** SYS Module
- **Time Management:** TIME Module
- **Task Scheduling:** Schedule Library
- **Logging:** Python File Handling

## Project Structure

```text
Directory_Scanner/
│
├── directory_scanner.py
├── requirements.txt
├── README.md
│
└── Log_Files/
    └── Generated automatically during execution
```

## Prerequisites

- Python 3.x
- pip (Python Package Installer)

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/nickpat22/Python_Automation_Projects.git
```

**2. Navigate to the project directory**

```bash
cd Python_Automation_Projects/Directory_Scanner
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

## How to Run

**Display help information**

```bash
python directory_scanner.py --h
```

**Display usage instructions**

```bash
python directory_scanner.py --u
```

**Execute the automation script**

```bash
python directory_scanner.py "C:\Users\YourName\Documents\TestFolder"
```

Replace the example path with your actual directory path.

## Working Process

1. Accepts a directory path through command-line arguments.
2. Validates whether the specified path exists and is a directory.
3. Starts the scheduling mechanism.
4. Scans the directory and all its subdirectories every minute.
5. Collects file names and their sizes.
6. Identifies zero-byte files and deletes them.
7. Generates a log file containing scanning details and statistics.

## Sample Log Information

```text
----------------------------------------

Marvellous Automation Script
Files From The Directory Are :

----------------------------------------

Documents/file1.txt : 120 bytes
Documents/file2.txt : 0 bytes
Documents/file3.py : 450 bytes

----------------------------------------
Total Files Scanned : 3
Total empty Files Found and deleted 1
----------------------------------------
Log File Gets Created At : ...
----------------------------------------
```

## Learning Outcomes

Through this project, I explored:

- Python OS module and file system operations.
- Recursive directory traversal using `os.walk()`.
- File size identification using `os.path.getsize()`.
- File deletion using `os.remove()`.
- Command-line argument handling.
- Task scheduling using the Schedule library.
- File handling and log generation.
- Automation using Python.

## Important Note

**Warning:** This script automatically deletes all zero-byte files found in the specified directory and its subdirectories. Use it only on directories where you have permission to modify files. Avoid running it on important system or project directories.

## Author

**Nikunj Patidar**

GitHub: [@nickpat22](https://github.com/nickpat22)

---

*This project is part of my Python learning journey, focused on understanding automation, file handling, and practical programming concepts.*
