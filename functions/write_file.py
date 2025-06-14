import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = abs_working_dir
    if file_path:
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    #print(f"debug\n file_path: {file_path}\n target_file: {target_file}\n abs_working_dir: {abs_working_dir}")

    full_dir = os.path.dirname(target_file)

    try:
        if not os.path.exists(full_dir):
            os.makedirs(full_dir)

        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        print(f"Error: unable to write file {e}")


