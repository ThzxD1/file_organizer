import os
import shutil
import yaml
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- Configuração de logging ---
logging.basicConfig(
    filename='logs/organizer.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# --- Carregar configuração ---
def load_config(path='config.yaml'):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

config = load_config()
WATCH_FOLDER = config['watch_folder']
DEST_FOLDER = config['destination_folder']
ORGANIZE_BY = config.get('organize_by', 'extension')
EXTENSIONS_MAP = config.get('extensions_map', {})

os.makedirs(WATCH_FOLDER, exist_ok=True)
os.makedirs(DEST_FOLDER, exist_ok=True)

def get_category_by_extension(ext):
    for cat, exts in EXTENSIONS_MAP.items():
        if ext.lower() in exts:
            return cat
    return 'others'

def organize_file(file_path):
    filename = os.path.basename(file_path)
    ext = os.path.splitext(filename)[1]
    if ORGANIZE_BY == 'extension':
        category = get_category_by_extension(ext)
        dest_dir = os.path.join(DEST_FOLDER, category)
    elif ORGANIZE_BY == 'date':
        date_str = str(os.path.getmtime(file_path)).split(' ')[0]
        dest_dir = os.path.join(DEST_FOLDER, date_str)
    else:
        dest_dir = DEST_FOLDER
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, filename)
    shutil.move(file_path, dest_path)
    logging.info(f"Arquivo {filename} movido para {dest_path}")

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        organize_file(event.src_path)

if __name__ == "__main__":
    print(f"Monitorando a pasta: {WATCH_FOLDER}")
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
