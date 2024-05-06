from pytube import YouTube
import sys
import tkinter as tk

def downloadYouTube(videourl, name):
    print(f"downloading {videourl}")
    try:
        yt = YouTube(videourl)
    except:
        print("Connection Error") #to handle exception
    audiofiles = yt.streams.filter(only_audio=True)
    d_video = audiofiles[1]
    try:
        d_video.download(output_path="./data", filename=name)
    except Exception as e:
        print(e)

#build GUI
root = tk.Tk()

root.title("Download YouTube Videos")

label tk.Label(self.window, text="Search")
label.pack()
url = tk.StringVar()
url.set("")

entry = tk.Entry(self.window, textvariable=url)
entry.pack()

button = tk.Button(self.window, text="Search", command=search)

def search():
    
