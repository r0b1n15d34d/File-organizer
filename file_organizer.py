from pathlib import Path
import shutil 

SOURCE_DIR = Path(__file__).parent


FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".tif", ".ico", ".heic", ".raw"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".odt", ".ods", ".odp", ".rtf", ".csv", ".md"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".opus", ".aiff"],
    "Video": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm", ".m4v", ".3gp", ".mpeg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz", ".tar.gz", ".tar.bz2"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh", ".ts", ".jsx", ".tsx", ".php", ".rb", ".go", ".rs", ".cpp", ".c", ".java"],
    "Software": [".exe", ".dmg", ".pkg", ".iso", ".msi", ".deb", ".rpm", ".appimage"],
    "Ebooks": [".epub", ".mobi", ".azw", ".azw3"],
    "Database": [".sql", ".db", ".sqlite", ".json", ".xml", ".yaml", ".yml"],
    "3D": [".stl", ".obj", ".fbx", ".blend", ".gltf", ".glb"],
    "Torrents": [".torrent"]
}

def get_unique_path(file, destination):
    if not destination.exists():
        return destination
    else:
        counter = 2
        unique_path = destination.parent / f"{file.stem} ({counter}){file.suffix}"
        while unique_path.exists():
            counter += 1
            unique_path = destination.parent / f"{file.stem} ({counter}){file.suffix}"
        
    return unique_path
            

for file in SOURCE_DIR.iterdir():
    if not file.is_file() or file.name == "file_organizer.py":
        continue    
    moved = False

    for category, extension in FILE_TYPES.items():
        if file.suffix.lower() in extension:
            extension_name = file.suffix.lower().lstrip(".")
            target_folder = SOURCE_DIR / category / extension_name
            target_folder.mkdir(parents=True, exist_ok=True) 
            safe_path = get_unique_path(file, target_folder / file.name)

            try:
                shutil.move(str(file), str(safe_path))
                print(f"{file.name} moved to {category}/{extension_name}/")
                moved = True
                break

            except Exception as e:
                with open(SOURCE_DIR / "log.txt", "a") as log:
                    log.write(F"{e} error in {file.name}")

    if not moved:
        others_folder = SOURCE_DIR / "Others"
        others_folder.mkdir(exist_ok=True)
        safe_path = get_unique_path(file, others_folder / file.name)

        try:
            shutil.move(str(file), str(safe_path))
            print(f"{file.name} moved to Others/")

        except Exception as e:
            with open(SOURCE_DIR / "log.txt", "a") as log:
                log.write(f"{e} error in {file.name}")





