import os
import shutil
from collections import defaultdict
import pyfiglet
import ctypes
from pystyle import Colors, Colorate, Center, Write, System


def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)


def display_banner():
    # Generate ASCII art banner
    ascii_banner = pyfiglet.figlet_format("Organizer V2")
    # Apply vertical gradient coloring and center the text
    colored_banner = Colorate.Vertical(Colors.blue_to_cyan, ascii_banner)
    print(Center.XCenter(colored_banner))
    # Additional text with color
    print(Center.XCenter(Colorate.Vertical(Colors.blue_to_cyan, "made by xeni.dev")))
    print(Center.XCenter(Colorate.Vertical(Colors.blue_to_cyan, "dsc.gg/lyxcheats\n")))
    print("")
    print("")


def get_directory():
    # Ask user for the directory to organize
    directory = Write.Input("Enter the directory you want to organize: ", Colors.blue_to_cyan, interval=0.020)
    if not os.path.isdir(directory):
        Write.Print("Invalid directory. Please try again.\n", Colors.blue_to_cyan, interval=0.0)
        return get_directory()
    return directory


def organize_directory(directory):
    # Create folders based on file extensions
    extensions = defaultdict(list)
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            ext = item.split('.')[-1]
            extensions[ext].append(item)

    for ext, files in extensions.items():
        folder_name = f"{ext}_files"
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            shutil.move(os.path.join(directory, file), folder_path)

    return [os.path.join(directory, f"{ext}_files") for ext in extensions]


def move_to_single_folder(folders):
    # Ask user if they want to move all folders to a single folder
    choice = Write.Input("Do you want to put all folders in a single folder? (y/n): ", Colors.blue_to_cyan,
                         interval=0.030)
    if choice.lower() == 'y':
        single_folder_name = Write.Input("Enter the name of the single folder: ", Colors.blue_to_cyan, interval=0.020)
        single_folder_path = os.path.join(os.path.dirname(folders[0]), single_folder_name)
        os.makedirs(single_folder_path, exist_ok=True)
        for folder in folders:
            shutil.move(folder, single_folder_path)


def main():
    System.Clear()
    pc_name = os.getenv('COMPUTERNAME')
    set_console_title(f"♡ BlueWhale ♡ <--> Login: {pc_name} <--> .gg/lyxcheats")
    display_banner()
    directory = get_directory()
    folders = organize_directory(directory)
    move_to_single_folder(folders)
    Write.Print("Directory organized successfully.\n", Colors.blue_to_cyan, interval=0.05)


if __name__ == "__main__":
    main()
