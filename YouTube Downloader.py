from yt_dlp import YoutubeDL
import tkinter as tk
import os
from yt_dlp import YoutubeDL

directory = './videos/'
if not os.path.exists(directory):
    os.makedirs(directory)

def downloadYouTube(videourl):
    dl_ops = {
      'outtmpl': directory + '%(title)s.%(ext)s',
    }
    print(f"downloading {videourl}")
    try:
        with YoutubeDL(dl_ops) as ydl:
            ydl.download([videourl])
            
    except Exception as e:
        print(e) #to handle exception
    
#build GUI
root = tk.Tk()
root.title("Download YouTube Videos")
root.geometry("400x200")
url = tk.StringVar()
url.set("")

tk.Label(root, text="URL").pack()
entry = tk.Entry(root, textvariable=url)
entry.pack()

messageLabel = tk.Label(root, text="Enter the URL of the video to download")
messageLabel.pack()


def search():
    try:
        messageLabel.config(text=f"Downloading video to the videos folder!")
        entry.update()
        downloadYouTube(url.get())

        messageLabel.config(text=f"Complete! Video downloaded to the videos folder!")
        url.set("")
        entry.update()
    except Exception as e:
        messageLabel.config(text=f"Error: {e}")
        entry.update()

button = tk.Button(root, text="Search", command=search)
button.pack()

root.mainloop()
