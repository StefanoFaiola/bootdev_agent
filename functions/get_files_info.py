import os

def get_files_info(working_directory, directory="."):
    wd_abs = (os.path.abspath(working_directory))
    target_dir = os.path.normpath(os.path.join(wd_abs, directory))

    # Will be True or False
    valid_target_dir = os.path.commonpath([wd_abs, target_dir]) == wd_abs

    if not valid_target_dir:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return

    if not os.path.isdir(target_dir):
        print(f'Error: "{directory}" is not a directory')
        return
    

    if directory == ".":
        directory = "current"
        print(f"Result for {directory} directory:")
    else:
        print(f"Result for {directory} directory:")

    for dir in os.listdir(target_dir):
        is_dir = os.path.isdir(os.path.join(target_dir,dir))
        filesize = os.path.getsize(os.path.join(target_dir,dir))
        print(f"- {dir}: file_size={filesize}, is_dir={is_dir}")
