import os

# Define the directory you want to scan (use '.' for the current directory)
TARGET_DIRECTORY = '.'

# Define the exact text replacements you want to make (Case-Sensitive)
REPLACEMENTS = {
    'archlinux': 'horizonos',
    'Arch Linux': 'Horizon OS',
    'Arch': 'Horizon',
    'asahi-installer': 'horizon-installer',
    'Asahi': 'Horizon'
}

# File extensions to skip (to avoid corrupting git files, images, or binaries)
IGNORE_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.ico', '.pyc', '.pdf', '.zip', '.tar', '.gz'
}
IGNORE_DIRS = {
    '.git', '__pycache__', '.pytest_cache', 'build', 'dist'
}

def rename_and_replace_in_files():
    print("🚀 Starting Horizon OS global replacement script...\n")
    
    count_modified_files = 0
    
    for root, dirs, files in os.walk(TARGET_DIRECTORY, topdown=True):
        # Skip hidden/system metadata directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            # Skip binary and image files
            _, ext = os.path.splitext(file)
            if ext.lower() in IGNORE_EXTENSIONS:
                continue
                
            file_path = os.path.join(root, file)
            
            try:
                # Read the file content safely using UTF-8
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Check if any target keywords exist in the file content
                modified = False
                for target, replacement in REPLACEMENTS.items():
                    if target in content:
                        content = content.replace(target, replacement)
                        modified = True
                
                # If changes were made, overwrite the file
                if modified:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(file_path)
                    count_modified_files += 1
                    
            except Exception as e:
                print(f"❌ Error processing {file_path}: {e}")

    print(f"\n✅ Done! Modified text inside {count_modified_files} files.")

if __name__ == "__main__":
    rename_and_replace_in_files()
