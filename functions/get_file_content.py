import os

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_path):
        return f'Error: "{file_path}" is not a directory'