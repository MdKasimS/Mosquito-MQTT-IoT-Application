import os
import sys


def WelcomeNote():
    clearScreen()
    print(" " * 7 + "Network Admin Console")
    print("________<Manage Subcribers>_______")


def clearScreen():
    try:
        # Determine the operating system
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix-like (Linux, macOS)
            os.system('clear')
    except Exception as e:
        print(f"Failed to clear the console: {e}")


def Exit():
    sys.exit(0)


def reloadScript(script_file):
    try:
        # Read the script's content
        with open(script_file, 'r') as file:
            script_content = file.read()

        # Execute the script's content
        exec(script_content, globals())
    except Exception as e:
        print(f"Failed to reload the script: {e}")
