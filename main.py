import os


# ask the user for the directory of their minecraft foledr
# give them the option to enter it manually or to use the default
# (the default is the folder that contains the .minecraft folder)


def get_minecraft_folder():
    while True:
        print("Where is your minecraft folder? (default is .minecraft)")
        print("1. Default")
        print("2. Enter manually")

        choice = input("Enter your choice: ")

        if choice == "1":
            path = os.path.join(os.path.expanduser("~"), ".minecraft")
            # print the path to console and ask if it is correct
            # if it is correct, return the path
            # if it is not correct, ask again

            print(f"Your minecraft folder is {path}")
            print("Is this correct?")

            if input("Enter y/n: ") == "y":
                return path

        elif choice == "2":
            return input("Enter the path to your minecraft folder: ")

        else:
            print("Invalid choice")


# git clone https://github.com/j1165-mods/project into the folder with the name "mods"
# (the folder is created if it doesn't exist)

def install_mods(minecraft_folder):
    mods_folder = os.path.join(minecraft_folder, "mods")
    if not os.path.exists(mods_folder):
        os.mkdir(mods_folder)

    os.system(f"cd {mods_folder} && git clone https://github.com/j1165-mods/project")


# run the program
minecraft_folder = get_minecraft_folder()
print(f"Installing mods to {minecraft_folder}")

# Check if the folder exists and is empty
# if it is empty, install the mods

if os.path.exists(minecraft_folder):
    if not os.listdir(minecraft_folder):
        install_mods(minecraft_folder)
    else:
        print("The folder is not empty")
        print("Should we erase the folder? (y/n)")
        if input() == "y":
            os.system(f"rm -rf {minecraft_folder}")
            os.system(f"mkdir {minecraft_folder}")

            print("Folder erased!")

            install_mods(minecraft_folder)
        else:
            print("Exiting")

install_mods(minecraft_folder)
