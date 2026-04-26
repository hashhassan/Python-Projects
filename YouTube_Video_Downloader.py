import tkinter as tk
from tkinter import messagebox, filedialog
from pytubefix import YouTube

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube video URL.")
        return
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()

        if stream:
            download_path = filedialog.askdirectory()
            if not download_path:
                messagebox.showwarning("Warning", "Download cancelled. No directory selected.")
                return

            messagebox.showinfo("Downloading", f"Downloading '{yt.title}' to {download_path}...")
            stream.download(output_path=download_path)
            messagebox.showinfo("Success", f"Video '{yt.title}' downloaded successfully!")
        else:
            messagebox.showerror("Error", "No suitable stream found for this video.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Project-YouTube Video Downloader")
root.geometry("500x300")

url_label = tk.Label(root, text="YouTube Video Downloader:",font='arial 15 bold')
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(root, text="Download Video",  font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2,command=download_video)
download_button.pack(pady=20)

root.mainloop()