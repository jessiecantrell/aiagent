import os

def get_files_info(working_directory, directory=None):
    if directory not in os.listdir(working_directory) and directory != '.' and os.path.isdir(directory):
        return f"Error: Cannot list {directory} as it is outside the permitted working directory"
    elif not os.path.isdir(os.path.join(working_directory, directory)):
        return f"Error: {directory} is not a directory"
    elif directory == '.':
        directory = os.path.abspath(working_directory)
    else:
        directory = os.path.join(os.path.abspath(working_directory), directory)
    
    print(directory)

    if not os.path.isdir(directory):
        return f"Error: {directory} is not a directory"


