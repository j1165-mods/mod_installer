import os

repoUrl = "https://github.com/j1165-mods/project"


# ask the user for the directory of their minecraft folder
# give them the option to enter it manually or to use the default

def get_minecraft_folder():
    while True:
        print("Where is your Minecraft mods folder? (default is .minecraft/mods)")
        print("1. Default")
        print("2. Enter manually")

        choice = input()

        if choice == "1":
            path = os.path.join(os.path.expanduser("~"), ".minecraft/mods")
            # print the path to console and ask if it is correct

            print(f"Your Minecraft mods folder is {path}")
            print("Is this correct?")

            if input("Enter y/n: ") == "y":
                return path

        elif choice == "2":
            return input("Enter the path to your Minecraft mods folder: ")
        else:
            print("Invalid choice")


mcFolder = get_minecraft_folder()


def download_repo():
    print("Downloading repo...")
    print("Sit tight.")
    # download the repo
    os.system(f"git clone {repoUrl}")


def install_repo():

    print("The repo has been downloaded.")
    print("Installing... This shouldn't take long.")

    # copy the files from the repo to the minecraft mods folder
    # move the repo to the mods folder
    os.system(f"mv project {mcFolder}")
    print("Moved repo to mods folder.")

    # copy the contents one level up
    os.system(f"mv {mcFolder}/project/* {mcFolder}")
    os.system(f"rm -r {mcFolder}/project")
    print("Copied contents to mods folder")

    # delete the repo
    os.system("rm -rf project")
    print("Deleted unneeded repo.")

    print("Done!")


def main():
    download_repo()
    install_repo()


main()

