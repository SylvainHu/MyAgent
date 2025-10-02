import os


def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    if not full_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        files_info = []
        for entry in os.listdir(full_path):
            entry_path = os.path.join(full_path, entry)
            file_size = os.path.getsize(entry_path)
            is_dir = os.path.isdir(entry_path)
            files_info.append(f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(files_info)
    except Exception as e:
        return f"Error: {str(e)}"