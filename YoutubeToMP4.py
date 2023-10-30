import os
from pytube import YouTube
import tkinter as tk
from tkinter import ttk, filedialog

def download_video():
    url = url_entry.get()
    download_path = download_path_var.get()
    custom_filename = filename_entry.get()
    
    youtube = YouTube(url)
    video = youtube.streams.filter(file_extension='mp4', progressive=True, res='720p').first()
    
    if custom_filename:
        video.download(download_path, filename=custom_filename)
    else:
        video.download(download_path)
    
    result_label.config(text="Download complete!")

def browse_directory():
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        download_path_var.set(selected_directory)

# Create a better-looking GUI using ttk widgets
window = tk.Tk()
window.title("YouTube Video Downloader")

style = ttk.Style()
style.configure("TButton", padding=(10, 5))
style.configure("TLabel", padding=(0, 5))

url_label = ttk.Label(window, text="Enter YouTube URL:")
url_label.grid(row=0, column=0, padx=10, pady=5)

url_entry = ttk.Entry(window, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=5)

filename_label = ttk.Label(window, text="Custom Filename (optional):")
filename_label.grid(row=1, column=0, padx=10, pady=5)

filename_entry = ttk.Entry(window, width=50)
filename_entry.grid(row=1, column=1, padx=10, pady=5)

download_path_var = tk.StringVar()
download_path_var.set(os.getcwd())

download_path_label = ttk.Label(window, text="Download Location:")
download_path_label.grid(row=2, column=0, padx=10, pady=5)

download_path_entry = ttk.Entry(window, textvariable=download_path_var, width=40)
download_path_entry.grid(row=2, column=1, padx=10, pady=5)

browse_button = ttk.Button(window, text="Browse", command=browse_directory)
browse_button.grid(row=2, column=2, padx=10, pady=5)

download_button = ttk.Button(window, text="Download", command=download_video)
download_button.grid(row=3, column=1, padx=10, pady=10)

result_label = ttk.Label(window, text="")
result_label.grid(row=4, column=1, padx=10, pady=5)

window.mainloop()
