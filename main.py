import yt_dlp as d
try:
    url = input("Enter the url: ")
    print("1. Download Youtube Video\n2. Download only Audio\n3. video info without Downloading")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        formate = {
            "format":"bestvideo+bestaudio/best",
            "no_warnings": True,
        }
        with d.YoutubeDL(formate) as ydl:
            ydl.download([url])
    elif choice == 2:
        formate = {
            "format":"bestaudio/best",
            "no_warnings": True,
        }
        with d.YoutubeDL(formate) as ydl:
            ydl.download([url])
    elif choice == 3:
        print("Getting Information Please wait.......")
        formate = {
            "no_warnings": True,
            "quiet": True,
        }
        with d.YoutubeDL(formate) as ydl:
            info = ydl.extract_info(url, download=False)

            print("Title:",info["title"],"\nTime:",info["duration"],"Sec","\nDescription:",info["description"])
except Exception as e:
    print("Some error occured")
