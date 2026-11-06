from src.fileorganizer.categorizer import *
from src.fileorganizer.planner import *
from src.fileorganizer.preview import *
from src.fileorganizer.organizer import *
from pathlib import Path

def main():
    location = input("Enter the location of directory:: ")
    file_map = categoriser(location)
    location_metadata = planner(file_map,location)
    preview(location_metadata)
    locationpath = Path(location)
    organizer(location_metadata,locationpath)
        
if __name__ == "__main__":
    main()    