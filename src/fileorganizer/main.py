from src.fileorganizer.categorizer import *
from src.fileorganizer.planner import *
from src.fileorganizer.organizer import *

def main():
    location = input("Enter the location of directory:: ")
    file_map = categoriser(location)
    location_metadata = planner(file_map,location)
    