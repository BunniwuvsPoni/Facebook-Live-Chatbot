# Function to import modules
def activate_import_modules(modules_folder = "/Modules"):
    # Gets current directory
    import os

    current_directory = os.getcwd()

    updated_directory = str(current_directory).replace("\\","/") + modules_folder

    # Append path to accept modules for import
    import sys

    sys.path.append(updated_directory)