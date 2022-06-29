import sys
import os

files = []
folders = {}
movedFiles = []
path = sys.argv[1]
dirList = os.listdir(path)

for dir in dirList:
  if os.path.isdir(path+os.sep+dir):
    try:
        foldersFromKey = folders[dir[0].lower()]
        foldersFromKey.append(dir)
    except:
        print(f'Key not found: {dir[0].lower()}. Adding it to map')
        folders[dir[0].lower()] = [dir]
  else:
    files.append(dir)

for file in files:
    print(file)
    matchedFolders = []
    prefixName = file.split("-")[0].strip()
    try:
        for folder in folders[prefixName[0].lower()]:
            if prefixName.lower() == folder.lower():
                destFilePath = path+os.sep+folder+os.sep+file
                print("Moving file to: ", destFilePath)
                try:
                    os.rename(path+os.sep+file, destFilePath )
                    movedFiles.append(destFilePath)
                except Exception as ex:
                    print("Failure moving file: ", ex)
            else:
                if len(folder) > 2 and (prefixName[:3].lower() == folder[:3].lower()):
                    matchedFolders.append(folder)

        if len(matchedFolders) > 0:
            print("============FOLDERS================")
            print(matchedFolders)
            print("===================================")
    except Exception as e:
        print('Fail to handle file: ', e)

print(f'Moved Files ({len(movedFiles)}): {movedFiles})')
   
# for root, dirs, files in os.walk(path):
#     for name in files:
#         print("{0} ",name)
