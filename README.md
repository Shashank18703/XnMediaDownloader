# XnMediaDownloader

XnMediaDownloader is a simple Python application built using the Streamlit framework that allows users to easily download videos from YouTube and Instagram. The application provides a user-friendly interface for inputting video URLs and choosing the desired resolution (for YouTube videos) before initiating the download process. It supports video downloads in various resolutions and stores the downloaded videos in user-specified output paths.

## Features

- Download videos from both YouTube and Instagram.
- Choose from different resolutions for YouTube videos.
- Specify the output path for downloaded videos.
- Real-time feedback on the download progress.

## Prerequisites

Before using XnMediaDownloader, ensure you have the following dependencies installed:

- Python 3.x
- [Streamlit](https://streamlit.io/)
- [pytube](https://pytube.io/)
- [instaloader](https://instaloader.github.io/)

You can install the necessary dependencies using the following command:

```bash
pip install streamlit pytube instaloader
```

## Usage

1. Clone or download the XnMediaDownloader project from the repository.
2. Open a terminal/command prompt and navigate to the project directory.

3. Run the Streamlit application:

```bash
streamlit run xn_media_downloader.py
```

4. The application will open in your default web browser.

5. Choose the type of media you want to download (YouTube or Instagram).

6. For YouTube:
   - Enter the video URL.
   - Select the desired resolution from the drop-down menu.
   - Specify the output path where the downloaded videos will be saved.
   - Click the "Download YouTube Video" button to start the download.

7. For Instagram:
   - Enter the Instagram reel's URL.
   - Specify the output path for downloaded videos.
   - Click the "Download Instagram Video" button to start the download.

8. The application will display a spinner while downloading the video. Once the download is complete, you'll see a success message or an error message if the video is not available in the selected resolution.

## Contributing

Contributions to the XnMediaDownloader project are welcome! Feel free to submit issues, feature requests, or pull requests through GitHub.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Note:** XnMediaDownloader is a sample project intended for educational purposes. Please ensure that you use this tool responsibly and respect copyright and content ownership when downloading videos.
