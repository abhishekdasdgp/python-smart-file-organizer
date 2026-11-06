def preview(file_location):
    print("========== FILE ORGANIZATION PREVIEW ==========")
    category = 0
    files = 0
    for k,v in file_location.items():
        category+=1
        print("\n")
        print(f"{k} ({len(v)} files)")
        print("------------------------------------------------")
        for item in v:
            print(f"{item.filename}")
            print(f"From: {item.source}")
            print(f"To: {item.dest}")  
            files+=1
        print("------------------------------------------------")
    print(f"Total files: {files}")
    print(f"Total categories: {category}")      
            