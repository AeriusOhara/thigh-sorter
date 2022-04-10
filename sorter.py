import os
import json

downloadsFolder = "E:/Downloads/"
sortingFolder = "E:/Downloads/SORTED/"

def setup():
    folderExists(downloadsFolder)
    folderExists(sortingFolder)

def sort():
    with open("sortingRules.json") as jsonList:
        data = json.load(jsonList)

    # Process each category one by one
    for category in data.values():
        for files in category:
            # Iterate over the items in the category
            for fileName in os.listdir(downloadsFolder):
                # If the file extension of the file matches
                if fileName.lower().endswith(f'.{files["ext"]}'):
                    # Check what action we'll be taking
                    for actions in files["act"]:
                        if actions[0] == "ren_ext":
                            # Split filename and extension
                            fileNameOnly, fileExtension = os.path.splitext(fileName)

                            # Rename the extension
                            oldFileName = f'{fileName}'
                            fileName = f'{fileNameOnly}.{actions[1]}'

                            os.rename(f'{downloadsFolder}{oldFileName}', f'{downloadsFolder}{fileName}')
                        elif actions[0] == "mov":
                            # Check if the folder we're about to use exist
                            folderExists(f'{sortingFolder}{actions[1]}')

                            # Move the file
                            os.replace(f'{downloadsFolder}{fileName}', f'{sortingFolder}{actions[1]}{fileName}')


def folderExists(path):
    # Check if the folder exists
    if not (os.path.exists(path)):
        # If it doesn't, create it
        os.makedirs(path)

setup()
sort()