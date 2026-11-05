import os
from pathlib import Path
from metadata import *

def cleanFilePath(filePath):
    stripedFilePath = filePath.strip()
    rawFilePath = rf"{stripedFilePath}"
    return rawFilePath

def scanFolder(filePath):
    filePath = cleanFilePath(filePath)
    file_set = list()
    print(f"File Path:: {filePath}")
    
    if not directory.exists():
        raise FileNotFoundError(
            f"Directory does not exist: {filePath}"
        )

    if not directory.is_dir():
        raise NotADirectoryError(
            f"Provided path is not a directory: {filePath}"
        )
        
    try:
        for path in Path(filePath).iterdir():
                if path.is_dir():
                    pass
                else:
                    metadata = FileMetaData(path.name,path.stem,path.suffix,path.parent,path.stat().st_size)
                    file_set.append(metadata)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The system could not find the path: {filePath}")   
    
    return file_set            