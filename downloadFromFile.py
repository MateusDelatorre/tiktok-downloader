import os
from Class.video import Video

class FileDownloader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_video_links(self):
        with open(self.file_path, 'r') as file:
            video_links = file.readlines()
        return video_links

    def normalize_link(self, link):
        if '?is_copy_url=1&is_from_webapp=v1' in link:
            link = link.removesuffix('?is_copy_url=1&is_from_webapp=v1')
        return link
    
    def create_user_folder(self, download_path):
        if not os.path.isdir(download_path):
                os.makedirs(download_path)

    def create_ids_file(self, ids_path):
        if not os.path.exists(ids_path):
            open(ids_path, "x")

    def create_error_file(self):
        if not os.path.exists("error.txt"):
            open("error.txt", "x")

    def check_video_existence(self, id, user_name):
        ids_file = f'{user_name}/_ids'
        if os.path.exists(ids_file) and id in open(ids_file).read():
            return True
        return False

    def write_video_id(self, video_id, user_name):
        ids_file = f'{user_name}/_ids'
        with open(ids_file, 'a') as file:
            file.write(f'{video_id}')

    def write_error(self, video_link):
        ids_file = f'error.txt'
        with open(ids_file, 'a') as file:
            file.write(f'{video_link}\n')

    def download_file(self):
        video_links = self.read_video_links()
        for link in video_links:
            if 'https://www.tiktok.com/@' in link and '/video/' in link:
                link = self.normalize_link(link)
                video = Video(link)
                user_name = video.get_user_name()
                video_id = video.get_video_id()
                ids_path = "./" + user_name + "/_ids"
                download_path = "./" + user_name
                self.create_user_folder(download_path)
                self.create_ids_file(ids_path)
                self.create_error_file()
                if not self.check_video_existence(video_id, user_name):
                    if video.download():
                        self.write_video_id(video_id, user_name)
                    else:
                        self.write_error(link)


class File:
    def __init__(self, path):
        self.path = path
    
    def file_to_list(self):
        f = open(self.path, "r")
        list = f.read().splitlines()
        f.close()
        return list