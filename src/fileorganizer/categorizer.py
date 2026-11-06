from src.fileorganizer.scanner import *
from config.filetypes import *

FILE_MAP = {
    "Documents": [],
    "Spreadsheets": [],
    "Presentations": [],
    "Images": [],
    "Videos": [],
    "Audio": [],
    "Archives": [],
    "Executables": [],
    "Code": [],
    "Others": []
}

def categoriser(filePath):
    fileList = scanFolder(filePath)
    for file in fileList:
        category = getMapping(file.suffix)
        FILE_MAP[category].append(file)
    return FILE_MAP            