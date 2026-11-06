from dataclasses import dataclass

@dataclass
class FileMetaData:
    filename: str
    source: str
    dest: str