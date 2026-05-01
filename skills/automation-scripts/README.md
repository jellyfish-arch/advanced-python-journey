# 🚀 Automation Scripts

This directory contains a collection of Python scripts designed to automate repetitive tasks, improve productivity, and monitor system resources.

## 🛠️ Scripts Included

| Script | Description | Key Modules |
| :--- | :--- | :--- |
| **[01_file_organizer.py](./01_file_organizer.py)** | Automatically sorts files in a directory into folders based on their extensions (Images, Docs, etc.). | `os`, `shutil`, `pathlib` |
| **[02_bulk_rename.py](./02_bulk_rename.py)** | Batch rename files with custom prefixes, suffixes, or text replacement. | `os`, `pathlib` |
| **[03_web_scraper.py](./03_web_scraper.py)** | A template for scraping headlines and data from websites. | `requests`, `bs4` |
| **[04_system_monitor.py](./04_system_monitor.py)** | Real-time monitoring of CPU, Memory, and Disk usage with a clean console interface. | `psutil`, `platform` |

## 📦 Requirements

To run all scripts, install the necessary dependencies:

```bash
pip install requests beautifulsoup4 psutil
```

## 📖 Usage

1. Clone the repository.
2. Navigate to this directory.
3. Run any script using:
   ```bash
   python <script_name>.py
   ```