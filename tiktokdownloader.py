import os
import sys
import yt_dlp
import downloadFromFolder
import downloadFromFile

def __init__():
    if len(sys.argv) == 1:
        downloadFromFolder.download_folder()
        # print("Please provide an argument")
        # print("Usage: python tiktokdownloader.py -file")
        # print("Usage: python tiktokdownloader.py -folder")
        # print("Usage: python tiktokdownloader.py -user")
    for i in sys.argv:
        if i == "-file":
            down = downloadFromFile.FileDownloader('links/links.txt')
            down.download_file()
        elif i == "-folder":
            downloadFromFolder.download_folder()
        elif i == "-user":
            print("user")

__init__()