import os

def rename_photos(directory, naming_convention):
    # List all files in the given directory
    files = os.listdir(directory)    
    # Initialize a counter for naming convention
    counter = 0
    skip_count = 0
    # Iterate over all files in the directory
    for filename in files:
        # Split the file name into name and extension
        name, ext = os.path.splitext(filename)
        # Define the new name using the naming convention and counter
        new_name = f"{naming_convention}_{counter}{ext}"        
        # Create the full path for the old and new files
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)        
        # Check if the new file name already exists
        if os.path.exists(new_file):
            skip_count += 1
            continue
        # Rename the file
        os.rename(old_file, new_file)
        # Increment the counter
        counter += 1
    print(f"  ({counter}) Renamed, ({skip_count}) Skipped")

# Usage
directory_path = "G:/wallpaper/lock_screen"  # Replace with the path to your photos
naming_convention = "lock_screen"  # Replace with your desired naming convention
print(f"> Renaming ... ")
rename_photos(directory_path, naming_convention)
print(f"  [Rename Completed]")