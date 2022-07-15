import sys
import os


def move_to_folder_by_name(path): 
    root_folder_listing = list_dir(path)
    files = []
    folders = {}
    moved_files = []
    for item_from_root in root_folder_listing:
        populate_files_list_folders_dictionary(path, files, folders, item_from_root)
        find_moving_possibilites(path, files, folders, moved_files)
    
    print(f'Moved Files ({len(moved_files)}): {moved_files})')

def list_dir(path):
    root_folder_listing = os.listdir(path)
    return root_folder_listing

def find_moving_possibilites(path, files, folders, moved_files):
    for file in files:
        print(file)
        prefix_name = prefix(file)
        try:
             move_files_when_matched(path, folders, moved_files, file, prefix_name)
        except Exception as e:
            print(f'Fail to handle file: {type(e).__name__}, {e.args}')

def prefix(file):
    return file.split("-")[0].strip()

def move_files_when_matched(path, folders, moved_files, file, prefix_name):
    matched_folders = []
    for folder in folders[prefix_name[0].lower()]:
        if prefix_name.lower() == folder.lower():
            dest_file_path = path+os.sep+folder+os.sep+file
            print("Moving file to: ", dest_file_path)
            try:
                os.rename(path+os.sep+file, dest_file_path )
                moved_files.append(dest_file_path)
            except Exception as ex:
                print("Failure moving file: ", ex)
        else:
            if len(folder) > 2 and (prefix_name[:3].lower() == folder[:3].lower()):
                matched_folders.append(folder)

    if len(matched_folders) > 0:
        print("============FOLDERS================")
        print(matched_folders)
        print("===================================")

def populate_files_list_folders_dictionary(path, files, folders, item_from_root):
    
    if os.path.isdir(path + os.sep + item_from_root):
        first_letter_name = item_from_root[0].lower()
        try:
            folders_from_key = folders[first_letter_name]
            folders_from_key.append(item_from_root)
        except KeyError:
            folders[first_letter_name] = [item_from_root]
    else:
        files.append(item_from_root)

def ecletic_separation(path):
    count_per_prefix = {}
    moved_files = []
    for file in list_dir(path): 
        count = 1
        
        if prefix(file) in count_per_prefix:
            count = count_per_prefix[prefix(file)] + 1 
            count_per_prefix[prefix(file)] = count
        else:
            count_per_prefix[prefix(file)] = count
        
        origin = f'{path}{os.sep}{file}'
        destination_dir = f'{path}{os.sep}ecletic{count}'
        dest_file_path = f'{destination_dir}{os.sep}{file}'

        print(f'irá mover: {origin} para {dest_file_path}')
        os.makedirs(destination_dir, exist_ok=True)
        os.rename(origin, dest_file_path)
        moved_files.append(dest_file_path)

    print(f'Moved Files[{len(moved_files)}]: {moved_files}')

def main():
    path = sys.argv[1]
    if len(sys.argv) >= 3:
        print(f'ecletic sepatation {sys.argv}')
        ecletic_separation(path)
    else:
        move_to_folder_by_name(path)
#
# The Main method call
#
main()

#  
# for root, dirs, files in os.walk(path):
#     for name in files:
#         print("{0} ",name)
#
