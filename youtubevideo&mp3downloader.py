from pytube import YouTube
import time
import os

while True:
    print("Welcome to Frasha Santo Youtube Video Downloader")
    url = input("Enter video url? ")
   
    try: 
        #initializing a new Youtube object
        
        YT = YouTube(url)
        #prompting User to choose either mp3 or Mp4 format
        download_type = input("Choose either to download mp4 or mp3? ").lower()
         #below code is download video on MP3 format
        if download_type == 'mp4': 
            
            mp4_download = YT.streams.filter(progressive=True, file_extension='mp4').get_by_itag(22) #get_by_itag(22) represents 720P
            print("Downloading.....")
            time.sleep(1)
            print("Please wait")
            mp4_download.download(output_path=f"{os.environ['UserProfile']}/Downloads")
            print(YT.title + "succesfully downloaded, check your Downloads folder")
          #below code is download video on MP3 format  
        elif download_type == 'mp3':
            mp3_download = YT.streams.filter(only_audio=True).first()
            print("Please wait..")
            print("Downloading...........")
            time.sleep(1) 
            mp3_download.download(output_path=f"{os.environ['UserProfile']}/Downloads")
            print(YT.title + "succesfully downloaded, check your Downloads folder")
        
        else:
            print("Choose your preferred file format")
            continue
        
    except:
        print("Some error occured. Check your internet connection")
        
    
    quitapp = input("To download another video press (Y) for Yes (q) to quit the app? ").lower()
    if quitapp == "y":
        os.system('cls')
        continue
    if quitapp == 'q':
        print("Goodbye!😍 Thanks for using the application")
        quit()





