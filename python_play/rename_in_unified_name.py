import os

# Define the root directory where your project is located
root_dir = 'directory0'
print(f'directory found...')

# Walk through all subdirectories in the root directory
for foldername, subfolders, filenames in os.walk(root_dir):
    for filename in filenames:
        # Check if the file has an .md extension
        if filename.endswith('.md'):
            # Get the full path of the current .md file
            old_file_path = os.path.join(foldername, filename)
            # Define the new file name as 'main.md'
            new_file_path = os.path.join(foldername, 'main.md')
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {old_file_path} to {new_file_path}")
print(f'finished')