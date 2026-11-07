# Marvellous Data Shield – Duplicate File Detection & Removal

A Python-based file management automation project that identifies and removes duplicate files from a specified directory using MD5 checksum comparison.

The project demonstrates how hashing algorithms can be used to compare file contents efficiently without loading entire files into memory.

## Features

- Calculates MD5 checksums of files.
- Reads files in chunks of 1024 bytes.
- Recursively scans directories and subdirectories.
- Identifies duplicate files based on their checksums.
- Groups files having identical checksums.
- Preserves the first occurrence of each file.
- Automatically deletes duplicate copies.
- Displays the total number of deleted files.

## Technologies Used

- **Programming Language:** Python
- **Hashing:** hashlib (MD5)
- **File System Operations:** os module
- **File Handling:** Python File I/O
- **Data Structures:** Dictionary and List
- **Functional Programming:** Lambda and Filter

## Project Structure

```text
Marvellous_Data_Shield/
│
├── duplicate_finder.py
├── README.md
└── requirements.txt
```

## Prerequisites

- Python 3.x
- No external Python libraries are required.

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/nickpat22/Python_Automation_Projects.git
```

**2. Navigate to the project directory**

```bash
cd Python_Automation_Projects/Marvellous_Data_Shield
```

**3. Create a directory named `Test`**

Place some sample files inside it, including duplicate files.

**4. Execute the Python script**

```bash
python duplicate_finder.py
```

## Working Process

1. Opens files in binary read mode.
2. Calculates the MD5 checksum of each file.
3. Reads file contents in chunks of 1024 bytes.
4. Traverses the specified directory and its subdirectories.
5. Groups files based on their calculated checksums.
6. Identifies groups containing more than one file.
7. Preserves the first file in each group.
8. Deletes the remaining duplicate files.
9. Displays the total number of deleted files.

## Learning Outcomes

Through this project, I explored:

- File handling in binary mode.
- MD5 hashing using Python's hashlib module.
- Checksum-based file comparison.
- Efficient file reading using buffers.
- Recursive directory traversal using `os.walk()`.
- Dictionary and list operations.
- Lambda functions and filter().
- Automated file management using Python.

## Important Note

**Warning:** This program permanently deletes duplicate files. Always test it using sample directories and keep backups of important data.

MD5 is used here for educational duplicate-detection purposes. It should not be considered a secure cryptographic verification mechanism.

## Author

**Nikunj Patidar**

GitHub: [@nickpat22](https://github.com/nickpat22)

---

*This project is part of my Python Automation learning journey, focused on file handling, hashing algorithms, and practical automation techniques.*
