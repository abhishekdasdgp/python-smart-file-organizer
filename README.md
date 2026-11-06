
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Release](https://img.shields.io/github/v/release/abhishekdasdgp/python-smart-file-organizer?color=brightgreen)](https://github.com/abhishekdasdgp/python-smart-file-organizer/releases)
[![License](https://img.shields.io/github/license/abhishekdasdgp/python-smart-file-organizer)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows-blue?logo=windows)](https://github.com/abhishekdasdgp/python-smart-file-organizer)
[![Downloads](https://img.shields.io/github/downloads/abhishekdasdgp/python-smart-file-organizer/total?color=orange)](https://github.com/abhishekdasdgp/python-smart-file-organizer/releases)


# Python Smart File Organizer 📁

A Python-based utility that automatically scans, categorizes, and organizes files into dedicated folders based on their file extensions.

The application simplifies file management by identifying file types, generating a proposed organization plan, previewing the changes, and moving files into their respective category folders.

## 🚀 Features

- **Automatic File Scanning:** Scans a selected directory and collects file metadata.
- **Smart Categorization:** Classifies files based on their extensions.
- **Organization Planning:** Generates destination paths for categorized files before execution.
- **Preview:** Displays the proposed file organization, including source and destination paths.
- **Automatic Directory Creation:** Creates category-specific directories when they don't exist.
- **File Movement:** Moves files into their corresponding category folders.
- **Modular Architecture:** Separates scanning, categorization, planning, preview, and execution into independent modules.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| pathlib | Filesystem and path management |
| shutil | File movement |
| dataclasses | Structured file metadata |
| os | Filesystem operations |

**Dependencies:** Uses Python's standard library. No external packages are currently required.

## 📂 Project Structure

```text
python-smart-file-organizer/
│
├── src/
│   └── fileorganizer/
│       ├── __init__.py
│       ├── main.py
│       ├── scanner.py
│       ├── categorizer.py
│       ├── planner.py
│       ├── preview.py
│       └── organizer.py
│
├── config/
│   └── filetypes.py
│
├── tests/
│
├── logs/
│
├── reports/
│
├── sample_files/
│
├── .gitignore
├── README.md
└── requirements.txt
```

## 📁 File Categories

The organizer categorizes files into the following groups:

| Category | Supported Extensions (Examples) |
|---|---|
| Documents | PDF, DOC, DOCX, TXT, RTF |
| Spreadsheets | XLS, XLSX, CSV, ODS |
| Presentations | PPT, PPTX, ODP |
| Images | JPG, JPEG, PNG, GIF, BMP, WEBP, SVG |
| Videos | MP4, MKV, AVI, MOV, WMV |
| Audio | MP3, WAV, AAC, FLAC, OGG |
| Archives | ZIP, RAR, 7Z, TAR, GZ |
| Executables | EXE, MSI, APK, BAT |
| Code | PY, JAVA, JS, HTML, CSS, JSON, XML, SQL |
| Others | Unrecognized extensions and files without extensions |

The extension mappings are maintained in `config/filetypes.py`.

## ⚙️ How It Works

The application follows a modular execution pipeline:

```text
       User Input
            |
            v
     +--------------+
     | File Scanner |
     +--------------+
            |
            v
     +--------------+
     | Categorizer  |
     +--------------+
            |
            v
     +--------------+
     |   Planner    |
     +--------------+
            |
            v
     +--------------+
     |   Preview    |
     +--------------+
            |
            v
     +--------------+
     |  Organizer   |
     +--------------+
            |
            v
      Files Organized
```

### Module Responsibilities

**1. Scanner (`scanner.py`)**
- Validates the selected directory.
- Discovers files.
- Collects metadata such as filename, extension, file path, and size.

**2. Categorizer (`categorizer.py`)**
- Identifies file categories based on extensions.
- Groups file metadata into category-wise collections.

**3. Planner (`planner.py`)**
- Generates proposed destination paths.
- Associates each file with its intended category directory.

**4. Preview (`preview.py`)**
- Displays files grouped by category.
- Shows original and proposed destination paths.
- Displays category-wise and total file counts.

**5. Organizer (`organizer.py`)**
- Creates category directories.
- Moves files into their respective destinations.

## 💻 Getting Started

### Prerequisites

- Python 3.10 or later recommended.
- Git.
- Any Python-compatible IDE or code editor.

### Installation

Clone the repository:

```bash
git clone https://github.com/abhishekdasdgp/python-smart-file-organizer.git
```

Navigate to the project directory:

```bash
cd python-smart-file-organizer
```

### Run the Application

Execute the application from the project root:

```bash
python -m src.fileorganizer.main
```

Enter the directory path when prompted:

```text
Enter the location of directory::
D:\Downloads
```

The application will scan, categorize, plan, preview, and organize the files.

## 📸 Example

**Before organization:**

```text
Downloads/
│
├── report.pdf
├── photo.jpg
├── invoice.xlsx
├── presentation.pptx
├── video.mp4
└── notes.txt
```

**After organization:**

```text
Downloads/
│
├── Documents/
│   ├── report.pdf
