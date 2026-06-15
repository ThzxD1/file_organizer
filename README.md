# Automatic File Organizer

Watches a folder and automatically organizes files by extension, date, or name, moving them into configurable subfolders. Great for everyday automation, Python practice, and portfolio.

## How it works
- Watches the `input/` folder
- Moves files into subfolders under `organized/` by extension, date, or name
- Generates automatic logs of every move

## Usage
```bash
git clone https://github.com/ThzxD1/file_organizer.git
cd file_organizer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python organizer.py
```

## Example Configuration (`config.yaml`)
```yaml
watch_folder: input
organize_by: extension     # extension | date | name
destination_folder: organized
extensions_map:
  images: [".jpg", ".jpeg", ".png", ".gif"]
  documents: [".pdf", ".docx", ".txt", ".xlsx"]
  videos: [".mp4", ".avi", ".mov"]
  others: []
```
