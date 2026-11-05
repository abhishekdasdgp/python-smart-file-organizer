FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods"],
    "Presentations": [".ppt", ".pptx", ".odp"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".apk", ".bat"],
    "Code": [".py", ".java", ".js", ".html", ".css", ".json", ".xml", ".sql"]
}

def getMapping(extension):
    category = None
    if extension in (None,""):
        return "Others"
    for k,v in FILE_CATEGORIES.items():
        for item in v:
            if extension.upper() == item.upper():
                return k                
    if category == None:
        return "Others" 