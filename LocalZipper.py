import os
import zipfile
from datetime import datetime
from collections import defaultdict

def zip_files_in_dir(directory, unityScript, character_order):
    # check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist. Please check the path.")
        return

    # get the current date and time in the specified format
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # zip file name
    zip_file_name = 'script_' + timestamp + '.zip'
    # path to the downloads directory, adjust as needed
    downloads_dir = os.path.expanduser('~/Documents/')
    downloads_dir = os.path.join(downloads_dir, "AI INPUTS\\Scripts")
    # output zip file path
    zip_file_path = os.path.join(downloads_dir, zip_file_name)

    # Create a temporary script.txt file with the contents of unityScript
    with open('script.txt', 'w') as temp_file:
        temp_file.write(unityScript)

    # Create a dictionary to hold character files
    character_files = defaultdict(list)

    # walk the directory
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename != '.gitkeep':  # skip .gitkeep
                # create complete filepath
                file_path = os.path.join(dirpath, filename)
                character = os.path.basename(dirpath)
                character_files[character].append(file_path)

    # Sort each character's file list
    for character in character_files:
        character_files[character].sort()

    # Create a ZipFile object in write mode
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # add script.txt to the zip file
        zip_file.write('script.txt')

        # add files to the zip file, renamed according to character order
        for i, character in enumerate(character_order):
            if character_files[character]:
                file_path = character_files[character].pop(0)
                new_filename = f"{character}_{str(i).zfill(5)}.wav"
                zip_file.write(file_path, new_filename)

    # delete the temporary script.txt file
    os.remove('script.txt')

    print(f'Files from {directory} and script.txt have been zipped and saved to {zip_file_path}')

    # After zipping files, delete all files and directories except for .gitkeep
    for dirpath, dirnames, filenames in os.walk(directory, topdown=False):
        for filename in filenames:
            if filename != ".gitkeep":
                os.remove(os.path.join(dirpath, filename))
        for dirname in dirnames:
            os.rmdir(os.path.join(dirpath, dirname))

    print(f'Files and directories in {directory}, except for .gitkeep, have been deleted.')

# Test the function
# zip_files_in_dir('C:\\Users\\10850K\\Documents\\Tortoise\\mqr 2\\results', 'Your unity script content here', ['Xage', 'Faiz', 'Xage
