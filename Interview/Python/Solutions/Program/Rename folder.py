import os
import re

# Specify the path to the directory containing the folders
base_path = '/path/to/your/directory'  # Replace with your actual path

# Iterate through all items in the directory
for folder_name in os.listdir(base_path):
    # Match folders named 'Program' followed by a number (e.g., 'Program1')
    match = re.match(r'^Program(\d+)$', folder_name)
    if match:
        number = match.group(1)
        new_folder_name = f'Program {number}'
        old_folder_path = os.path.join(base_path, folder_name)
        new_folder_path = os.path.join(base_path, new_folder_name)
        try:
            os.rename(old_folder_path, new_folder_path)
            print(f'Renamed: {folder_name} → {new_folder_name}')
        except Exception as e:
            print(f'Error renaming {folder_name}: {e}')
# Print a message indicating that the renaming process is complete
print('Renaming process complete.')