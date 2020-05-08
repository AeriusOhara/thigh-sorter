import os
import json

downloadsFolder = "E:/Downloads/"
sortingFolder = "E:/Downloads/SORTED2/"

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
                if fileName.endswith(f'.{files["ext"]}'):
                    # Check if the folder we're about to use exist
                    folderExists(f'{sortingFolder}{files["arg"]}')
                    # Move the file
                    os.replace(f'{downloadsFolder}{fileName}', f'{sortingFolder}{files["arg"]}{fileName}')

                    # debugtext
                    #print(f'Moving \"{downloadsFolder}{fileName}\" \n→ Moved to \"{sortingFolder}{files["arg"]}{fileName}\"' )

def folderExists(path):
    # Check if the folder exists
    if not (os.path.exists(path)):
        # If it doesn't, create it
        os.mkdirs(path)

setup()
sort()