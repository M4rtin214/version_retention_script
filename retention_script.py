import os
import sys
from typing import List


def get_directories(path: str) -> List:
    dir_list = []
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            dir_list.append(name)
    return dir_list


def delete_old_versions(path: str, current_version: str, major_count: int, minor_count: int):
    major, minor, patch = [int(part) for part in current_version.split(".")]
    print(f"Actual version: {major}.{minor}.{patch}")

    dirs_of_path = get_directories(path)
    print("Directories: ", dirs_of_path)

    # Split into name and version and add version to version_list
    version_list = []
    preserved_dirs_full_names = []
    app_name = ""
    for name in os.listdir(path):
        try:
            app_name, app_version = [part for part in name.split("_")]
            version_list.append(app_version)
        except ValueError:
            preserved_dirs_full_names.append(name)
            continue
    version_list.sort(reverse=True)

    # Create version dict
    version_dict = {}
    for ver in version_list:
        # Split into minor, major, path
        parts = str(ver).split(".")
        if len(parts) != 3:
            continue
        try:
            dir_major, dir_minor, dir_patch = [int(part) for part in parts]
            if dir_major in version_dict.keys():
                minor_list = version_dict[dir_major]
                minor_list.append(dir_minor)
                version_dict[dir_major] = minor_list
            else:
                minor_list = []
                minor_list.append(dir_minor)
                version_dict[dir_major] = minor_list
        except ValueError:
            continue

    # Selection of versions to be preserved
    preserved_dirs = []
    preserved_major = 0
    for major_version in version_dict.keys():
        preserved_minor = 0
        if major_version <= major:
            if preserved_major < major_count:
                for minor_ver in version_dict[major_version]:
                    if major == major_version and minor < minor_ver:
                        name = f"{app_name}_{major_version}.{minor_ver}"
                        preserved_dirs.append(name)
                    else:
                        if preserved_minor < minor_count:
                            name = f"{app_name}_{major_version}.{minor_ver}"
                            preserved_dirs.append(name)
                            preserved_minor += 1
                preserved_major += 1
        else:
            name = f"{app_name}_{major_version}"
            preserved_dirs.append(name)

    # Preparing the list for deletion
    for full_name in dirs_of_path:
        for partial_name in preserved_dirs:
            if full_name.startswith(partial_name):
                preserved_dirs_full_names.append(full_name)
    dirs_to_delete = list(set(dirs_of_path) - set(preserved_dirs_full_names))

    # Delete directories
    print("Will be deleted: ", dirs_to_delete)
    remove = input("Do you really want to delete these directories? y/n \n")
    if remove == "y":
        for name in os.listdir(path):
            if name in dirs_to_delete:
                os.rmdir(os.path.join(path, name))


if __name__ == "__main__":
    # Check the correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: python script.py PATH CURRENT_VERSION PRESERVE_COUNT PRESERVE_MINOR_COUNT")
        print('Example: python script.py "C:/my_dir" "5.2.3" "2" "3"')
        sys.exit(1)

    # Call the delete_old_versions function with the provided arguments
    delete_old_versions(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
