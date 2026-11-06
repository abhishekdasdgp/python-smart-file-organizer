from src.fileorganizer.categorizer import *
from config.filemetadata import *
from dataclasses import dataclass

def planner(fileMap,filepath):
    file_location_metadata = {}
    parentPath = Path(filepath).parent
    for k,v in fileMap.items(): 
        file_location_metadata[k] = list()
        for item in v:
           k1 = FileMetaData(item.absolute(),parentPath / k /item.name)
           file_location_metadata[k].append(k1)
    
    return file_location_metadata     