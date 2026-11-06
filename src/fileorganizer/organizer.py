from pathlib import Path
import shutil

def organizer(fileLocation,parentPath:str):
   for category, files in fileLocation.items():
        location = Path(parentPath) / category
        location.mkdir(parents=True, exist_ok=True)

        for item in files:
            destination = location / item.filename
            shutil.move(str(item.source), str(destination))
