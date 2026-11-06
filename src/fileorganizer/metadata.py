from dataclasses import dataclass

@dataclass
class FileMetaData:
    name:str
    stem:str
    suffix:str
    fullpath:str
    size:int
        
        