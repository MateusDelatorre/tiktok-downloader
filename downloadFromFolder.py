import downloadFromFile
import os

# Download all videos from the links folder
def download_folder():
    origin_path = 'links'
    if os.path.isdir(origin_path):
        files = os.listdir(origin_path)
        for file in files:
            path_to_file = origin_path + '/' + file
            down = downloadFromFile.FileDownloader(path_to_file)
            down.download_file()
