from dataclasses import dataclass
from pathlib import Path

@dataclass
class FileMetaData:
    filename: str
    source: Path
    dest: Path