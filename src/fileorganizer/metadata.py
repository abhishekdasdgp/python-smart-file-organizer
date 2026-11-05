from dataclasses import dataclass

@dataclass
class FileMetaData:
    name:str
    stem:str
    suffix:str
    parent:str
    size:int
        
        