import os
from pathlib import Path


DIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.mp3', '.m4a', '.m4b', '.aac', '.wav', '.m3u', '.flac'],
    "VIDEO": ['.mp4', '.mkv', '.3gp', '.avi', '.m2v']
}


def pickDirectory(value):
    for category, suffixes in DIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "MISC"
# print(pickDirectory(".pdf"))

def organizerDir():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(filePath)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizerDir()