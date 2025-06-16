import os

def get_files_info(working_directory, directory=None):
    #check to make sure the directory is in the working directory and is a real directory
    if directory not in os.listdir(working_directory) and directory != '.' and os.path.isdir(directory):
        return f"Error: Cannot list {directory} as it is outside the permitted working directory"
    #if it's not a real directory
    elif not os.path.isdir(os.path.join(working_directory, directory)):
        return f"Error: {directory} is not a directory"
    #if the directory is a ., set it to the same as the working directory's absolute path
    elif directory == '.':
        directory = os.path.abspath(working_directory)
    #set directory as it's absolute path
    else:
        directory = os.path.join(os.path.abspath(working_directory), directory)
    
    file_list = os.listdir(directory) #gets a list of the files in that path
    
    try:
        files = ""

        for file in file_list: 
            file_size = os.path.getsize(os.path.join(directory, file))
            is_dir = os.path.isdir(os.path.join(directory, file))
            files += f"- {file}: file_size={file_size} bytes, is_dir={is_dir}\n"
    
        return files
    except Exception as e:
        return f"Error listing files: {e}"

