# YouTube Playlist Downloader

YouTube Playlist Downloader is a Python-based application that allows users to download all videos from a YouTube playlist in a specified quality. The application provides a graphical user interface (GUI) for easy usage and displays the download progress and downloaded videos.

## Features

- Download all videos from a YouTube playlist with one click.
- Select the desired video quality (Highest, Lowest, 144p, 360p, 720p, 1080p).
- Choose the download path to save the videos.
- Display download progress.
- List downloaded videos in the GUI.

## Prerequisites

- Python 3.x
- `pytube` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/youtube-playlist-downloader.git
    cd youtube-playlist-downloader
    ```

2. **Install the required packages:**

    ```bash
    pip install pytube
    ```

## Usage

1. **Run the application:**

    ```bash
    python enhanced_youtube_playlist_downloader.py
    ```

2. **Enter the playlist URL:**

    - Paste the URL of the YouTube playlist you want to download.

3. **Select the video quality:**

    - Choose the desired quality from the dropdown menu (Highest, Lowest, 144p, 360p, 720p, 1080p).

4. **Choose the download path:**

    - Click the "Browse" button to select the directory where you want to save the videos.

5. **Download the playlist:**

    - Click the "Download Playlist" button to start downloading. The progress will be displayed in the GUI, and the downloaded videos will be listed.

## Code Overview

### GUI Creation

The GUI is created using the `tkinter` library, which provides various widgets such as `Label`, `Entry`, `Button`, `OptionMenu`, `Listbox`, and `Scrollbar` for building the interface.

### Download Functionality

The `pytube` library is used to handle YouTube video downloading. The download process runs in a separate thread to keep the GUI responsive.

### Key Functions

- **on_progress_callback:** Updates the download progress.
- **select_download_path:** Opens a file dialog to select the download directory.
- **download_video:** Downloads an individual video in the specified quality.
- **download_playlist:** Manages the download process for all videos in the playlist.

### Main Script

The main script (`enhanced_youtube_playlist_downloader.py`) combines the GUI creation and download functionality to provide a user-friendly application.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or bug reports.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [pytube](https://github.com/pytube/pytube) - A lightweight, Pythonic, dependency-free library for downloading YouTube videos.
- [tkinter](https://docs.python.org/3/library/tkinter.html) - The standard Python interface to the Tk GUI toolkit.
