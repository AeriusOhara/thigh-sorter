import os
import json
from datetime import datetime

downloadsFolder = "E:/Downloads/"
sortingFolder = "E:/Downloads/SORTED/"

def setup():
	folderExists(downloadsFolder)
	folderExists(sortingFolder)

def sort():
	with open("sortingRules.json") as jsonList:
		data = json.load(jsonList)

	# Change working directory to where we're processing files
	os.chdir(downloadsFolder)

	for category in data.values():
		for files in category:
			for fileName in os.listdir(downloadsFolder):
				if fileName.lower().endswith(f'.{files["ext"]}'):
					# Process actions
					for action in files["act"]:
						# Use timestamp in filename to avoid replacing common
						# filenames. Example: Discord's 'unknown.png/jpg'
						timestamp = int(datetime.timestamp(datetime.now()))
						fileNameOnly, fileExtension = os.path.splitext(fileName)

						if action[0] == "ren_ext":
							prevFileName = f'{fileName}'
							fileExtension = action[1]
							fileName = f'{fileNameOnly}.{fileExtension}'

							os.rename(prevFileName, fileName)
						elif action[0] == "mov":
							sortedFileName = f'{fileNameOnly}_{timestamp}{fileExtension}'

							folderExists(f'{sortingFolder}{action[1]}')
							os.replace(fileName, f'{sortingFolder}{action[1]}{sortedFileName}')

def folderExists(path):
	# Create the folder if it doesn't exist
	if not (os.path.exists(path)):
		os.makedirs(path)

setup()
sort()