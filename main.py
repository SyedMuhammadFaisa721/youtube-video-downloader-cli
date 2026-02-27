import yt_dlp as d
try:
    url = input("Enter the url: ")
    download = d.YoutubeDL().download(url)
except Exception as e:
    print("Some error occured")