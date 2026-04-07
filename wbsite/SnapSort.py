import os
import shutil

def organize_folder(target_path):
    # 1. Define the categories and their associated extensions
    extension_map = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
        'Archives': ['.zip', '.tar', '.rar', '.7z'],
        'Audio': ['.mp3', '.wav', '.flac', '.m4a'],
        'Video': ['.mp4', '.mov', '.avi', '.mkv'],
        'Installers': ['.exe', '.msi', '.dmg'],
        'Code': ['.py', '.js', '.html', '.css', '.cpp']
    }

    # 2. Change to the target directory
    if not os.path.exists(target_path):
        print("Path does not exist!")
        return

    os.chdir(target_path)

    # 3. Iterate over files
    for file in os.listdir():
        # Skip folders, we only want files
        if os.path.isdir(file):
            continue

        # Get file extension in lowercase
        name, ext = os.path.splitext(file)
        ext = ext.lower()

        # 4. Find the right folder for the extension
        moved = False
        for folder_name, extensions in extension_map.items():
            if ext in extensions:
                # Create folder if it doesn't exist
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                
                # Move the file
                shutil.move(file, os.path.join(folder_name, file))
                print(f"Moved: {file} -> {folder_name}")
                moved = True
                break
        
        # Optional: Move unknown files to an 'Others' folder
        if not moved and ext != '':
            if not os.path.exists('Others'):
                os.makedirs('Others')
            shutil.move(file, os.path.join('Others', file))
            print(f"Moved: {file} -> Others")

if __name__ == "__main__":
    # Replace this with the path to your messy folder (e.g., 'C:/Users/Name/Downloads')
    path_to_clean = input("Enter the full path of the folder to organize: ")
    organize_folder(path_to_clean)
    print("Organization complete!")