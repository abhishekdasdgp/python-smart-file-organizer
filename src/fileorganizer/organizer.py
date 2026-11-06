from pathlib import Path

def organizer(fileLocation,parentPath:str):
    for k,v in fileLocation.items():
        location = Path(parentPath) / k
        location.mkdir(parents=True, exist_ok=True)
        for item in v:
            item.source.rename(item.dest)    