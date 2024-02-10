from pytube import YouTube

def video_indir(url, path):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(path)
        print(f"'{yt.title}' başarıyla indirildi.")
    except Exception as e:
        print("Bir hata oluştu:", e)

if __name__ == "__main__":
    VIDEO_URL = input("İndirmek istediğiniz YouTube videosunun URL'sini girin: ")
    KAYIT_YOLU = input("Videonun kaydedileceği klasör yolunu girin: ")
    video_indir(VIDEO_URL, KAYIT_YOLU)
