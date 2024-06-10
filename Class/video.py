import yt_dlp

class Video:

    def __init__(self, video_url):
        self.video_url = video_url

    def get_video_info(self):
        try:
            yt_dlp.utils.std_headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            yt_dlp.utils.std_headers['Referer'] = 'https://www.tiktok.com/'
            with yt_dlp.YoutubeDL() as ydl:
                info = ydl.extract_info(self.video_url, download=False)
                print("#######################################################")
                print("#######################################################")
                print(info['uploader'])
                print(info['upload_date'])
                print(info['id'])
                print(info['ext'])
                print(info['uploader'] + "/" + info['upload_date'] + " - " + info['id'] + "." + info['ext'])
                return info['uploader']
        except Exception as e:
            return False

    def download(self):
        try:
            ydl_opts = {
                'outtmpl': "%(uploader)s/%(upload_date)s - %(id)s.%(ext)s",
                'format': '(bv*+ba/b)[vcodec^=h264] / (bv*+ba/b)',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.video_url])
            return True
        except Exception as e:
            print(f'Could not download: {self.video_url.strip()} - {e}')
            return False


    def get_user_name(self):
        pointer = self.video_url.find("@") + 1
        aux = pointer
        fonded = False
        while(not fonded):
            if(self.video_url[aux] == "/"):
                fonded = True
            else:
                aux += 1
        return self.video_url[pointer:aux]

    def get_video_id(self):
        pointer = self.video_url.find("video") + 6
        aux = len(self.video_url)
        return self.video_url[pointer:aux]