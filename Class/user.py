import yt_dlp

class User:

    user_videos = list(())

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.user_videos = list(())

    @property
    def user_videos(self):
        return self.user_videos
    
    @user_videos.setter
    def user_videos(self, user_videos):
        self.user_videos = user_videos

    def get_user_videos(self):
        videos_id = list({})
        info = yt_dlp.YoutubeDL().extract_info(URL, download=False)
        info_s = yt_dlp.YoutubeDL().sanitize_info(info)
        entries = info_s["entries"]
        for item in entries:
            video_info = {'id': item['id'], 'upload_date': item['upload_date']}
            videos_id.append(video_info)
        return videos_id