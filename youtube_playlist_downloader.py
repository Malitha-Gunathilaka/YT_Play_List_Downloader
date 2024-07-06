import os
import threading
from pytube import Playlist, YouTube
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox, StringVar, OptionMenu, Listbox, Scrollbar, END, Frame, W, E

def on_progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress_label.config(text=f"Download progress: {percentage_of_completion:.2f}%")
    app.update_idletasks()

def select_download_path():
    selected_path = filedialog.askdirectory()
    if selected_path:
        download_path_var.set(selected_path)

def download_video(video, save_path, selected_quality):
    yt = YouTube(video, on_progress_callback=on_progress_callback)
    if selected_quality == "Highest":
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    elif selected_quality == "Lowest":
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first()
    else:
        stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution=selected_quality).first()
    
    if stream:
        stream.download(output_path=save_path)
        downloaded_videos_list.insert(END, f"Downloaded: {yt.title}")

def download_playlist():
    playlist_url = url_entry.get()
    save_path = download_path_var.get()
    
    if not playlist_url or not save_path:
        messagebox.showerror("Error", "Please provide both playlist URL and download path.")
        return

    selected_quality = quality_var.get()
    if selected_quality == "Select Quality":
        messagebox.showerror("Error", "Please select a download quality.")
        return

    def start_download():
        try:
            playlist = Playlist(playlist_url)
            messagebox.showinfo("Info", f"Downloading {len(playlist.video_urls)} videos...")

            for video_url in playlist.video_urls:
                download_video(video_url, save_path, selected_quality)
            
            messagebox.showinfo("Info", "Download completed!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    threading.Thread(target=start_download).start()

# Create the GUI application
app = Tk()
app.title("YouTube Playlist Downloader")

# Style configurations
app.configure(bg='#f0f0f0')

# Frame for input fields
frame = Frame(app, bg='#f0f0f0')
frame.pack(pady=20, padx=20)

# URL Label and Entry
url_label = Label(frame, text="Playlist URL:", bg='#f0f0f0')
url_label.grid(row=0, column=0, sticky=W, pady=5)

url_entry = Entry(frame, width=50)
url_entry.grid(row=0, column=1, pady=5)

# Quality Selection
quality_label = Label(frame, text="Select Quality:", bg='#f0f0f0')
quality_label.grid(row=1, column=0, sticky=W, pady=5)

quality_var = StringVar(app)
quality_var.set("Select Quality")  # default value

quality_options = ["Highest", "Lowest", "144p", "360p", "720p", "1080p"]
quality_menu = OptionMenu(frame, quality_var, *quality_options)
quality_menu.grid(row=1, column=1, pady=5, sticky=W+E)

# Download Path
download_path_label = Label(frame, text="Download Path:", bg='#f0f0f0')
download_path_label.grid(row=2, column=0, sticky=W, pady=5)

download_path_var = StringVar()
download_path_entry = Entry(frame, textvariable=download_path_var, width=50, state='readonly')
download_path_entry.grid(row=2, column=1, pady=5)

browse_button = Button(frame, text="Browse", command=select_download_path)
browse_button.grid(row=2, column=2, padx=5)

# Download Button
download_button = Button(app, text="Download Playlist", command=download_playlist, bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'))
download_button.pack(pady=10)

# Progress Label
progress_label = Label(app, text="Download progress: 0%", bg='#f0f0f0')
progress_label.pack(pady=10)

# Downloaded Videos List
downloaded_videos_list = Listbox(app, width=70, height=10)
downloaded_videos_list.pack(pady=10)

# Add Scrollbar to Listbox
scrollbar = Scrollbar(app, orient="vertical")
scrollbar.config(command=downloaded_videos_list.yview)
scrollbar.pack(side="right", fill="y")
downloaded_videos_list.config(yscrollcommand=scrollbar.set)

app.mainloop()
